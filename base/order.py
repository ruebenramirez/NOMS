
class OMSOrder():
    def __init__(self, seller, customer, orderLineItems):
        self.seller = seller
        self.customer = customer
        self.orderLineItems
        self.customerApproved = false
        self.sellerApproved = true

    def customerApprove(self):
        self.customerApproved = true

    def sellerApproved(self):
        self.sellerApproved = true

    def isApproved(self):
        approved = self.customerApproved && self.sellerApproved
        return approved

    def processOrder(self):
        if isApproved():
            # continue to process
            pass
