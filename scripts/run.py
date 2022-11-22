#!/usr/bin/env python3


import sys


def readStdin():
    return sys.stdin.read()


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
    cmd = "cd grpc_interface &&\
		python3 -m venv venv &&\
		source venv/bin/activate &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt"
    try:
        os.system(cmd)
        return 0
    except:
        sys.stdout.write("[x] Error running Interface\n")
        return -3


def main():
    op = readStdin()
    if op == "all":
        return runAll()
    elif op == "embed":
        return runEmbed()
    elif op == "admin":
        return runAdmin()
    else:
        return 1


if __name__ == '__main__':
    sys.exit(main())
