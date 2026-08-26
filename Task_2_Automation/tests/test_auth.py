from playwright.sync_api import sync_playwright

from Task_2_Automation.pages.login_page import LoginPage

def test_auth_001_successful_login():
    """
    TC_AUTH_001: Verify that a standard user can log in successfully.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        assert "inventory.html" in page.url

        browser.close()