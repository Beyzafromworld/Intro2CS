plan = ["cook", "study", "watch movie", "read book", "walk"]
print(plan[0])
print(plan[4])
print(plan[1:4])
print(plan[::-1])
plan[1] = "exercise"
print(plan)
plan.append("sleep")
print(plan)
plan.insert(0, "wake up")
print(plan)
plan.remove("cook")
print(plan)
weekend_plan = ["go shopping", "go hiking"]
print(plan + weekend_plan)

city = ("Poznan", "Poland", "52,41", "16,93")
print(city[1])
print(city[3])
print(type(city))
the_city, country, latitude, longitude = city
print(the_city, country)
list_city = list(city)
list_city[1] = "Germany"
city = tuple(list_city)
print(city)
