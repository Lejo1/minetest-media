# Python script to server the index.mth file dynammicly
from http.server import BaseHTTPRequestHandler, HTTPServer
from binascii import b2a_hex
import time

hostName = "media.minetest.land"
serverPort = 8080
hash_file = "hashes.txt"

hashes = set()
with open(hash_file, "r") as file:
    for hash in file.readlines():
        hashes.add(hash.strip())


class MediaServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<meta http-equiv="refresh" content="0; URL=https://github.com/Lejo1/minetest-media">')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        media_size = (content_length - 6)
        if media_size % 20 != 0:
            print("Got Invalid Size")
            return

        input = self.rfile.read(content_length)
        if input [:6] != b"\x4d\x54\x48\x53\x00\x01":
            print("Got invalid protocol or version!")
            return

        out = b"\x4d\x54\x48\x53\x00\x01"

        for i in range(6, content_length, 20):
            hash = input[i:i+20]
            if b2a_hex(hash) in hashes:
                out += hash

        self.send_response(200)
        self.send_header("Content-Type", "octet/stream")
        self.end_headers()
        self.wfile.write(out)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MediaServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
