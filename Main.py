# Created by David Krupar

# Using various imports to provide cleaner file structure
import datetime
from Data import nearest_neighbor, Data
from Vehicle import Vehicle

# Create vehicle objects, included in main to allow for quick adjustments to parcel assignments to trucks
vehicle1 = Vehicle([40, 1, 33, 8, 17, 37, 20, 30, 34, 13, 14, 15, 16, 19, 29],
                   "4001 South 700 East", datetime.timedelta(hours=8), 16, 18, None, 0.0)

vehicle2 = Vehicle([3, 10, 36, 38, 18, 11, 7, 35, 5, 12, 9, 28, 2, 39],
                   "4001 South 700 East", datetime.timedelta(hours=10, minutes=20), 16, 18, None, 0.0)

vehicle3 = Vehicle([6, 21, 32, 27, 31, 23, 4, 26, 24, 22, 25],
                   "4001 South 700 East", datetime.timedelta(hours=9, minutes=5), 16, 18, None, 0.0)


# Applying algorithm to parcels per individual vehicle
nearest_neighbor(vehicle1)
nearest_neighbor(vehicle3)

# Created to ensure vehicles delivering <= driver count
if min(vehicle1.time, vehicle3.time) > datetime.timedelta(hours=10, minutes=20):
    vehicle2.depart_time = min(vehicle1.time, vehicle3.time)
else:
    vehicle2.depart_time = datetime.timedelta(hours=10, minutes=20)

nearest_neighbor(vehicle2)


class Main:

    # Interface

    # Prints total distance for all packages
    print("\nDistance Required = ", int(vehicle1.distance + vehicle2.distance + vehicle3.distance), "Miles\n")

    # Requesting input from user
    run = input("To run interface, type 'all' or 'single' ")

    # If statement for "all" or "single" parcel query
    if run == "all":
        try:
            # Requesting time input from user and formatting for function call
            user_time = input("\nEnter time using format HH:MM:SS\n")
            (h, m, s) = user_time.split(":")
            formatted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # Calling get_val, known as lookup, for parcel hash table
            for parcel in range(1, 41):
                p = Data.p_ht.get_val(parcel)
                p.parcel_detail(formatted_time)
                print(str(p))
            print("\nThank you!")
        except ValueError:
            print("Invalid entry")
            exit()

    elif run == "single":
        try:
            # Requesting time input from user and formatting for function call
            user_time = input("\nEnter time using format HH:MM:SS\n")
            (h, m, s) = user_time.split(":")
            formatted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # Requesting parcel ID for query
            single = input("Enter parcel ID: \n")
            # Calling get_val, known as lookup, for parcel hash table
            p = Data.p_ht.get_val(int(single))
            p.parcel_detail(formatted_time)
            print(str(p))
            print("\nThank you!")

        except ValueError:
            print("Invalid entry")
            exit()
