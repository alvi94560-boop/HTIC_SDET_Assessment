from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")

    def click_checkout(self):
        self.checkout_button.click()

    def is_checkout_information_page_displayed(self) -> bool:
        return (
            self.first_name_input.is_visible()
            and self.last_name_input.is_visible()
            and self.postal_code_input.is_visible()
        )