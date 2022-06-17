#open CIFP to parse and fix.dat to write
with open("FAACIFP18") as source:
    
    #create master dictionary to store data
    fix = {}

    #repeat for each line in CIFP
    for z in list(source):

        #check if line is relevant data
        if(z[4:10] == "EAENRT"):

            #add waypoint to dictionary
            if(z[13:18] not in fix):
                fix[z[13:18]] = {"name":{},"lat":{},"lon":{}}

            #add waypoint data
            fix[z[13:18]]["name"] = z[13:18]
            fix[z[13:18]]["lat"] = z[32:35].replace("N"," ").replace("S","-")+"."+z[35:41]
            fix[z[13:18]]["lon"] = z[41:45].replace("E"," ").replace("W","-")+"."+z[45:51]

        #check other relevant data lines
        if(z[4] == "P" and z[12] == "C"):

            #add waypoint to dictionary
            if(z[98:103] not in fix):
                fix[z[98:103]] = {"name":{},"lat":{},"lon":{}}

            #add waypoint data
            fix[z[98:103]]["name"] = z[98:103]
            fix[z[98:103]]["lat"] = z[32:35].replace("N"," ").replace("S","-")+"."+z[35:41]
            fix[z[98:103]]["lon"] = z[41:45].replace("E"," ").replace("W","-")+"."+z[45:51]

#open fix.dat to write
with open("FAACIFP18") as source, open("fix.dat",'w') as dest:

    #write top info line
    dest.write(f"""I
    XP740 compliant for fgfs. Extracted using fix.py by TOASTER and SkyClan480 from 28-day CIFP subscriptions effective """+input("CIFP effective date >>> ")+""" from FAA.gov\n\n""")

    for z in list(source):
        
        #relevant line check
        if(z[4:10] == "EAENRT"):

            #write waypoint data
            dest.write(fix[z[13:18]]["lat"]+" ")
            dest.write(fix[z[13:18]]["lon"]+" ")
            dest.write(fix[z[13:18]]["name"]+"\n")

        #other relevant line check
        if(z[4] == "P" and z[12] == "C"):

            #write waypoint data
            dest.write(fix[z[98:103]]["lat"]+" ")
            dest.write(fix[z[98:103]]["lon"]+" ")
            dest.write(fix[z[98:103]]["name"]+"\n")
    
    #terminate file with 99
    dest.write("99")
