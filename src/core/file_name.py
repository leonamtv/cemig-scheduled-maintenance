import time
import os
from .file_path import XLSX_DUMP_PATH

base_string = 'desligamento_programado'
ext_string = 'xlsx'


def get_new_file_name():
    now_ts = time.time()
    timestamp_for_filename = str(now_ts).replace('.', '')
    return fr"""{base_string}_{timestamp_for_filename}.{ext_string}"""


def get_new_file_path():
    return os.path.join(XLSX_DUMP_PATH, get_new_file_name())


if __name__ == '__main__':
    for _ in range(10):
        print(get_new_file_name())

