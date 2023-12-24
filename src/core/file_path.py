import os
import glob

from core.config import xlsx_dump_path


def get_most_recent_downloaded_file():
    if os.path.isdir(xlsx_dump_path):
        list_of_files = glob.glob(xlsx_dump_path + '*')
        return max(list_of_files, key=os.path.getctime)

