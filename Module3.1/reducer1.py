import sys

attributes = ['Totalcases', 'Activecases', 'Totaldeaths', 'Totalrecovered', 'Totaltests', 'DeathsPer1M', 'TestsPer1M', 'Newcases', 'Newdeaths', 'Newrecovered']
country_data = []
world_data = []

for line in sys.stdin:
    line = line.strip().split('-')
    if line[0] == 'World':
        world_data.extend(line[1:])
    else:
        country_data.extend(line[1:])

for i, attribute in enumerate(attributes):
    print(f"{attribute}---{country_data[i]}")

print('\n\n\n')
print('percent in change w.r.t world cases:\n')

for i, attribute in enumerate(attributes):
    world_val = float(world_data[i].replace(',', '')) if world_data[i] != 'N/A' else 0
    country_val = float(country_data[i].replace(',', '')) if country_data[i] != 'N/A' else 0

    percentage_change = (country_val / world_val) * 100 if world_val != 0 else 0
    print(f"{attribute}---{percentage_change}")
