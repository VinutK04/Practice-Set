class Customer:
    def __init__(self, customer_name, bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount

    def purchase(self):
        discount = 5
        self.amount = self.bill_amount - self.bill_amount*discount/100
        return self.amount

    def pays_bill(self, amount):
        print(self.customer_name,"Pay bill amount of Rs.",self.amount)

c1 = Customer("Vinut", 10000)
c2 = Customer("Virat", 20000)
c3 = Customer("Vikram", 30000)

c3.purchase()
c3.pays_bill(30000)