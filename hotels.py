"""
10 floors [0-9]
26 rooms [A-Z]

After a series of checks in check how many available rooms

example:
+4B - checked in at 4B
-4B - checked out of 4B
+6J - checked in at 6J

input is a list of strings 
"""

def reserve(bookings):
    rooms = 0

    for booking in bookings:
        if booking[0] == "+":
            rooms += 1
        else:
            rooms -= 1

    return rooms

test = ["+4B", "-4B", "+6J"]
print(reserve(test))