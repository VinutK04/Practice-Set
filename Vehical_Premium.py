class Vehical:
    def __init__(self, vehical_id, vehical_type, cost, premium):
        self.vehical_id = vehical_id
        self.vehical_type = vehical_type
        self.cost = cost
        self.premium = premium

    def premium_amount(self):
        if self.vehical_type == "Two Wheeler":
            self.premium = 2
        elif self.vehical_type == "Four Wheeler":
            self.premium = 6
        else:
            print("Enter Valid Vehical type")
            self.premium = 0
        total_cost = self.cost + self.cost * self.premium/100
        print("-----------------------")
        print("Vehical ID", self.vehical_id)
        print("Type",self.vehical_type)
        print("Cost",self.cost)
        print("Premium",self.premium)
        print("Total Cost", total_cost)
        print("-----------------------")

print("Vehical1")
v1 = Vehical(1001, "Two Wheeler", 10000, 2)
v1.premium_amount()

print("Vehical2")
v2 = Vehical(3003, "Three Wheeler", 30000, 3)
v2.premium_amount()

print("Vehical3")
v3 = Vehical(4004, "Four Wheeler", 40000, 4)
v3.premium_amount()