package main

import (
	"context"
	"errors"
	"fmt"
	"net"
	"log"


	"github.com/rodfer0x80/GoRPC/grpc_api"

	"google.golang.org/grpc"
)

type adminServer struct {
	work, stdout chan *grpc_api.Command
	grpc_api.UnimplementedAdminServer
}

func MakeAdminServer(work, stdout chan *grpc_api.Command) *adminServer {
	s := new(adminServer)
	s.work = work
	s.stdout = stdout
	return s
}

func (s *adminServer) ExecuteCommand(ctx context.Context, cmd *grpc_api.Command) (*grpc_api.Command, error) {
	var res *grpc_api.Command
	go func() {
		s.work <- cmd
	}()
	res = <-s.stdout
	return res, nil
}

type embedServer struct {
	work, stdout chan *grpc_api.Command
	grpc_api.UnimplementedEmbedServer
}

func MakeEmbedServer(work, stdout chan *grpc_api.Command) *embedServer {
	s := new(embedServer)
	s.work = work
	s.stdout = stdout
	return s
}

func (s *embedServer) GetCommand(ctx context.Context, empty *grpc_api.Empty) (*grpc_api.Command, error) {
	var cmd = new(grpc_api.Command)
	select {
	case cmd, ok := <-s.work:
		if ok {
			return cmd, nil
		}
		return cmd, errors.New("Channel error")
	default:
		return cmd, nil
	}
}

func (s *embedServer) SentResult(ctx context.Context, result *grpc_api.Command) (*grpc_api.Empty, error) {
	s.stdout <- result
	return &grpc_api.Empty{}, nil
}

func main() {
	var (
		admin_listener, embed_listener net.Listener
		err                            error
		opts                           []grpc.ServerOption
		work, stdout                   chan *grpc_api.Command
	)

	work, stdout = make(chan *grpc_api.Command), make(chan *grpc_api.Command)
	admin := MakeAdminServer(work, stdout)
	embed := MakeEmbedServer(work, stdout)

	if admin_listener, err = net.Listen("tcp", fmt.Sprintf("localhost:%d", 32001)); err != nil {
		log.Fatal(err)
	}

	if embed_listener, err = net.Listen("tcp", fmt.Sprintf("localhost:%d", 32666)); err != nil {
		log.Fatal(err)
	}

	grpcAdminServer, grpcEmbedServer := grpc.NewServer(opts...), grpc.NewServer(opts...)

	grpc_api.RegisterAdminServer(grpcAdminServer, admin)
	grpc_api.RegisterEmbedServer(grpcEmbedServer, embed)

	go func() {
		grpcEmbedServer.Serve(embed_listener)
	}()
	grpcAdminServer.Serve(admin_listener)
}
