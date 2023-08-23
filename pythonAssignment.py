# SHASHWAT JAIN
# SOFTWARE ENGINEERING LAB 4 ASSIGNMENT
# PYTHON ASSIGNMENT

# Q1. Write a Python program to search and print the result data of the above table.
# User must have option to choose the search parameter
# 1. Flights for a particular City, 
# 2. Flights From a city, 
# 3. Flights between two given cities.

class Flights:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

    def tocity(self, input_city):
        lst = []
        for i in range(len(self.to_city)):
            if self.to_city[i] == input_city.upper():
                lst.append(i)
        return lst

    def fromcity(self, input_city):
        lst = []
        for i in range(len(self.from_city)):
            if self.from_city[i] == input_city.upper():
                lst.append(i)
        return lst

    def fromtocity(self, input_cities):
        lst = []
        for i in range(len(self.from_city)):
            if self.from_city[i] == input_cities[0].upper() and self.to_city[i] == input_cities[1].upper():
                lst.append(i)
        return lst

    def display(self, lst):
        if len(lst) == 0:
            print("No flights found")
        else:
            print("Flight ID\tFrom\tTo\tPrice")
            for i in lst:
                print(f"{self.flight_id[i]}\t\t{self.from_city[i]}\t{self.to_city[i]}\t{self.price[i]}")

Flight_id = ['AI161E90', 'BR161F91', 'AI161F99', 'VS171E20', 'AS171G30', 'AI131F49']
From = ["BLR", "BOM", "BBI", "JLR", "HYD", "HYD"]
To = ["BOM", "BBI","BLR","BBI", "JLR", "BOM"]
Price = [5600,6750,8210,5500,4400,3499]

f = Flights(Flight_id, From, To, Price)
print("Enter your Preference: \n1. Flights for a particular City\n2. Flights From a city\n3. Flights between two given cities")
choice = int(input("Your Preference: "))
if choice == 1:
    print("Enter the City you want to travel to: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur")
    input_city = input("Your choice only initials: ").upper()
    lst = f.tocity(input_city)
    f.display(lst)
elif choice == 2:
    print("Enter the City you want to travel from: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur")
    input_city = input("Your choice: ").upper()
    lst = f.fromcity(input_city)
    f.display(lst)
elif choice == 3:
    print("Enter the City you want to travel from and to i.e. From to: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur")
    input_cities = input("Your choice: ").split()
    lst = f.fromtocity(input_cities)
    f.display(lst)