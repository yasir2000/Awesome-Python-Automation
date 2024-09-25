import os
from dotenv import load_dotenv
import http.server
import socketserver
from urllib.parse import urlparse
from cgi import FieldStorage
from abc import ABC, abstractmethod
from pywebcopy import save_webpage

# Load environment variables from .env file
load_dotenv()

# Fetch configuration values from environment variables
PORT = int(os.getenv('PORT', 7000))
HOST = os.getenv('HOST', '127.0.0.1')

# Abstract Factory Pattern
class WebpageDownloaderFactory(ABC):
    @abstractmethod
    def create_downloader(self):
        pass

class PyWebCopyDownloaderFactory(WebpageDownloaderFactory):
    def create_downloader(self):
        return PyWebCopyDownloader()

# Strategy Pattern
class WebpageDownloader(ABC):
    @abstractmethod
    def download(self, url: str, project_folder: str):
        pass

class PyWebCopyDownloader(WebpageDownloader):
    def download(self, url: str, project_folder: str):
        kwargs = {'project_name': url}
        save_webpage(url=url, project_folder=project_folder, **kwargs)

# Facade Pattern
class WebpageManager:
    def __init__(self, downloader_factory: WebpageDownloaderFactory):
        self.downloader = downloader_factory.create_downloader()

    def process_url(self, url: str):
        parsed_url = urlparse(url)
        project_folder = f'./{parsed_url.netloc}'
        if not os.path.isdir(project_folder):
            self.downloader.download(url, project_folder)
        return f'{parsed_url.netloc}/index.html'

# Request Handler adhering to SRP
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.webpage_manager = WebpageManager(PyWebCopyDownloaderFactory())
        super().__init__(*args, **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        form = FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )
        
        url = form.getvalue('submitButton')
        url_with_protocol = f'https://{url}/'

        try:
            path = self.webpage_manager.process_url(url_with_protocol)
            self.send_response(301)
            self.send_header('Location', path)
            self.end_headers()
        except Exception as e:
            self.send_error(500, f"Error processing request: {str(e)}")

# Dependency Injection and IoC
def main():
    with socketserver.TCPServer((HOST, PORT), RequestHandler) as server:
        print(f"Serving on {HOST}:{PORT}")
        server.serve_forever()

if __name__ == '__main__':
    main()
