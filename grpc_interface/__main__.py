#!/usr/bin/env python3

import sys
import os
import subprocess
import http.server
import socketserver


def runServer(server_class=http.server.HTTPServer, handler_class=http.server.SimpleHTTPRequestHandler, host="127.0.0.1", port=8080):
    server_address = (host, port)
    try:
        with socketserver.TCPServer(("", port), handler_class) as httpd:
            sys.stdout.write(f"[*] Serving at {host}:{port}\n")
            openInterface(host, port)
            httpd.serve_forever()
    except KeyboardInterrupt as e:
        sys.exit(0)
    return 0


def openInterface(host="127.0.0.1", port="8080"):
    browser = os.environ['BROWSER']
    cmd = f"{browser} {host}:{port}".split(" ")
    subprocess.check_output(cmd)
    return 0


def main():
    host = "127.0.0.1"
    port = 3420
    runServer(host=host, port=port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
