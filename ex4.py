cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_drivern=cars-drivers
cars_drivern=drivers
carpool_capacity=cars_drivern*space_in_a_car
average_passenger_per_car=passengers/cars_drivern


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers avaliable.")
print("There will be",cars_not_drivern,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We need to put about",average_passenger_per_car,"in each car.")