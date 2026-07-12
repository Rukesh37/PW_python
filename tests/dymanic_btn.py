from playwright.sync_api import Page, expect

def test_dynamic_btn(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(4000)
    page.evaluate("window.scrollBy(0,400)")
    page.wait_for_timeout(4000)
    page.get_by_role('button',name="START").hover()
    page.wait_for_timeout(4000)
    page.get_by_role('button',name="START").click()
    page.wait_for_timeout(4000)
    page.get_by_role('button',name="STOP").click()
    page.wait_for_timeout(4000)
    page.get_by_role('button',name="START").click()
    page.wait_for_timeout(4000)