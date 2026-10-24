from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE = Path(__file__).parent
FILES = {
    "/": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = FILES.get(self.path)
        if not entry:
            self.send_error(404)
            return
        name, content_type = entry
        body = (BASE / name).read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("Serving on http://localhost:8000")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
