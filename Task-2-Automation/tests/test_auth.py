from playwright.sync_api import sync_playwright


def test_auth_001_successful_login():
    """
    TC_AUTH_001: Verify that a standard user can log in successfully.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        assert "inventory.html" in page.url
        browser.close()