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
    def enter_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def enter_postal_code(self, postal_code: str):
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.page.locator("#continue").click()

    def is_checkout_overview_displayed(self) -> bool:
        return self.page.locator(".checkout_summary_container").is_visible()