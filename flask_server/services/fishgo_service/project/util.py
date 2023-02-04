from playwright.sync_api import Playwright, sync_playwright
def flash_bang():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_context().new_page()

        page.goto("http://10.2.177.147:8080/")

        button = page.query_selector("#flashbtn")
        button.click()

        browser.close()