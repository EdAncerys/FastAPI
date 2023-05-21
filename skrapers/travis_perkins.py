from requests_html import HTMLSession


class TravisPerkinsScraper:

    def __init__(self):
        self.session = HTMLSession()

    def scrape_products_by_url(self, url):
        response = self.session.get(url)
        response.html.render()
        print(f'Response code: {response.status_code}')

        categories = response.html.find('div[data-test-id="category-wrapper"]')
        for category in categories:
            title = category.find('h6', first=True).text.strip()
            img_url = category.find('img', first=True).attrs['src'][2:]
            print(f"Category Name: {title}\nImage URL: {img_url}\n")

    def scrape_categories(self):
        url = f'https://www.travisperkins.co.uk/product/c/1000000/'
        self.scrape_products_by_url(url)

    def scrape_building_materials(self):
        url = f'https://www.travisperkins.co.uk/product/building-materials/c/1500029/'
        self.scrape_products_by_url(url)

    def scrape_timber_materials(self):
        url = f'https://www.travisperkins.co.uk/product/timber-and-sheet-materials/c/1500000/'
        self.scrape_products_by_url(url)

    def scrape_decorating_materials(self):
        url = f'https://www.travisperkins.co.uk/product/decorating-and-interiors/c/1500538/'
        self.scrape_products_by_url(url)

    def scrape_products_by_category(self, category):
        if category == "Building Materials":
            self.scrape_building_materials()
        if category == "Timber & Sheet Materials":
            self.scrape_timber_materials()
        if category == "Decorating & Interiors":
            self.scrape_decorating_materials()
        else:
            print(f"No handler found for the category: {category}")


instance = TravisPerkinsScraper()
instance.scrape_categories()
instance.scrape_products_by_category('Decorating & Interiors')
