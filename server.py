import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

def get_local_ip_address():
    """Find the server's local IP address that can be accessed within the network."""
    # Attempt to connect to an Internet address, and the chosen IP is the one
    # that can communicate with the Internet (hence, the local network IP)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Use Google's public DNS server address to find the local network IP
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        print(f"Could not determine the local IP address: {e}")
        return None

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # No IP restriction; serve the request as usual
        super().do_GET()

    def translate_path(self, path):
        """Translate URL paths to filesystem paths."""
        # Set the base directory to the 'static' folder
        path = super().translate_path(path)
        relpath = os.path.relpath(path, os.getcwd())
        return os.path.join(os.getcwd(), 'static', relpath)

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('', 8000)  # Serve on all addresses, port 8000
    httpd = server_class(server_address, handler_class)
    local_ip = get_local_ip_address()
    if local_ip:
        print(f"Serving HTTP on {local_ip} port 8000...")
    else:
        print("Serving HTTP on port 8000 without a specific IP address...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping...")
    finally:
        httpd.server_close()  # Cleanly close the server
        print("Server stopped.")

if __name__ == '__main__':
    run()

