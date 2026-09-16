from playwright.sync_api import Playwright

# cred = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"}
prodData = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
class APIUtils:
    
    
    def getToken(self,playwright: Playwright, user_credentials):
        email = user_credentials["userEmail"]
        password = user_credentials["user_password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data= {"userEmail": email, "userPassword": password})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    
    def createOrder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data= prodData,
                                 headers= {"Authorization": token,
                                           "content-Type": "application/json"})
        print(response.json())
        responseBody = response.json()
        orderId = responseBody["orders"][0]
        return orderId
        