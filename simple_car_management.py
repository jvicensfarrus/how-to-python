#!/usr/bin/env python
# -*-coding:utf-8-*-
#Developed by Jordi Vicens Farrus
#Very simple application where you can manage entries for a new cars and where you can save/see this entries into a file.
import string
import time
from time import sleep

#Create class and methods
class Car():
    cars = 0
    def __init__(self, brand=None, color=None, fuel=None, price=None):
        self.brand = brand
        self.color = color
        self.fuel = fuel
        self.price = price

        if brand is not None and color is not None and fuel is not None and price is not None:
            self.cars = self.cars+1
            newfile = open("cars.txt", "a")
            newfile.write("| Car brand: {} - Car color: {} - Car fuel: {} - Car price: {} |\n".format(self.brand, self.color, self.fuel, self.price))
            newfile.close()
            print("New car created successfully.\n\n")

    def showcars(self):
        readfile=open("cars.txt", "r+")
        allcars = readfile.read()
        readfile.close()
        return allcars

option = 0
while True:
    #Enter to the menu
    if option == 0:
        print("What do you want to do?\n")
        option = int(input("1.-Enter a new car | 2.-Show all the cars | 3.-Exit\n"))
    #Entry new car
    elif option==1:
        print("Let's entry a new car.")
        brand = raw_input("From which brand is this car?\n").lower()
        color = raw_input("In which color?\n").lower()
        fuel = raw_input("Which fuel use this %s?\n" % brand).lower()
        price = raw_input("Which price has this car?\n")

        c = Car(brand, color, fuel, price)
        option = 0
    #Read the file and print it.
    elif option == 2:
        c = Car()
        print(c.showcars())
        print("\n")
        option = 0
        sleep(1)
    #Exit program
    elif option == 3:
        exit("Thank you so much for using me.")
    else:
        option = 0
