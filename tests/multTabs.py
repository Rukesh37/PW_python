from playwright.sync_api import Page, expect

def test_mult_tabs(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator('input[class="wikipedia-search-input"]').fill('Football')
    page.locator('[class="wikipedia-search-button"]').click()
    page.wait_for_timeout(4000)
    page.locator('(//div[@class="wikipedia-search-results"]//child::a[1])[1]').click()
    page.wait_for_timeout(4000)
    page.locator('(//div[@class="wikipedia-search-results"]//child::a[1])[2]').click()
    page.wait_for_timeout(4000)
    page.locator('(//div[@class="wikipedia-search-results"]//child::a[1])[3]').click()
    page.wait_for_timeout(4000)
    page.locator('(//div[@class="wikipedia-search-results"]//child::a[1])[4]').click()
    page.wait_for_timeout(4000)
    pages= page.context.pages
    tabs1= pages[1]
    tabs2= pages[2]
    tabs3= pages[3]
    tabs1.bring_to_front()
    tabs1.wait_for_timeout(4000)
    tabs1.evaluate("window.scrollBy(0,400)")
    tabs1.wait_for_timeout(4000)
    tabs1.close()
    tabs2.bring_to_front()
    tabs2.wait_for_timeout(4000)
    tabs2.evaluate("window.scrollBy(0,400)")
    tabs2.wait_for_timeout(4000)
    tabs2.close()
    tabs3.bring_to_front()
    tabs3.wait_for_timeout(4000)
    tabs3.evaluate("window.scrollBy(0,400)")
    tabs3.wait_for_timeout(4000)
    tabs3.close()
    page.bring_to_front()
    page.wait_for_timeout(4000)
    page.evaluate("window.scrollBy(0,400)")
    page.wait_for_timeout(4000)
    