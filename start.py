#!/usr/bin/env python3
"""Open the Sticky Updater: serves this folder on http://localhost:8471 and opens Chrome/Edge.

Web Serial (USB access from the browser) needs a secure page; localhost counts.
Run:  python3 start.py      (Ctrl+C to stop)
"""
import functools
import http.server
import threading
import webbrowser
from pathlib import Path

PORT = 8471
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(Path(__file__).resolve().parent))
server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
url = f"http://localhost:{PORT}/"
print(f"Sticky Updater at {url}  (open it in Chrome or Edge; Ctrl+C to stop)")
threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
