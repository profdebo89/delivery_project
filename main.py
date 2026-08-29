from package import Package
from hash_table import HashTable
import datetime

def str_to_time(the_str):
	hour, minute, second = 0, 0, 0
	time_info = the_str.strip().split(":")
	if len(time_info) > 2:
		hour, minute, second = int(time_info[0]), int(time_info[1]), int(time_info[2][0:2])
	the_time = datetime.timedelta(hours=hour, minutes=minute, seconds=second)
	return the_time


def delivery(the_truck, start_time, user_time, h_table, the_list, the_dict):
	current_address = "HUB"
	truck_speed = 18.0
	truck_route_distance = 0.0
	truck_index = 0
	package_obj = None
	current_time = start_time
	delivered_packages = []

	while len(the_truck) > 0:

		current_index = the_dict[current_address]
		dest_address = ""
		min_distance = 140.0

		# find the address closest to current address
		for item in range(len(the_truck)):

			# find address
			temp_package_obj = h_table.lookup(the_truck[item])

			if temp_package_obj.get_id() == 9 and user_time >= datetime.timedelta(hours=10, minutes=20):
				temp_package_obj.set_address("410 S State St")
				temp_package_obj.set_city("Salt Lake City")
				temp_package_obj.set_zip_code("84111")

			# temp_package_obj.set_loading_time(start_time)

			temp_dest_address = temp_package_obj.get_address()

			# get index of address from dictionary
			dest_index = the_dict[temp_dest_address]

			if current_index >= dest_index:
				distance = float(the_list[current_index][dest_index])
			else:
				distance = float(the_list[dest_index][current_index])

			# Find the closest address based on the current minimum distance
			if distance < min_distance:
				min_distance = distance
				package_obj = temp_package_obj
				truck_index = item
				dest_address = temp_dest_address

		package_obj.set_loading_time(start_time)

		print(f"current_address: {current_address}, destination: {dest_address}, min_distance = {min_distance}")

		time_to_dest = (min_distance / truck_speed) * 3600

		delivery_time = current_time + datetime.timedelta(seconds=time_to_dest)

		package_obj.set_delivery_time(delivery_time)

		package_obj.set_delivery_status(user_time)

		print(package_obj)

		# Change current address

		current_address = dest_address

		# Increment the total distance the truck travels

		truck_route_distance += min_distance

		# Set start time to delivery time of the package

		current_time = delivery_time

		# Remove package from the truck

		the_truck.pop(truck_index)

	return truck_route_distance
	
def main():

	input_time_str = input("Enter time in 24-hr format (HH:MM:SS)  ")
	input_time = str_to_time(input_time_str)

	hash_table = HashTable()
	distance_dict = {}
	distance_list = []
	load_time_01 = datetime.timedelta(hours=8, minutes=0, seconds=0)
	load_time_02 = load_time_01 + datetime.timedelta(hours=1, minutes=6)
	load_time_03 = load_time_01 + datetime.timedelta(hours=2, minutes=20)

	# Get package data from package-file.csv
	with open("package-file.csv", "r") as package_file:
		package_file_content = package_file.read()
	package_lines = package_file_content.split("\n")

	for line_num in range(1, len(package_lines)-1):
		package_info = package_lines[line_num].split(",")
		package = Package()
		package.set_id(int(package_info[0]))
		package.set_address(package_info[1])
		package.set_city(package_info[2])
		package.set_state(package_info[3])
		package.set_zip_code(package_info[4])
		package.set_deadline(str_to_time(package_info[5]))
		package.set_weight(package_info[6])
		package.set_loading_time(load_time_01)
		package.set_delivery_time(load_time_01)
		package.set_delivery_status(input_time)
		hash_table.insert(package.get_id(), package)

	# Get distance data from file
	with open("distance-file.csv", "r") as distance_file:
		distance_file_content = distance_file.read()
	distance_file_lines = distance_file_content.split("\n")

	for line_num in range(len(distance_file_lines)-1):
		distance_info = distance_file_lines[line_num].split(",")
		distance_dict[distance_info[0]] = line_num
		distance_list.append(distance_info[1:])

	# The trucks w/ constraints
	truck_01 = [13, 14, 15, 16, 19, 20, 1, 27, 29, 30, 31, 37, 40]
	truck_02 = [6, 25, 28, 32, 3, 18, 36, 38, 2, 4, 5, 7, 8, 10, 11]
	truck_03 = [12, 17, 21, 22, 23, 24, 26, 33, 34, 35, 39, 9]

	# Part A hash table test
	# print(hash_table)

	# Part B lookup test
	# print(hash_table.lookup(22))

	# Part B distance data test
	# for key, value in distance_dict.items():
	# 	print(key + ":" + str(value))
	# 	print(distance_list[value])

	# print(f"Example \n Distance: {distance_list[2][1]}, Address: (find key for second index based on value)")

	# Part C test
	# print(f"Truck 1 #: {len(truck_01)}, Truck 2#: {len(truck_02)}, Truck 3#: {len(truck_03)}")

	# print(hash_table) 

	total_route_mileage = 0.0

	print("Truck 1 route")
	total_route_mileage += delivery(truck_01, load_time_01, input_time, hash_table, distance_list, distance_dict)

	print("Truck 2 route")
	total_route_mileage += delivery(truck_02, load_time_02, input_time, hash_table, distance_list, distance_dict)

	print("Truck 3 route")
	total_route_mileage += delivery(truck_03, load_time_03, input_time, hash_table, distance_list, distance_dict)

	print(total_route_mileage)

	print(hash_table)

if __name__ == '__main__':
	# Display total mileage of route
	# Prompt user to enter a time
	# Prompt user for choice to check the status of an individual package or all packages

	main()

