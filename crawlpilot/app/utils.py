import requests
from bs4 import BeautifulSoup
from run import summarizer


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').text if soup.find('h1') else 'No title'
    text = soup.get_text()
    summary = summarizer(text, max_length=56, min_length=30, do_sample=False)[0]['summary_text']
    # summary = "hello there"
    links = [a['href'] for a in soup.find_all('a', href=True)]
    print(summary,links,title)
    return title, summary, links
