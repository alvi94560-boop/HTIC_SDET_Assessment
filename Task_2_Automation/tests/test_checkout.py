from playwright.sync_api import sync_playwright

from Task_2_Automation.pages.login_page import LoginPage
from Task_2_Automation.pages.inventory_page import InventoryPage
from Task_2_Automation.pages.checkout_page import CheckoutPage

def test_chk_001_navigate_to_checkout():
    """
    TC_CHK_001: Verify that a user can navigate from the
    cart to the checkout information page.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()
        checkout_page = CheckoutPage(page)
        checkout_page.click_checkout()
        assert checkout_page.is_checkout_information_page_displayed()

        browser.close()