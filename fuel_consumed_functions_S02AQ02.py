def cal_distance(Starting_values,Ending_values,Fuel_consumed,Dist_droven,tank_capacity ):
    Distance_travelled = Ending_values - Starting_values
    mileage = Distance_travelled / Fuel_consumed
    Dis = mileage * tank_capacity
    Number_of_stops = int(Dist_droven / Dis)
    return mileage, Number_of_stops

Starting_values = float(input("Enter the Starting_value:"))
Ending_values = float(input("Enter the Ending_values:"))
Fuel_consumed = float(input("Enter the value of Fuel_consumed:"))
Dist_droven = 560
tank_capacity = float(input("Enter the tank_capacity:"))
mileage,Number_of_stops = cal_distance(Starting_values,Ending_values,Fuel_consumed,Dist_droven,tank_capacity )
print("mileage is", mileage,"kms/litre" )
print("Number of stops = " ,Number_of_stops )
