from requests_html import HTMLSession


class TestScraper:
    def scrape_data(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        session = HTMLSession()
        res = session.get(url)
        print(res.status_code)

        dom = res.html.find('div.quote')
        print(dom)
        for q in dom:
            text = q.find('span.text', first=True).text.strip()
            print(text)


quotes = TestScraper()
quotes.scrape_data('life')
