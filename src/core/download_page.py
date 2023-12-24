from urllib.request import urlopen, Request
from .header_utils import get_headers


def get_content(url: str):
    request = Request(url=url, headers=get_headers())
    html = urlopen(request).read()
    return str(html)

