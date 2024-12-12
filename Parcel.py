# Using object-oriented principles from past WGU courses
# Creating class for parcel object
class Parcel:
    def __init__(self, ID, address, city, state, zipcode, deadline_time, tonnage, current):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.tonnage = tonnage
        self.current = current
        self.dep_time = None
        self.del_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline_time, self.tonnage, self.del_time,
                                                       self.current)

    # Critical method for program.  This is called in various occasions
    # in the user interface.  It provides "status of parcel delivery"
    def parcel_detail(self, convert_timedelta):
        if self.del_time < convert_timedelta:
            self.current = "Delivered"
        elif self.dep_time > convert_timedelta:
            self.current = "En route"
        else:
            self.current = "At The Hub"


