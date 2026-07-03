from playwright.sync_api import sync_playwright
def test_valid_login():
    username = "standard_user"
    password = "secret_sauce"
    expected =  "success"
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name" , username)
        page.fill("#password" , password)
        page.click("text= Login")
        if expected == "success":
            page.wait_for_selector(".inventory_list")
            print(f"✅ PASS — {username} logged in successfully")

def test_locked_user():
    username = "locked_out_user"
    password = "secret_sauce"
    expected =  "locked"
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name" , username)
        page.fill("#password" , password)
        page.click("text= Login")
        if expected == "locked":
            error = page.text_content("[data-test='error']")
            assert "locked out" in error.lower()
            print(f"✅ PASS — locked_out_user correctly blocked")
def test_invalid_credentials():        
    username = "invalid_user"
    password = "wrongpass"
    expected =  "fail"
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name" , username)
        page.fill("#password" , password)
        page.click("text= Login")
        if expected == "fail" :
            error = page.text_content("[data-test='error']")
            assert "do not match" in error.lower()
            print(f"✅ PASS — invalid credentials correctly rejected")

