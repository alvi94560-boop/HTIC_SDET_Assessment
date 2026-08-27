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
        self.cart_items = page.locator(".cart_item")
        self.remove_buttons = page.locator("button[id^='remove-']")

    def is_backpack_displayed(self) -> bool:
        return self.backpack_item.is_visible()

    def get_backpack_price(self) -> str:
        return self.backpack_price.inner_text()

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()

    def remove_all_items(self):
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()

    def is_cart_empty(self) -> bool:
        return self.cart_items.count() == 0