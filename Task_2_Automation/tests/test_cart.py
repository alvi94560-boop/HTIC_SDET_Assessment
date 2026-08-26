from playwright.sync_api import sync_playwright

from Task_2_Automation.pages.login_page import LoginPage
from Task_2_Automation.pages.inventory_page import InventoryPage


def test_cart_001_add_item_to_cart():
    """
    TC_CART_001: Verify that adding a product increases
    the shopping cart badge counter.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login
        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        assert inventory_page.is_backpack_removed_button_visible()
        assert inventory_page.get_cart_badge_count() == "1"

        browser.close()