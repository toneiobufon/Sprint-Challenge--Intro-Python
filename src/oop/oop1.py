# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #base class for all vehicles
    pass

class FlightVehicle(Vehicle): #base class for flight vehilces and subclass of vehicles
    pass

class Starship(FlightVehicle, Vehicle): #base class for startships ans subclass of flightVehicle
    pass

class Airplane(FlightVehicle, Vehicle): # subclass of flightvehicle and vehicles
    pass


class GroundVehicle(Vehicle): #subclass of vehicle and base class for ground vehicles
    pass

class Car(GroundVehicle, Vehicle): #subclass of groundvehicle and inherits from vehicle
    pass

class Motorcycle(GroundVehicle): #subclass of groundvehicle and inherits from vehicle 
    pass

