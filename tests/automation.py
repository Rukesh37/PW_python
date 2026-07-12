from playwright.sync_api import Page,expect
import random
import time
from datetime import datetime, timedelta
current_time=datetime.now().strftime("%m/%d/%Y")
future_date=datetime.now()+timedelta(days=7)
print(current_time)
print(future_date.strftime("%m/%d/%Y"))


def test_automation(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/",timeout=5000)
    page.get_by_placeholder("Enter Name").fill("Test")
    page.get_by_placeholder("Enter EMail").fill("Testing@gmail.com")
    page.wait_for_timeout(4000)
    page.get_by_placeholder("Enter Phone").fill("1234567890")
    page.wait_for_timeout(4000)
    page.evaluate("window.scrollBy(0,400);")
    page.wait_for_timeout(4000)
    page.locator('[id="textarea"]').fill("this is my address please do not contact to me.")
    page.locator('[id="male"]').click()
    page.wait_for_timeout(4000)
    page.locator('[id="sunday"]').check()
    page.wait_for_timeout(4000)
    page.evaluate("window,scrollBy(0,400)")
    page.locator('[id="country"]').click()
    page.wait_for_timeout(4000)
    countrys=page.locator('[id="country"] option').all_inner_texts()
    #print('Country:', countrys.strip())
    state=[]
    for country in countrys:
        print('Country:', country.strip())
        state.append(country.strip())
    page.wait_for_timeout(4000)
    print('Total Country:', len(state), state)
    random_country=random.choice(state)
    page.locator('[id="country"]').select_option(random_country)
    page.wait_for_timeout(4000)
    page.keyboard.press('Enter')
    page.wait_for_timeout(4000)
    colors=page.locator('[id="colors"] option').all_inner_texts()
    mcolor=[]
    for color in colors:
        print('Color:', color.strip())
        mcolor.append(color.strip())
    page.wait_for_timeout(4000)
    random_color=random.choice(mcolor)
    page.locator('[id="colors"]').select_option(random_color)
    page.wait_for_timeout(4000)
    animals=page.locator('[id="animals"] option').all_inner_texts()
    manimals=[]
    for animal in animals:
        print('Animal:', animal.strip())
        manimals.append(animal.strip())
    page.wait_for_timeout(4000)
    random_animal=random.choice(manimals)
    page.locator('[id="animals"]').select_option(random_animal)
    page.wait_for_timeout(4000)
    page.locator('[id="datepicker"]').fill(current_time)
    page.keyboard.press('Enter')
    page.wait_for_timeout(4000)
    page.keyboard.press('Tab')
    page.locator('[name="SelectedDate"]').fill(str(future_date))
    page.keyboard.press('Enter')

    page.wait_for_timeout(4000)