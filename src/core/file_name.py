import time
import os

from core.config import base_string_file_name, ext_string_file_name
from .file_path import xlsx_dump_path


def get_new_file_name():
    now_ts = time.time()
    timestamp_for_filename = str(now_ts).replace('.', '')
    return fr"""{base_string_file_name}_{timestamp_for_filename}.{ext_string_file_name}"""


def get_new_file_path():
    return os.path.join(xlsx_dump_path, get_new_file_name())


if __name__ == '__main__':
    for _ in range(10):
        print(get_new_file_name())

