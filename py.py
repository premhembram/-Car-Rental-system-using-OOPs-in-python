
class Car:
    def _init_(self, car_id, model, rate_per_day):
        self.car_id = car_id
        self.model = model
        self.rate_per_day = rate_per_day
        self.available = True

    def _str_(self):
        status = "Available" if self.available else "Not Available"
        return f"Car {self.car_id}: {self.model} - {status}"

class Customer:
    def _init_(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def _str_(self):
        return f"Customer {self.customer_id}: {self.name}"
class Rental:
    def _init_(self, car, customer, days):
        self.car = car
        self.customer = customer
        self.days = days
        self.total_cost = car.rate_per_day * days

    def process_rental(self):
        if self.car.available:
            self.car.available = False
            print(f"{self.customer.name} rented {self.car.model} for {self.days} days. Total cost: ${self.total_cost}")
        else:
            print(f"Sorry, {self.car.model} is not available.")

def return_car(self):
        self.car.available = True
        print(f"{self.customer.name} returned {self.car.model}. Thank you!")
car1 = Car(1, "Toyota Camry", 50)
car2 = Car(2, "Honda Civic", 40)

customer1 = Customer(101, "Alice")
customer2 = Customer(102, "Bob")

print(car1)
print(car2)

rental1 = Rental(car1, customer1, 3)
rental1.process_rental()

print(car1) 

rental2 = Rental(car1, customer2, 2)
rental2.process_rental() 

rental1.return_car()
print(car1)  