from playwright.sync_api import Page,expect

def test_uploadefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role('heading',name='Upload Files').scroll_into_view_if_needed()
    page.evaluate("window.scrollBy(0,300)")
    page.wait_for_timeout(4000)
    page.locator('[id="singleFileInput"]').set_input_files("C:/Users/DELL/Desktop/Testing_file.txt")
    page.wait_for_timeout(4000)
    page.get_by_role('button',name='Upload Single File').click()
    page.wait_for_timeout(4000)

def test_multFileUpload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role('heading',name='Upload Files').scroll_into_view_if_needed()
    page.evaluate('window.scrollBy(0,300)')
    page.wait_for_timeout(4000)
    page.locator('[id="multipleFilesInput"]').set_input_files(["C:/Users/DELL/Documents/test.txt","C:/Users/DELL/Desktop/Testing_file.txt","C:/Users/DELL/Documents/testing.pdf.txt","C:/Users/DELL/Downloads/1.txt"])
    page.wait_for_timeout(4000)
    page.get_by_role('button',name='Upload Multiple Files').click()
    page.wait_for_timeout(4000)