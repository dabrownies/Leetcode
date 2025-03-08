"""
Server outputs:
N - no reply
O - on time
L - late

figure out if the server is faulty

faulty means:
1 - late for 3 replies consecutively
2 - does not reply more than once

returns true or false if the server is faulty
"""

test1 = "LNOLL"
test2 = "ONONO"

def checkServer(message):
    no_reply_count, late_count = 0, 0

    for ch in message:
        if ch == "L":
            late_count += 1
            if late_count == 3:
                return False
        elif ch == "N":
            no_reply_count += 1
            late_count = 0
            if no_reply_count > 1:
                return False
        else:
            late_count = 0

    return True

def test(mes):
    l = r = 0
    late, no = 0, 0
    while r != len(mes):
        while mes[r] == "L" and r < len(mes):
            late += 1
            if late == 3:
                return False
            r += 1
        late = 0
        
        l = r

print(checkServer(test1))
print(checkServer(test2))
