#!/usr/bin/env python

with open("irish-dobs.txt") as irish_in, open("american-dobs.txt", "w") as american_out:
    s = irish_in.readline()
    while 0 < len(s):
        i_data = s.split() # separate date and person's name
        i_dob = i_data[0].split("/") # separate date
        a_dob = [i_dob[1], i_dob[0], i_dob[2]] # reorder date to get American version
        o_data =  "/".join(a_dob) + " " + " ".join(i_data[1:]) + "\n" #format properly and get people's names.
        american_out.write(o_data)
        s = irish_in.readline()