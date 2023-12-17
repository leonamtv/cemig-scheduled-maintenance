import pandas as pd
from core.download_file import download_and_save
from core.download_page import get_content
from core.file_path import get_most_recent_downloaded_file
from core.parser import find_url_from_html
from core.spreadsheet import DEFAULT_SHEET_NAME
from core.url import CEMIG_DESLIGAMENTO_PROGRAMADO_URL

pd.options.display.max_columns = 10

download_new_file = False
city = 'TIMOTEO'

if download_new_file:
    html_content = get_content(CEMIG_DESLIGAMENTO_PROGRAMADO_URL)
    parsed_result = find_url_from_html(html_content)
    download_and_save(parsed_result)

most_recent_spreadsheet_path = get_most_recent_downloaded_file()
scheduled_maintenance_df = pd.read_excel(most_recent_spreadsheet_path, sheet_name=DEFAULT_SHEET_NAME, skiprows=1,
                                             header=1)
filtered_scheduled_maintenance_df = scheduled_maintenance_df.query('CIDADE == @city')

# print(scheduled_maintenance_df.columns.values)
# print(scheduled_maintenance_df.head(10))
# print(scheduled_maintenance_df.tail(10))
# print(scheduled_maintenance_df.query('CIDADE == @city').head(10))

address_list = filtered_scheduled_maintenance_df['ENDEREÇOS'].to_list()
start_time_list = filtered_scheduled_maintenance_df['INÍCIO'].to_list()
end_time_list = filtered_scheduled_maintenance_df['FIM'].to_list()

for address, start_time, end_time in zip(address_list, start_time_list, end_time_list):
    escaped_address = fr"""[ {address.replace('\n', ' | ')} ]"""
    print(fr"""at {escaped_address} starting at {start_time} and ending at {end_time}""")
