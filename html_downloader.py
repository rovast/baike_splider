import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        content = urllib.request.urlopen(url)
        if(content.getcode() == 200):
            return content.read()
        else:
            return None