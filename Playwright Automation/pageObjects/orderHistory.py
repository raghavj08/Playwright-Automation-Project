from playwright.sync_api import expect

from pageObjects.orderDetails import OrderDetails
class OrderHistory:
    
    def __init__(self, page):
        self.page = page
        
    def selectOrder(self, orderId):
        row = self.page.locator("tr").filter(has_text = orderId)
        row.get_by_role("button", name = "View").click()
        orderDetails = OrderDetails(self.page)
        return orderDetails
        