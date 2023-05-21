from requests_html import HTMLSession

class WebScraper:
    def scrape_data(self, tag):
        url = f'https://quotes.toscrape.com/tag/{tag}'
        session = HTMLSession()
        res = session.get(url)
        print(res.status_code)

        quotes = res.html.find('div.quote')
        print(quotes)
        for q in quates:
            text = q.find('span.text', first=True).text.strip()
            print(text)


quates = WebScraper()
quates.scrape_data('life')
