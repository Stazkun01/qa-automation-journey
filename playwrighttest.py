from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://saucedemo.com")
    page.fill("#user-name" , "standard_user")
    page.fill("#password" , "secret_sauce")
    page.click("text=Login")
    page.screenshot(path="screenshot.png")
    page.wait_for_selector(".inventory_list")
    print("Login successful!")