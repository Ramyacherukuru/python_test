lap_michael     = (258.626, 255.931, 258.998, 255.195)
lap_montoya     = (258.680, 257.925, 259.828, 257.422)
lap_barrichello = (258.405, 256.700, 260.395)

#To find fastest lap for each driver

fastest_lap_michael = min(lap_michael)
fastest_lap_montoya = min(lap_montoya)
fastest_lap_barrichello = min(lap_barrichello)

print("Fastest lap for Michael Schumacher:", fastest_lap_michael)
print("Fastest lap for Montoya Juan-Pablo:", fastest_lap_montoya)
print("Fastest lap for Barrichello Rubens:", fastest_lap_barrichello)


#To find the average speed for each driver

lap_michael_avg = sum(lap_michael) / len(lap_michael)
lap_montoya_avg = sum(lap_montoya) / len(lap_montoya)
lap_barrichello_avg = sum(lap_barrichello) / len(lap_barrichello)

print("Average speed for Michael Schumacher:", lap_michael_avg)
print("Average speed for Montoya Juan-Pablo:", lap_montoya_avg)
print("Average speed for Barrichello Rubens:", lap_barrichello_avg)

#To find which driver has recorded the fastest lap
fastest_lap_driver = min(fastest_lap_michael, fastest_lap_montoya, fastest_lap_barrichello)

if fastest_lap_driver == fastest_lap_michael:
    print("Michael Schumacher has recorded the fastest lap")
elif fastest_lap_driver == fastest_lap_montoya:
    print("Montoya Juan-Pablo has recorded the fastest lap")
else:
    print("Barrichello Rubens has recorded the fastest lap")


# To find fastest lap average
fastest_lap_avg = min(lap_michael_avg, lap_montoya_avg, lap_barrichello_avg)

if fastest_lap_avg == lap_michael_avg:
    print("Michael Schumacher has fastest lap average")
elif fastest_lap_avg == lap_montoya_avg:
    print("Montoya Juan-Pablo has fastest lap average")
else:
    print("Barrichello Rubens has fastest lap average")


