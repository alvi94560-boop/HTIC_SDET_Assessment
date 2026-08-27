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

def test_chk_002_checkout_with_valid_customer_information():
    """
    TC_CHK_002: Verify that checkout can proceed when valid
    customer information is entered.
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
        checkout_page.enter_first_name("Alvi")
        checkout_page.enter_last_name("Test")
        checkout_page.enter_postal_code("682001")
        checkout_page.click_continue()
        assert checkout_page.is_checkout_overview_displayed()

        browser.close()

def test_chk_003_checkout_with_empty_first_name():
    """
    TC_CHK_003: Verify that checkout cannot continue when
    the first name is empty.
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
        checkout_page.enter_last_name("Test")
        checkout_page.enter_postal_code("682001")
        checkout_page.click_continue()
        assert "First Name is required" in checkout_page.get_error_message()

        browser.close()

def test_chk_007_verify_checkout_overview():
    """
    TC_CHK_007: Verify that the checkout overview displays
    correct order information.
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

        checkout_page.enter_first_name("Alvi")
        checkout_page.enter_last_name("Test")
        checkout_page.enter_postal_code("682001")
        checkout_page.click_continue()

        assert checkout_page.is_checkout_overview_displayed()
        assert checkout_page.get_item_name() == "Sauce Labs Backpack"
        assert checkout_page.get_item_price() == "$29.99"
        assert "$29.99" in checkout_page.get_subtotal()
        assert "$" in checkout_page.get_tax()
        assert "$" in checkout_page.get_total()

        browser.close()

def test_chk_008_complete_order_successfully():
    """
    TC_CHK_008: Verify that a user can successfully
    complete an order.
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
        checkout_page.enter_first_name("Alvi")
        checkout_page.enter_last_name("Test")
        checkout_page.enter_postal_code("682001")
        checkout_page.click_continue()
        checkout_page.click_finish()

        assert checkout_page.is_order_confirmation_displayed()

        browser.close()