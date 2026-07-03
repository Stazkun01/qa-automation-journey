from playwright.sync_api import sync_playwright
def testLogin(page,username,password,expected):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name" , username)
    page.fill("#password" , password)
    page.click("text= Login")

    if expected == "success":
        page.wait_for_selector(".inventory_list")
        print(f"✅ PASS — {username} logged in successfully")

    elif expected == "locked":
        error = page.text_content("[data-test='error']")
        assert "locked out" in error.lower()
        print(f"✅ PASS — locked_out_user correctly blocked")
    elif expected == "fail" :
        error = page.text_content("[data-test='error']")
        assert "do not match" in error.lower()
        print(f"✅ PASS — invalid credentials correctly rejected")
#test cases
test_cases = [
    ("standard_user",          "secret_sauce", "success"),
    ("locked_out_user",        "secret_sauce", "locked"),
    ("invalid_user",           "wrongpass",    "fail"),
]

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    for username , password , expected in test_cases:
        testLogin(page,username,password,expected)
    browser.close()