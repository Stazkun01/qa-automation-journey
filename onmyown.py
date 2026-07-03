from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://sauce-demo.myshopify.com/account/login")
    page.fill("#customer_email" , "test@mail.com")
    page.fill("#customer_password" , "testpass.com")
    page.click("text = Sign In")
    page.screenshot(path="scrnonmyown.png")
    browser.close()
