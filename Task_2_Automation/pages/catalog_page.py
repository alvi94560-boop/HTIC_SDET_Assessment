from playwright.sync_api import Page


class CatalogPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.product_cards = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_images = page.locator(".inventory_item_img img")
        self.sort_dropdown = page.locator(".product_sort_container")

    def get_product_count(self) -> int:
        return self.product_cards.count()

    def get_product_names(self) -> list[str]:
        return self.product_names.all_inner_texts()

    def get_product_prices(self) -> list[str]:
        return self.product_prices.all_inner_texts()

    def get_product_image_count(self) -> int:
        return self.product_images.count()

    def select_sort_option(self, option: str):
        self.sort_dropdown.select_option(label=option)

    def click_product(self, product_name: str):
        self.page.get_by_text(product_name, exact=True).click()