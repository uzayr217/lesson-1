#!/usr/bin/env python3
import http.server
import socketserver
import os

# Set port to 5000 as required by Replit
PORT = 5000

# Use current directory as the web root
os.chdir('.')

Handler = http.server.SimpleHTTPRequestHandler

# Add cache control headers to prevent caching issues in Replit's iframe
class NoCacheHTTPRequestHandler(Handler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache') 
        self.send_header('Expires', '0')
        super().end_headers()

# Bind to 0.0.0.0 to allow external access (required for Replit)
with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Server running at http://0.0.0.0:{PORT}/")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()