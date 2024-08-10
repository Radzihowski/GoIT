import logging
import http.server

logger = logging.getLogger(__name__)

class GoITHTTPHandler(http.server.BaseHTTPRequestHandler):
    def _process_request(self, methood: str):
        logger.debug(methood)

    def do_GET(self):
        self._process_request("get")

    def do_POST(self):
        self._process_request("post")

class GoITRequest:
    # Add attributes and methods as needed
    pass

class GoITResponce:
    # Add attributes and methods as needed
    pass

class GoITServer(http.server.HTTPServer):
    def __init__(
            self,
            address,
            port,
            static_folder
    ):
        super().__init__((address, port), GoITHTTPHandler)

        self.address = address
        self.port = port

        self.static_folder = static_folder

    def serve_forever(self, poll_interval: float = 0.5) -> None:
        logger.info(f"Server on {self.address}:{self.port}")
        return super().serve_forever(poll_interval)

