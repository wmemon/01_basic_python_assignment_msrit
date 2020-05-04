temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
print(f"Ascending sorted:- {temps}")
print()
cool_temps,warm_temps = temps[:2],temps[2:]
print(f"cool_temps:- {cool_temps} ,warm_temps:- {warm_temps}")
print()
temps_in_celsius = cool_temps+warm_temps
print(f"temp_in_celsius:- {temps_in_celsius}")
