# Package-Delivery-Software

Please refer to pdf file "Package Delivery Program" for detailed analysis.

Intro: Ask the user if they would like to A) deliver all packages or B) lookup single package status.

Look up a package - User enters the package ID they are looking for. The program returns the package information. This is where the chaining hash table is useful for fast lookup.

Start deliveries - Packages are selectively loaded onto all 3 trucks. The truck loading process implements the chaining hash table full of packages, the graph full of locations, and the greedy algorithm to get the shortest path that each truck will take. All 3 trucks are loaded even though there are only 2 drivers. The third truck will standby until one of the drivers returns after finishing that truck's deliveries.

Truck 1 leaves at 8:00AM - Truck 1 leaves to make deliveries.

Truck 2 waits then leaves - Because some packages are delayed on a flight, truck 2 waits for them to arrive at the hub. Once they arrive, truck 2 leaves and makes deliveries.

Truck 1 finishes, driver changes to truck 3, truck 3 leaves - Truck 3 makes deliveries.

Package address needs to change at 10:20AM - There is an alert that package #9 has the wrong address and needs to be fixed. The user fixes the address and the program continues.

Truck 2 and 3 return to the hub, all 40 packages were delivered to 27 locations, total milage was 86 miles.
