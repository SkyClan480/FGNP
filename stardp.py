#open CIFP file to parse
with open("FAACIFP18") as source:

    #create master dictionaries for star and sid to hold all parsed data
    star = {}
    sid = {}

    #repeat for each line in cifp
    for z in list(source):

        #check if line is relevant data
        if("SUSAP" in z and z[10] == "K"):

            #check if line is sid or star
            if(z[12] == "D"):

                #add sids dictionary
                if(z[6:10].strip() not in sid):
                    sid[z[6:10].strip()] = {}

                #add sid procedures dictionary
                if(z[13:19].strip() not in sid[z[6:10].strip()]):
                    sid[z[6:10].strip()][z[13:19].strip()] = {"proc":{}}

                #add sid transitions dictionary
                if(z[20:25].strip() not in sid[z[6:10].strip()][z[13:19].strip()]):
                    sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()] = {"trans":{}}

                #add sid waypoints dictionary
                if(z[29:34] not in sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]):
                    sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()] = {"wpt":{},"alt":{},"spd":{}}

                #create sub dictionaries for procedure, transition, and waypoint names
                sid[z[6:10].strip()][z[13:19].strip()]["proc"] = z[13:19].strip()
                sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]["trans"] = z[20:25].strip()
                sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["wpt"] = z[29:34].strip()
                sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["alt"] = z[82:89].replace(" ","")
                sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["spd"] = z[99:102].strip()

            elif(z[12] == "E"):

                #add stars dictionary
                if(z[6:10].strip() not in star):
                    star[z[6:10].strip()] = {}

                #add star procedures dictionary
                if(z[13:19].strip() not in star[z[6:10].strip()]):
                    star[z[6:10].strip()][z[13:19].strip()] = {"proc":{}}

                #add star transitions dictionary
                if(z[20:25].strip() not in star[z[6:10].strip()][z[13:19].strip()]):
                    star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()] = {"trans":{}}

                #add star waypoints dictionary
                if(z[29:34] not in star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]):
                    star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()] = {"wpt":{},"alt":{},"spd":{}}

                #create sub dictionaries for procedure, transition, and waypoint names
                star[z[6:10].strip()][z[13:19].strip()]["proc"] = z[13:19].strip()
                star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]["trans"] = z[20:25].strip()
                star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["wpt"] = z[29:34].strip()
                star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["alt"] = z[82:89].replace(" ","")
                star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["spd"] = z[99:102].strip()

#repeat line index and open dest file
with open("FAACIFP18") as source, open("tst.txt", 'w') as dest:

    for z in list(source):

        #relevant line check
        if("SUSAP" in z and z[10] == "K"):

            #write data for sids
            if(z[12] == "D"):
                dest.write(z[6:10].strip()+" DEP: ")
                dest.write(sid[z[6:10].strip()][z[13:19].strip()]["proc"]+" ")
                dest.write(sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]["trans"]+" ")
                dest.write(sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["wpt"]+" ")
                dest.write(sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["alt"])
                dest.write(sid[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["spd"]+"\n")

            #write data for stars
            elif(z[12] == "E"):
                dest.write(z[6:10].strip()+" ARR: ")
                dest.write(star[z[6:10].strip()][z[13:19].strip()]["proc"]+" ")
                dest.write(star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()]["trans"]+" ")
                dest.write(star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["wpt"]+" ")
                dest.write(star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["alt"]+" ")
                dest.write(star[z[6:10].strip()][z[13:19].strip()][z[20:25].strip()][z[29:34].strip()]["spd"]+"\n")