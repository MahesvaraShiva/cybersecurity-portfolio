from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

class ServerHandler(BaseHTTPRequestHandler):
    def block_request(self):
        print("Blocking request")
        self.send_response(403)  # Forbidden
        self.end_headers()

    def handle_request(self, request_path):
        # Implement firewall rules here
        if request_path == "/tomcatwar.jsp":
            self.block_request()
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()

    def do_GET(self):
        self.handle_request(self.path)

    def do_POST(self):
        self.handle_request(self.path)

if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
