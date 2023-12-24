import urllib.request

from core.file_name import get_new_file_path


def download_file(url: str, filename: str):
    urllib.request.urlretrieve(url, filename)


def download_and_save(url: str):
    download_file(url, get_new_file_path())
