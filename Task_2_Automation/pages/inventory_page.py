from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.backpack_add_button = page.locator(
            "button[name='add-to-cart-sauce-labs-backpack']"
        )
        self.backpack_remove_button = page.locator(
            "button[name='remove-sauce-labs-backpack']"
        )
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def is_backpack_removed_button_visible(self) -> bool:
        return self.backpack_remove_button.is_visible()

    def get_cart_badge_count(self) -> str:
        return self.cart_badge.inner_text()

    def open_cart(self):
        self.cart_icon.click()
    def remove_backpack_from_cart(self):
        self.backpack_remove_button.click()

    def is_cart_badge_visible(self) -> bool:
        return self.cart_badge.is_visible()