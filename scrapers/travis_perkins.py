import asyncio
from requests_html import AsyncHTMLSession


class TravisPerkinsScraper:
    def __init__(self):
        self.session = AsyncHTMLSession()

    async def scrape_products_from_url(self, url):
        response = await self.session.get(url)
        await response.html.arender()
        print(f"Response code: {response.status_code}")

        blob = []
        categories = response.html.find('div[data-test-id="category-wrapper"]')
        for category in categories:
            title = category.find("h6", first=True).text.strip()
            img_url = category.find("img", first=True).attrs["src"][2:]
            blob.append({"title": title, "url": img_url})
            # print(f"Category Name: {title}\nImage URL: {img_url}\n")
        return blob

    async def scrape_categories(self):
        url = f"https://www.travisperkins.co.uk/product/c/1000000/"
        return await self.scrape_products_from_url(url)

    async def scrape_building_materials(self):
        url = f"https://www.travisperkins.co.uk/product/building-materials/c/1500029/"
        return await self.scrape_products_from_url(url)

    async def scrape_timber_materials(self):
        url = f"https://www.travisperkins.co.uk/product/timber-and-sheet-materials/c/1500000/"
        return await self.scrape_products_from_url(url)

    async def scrape_decorating_materials(self):
        url = f"https://www.travisperkins.co.uk/product/decorating-and-interiors/c/1500538/"
        return await self.scrape_products_from_url(url)

    async def scrape_products_by_category(self, category: object) -> object:
        if category == "Building Materials":
            return await self.scrape_building_materials()
        if category == "Timber & Sheet Materials":
            return await self.scrape_timber_materials()
        if category == "Decorating & Interiors":
            return await self.scrape_decorating_materials()
        else:
            error = f"No handler found for the category: {category}"
            print(error)
            return error


async def main():
    # Wrap instance in async function to call it
    instance = TravisPerkinsScraper()
    data_one = await instance.scrape_decorating_materials()
    data_two = await instance.scrape_products_by_category("Decorating & Interiors")

    print(data_one)
    print(data_two)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
