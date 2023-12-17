import os
import glob

XLSX_DUMP_PATH = './xlsx_dump/'


def get_most_recent_downloaded_file():
    if os.path.isdir(XLSX_DUMP_PATH):
        list_of_files = glob.glob(XLSX_DUMP_PATH + '*')
        return max(list_of_files, key=os.path.getctime)

