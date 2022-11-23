"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):
    price_per_km = 1.23

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self, price_per_km=1.23):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${price_per_km:.2f}/km"

    def get_fare(self):
        return round(self.price_per_km * self.current_fare_distance)

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
