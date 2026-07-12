from playwright.sync_api import Page

def test_tabs(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(4000)
    page.locator('input[class="wikipedia-search-input"]').fill('Football')
    page.locator('[class="wikipedia-search-button"]').click()
    page.wait_for_timeout(4000)
    page.locator('(//div[@class="wikipedia-search-results"]//child::a[1])[1]').click()
    page.wait_for_timeout(4000)
    new_page= page.context
    page1=new_page.pages[1]
    page1.wait_for_timeout(4000)
    page1.evaluate("window.scrollBy(0,400)")
    page1.wait_for_timeout(4000)
    page1.close()
    page.wait_for_timeout(4000)
    page.evaluate("window.scrollBy(0,400)")
    page.wait_for_timeout(4000)