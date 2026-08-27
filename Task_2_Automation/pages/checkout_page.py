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
    def click_cancel(self):
        self.page.locator("#cancel").click()

    def is_checkout_overview_displayed(self) -> bool:
        return self.page.locator(".checkout_summary_container").is_visible()
    def get_error_message(self) -> str:
        return self.page.locator("[data-test='error']").inner_text()

    def get_item_name(self) -> str:
        return self.page.locator(".inventory_item_name").inner_text()

    def get_item_price(self) -> str:
        return self.page.locator(".inventory_item_price").inner_text()

    def get_subtotal(self) -> str:
        return self.page.locator(".summary_subtotal_label").inner_text()

    def get_tax(self) -> str:
        return self.page.locator(".summary_tax_label").inner_text()

    def get_total(self) -> str:
        return self.page.locator(".summary_total_label").inner_text()

    def click_finish(self):
        self.page.locator("#finish").click()

    def is_order_confirmation_displayed(self) -> bool:
        return self.page.locator(".checkout_complete_container").is_visible()