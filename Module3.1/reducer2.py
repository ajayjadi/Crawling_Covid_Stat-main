import sys

min_difference = float('inf')
initial_iteration = 0
country_data = []
temporary_data = []

for line in sys.stdin:
    if initial_iteration == 0:
        line = line.strip().split('-')
        last_four_values = line[-4:]

        for value in last_four_values:
            country_data.append(float(value))

        print(line[0])
        closest_country = line[0]
        print('Change in active cases in %', country_data[0])
        print('Change in daily deaths in %', country_data[1])
        print('Change in new recovered in %', country_data[2])
        print('Change in new cases in %', country_data[3])
        initial_iteration = 1
    else:
        line = line.strip().split('-')
        last_four_values = line[-4:]

        for value in last_four_values:
            temporary_data.append(float(value))

        for i in range(4):
            val = abs(temporary_data[i] - country_data[i])
            if val == 0:
                closest_country = line[0]
                print('Closest country similar to any query is')
                print(f"{closest_country} for Query {i+1}")
                exit()
            elif val < min_difference:
                min_difference = val
                closest_country = line[0]
        temporary_data.clear()

print('Closest country similar to any query is')
print(closest_country, initial_iteration)
