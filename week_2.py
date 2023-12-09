def k_to_f(kelvin):
  return (kelvin - 273.15) * 9 / 5 + 32


city_name = data["city"]["name"]
country_name = data["city"]["country"]

temps = []
humidities = []
uniq_descriptions = set()
min_temp = 1000
max_temp = -1000
min_temp_ts = None
max_temp_ts = None
for item in data["list"]:
  temp = item["main"]["temp"]
  temps.append(temp)
  if temp > max_temp:
    max_temp = temp
    max_temp_ts = item["dt_txt"]
  if temp < min_temp:
      min_temp = temp
      min_temp_ts = item["dt_txt"]
  if item["wind"]["speed"] > 1:
        humidities.append(item["main"]["humidity"])
  for weather_item in item["weather"]:
          uniq_descriptions.add(weather_item["description"])

avg_temp = k_to_f(sum(temps) / len(temps))
avg_humidities = sum(humidities) / len(humidities)
min_temp_f = k_to_f(min_temp)
max_temp_f = k_to_f(max_temp)
uniq_descriptions_str = ",".join(uniq_descriptions)

print(f"City Name: {city_name}")
print(f"Country Name: {country_name}")
print(f"Average Temperature: {avg_temp:.2F}")
print(
    f"Average humidity when wind speed is greater than 1: {avg_humidities:.2F}"
)
print(f"all distrinct weather descriptions:{uniq_descriptions_str}")
print(f"Minimum temperature: {min_temp_f:.2F}")
print(f"Timestamp for mininum temperature:{min_temp_ts}")
print(f"Maximum temperature: {max_temp_f:.2F}")
print(f"Timestamp for maximun temperature:{max_temp_ts}")
