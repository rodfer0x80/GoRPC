#!/bin/sh
cd grpc_embed &&\
	protoc -I . embed.proto --go-grpc_out=./ &&\
	mv github.com/rodfer0x80/GoRPC/grpc_embed/embed_grpc.pb.go . &&\
	rm -rf ./github.com &&\
	cd ..

cd grpc_api &&\
	protoc -I . embed.proto --go_out=. --go-grpc_out=. &&\
	mv github.com/rodfer0x80/GoRPC/grpc_api/embed_grpc.pb.go github.com/rodfer0x80/GoRPC/grpc_api/embed.pb.go . &&\
	rm -rf ./github.com &&\
	cd ..