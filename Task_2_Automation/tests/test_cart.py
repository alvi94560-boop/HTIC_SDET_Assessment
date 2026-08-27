from playwright.sync_api import sync_playwright

from Task_2_Automation.pages.login_page import LoginPage
from Task_2_Automation.pages.inventory_page import InventoryPage
from Task_2_Automation.pages.cart_page import CartPage

def test_cart_001_add_item_to_cart():
    """
    TC_CART_001: Verify that adding a product increases
    the shopping cart badge counter.
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
        assert inventory_page.is_backpack_removed_button_visible()
        assert inventory_page.get_cart_badge_count() == "1"

        browser.close()


def test_cart_002_remove_item_from_cart():
    """
    TC_CART_002: Verify that removing an item removes it
    from the shopping cart.
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
        assert inventory_page.get_cart_badge_count() == "1"
        inventory_page.remove_backpack_from_cart()
        assert not inventory_page.is_cart_badge_visible()

        browser.close()

def test_cart_003_add_multiple_items_to_cart():
    """
    TC_CART_003: Verify that multiple products can be added
    to the shopping cart.
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
        inventory_page.add_bike_light_to_cart()
        assert inventory_page.get_cart_badge_count() == "2"

        browser.close()

def test_cart_004_verify_cart_contents():
    """
    TC_CART_004: Verify that products added from the inventory
    page appear in the shopping cart.
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
        cart_page = CartPage(page)
        assert cart_page.is_backpack_displayed()

        browser.close()

def test_cart_005_verify_product_price_in_cart():
    """
    TC_CART_005: Verify that the product price displayed in
    the cart matches the price displayed in the inventory.
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
        inventory_price = inventory_page.get_backpack_price()
        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()
        cart_page = CartPage(page)
        cart_price = cart_page.get_backpack_price()
        assert cart_price == inventory_price

        browser.close()