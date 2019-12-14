#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:07:25 2019

@author: mirjamheinemans
"""

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        """Simulate rolling over in response to a command."""
        
        
        #%%

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("the name of the restaurant is " + self.name.title())
        print("the type of food is " + self.cuisine)
    def open_restaurant(self):
        print("the restaurant is open from 12-24")
    
    def set_number_served(self,servings):
        self.number_served = servings
        
    def increment_number_served(self, increase):
        self.number_served += increase         


restaurant = Restaurant("Holland", "pannekoek")
        
#%%
class User():
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        self.login_attempts = 0
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
#%%
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage): 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles
        
    
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())


my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100) 
my_used_car.read_odometer()

#%%
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70): 
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
             range = 240
        elif self.battery_size == 85:
             range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

#%%
class ElectricCar(Car):
       """Represent aspects of a car, specific to electric vehicles."""
       def __init__(self, make, model, year):
           """
           Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
           """
           super().__init__(make, model, year)
           self.battery = Battery()
           def describe_battery(self):
"""Print a statement describing the battery size."""
print("This car has a " + str(self.battery_size) + "-kWh battery.")
           
           
           
#%%
           
           
           
           
           