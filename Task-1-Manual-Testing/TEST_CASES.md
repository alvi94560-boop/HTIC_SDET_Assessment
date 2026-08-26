# SauceDemo Manual Test Cases

Application: SauceDemo
URL: https://www.saucedemo.com/
# Feature: Authentication & Session Management (FEAT-AUTH)

## TC_AUTH_001: Successful Login

* Feature: FEAT-AUTH
* Description: Verify that a standard user can log in successfully using valid credentials.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Enter `standard_user` in the Username field.
  2. Enter `secret_sauce` in the Password field.
  3. Click the Login button.
* Expected Result: User is successfully logged in and redirected to the inventory catalog page.

## TC_AUTH_002: Invalid Password

* Feature: FEAT-AUTH
* Description: Verify that login fails when an incorrect password is entered.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Enter `standard_user` in the Username field.
  2. Enter an incorrect password such as `wrong_password` in the Password field.
  3. Click the Login button.
* Expected Result: Login fails and an appropriate error message is displayed.

## TC_AUTH_003: Invalid Username

* Feature: FEAT-AUTH
* Description: Verify that login fails when an invalid username is entered.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Enter `invalid_user` in the Username field.
  2. Enter `secret_sauce` in the Password field.
  3. Click the Login button.
* Expected Result: Login fails and an appropriate error message is displayed.

## TC_AUTH_004: Empty Username

* Feature: FEAT-AUTH
* Description: Verify that login cannot be performed when the Username field is empty.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Leave the Username field empty.
  2. Enter `secret_sauce` in the Password field.
  3. Click the Login button.
* Expected Result: Login is not performed and a validation error indicating that the username is required is displayed.

## TC_AUTH_005: Empty Password

* Feature: FEAT-AUTH
* Description: Verify that login cannot be performed when the Password field is empty.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Enter `standard_user` in the Username field.
  2. Leave the Password field empty.
  3. Click the Login button.
* Expected Result: Login is not performed and a validation error indicating that the password is required is displayed.

## TC_AUTH_006: Empty Username and Password

* Feature: FEAT-AUTH
* Description: Verify that login cannot be performed when both credentials are empty.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Leave the Username field empty.
  2. Leave the Password field empty.
  3. Click the Login button.
* Expected Result: Login is not performed and a validation error is displayed.

## TC_AUTH_007: Locked User Login

* Feature: FEAT-AUTH
* Description: Verify that a locked user cannot log in.
* Pre-condition: User is on the SauceDemo login page.
* Execution Steps:

  1. Enter `locked_out_user` in the Username field.
  2. Enter `secret_sauce` in the Password field.
  3. Click the Login button.
* Expected Result: Login is rejected and an appropriate locked-user error message is displayed.

## TC_AUTH_008: Successful Logout

* Feature: FEAT-AUTH
* Description: Verify that a logged-in user can successfully log out.
* Pre-condition: User is logged in and is on the inventory catalog page.
* Execution Steps:

  1. Open the navigation menu.
  2. Click the Logout option.
* Expected Result: User is logged out and redirected to the SauceDemo login page.

## TC_AUTH_009: Session After Page Refresh

* Feature: FEAT-AUTH
* Description: Verify the session behavior when the inventory page is refreshed after login.
* Pre-condition: User is logged in and is on the inventory catalog page.
* Execution Steps:

  1. Refresh the browser page.
  2. Observe the displayed page.
* Expected Result: The application handles the active session correctly and the user remains on the inventory page.

## TC_AUTH_010: Access Inventory After Logout Using Browser Back

* Feature: FEAT-AUTH
* Description: Verify that a logged-out user cannot access protected inventory content through browser history.
* Pre-condition: User has successfully logged in and then logged out.
* Execution Steps:

  1. Log in using valid credentials.
  2. Log out using the navigation menu.
  3. Click the browser Back button.
  4. Observe the displayed page.
* Expected Result: A logged-out user should not be able to access protected inventory functionality without logging in again.

# Feature: Product Catalog & Discovery (FEAT-CATALOG)

## TC_CATALOG_001: Display Product Catalog

* Feature: FEAT-CATALOG
* Description: Verify that products are displayed correctly after successful login.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Observe the inventory page.
  2. Verify that product cards are displayed.
* Expected Result: Available products are displayed with their relevant information.

## TC_CATALOG_002: Verify Product Name

* Feature: FEAT-CATALOG
* Description: Verify that each product displays a product name.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Observe the displayed product cards.
  2. Check the product names.
* Expected Result: Each displayed product has a visible and readable product name.

## TC_CATALOG_003: Verify Product Price

* Feature: FEAT-CATALOG
* Description: Verify that each product displays a valid price.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Observe the displayed products.
  2. Check the price shown for each product.
* Expected Result: Each product displays a valid price using the expected currency format.

## TC_CATALOG_004: Verify Product Image

* Feature: FEAT-CATALOG
* Description: Verify that product images are displayed correctly.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Observe each product card.
  2. Check whether the product image is displayed.
* Expected Result: Product images are displayed correctly and correspond to the associated products.

## TC_CATALOG_005: Sort Products A to Z

* Feature: FEAT-CATALOG
* Description: Verify that products can be sorted alphabetically from A to Z.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Open the product sorting dropdown.
  2. Select `Name (A to Z)`.
  3. Observe the product order.
* Expected Result: Products are displayed in ascending alphabetical order by product name.

## TC_CATALOG_006: Sort Products Z to A

* Feature: FEAT-CATALOG
* Description: Verify that products can be sorted alphabetically from Z to A.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Open the product sorting dropdown.
  2. Select `Name (Z to A)`.
  3. Observe the product order.
* Expected Result: Products are displayed in descending alphabetical order by product name.

## TC_CATALOG_007: Sort Products by Price Low to High

* Feature: FEAT-CATALOG
* Description: Verify that products can be sorted from the lowest price to the highest price.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Open the product sorting dropdown.
  2. Select `Price (low to high)`.
  3. Observe the product order.
* Expected Result: Products are displayed from the lowest price to the highest price.

## TC_CATALOG_008: Sort Products by Price High to Low

* Feature: FEAT-CATALOG
* Description: Verify that products can be sorted from the highest price to the lowest price.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Open the product sorting dropdown.
  2. Select `Price (high to low)`.
  3. Observe the product order.
* Expected Result: Products are displayed from the highest price to the lowest price.

## TC_CATALOG_009: Open Product Details

* Feature: FEAT-CATALOG
* Description: Verify that a user can open the details of a product.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Click a product name or product image.
  2. Observe the product details page.
* Expected Result: The selected product details page is displayed and contains the correct product information.

# Feature: Cart & Badge Management (FEAT-CART)

## TC_CART_001: Add Item to Cart

* Feature: FEAT-CART
* Description: Verify that adding a product increases the shopping cart badge counter.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Locate the `Sauce Labs Backpack`.
  2. Click its `Add to cart` button.
  3. Observe the shopping cart badge.
* Expected Result: The product is added to the cart, the button changes to `Remove`, and the cart badge displays `1`.

## TC_CART_002: Remove Item From Cart

* Feature: FEAT-CART
* Description: Verify that a product can be removed from the cart.
* Pre-condition: User is logged in, on the inventory page, and the Sauce Labs Backpack has been added to the cart.
* Execution Steps:

  1. Click the `Remove` button for the Sauce Labs Backpack.
  2. Observe the shopping cart badge.
* Expected Result: The product is removed from the cart and the cart badge is removed or updated accordingly.

## TC_CART_003: Add Multiple Items to Cart

* Feature: FEAT-CART
* Description: Verify that multiple products can be added to the shopping cart.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Add the Sauce Labs Backpack to the cart.
  2. Add another available product to the cart.
  3. Observe the cart badge.
* Expected Result: Both products are added and the cart badge displays the correct number of items.

## TC_CART_004: Verify Cart Contents

* Feature: FEAT-CART
* Description: Verify that products added from the inventory page appear in the cart.
* Pre-condition: User is logged in and at least one product has been added to the cart.
* Execution Steps:

  1. Click the shopping cart icon.
  2. Observe the cart contents.
* Expected Result: All products previously added to the cart are displayed with the correct product information.

## TC_CART_005: Verify Product Price in Cart

* Feature: FEAT-CART
* Description: Verify that the product price displayed in the cart matches the price displayed in the inventory.
* Pre-condition: User is logged in and a product has been added to the cart.
* Execution Steps:

  1. Note the product price on the inventory page.
  2. Open the shopping cart.
  3. Compare the product price.
* Expected Result: The product price in the cart matches the corresponding inventory price.

## TC_CART_006: Remove All Items From Cart

* Feature: FEAT-CART
* Description: Verify that the cart can be emptied by removing all added products.
* Pre-condition: User is logged in and multiple products are present in the cart.
* Execution Steps:

  1. Open the shopping cart.
  2. Remove each product.
  3. Observe the cart.
* Expected Result: All products are removed and the cart is empty.

## TC_CART_007: Cart Navigation

* Feature: FEAT-CART
* Description: Verify that clicking the shopping cart icon navigates to the cart page.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Click the shopping cart icon.
* Expected Result: The user is navigated to the shopping cart page.

# Feature: Checkout Flow & Order Processing (FEAT-CHK)

## TC_CHK_001: Navigate to Checkout

* Feature: FEAT-CHK
* Description: Verify that a user can navigate from the cart to the checkout information page.
* Pre-condition: User is logged in and has at least one product in the cart.
* Execution Steps:

  1. Open the shopping cart.
  2. Click the `Checkout` button.
* Expected Result: The checkout information page is displayed.

## TC_CHK_002: Checkout With Valid Customer Information

* Feature: FEAT-CHK
* Description: Verify that checkout can proceed when valid customer information is entered.
* Pre-condition: User is logged in, has at least one product in the cart, and is on the checkout information page.
* Execution Steps:

  1. Enter a valid first name.
  2. Enter a valid last name.
  3. Enter a valid postal code.
  4. Click `Continue`.
* Expected Result: The user is taken to the checkout overview page.

## TC_CHK_003: Checkout With Empty First Name

* Feature: FEAT-CHK
* Description: Verify that checkout cannot continue when the first name is empty.
* Pre-condition: User is logged in, has a product in the cart, and is on the checkout information page.
* Execution Steps:

  1. Leave the First Name field empty.
  2. Enter a valid last name.
  3. Enter a valid postal code.
  4. Click `Continue`.
* Expected Result: Checkout does not continue and an appropriate validation error is displayed.

## TC_CHK_004: Checkout With Empty Last Name

* Feature: FEAT-CHK
* Description: Verify that checkout cannot continue when the last name is empty.
* Pre-condition: User is logged in, has a product in the cart, and is on the checkout information page.
* Execution Steps:

  1. Enter a valid first name.
  2. Leave the Last Name field empty.
  3. Enter a valid postal code.
  4. Click `Continue`.
* Expected Result: Checkout does not continue and an appropriate validation error is displayed.

## TC_CHK_005: Checkout With Empty Postal Code

* Feature: FEAT-CHK
* Description: Verify that checkout cannot continue when the postal code is empty.
* Pre-condition: User is logged in, has a product in the cart, and is on the checkout information page.
* Execution Steps:

  1. Enter a valid first name.
  2. Enter a valid last name.
  3. Leave the Postal Code field empty.
  4. Click `Continue`.
* Expected Result: Checkout does not continue and an appropriate validation error is displayed.

## TC_CHK_006: Checkout With All Required Fields Empty

* Feature: FEAT-CHK
* Description: Verify that checkout cannot continue when all required customer information fields are empty.
* Pre-condition: User is logged in, has a product in the cart, and is on the checkout information page.
* Execution Steps:

  1. Leave First Name empty.
  2. Leave Last Name empty.
  3. Leave Postal Code empty.
  4. Click `Continue`.
* Expected Result: Checkout does not continue and a validation error is displayed.

## TC_CHK_007: Verify Checkout Overview

* Feature: FEAT-CHK
* Description: Verify that the checkout overview displays the correct order information.
* Pre-condition: User has successfully entered valid checkout information and is on the checkout overview page.
* Execution Steps:

  1. Review the displayed product information.
  2. Review the displayed item price.
  3. Review the displayed subtotal.
  4. Review the displayed tax.
  5. Review the displayed total.
* Expected Result: The checkout overview displays the correct products, prices, subtotal, tax, and total amount.

## TC_CHK_008: Complete Order Successfully

* Feature: FEAT-CHK
* Description: Verify that a user can successfully complete an order.
* Pre-condition: User is logged in, has a product in the cart, has entered valid checkout information, and is on the checkout overview page.
* Execution Steps:

  1. Review the order details.
  2. Click the `Finish` button.
* Expected Result: The order is completed successfully and the order confirmation page is displayed.

## TC_CHK_009: Cancel Checkout

* Feature: FEAT-CHK
* Description: Verify that the user can cancel checkout before completing the order.
* Pre-condition: User is logged in and is on a checkout page.
* Execution Steps:

  1. Click the `Cancel` button.
* Expected Result: The user is returned to the appropriate previous page without completing the order.

# Feature: Navigation & System UI (FEAT-NAV)

## TC_NAV_001: Open Navigation Menu

* Feature: FEAT-NAV
* Description: Verify that the navigation menu can be opened.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Click the menu button.
* Expected Result: The navigation menu opens and available navigation options are displayed.

## TC_NAV_002: Close Navigation Menu

* Feature: FEAT-NAV
* Description: Verify that the navigation menu can be closed.
* Pre-condition: User is logged in and the navigation menu is open.
* Execution Steps:

  1. Click the close menu button.
* Expected Result: The navigation menu closes successfully.

## TC_NAV_003: Navigate to All Items

* Feature: FEAT-NAV
* Description: Verify that the All Items option navigates the user to the inventory catalog.
* Pre-condition: User is logged in and the navigation menu is open.
* Execution Steps:

  1. Click `All Items`.
* Expected Result: The user is navigated to the inventory catalog page.

## TC_NAV_004: Navigate to Cart Using Cart Icon

* Feature: FEAT-NAV
* Description: Verify that the shopping cart icon provides navigation to the cart page.
* Pre-condition: User is logged in and on the inventory catalog page.
* Execution Steps:

  1. Click the shopping cart icon.
* Expected Result: The user is navigated to the shopping cart page.

## TC_NAV_005: Logout From Navigation Menu

* Feature: FEAT-NAV
* Description: Verify that the Logout option in the navigation menu logs the user out.
* Pre-condition: User is logged in and the navigation menu is open.
* Execution Steps:

  1. Click `Logout`.
* Expected Result: The user is logged out and redirected to the SauceDemo login page.
## TC_NAV_006: Browser Back Navigation

* Feature: FEAT-NAV
* Description: Verify that browser Back navigation behaves correctly during normal navigation.
* Pre-condition: User is logged in and has navigated from the inventory page to another application page.
* Execution Steps:

  1. Click the browser Back button.
  2. Observe the displayed page.
* Expected Result: The browser navigates to the previous appropriate page without unexpected errors.
## TC_NAV_007: Browser Forward Navigation

* Feature: FEAT-NAV
* Description: Verify that browser Forward navigation behaves correctly after using browser Back.
* Pre-condition: User is logged in and has navigated between application pages.
* Execution Steps:

  1. Navigate to another page from the inventory page.
  2. Click the browser Back button.
  3. Click the browser Forward button.
* Expected Result: The browser returns to the previously visited application page correctly.

