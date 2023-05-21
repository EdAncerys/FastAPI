from requests_html import HTMLSession

class TravisPerkinsScraper:
    def __init__(self):
        self.session = HTMLSession()

    def scrape_categories(self):
        url = f'https://www.travisperkins.co.uk/product/c/1000000/'
        response = self.session.get(url)
        response.html.render()
        print(f'Response code: {response.status_code}')

        categories = response.html.find('div[data-test-id="paper"]')
        for category in categories:
            # name = category.find('h6[data-test-id="sub-categories-title"]', first=True).text.strip()
            name = category.find('h6[data-test-id="sub-categories-title"]', first=True)
            # img_url = category.find('img', first=True).attrs['src']
            print(category)
            # print(img_url)
            # print(f"Category Name: {name}\nImage URL: {image_url}\n")

    def scrape_products_by_category(self, category):
        url = f"https://www.travisperkins.co.uk/{category}"
        response = self.session.get(url)
        response.html.render()

        products = response.html.find('.product-listing')
        for product in products:
            name = product.find('.product-title', first=True).text
            price = product.find('.product-price', first=True).text
            print(f"Name: {name}\nPrice: {price}\n")


instance = TravisPerkinsScraper()
instance.scrape_categories()
