from bs4 import BeautifulSoup


def find_spreadsheet_link_from_html(html_content: str):
    soup = BeautifulSoup(html_content, 'html.parser')
    content = soup.findAll('a', {'target': '_blank', 'rel': 'noopener'})
    return content


def find_url_from_html(html_content: str):
    spreadsheet_link_tags = find_spreadsheet_link_from_html(html_content)
    if len(spreadsheet_link_tags) > 0:
        return spreadsheet_link_tags[0]['href']
    return None

