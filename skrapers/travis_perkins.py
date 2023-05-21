from requests_html import HTMLSession

class TravisPerkinsScraper:
    def __init__(self):
        self.session = HTMLSession()

    def scrape_categories(self):
        url = f'https://www.travisperkins.co.uk/product/c/1000000/'
        response = self.session.get(url)
        response.html.render()
        print(f'Response code: {response.status_code}')

        categories = response.html.find('div[data-test-id="category-wrapper"]') # 📌 Scrape all category divs in page
        for category in categories:
            title = category.find('h6', first=True).text.strip() # Main cat title
            img_url = category.find('img', first=True).attrs['src'][2:] # Cat pic url
            print(f"Category Name: {title}\nImage URL: {img_url}\n")

    def scrape_building_materials(self):
        url = f'https://www.travisperkins.co.uk/product/building-materials/c/1500029/'
        response = self.session.get(url)
        response.html.render()
        print(f'Response code: {response.status_code}')

        categories = response.html.find(
            'div[data-test-id="category-wrapper"]')  # 📌 Scrape all category divs in page
        for category in categories:
            title = category.find('h6', first=True).text.strip()  # Main cat title
            img_url = category.find('img', first=True).attrs['src'][2:]  # Cat pic url
            print(f"Category Name: {title}\nImage URL: {img_url}\n")

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
instance.scrape_building_materials()
