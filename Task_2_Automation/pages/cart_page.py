from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.backpack_item = page.locator(
            ".cart_item:has-text('Sauce Labs Backpack')"
        )
        self.backpack_price = page.locator(
            ".cart_item:has-text('Sauce Labs Backpack') .inventory_item_price"
        )

    def is_backpack_displayed(self) -> bool:
        return self.backpack_item.is_visible()

    def get_backpack_price(self) -> str:
        return self.backpack_price.inner_text()