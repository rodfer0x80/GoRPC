#!/bin/sh
cd grpc_embed &&\
	protoc -I . embed.proto --go-grpc_out=./