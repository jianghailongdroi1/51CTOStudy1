import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9000
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()