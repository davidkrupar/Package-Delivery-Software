import csv
from Hash import Generate
from Parcel import Parcel
import datetime


class Data:

    # Create parcel object from parcel file, using CSV file from reader
    # Loads parcel objects into p_ht, parcel hash table
    def create_object(filename, p_ht):
        with open(filename) as p_info:
            p_directory = csv.reader(p_info)
            for parcel in p_directory:
                pID = int(parcel[0])
                pAddress = parcel[1]
                pcity = parcel[2]
                pState = parcel[3]
                pZipcode = parcel[4]
                pDeadline_time = parcel[5]
                pTonnage = parcel[6]
                pCurrent = "At The Hub"

                p = Parcel(pID, pAddress, pcity, pState, pZipcode, pDeadline_time, pTonnage, pCurrent)

                p_ht.set_val(pID, p)

    p_ht = Generate()

    create_object("CSV/Package_File.csv", p_ht)


# Method for parcel sorting per vehicle using nearest neighbor algorithm
# Also used to calculate distance per vehicle
def nearest_neighbor(vehicle):
    # Array created for parcels not delivered
    pending_d = []
    for parcel in vehicle.first_order:
        p = Data.p_ht.get_val(parcel)
        pending_d.append(p)
    # Wipes individual vehicle parcel ordering
    vehicle.first_order.clear()

    # Applies algorithm until pending deliveries is 0
    while len(pending_d) > 0:
        n_p = None
        n_a = 2000
        for p in pending_d:
            # Uses CSV files to compute distances and create most efficient ordering
            if xy_differential(pull_data(vehicle.start), pull_data(p.address)) <= n_a:
                n_a = xy_differential(pull_data(vehicle.start), pull_data(p.address))
                n_p = p

        # Functions to add/remove parcel
        vehicle.first_order.append(n_p.ID)
        pending_d.remove(n_p)
        # Function to compute mileage
        vehicle.distance += n_a
        # Function to update vehicle address
        vehicle.start = n_p.address
        # Functions to update timestamps
        vehicle.time += datetime.timedelta(hours=n_a / 18)
        n_p.del_time = vehicle.time
        n_p.dep_time = vehicle.depart_time


# Compute int ID of text formatted address
def pull_data(location):
    for row in CSV_A:
        if location in row[2]:
            return int(row[0])


# Compute distance between addresses
def xy_differential(x, y):
    differential = CSV_D[x][y]
    if differential == '':
        differential = CSV_D[y][x]
    return float(differential)


# Python CSV reader for provided distances
with open("CSV/Distance_File.csv") as csvfile:
    CSV_D = csv.reader(csvfile)
    CSV_D = list(CSV_D)

# Python CSV reader for provided addresses
with open("CSV/Address_File.csv") as csvfile1:
    CSV_A = csv.reader(csvfile1)
    CSV_A = list(CSV_A)

# Python CSV reader for provided parcels
with open("CSV/Package_File.csv") as csvfile2:
    CSV_P = csv.reader(csvfile2)
    CSV_P = list(CSV_P)
