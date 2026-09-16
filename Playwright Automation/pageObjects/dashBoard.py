from pageObjects import orderHistory


class DashBoard:
    def __init__(self, page):
        self.page = page
    
    def selectOrderNavLink(self):
        print("Hello")
        self.page.get_by_role("button", name= "ORDERS").click()
        print("Hello")
        orderHistoryPage = orderHistory.OrderHistory(self.page)
        return orderHistoryPage