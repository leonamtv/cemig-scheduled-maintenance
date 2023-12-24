from bs4 import BeautifulSoup

from core.config import bs4_features, href_attribute, a_tag, bs4_search_attributes


def find_spreadsheet_link_from_html(html_content: str):
    soup = BeautifulSoup(html_content, bs4_features)
    content = soup.findAll(a_tag, bs4_search_attributes)
    return content


def find_url_from_html(html_content: str):
    spreadsheet_link_tags = find_spreadsheet_link_from_html(html_content)
    if len(spreadsheet_link_tags) > 0:
        return spreadsheet_link_tags[0][href_attribute]
    return None

