from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.backpack_add_button = page.locator(
            "button[name='add-to-cart-sauce-labs-backpack']"
        )
        self.backpack_remove_button = page.locator(
            "button[name='remove-sauce-labs-backpack']"
        )
        self.bike_light_add_button = page.locator(
            "button[name='add-to-cart-sauce-labs-bike-light']"
        )
        self.backpack_price = page.locator(
            ".inventory_item:has-text('Sauce Labs Backpack') .inventory_item_price"
     )
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_button.click()

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
    
    def get_backpack_price(self) -> str:
        return self.backpack_price.inner_text()