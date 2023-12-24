import os
import glob

from core.config import number_of_files_to_maintain
from core.file_path import xlsx_dump_path
from core.log_utils import log, print_divisor_line


def get_files_for_deletion():
    if os.path.isdir(xlsx_dump_path):
        list_of_files = glob.glob(xlsx_dump_path + '*')
        sorted_list_of_files = sorted(list_of_files, key=os.path.getctime)
        number_of_files = len(sorted_list_of_files)
        if number_of_files > number_of_files_to_maintain:
            return sorted_list_of_files[:number_of_files - number_of_files_to_maintain]
    return []


def delete_older_files():
    files_eligible_for_deletion = get_files_for_deletion()
    if len(files_eligible_for_deletion) == 0:
        log('There are no older files to delete')
    else:
        print_divisor_line()
        for index, file in enumerate(files_eligible_for_deletion):
            if not os.path.isfile(file):
                log(f"Skipping {file} | Reason: File does not exist", with_divisor=True)
            else:
                log(f"Deleting {file}", with_divisor=True)
                os.remove(file)
