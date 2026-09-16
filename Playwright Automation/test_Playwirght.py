import time

from flask import json
import playwright
from playwright.sync_api import Page, Playwright, expect
import pytest

from pageObjects.dashBoard import DashBoard
from pageObjects.login import LoginPage
from utils.apiBase import APIUtils

# def test_playwrightBasics(playwright):
#     browser = playwright.chromium.launch(headless=False) #launcing the chromium engine and headless is false in order to open the browser
#     context = browser.new_context() #above we just launched the engine here we are going to the incognito tab to search for the url
#     page = context.new_page() #here we openend a new page
#     page.goto("https://rahulshettyacademy.com") #hitting url
    
# def test_playwrightshorutcut(page:Page):
#     page.goto("https://rahulshettyacademy.com")
    
# def test_coreLocators(page:Page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractice/")
#     page.get_by_label("Username:").fill("rahulshettyacademy")
#     page.get_by_label("Password:").fill("Learning@830$3mK2")
#     page.get_by_role("combobox").select_option("teach")
#     page.get_by_role("link", name = "terms and conditions").click()
#     page.locator("#terms").check()
#     page.get_by_role("button",name = "Sign In").click()
#     iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
#     iphoneProduct.get_by_role("button").click()
#     nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
#     nokiaProduct.get_by_role("button").click()
#     page.get_by_text("Checkout").click()
#     expect(page.locator(".media-body")).to_have_count(2)
#     time.sleep(5)
    
# def test_childWindowHandle(page: Page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractice/")
#     with page.expect_popup() as newPage_info:
#         page.get_by_role("link",name = "Free Access to InterviewQues/ResumeAssistance/Material").click()
#         child_page = newPage_info.value
#         text = child_page.locator(".red").text_content()
#         print(text)
#         words = text.split("at")
#         email = words[1].strip().split(" ")[0]
#         print(email)
#         assert email == "mentor@rahulshettyacademy.com"
#         time.sleep(5)

# def test_moreValidations(page: Page):
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#     expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
#     page.get_by_role("button", name = "Hide").click()
#     expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
#     page.get_by_role("button",name = "Show").click()
    
    
#     page.on("dialog", lambda dialog: dialog.accept())
#     page.get_by_role("button", name = "Confirm").click()
    
    
#     page.locator("#mousehover").hover()
#     time.sleep(5)
#     page.get_by_role("link", name = "top")
#     time.sleep(5)
    
#     pageFrame = page.frame_locator("#courses-iframe")
#     pageFrame.get_by_role("link", name = "All Access plan").click()
#     expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
#     time.sleep(5)

# def test_tableEg(page: Page):
#     page.goto("https://rahulshettyacademy.com/seleniumPractice/#/offers")
#     for index in range(page.locator("th").count()):
#         if page.locator("th").nth(index).filter(has_text= "Price").count() > 0:
#             price_colValue = index
#             break
#     riceRow = page.locator("tr").filter(has_text="Rice")
#     expect(riceRow.locator("td").nth(price_colValue)).to_have_text("37")

# def test_newEg(playwright: Playwright):
#     browser = playwright.chromium.launch(headless= False)
#     context = browser.new_context()
#     page = context.new_page()
    
#     apiUtils = APIUtils()
#     orderId = apiUtils.createOrder(playwright)
    
#     page.goto("https://rahulshettyacademy.com/client")
#     page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
#     page.get_by_placeholder("enter your passsword").fill("Iamking@000")
#     page.get_by_role("button",name = "Login").click()
#     page.get_by_role("button", name= "ORDERS").click()
#     row = page.locator("tr").nth(1)
#     expect(row.locator("th").nth(0)).to_have_text(orderId)
#     btn = row.locator("td").nth(-2)
#     btn.get_by_role("button").click()
#     text = page.locator(".tagline").text_content()
#     print(text)
#     page.get_by_role("button", name= " Sign Out ").click()
#     time.sleep(5)

# fakePayloadOrderResponse = {"data": [], "message": "No Orders"}
# def intercept_response(route):
#     route.fulfill(
#         json = fakePayloadOrderResponse
#     )

# def test_network1(page: Page):
    # page.goto("https://rahulshettyacademy.com/client")
    # page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    # page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    # page.get_by_role("button",name = "Login").click()
    # page.get_by_role("button", name= "ORDERS").click()
#     text = page.locator(".mt-4").text_content()
#     print(text)
#     time.sleep(5)

# def intercept_response(route):
#     route.continue_(url = "https://rahulshettyacademy.com/api/ecom/orders/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


# def test_network2(page:Page):
#     page.goto("https://rahulshettyacademy.com/client")
#     page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_response)
#     page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
#     page.get_by_placeholder("enter your passsword").fill("Iamking@000")
#     page.get_by_role("button",name = "Login").click()
#     page.get_by_role("button", name= "ORDERS").click()
#     page.get_by_role("button", name= "View").first.click()
#     print(page.locator(".blink_me").text_content())
#     time.sleep(5)
    
# def test_session_storage(playwright: Playwright):
    
#     apiutils = APIUtils()
#     getTokenValue = apiutils.getToken(playwright)
#     browser = playwright.chromium.launch(headless= False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.add_init_script(f"""localStorage.setItem('token','{getTokenValue}')""")
#     page.goto("https://rahulshettyacademy.com/client")
#     page.get_by_role("button", name= "ORDERS").click()
#     expect(page.get_by_text("Your Orders")).to_be_visible()

with open("data/credentials.json") as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials_list = test_data["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_newEgPart2(playwright: Playwright, user_credentials, browserInstance):
    
        
    apiUtils = APIUtils()
    orderId = apiUtils.createOrder(playwright,user_credentials)
    
    loginPage = LoginPage(browserInstance,user_credentials)
    loginPage.navigate()
    dashboard = loginPage.login()
    
    orderHistoryPage = dashboard.selectOrderNavLink()
    
    orderDetails = orderHistoryPage.selectOrder(orderId)
    
    orderDetails.verifyOrder()
    
    browserInstance.get_by_role("button", name= " Sign Out ").click()
    time.sleep(5)