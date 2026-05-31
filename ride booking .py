# Parent Class
class Person:

    # Constructor
    def __init__(self, name):

        self.name = name


# Customer Class
class Customer(Person):

    def __init__(self, name):

        super().__init__(name)


# Driver Class
class Driver(Person):

    def __init__(self, name, vehicle):

        super().__init__(name)

        self.vehicle = vehicle


# Ride Class
class Ride:

    # Constructor
    def __init__(self, customer, driver, distance):

        self.customer = customer
        self.driver = driver

        # Private Variable
        self.__distance = distance

        # Ride Status
        self.status = "Booked"

    # Fare Calculation
    def calculate_fare(self):

        fare = self.__distance * 15

        return fare

    # Ride Details
    def show_ride_details(self):

        print("\n----- Ride Details -----")

        print("Customer:", self.customer.name)

        print("Driver:", self.driver.name)

        print("Vehicle:", self.driver.vehicle)

        print("Distance:", self.__distance, "KM")

        print("Fare: ₹", self.calculate_fare())

    # Track Ride
    def track_ride(self):

        print("\nRide Status:", self.status)

        self.status = "Driver Arriving"

        print("Ride Status:", self.status)

        self.status = "Ride Started"

        print("Ride Status:", self.status)

        self.status = "Ride Completed"

        print("Ride Status:", self.status)


# Customer Object
c1 = Customer("Shashi")

# Driver Object
d1 = Driver("Rahul", "Swift Dzire")

# Ride Booking
ride1 = Ride(c1, d1, 10)

# Show Ride Details
ride1.show_ride_details()

# Track Ride
ride1.track_ride()