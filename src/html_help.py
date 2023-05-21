from bs4 import BeautifulSoup
import requests

def get_raw_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return str(soup)

def get_body_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    body = soup.find('body')
    if body:
        return body.prettify(formatter='html')
    else:
        return None
