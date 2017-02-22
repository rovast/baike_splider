import re
import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self,page_url,page_cont):
        if page_url is None or page_cont is None:
            return None
        soup = BeautifulSoup(page_cont,'html.parser',from_encoding="utf-8")

        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        new_urls = set()
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>PHP</h1>
        title = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1').get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary = soup.find('div',class_="lemma-summary").get_text()

        data = {}
        data['title'] = title
        data['url'] = page_url
        data['summary'] = summary
        return data
