from playwright.sync_api import Page,expect

def test_dataFiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role('heading',name='Static Web Table').scroll_into_view_if_needed()
    page.wait_for_timeout(4000)
    bookTables=page.locator('[name="BookTable"]').all_text_contents()
    book=[]
    for bookTable in bookTables:
        book.append(bookTable.strip())

    print(book)

    locotor=page.locator('[name="BookTable"]').filter(has_text="Javascript")
    print(locotor)
    page.wait_for_timeout(5000)

def test_row_select(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role('heading',name='Static Web Table').scroll_into_view_if_needed()
    page.wait_for_timeout(4000)
    rows=page.locator('[name="BookTable"] tr')
    selenium_row=rows.filter(has_text="Selenium")
    count=selenium_row.count()
    for i in range(count):
        print(selenium_row.nth(i).inner_text())
    page.close()
    
