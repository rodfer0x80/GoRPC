#!/usr/bin/env python3


import sys
import os 


def buildAll():
    ret = 0
    ret = buildEmbed()
    if ret:
        return ret
    else:
        ret = buildAdmin()
    if ret:
        return ret
    else:
        buildInterface()
    return 0

def buildEmbed():
    cmd = "cd grpc_embed &&\
            protoc -I . embed.proto --go-grpc_out=./ &&\
            mv github.com/rodfer0x80/GoRPC/grpc_embed/embed_grpc.pb.go . &&\
            rm -rf ./github.com &&\
            cd .."
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error building Embed\n")
        return -1
    return 0

def buildAdmin():
    cmd = "cd grpc_api &&\
            protoc -I . embed.proto --go_out=. --go-grpc_out=. &&\
            mv github.com/rodfer0x80/GoRPC/grpc_api/embed_grpc.pb.go github.com/rodfer0x80/GoRPC/grpc_api/embed.pb.go . &&\
            rm -rf ./github.com &&\
            cd .."
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error building API\n")
        return -2
    return 0

    cmd = "cd grpc_admin &&\
            go build main.go ./bin/admin &&\
            cd .."
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error building Admin\n")
        return -3
    return 0

def buildInterface():
    cmd = "cd ./grpc_interface &&\
            python3 -m venv venv &&\
            source ./venv/bin/activate &&\
            pip install --upgrade pip &&\
            pip install -r requirements.txt"
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error building Interface\n")
        return -4

def main():
    op = sys.stdin.read(3)
    if op == "all":
        return buildAll()
    elif op == "emb":
        return buildEmbed()
    elif op == "adm":
        return buildAdmin()
    elif op == "ifc":
        return buildInterface()
    else:
        return 1


if __name__ == '__main__':
	sys.exit(main())



