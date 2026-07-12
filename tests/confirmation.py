from playwright.sync_api import Page,expect

def test_confAlerts(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(4000)
    page.on('dialog',lambda dialog: dialog.accept())
    page.wait_for_timeout(4000)
    page.get_by_role('heading',name='Alerts & Popups').scroll_into_view_if_needed()
    page.wait_for_timeout(4000)
    page.evaluate("window.scrollBy(0,600)")
    page.wait_for_timeout(4000)
    page.get_by_role('button',name='Confirmation Alert').click()
    page.wait_for_timeout(4000)