Starting_values = float(input("Enter the Starting_value:"))
Ending_values = float(input("Enter the Ending_values:"))
Fuel_consumed = float(input("Enter the value of Fuel_consumed:"))
Distance_travelled = Ending_values - Starting_values
mileage = Distance_travelled / Fuel_consumed
print("mileage is", mileage,"kms/litre" )
Distance_droven = 560
tank_capacity = float(input("Enter the tank_capacity:"))
Dis = mileage * tank_capacity
Number_of_stops = int(Distance_droven / Dis)
print("Number of stops = " ,Number_of_stops )
