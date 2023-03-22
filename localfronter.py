from mitmproxy import http
from mitmproxy import ctx
import re

class HTTPSProxy:
    def __init__(self, target_host, target_sni, proxy_host, proxy_port):
        self.target_host = target_host
        self.target_sni = target_sni
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port

    def run(self):
        from mitmproxy.tools.main import mitmdump
        mitmdump(['-p', str(self.proxy_port), '-s', __file__])

    def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.scheme != "https":
            return

        # modify the Forwarded header
        flow.request.headers["Forwarded"] = f"for={self.proxy_host};proto=https"

        # modify the Host header
        flow.request.headers["Host"] = self.target_host

        # modify the SNI header
        flow.request.headers["SNI"] = self.target_sni

        # modify the DNS resolution for the target host
        flow.request.host = self.proxy_host
        flow.request.port = self.proxy_port

addons = [
    HTTPSProxy("safe.domaintargetexample.com", "safe.domaintargetexample.com", "fun.safewebsite.com", 8080)
]
