#!/usr/bin/env python3


import sys
import os


def runAll():
    runAdmin()
    runInterface()
    return 0


def runEmbed():
    cmd = "./bin/embed"
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error running Embed\n")
        return -1


def runAdmin():
    cmd = "./bin/admin"
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error running Admin\n")
        return -2


def runInterface():
    cmd = "source ./grpc_interface/venv/bin/activate &&\
		python ./grpc_interface/__main__.py"
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error running Interface\n")
        return -3


def main():
    op = sys.stdin.read(3)
    if op == "all":
        return runAll()
    elif op == "emb":
        return runEmbed()
    elif op == "adm":
        return runAdmin()
    elif op == "ifc":
        return runInterface()
    else:
        return 1


if __name__ == '__main__':
    sys.exit(main())
