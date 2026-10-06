# single inheritance Example with runtime polymorphism

class FoodOrder:
    def __init__(self,cust_name,order_amount):
        self.cust_name=cust_name
        self.order_amount=order_amount
    def details(self):
        print("Customer Name: ",self.cust_name)
        print("Order Amount : ",self.order_amount)    
    def calculate_total(self):
        print("Total Amount : ",self.order_amount)
class OnlineOrder(FoodOrder):
    def __init__(self,cust_name,order_amount):
        super().__init__(cust_name,order_amount)
           
    def calculate_total(self):
        if self.order_amount < 500:
            delivery_charge = 50
        elif self.order_amount < 1000:
            delivery_charge = 30
        else:
            delivery_charge = 0
        total_amount=self.order_amount+delivery_charge
        
        print("Total Amount After Delivary : ",total_amount)
f=FoodOrder("Vishnu",400)
f.details()
f.calculate_total()
o=OnlineOrder("Vishnu",900)
o.calculate_total()

# Movie Ticket

class MovieTicket:
    def __init__(self,movie_name,ticket_price,number_of_ticket):
        self.movie_name=movie_name
        self.ticket_price=ticket_price
        self.number_of_ticket=number_of_ticket
    def  calculate_total(self):
        total=self.ticket_price*self.number_of_ticket
        print("Movie Name: ",self.movie_name)
        print("Ticket Price : ",self.ticket_price)
        print("Total No of Tickets : ",self.number_of_ticket)
        print("Total Amount : ",total)
class PremiumSeat(MovieTicket):
    def __init__(self,movie_name,ticket_price,number_of_ticket):
        super().__init__(movie_name,ticket_price,number_of_ticket)
    def calculate_total(self):
        if self.number_of_ticket >= 5:
            total=self.ticket_price * self.number_of_ticket
            discount=total * (10/100)
            total_price=total-discount
            print("More than 5 Tickets got 10% Discount Total Price : ",total_price)
        
        premium_charge=self.number_of_ticket*150
        premium_price=self.ticket_price*self.number_of_ticket+premium_charge 
        print("Total Price Premium Ticket: ",premium_price) 
m=MovieTicket("Irumudi",250,2)
m.calculate_total() 
p=PremiumSeat("Irumudi",250,5)
p.calculate_total()                     


# Hierarichal inheritance runtime polymorphism


# class Employee:
#     def __init__(self,name,employee_id,base_salary):
#         self.name=name
#         self.employee_id=employee_id
#         self.base_salary=base_salary
#     def display_details(self):
#         print("Name : ",self.name)
#         print("ID : ",self.employee_id)
        
#     def calculate_salary(self):
#         print("Base Salary : ",self.base_salary) 

# class Manager(Employee):
#     def __init__(self,name,employee_id,base_salary,team_size):
#         super().__init__(name,employee_id,base_salary)
#         self.team_size=team_size
#     def  team(self):
#         super().display_details()
#         print("Size : ",self.team_size)
#     def calculate_salary(self):
#         salary=self.base_salary*(20/100)
#         total=self.base_salary+salary
#         print("Manager Salary : ", int(total))   

# class Devloper(Employee):
#     def __init__(self,name,employee_id,base_salary,Program_language):
#         super().__init__(name,employee_id,base_salary)
#         self.Program_language=Program_language
#     def  Language_knowm(self):
#         super().display_details()
#         print("Language : ",self.Program_language)
#     def calculate_salary(self):
#         salary=self.base_salary*(10/100)
#         total=self.base_salary+salary
#         print("Devloper Salary : ", int(total))   


# e=Employee("Vishnu",1003,30000)
# e.display_details()
# e.calculate_salary()

# d=Devloper("Vishnu",1001,30000,"Python")
# d.calculate_salary()

# manager=Manager("Vishnu",1002,30000,4)
# manager.calculate_salary()


# # Payment Process System


# class Payment:
#     def __init__(self,amount):
#         self.amount=amount
#     def caliculate_fee(self):
#         print("Final Amount : ",self.amount)
# class Upi(Payment):
#     def __init__(self,amount):
#         super().__init__(amount)
#     def caliculate_fee(self):
#         fee=self.amount*(1/100)
#         total_fee=self.amount+fee
#         print("Amount After UPI Charge: ",int(total_fee))
# class Card(Payment):
#     def __init__(self,amount):
#         super().__init__(amount)
#     def caliculate_fee(self):
#         fee=self.amount*(2/100)
#         total_fee=self.amount+fee
#         print("Amount After Card Chharges: ",int(total_fee))

# pay=Payment(5000)
# pay.caliculate_fee()

# upi=Upi(5000)
# upi.caliculate_fee()

# card=Card(5000)
# card.caliculate_fee()        

# # multi Level Examples runtime polymorphism

# class Vehicle:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def calculate_cost(self):
#         return self.price

# class Car(Vehicle):
#     def calculate_cost(self):
#         insurance = self.price * 0.05
#         return self.price + insurance

# class ElectricCar(Car):
#     def calculate_cost(self):
#         insurance = self.price * 0.04
#         subsidy = 50000
#         return self.price + insurance - subsidy


# v = Vehicle("Tata", 800000)
# c = Car("Hyundai", 800000)
# elec = ElectricCar("Tata", 800000)

# print("Vehicle Cost:", v.calculate_cost())
# print("Car Cost:", int(c.calculate_cost()))
# print("Electric Car Cost:", int(elec.calculate_cost()))

# # Products

# class Product:
#     def __init__(self, product_name, price):
#         self.product_name = product_name
#         self.price = price

#     def calculate_final_price(self):
#         return self.price

# class Electronics(Product):
#     def calculate_final_price(self):
#         gst = self.price * 0.18
#         total = self.price + gst
#         return total

# class Laptop(Electronics):
#     def calculate_final_price(self):
#         gst = self.price * 0.18
#         discount = self.price * 0.10
#         total = self.price + gst - discount
#         return total

# p = Product("Product", 50000)
# e = Electronics("Electronic Item", 50000)
# l = Laptop("Dell Laptop", 50000)

# print("Product Price:", int(p.calculate_final_price()))
# print("Electronics Price:", int(e.calculate_final_price()))
# print("Laptop Price:", int(l.calculate_final_price()))


# multiple Inheritance runtime polymorphism

class Employee:
    def work(self):
        print("Employee is working")
    def show(self):
        print("Employee details")

class Skills:
    def work(self):
        print("Skills are being practiced")
    def programming(self):
        print("Programming: Python")

class Developer(Employee, Skills):
    def work(self):
        print("Developer is writing code")

    def develop_project(self):
        print("Developer is developing a project")

dev = Developer()
dev.work()
dev.show()
dev.programming()
dev.develop_project()
