import pandas as pd

from core.config import address_column
from core.config import start_time_column
from core.config import end_time_column
from core.config import query_for_city
from core.file_path import get_most_recent_downloaded_file
from core.log_utils import log_parsed_result
from core.log_utils import print_divisor_line
from core.log_utils import log
from core.config import default_sheet_name
from core.download_file import download_and_save
from core.download_page import get_content
from core.garbage_collector import delete_older_files
from core.parser import find_url_from_html
from core.config import cemig_desligamento_programado_url
from core.config import should_delete_older_files
from core.config import should_download_new_file


def download_new_file_check_and_execution():
    if should_download_new_file:
        html_content = get_content(cemig_desligamento_programado_url)
        parsed_result = find_url_from_html(html_content)
        download_and_save(parsed_result)


def sanitization_check_and_execution():
    if should_delete_older_files:
        delete_older_files()


def default_flow(city):
    sanitization_check_and_execution()
    download_new_file_check_and_execution()

    most_recent_spreadsheet_path = get_most_recent_downloaded_file()
    scheduled_maintenance_df = pd.read_excel(most_recent_spreadsheet_path,
                                             sheet_name=default_sheet_name,
                                             skiprows=1,
                                             header=1)
    filtered_scheduled_maintenance_df = scheduled_maintenance_df.query(query_for_city)

    address_list = filtered_scheduled_maintenance_df[address_column].to_list()
    start_time_list = filtered_scheduled_maintenance_df[start_time_column].to_list()
    end_time_list = filtered_scheduled_maintenance_df[end_time_column].to_list()

    if len(address_list) == len(start_time_list) == len(end_time_list) > 0:
        print_divisor_line()
        for address, start_time, end_time in zip(address_list, start_time_list, end_time_list):
            log_parsed_result(address, start_time, end_time)
    else:
        log("Error in logging the parsed result")
