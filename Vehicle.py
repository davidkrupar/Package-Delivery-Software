# Using object-oriented principles from past WGU courses
# Creating class for vehicle object
class Vehicle:
    def __init__(self, first_order, start, depart_time, availability, mph, current, distance):
        self.first_order = first_order
        self.start = start
        self.depart_time = depart_time
        self.availability = availability
        self.mph = mph
        self.current = current
        self.distance = distance
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.first_order, self.start, self.depart_time, self.availability, self.mph,
                                               self.current, self.distance)