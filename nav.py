import math, os
try: os.mkdir("NavData")
except: pass

from pairing import pairing

#open NAV.txt to parse and nav.dat to create, w to overwrite existing nav.dat if present
with open("NAV.txt") as source, open("NavData/nav.dat",'w') as dest:

#write heading text with information about this script and the source of the data
    dest.write(f"""I
XP810 compliant for fgfs. Extracted with nav.py by TOASTER and SkyClan480 from 28-Day NASR Subscriptions effective """+input("NASR effective date >>> ")+' from FAA.gov\n\n')

    #parse for each line z in NAV.txt
    for z in list(source):

        #only parse NAV1 lines that are not VOT type
        if("NAV1" in z and "VOT" not in z and "FAN MARKER" not in z):

            #first tackle the double entries
            if("NDB/DME" in z):
                
                #NDB entry
                dest.write("2 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

                #DME entry
                dest.write("13 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

            if("VOR/DME" in z or "VORTAC" in z):

                #VOR entry
                dest.write("3 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #write a default reception range of 200 for VORs (as they don't supply a tx power value)
                dest.write("200 ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

                #DME/TACAN entry
                dest.write("12 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")
            
            #write the single entry types
            if("NDB" in z and "NDB/DME" not in z):
                dest.write("2 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

            elif("VOR" in z and "VOR/DME" not in z and "VORTAC" not in z):
                dest.write("3 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #write a default reception range of 200 for VORs (as they don't supply a tx power value)
                dest.write("200 ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

            elif("DME" in z and "NDB/DME" not in z and "VOR/DME" not in z):
                dest.write("13 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                if("VOR" not in z and z[489:495]=='      '):
                    dest.write("81 ")
                elif("VOR" not in z):
                    dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

            elif("TACAN" in z):
                dest.write("13 ")

                #convert coordinates to decimal degrees and write
                dest.write(f"{'-' if z[384]=='S' else ' '}{int(z[371:373])+int(z[374:376])/60+float(z[377:383])/3600:09.6f} {'-' if z[409]=='W' else ' '}{int(z[396:399])+int(z[400:402])/60+float(z[403:409])/3600:010.6f} ")

                #convert elevation to integer type and write, then add a space
                dest.write(f"{int(float(z[473:479].replace(' ','') or 0))}")
                dest.write(" ")

                #convert MHz frequencies to KHz and write, or find channel frequency if only channel is listed
                dest.write(f"{int(float(z[533:539])*10) if '.' in z[533:539] else z[533:539].strip()} ")
                if(z[533:539].strip() == ""):
                    dest.write(f"{pairing[z[529:533].strip()] if z[529:533].strip() in pairing else pairing['0'+z[529:533].strip()]} ")

                #calculate reception range based on power(if notated, otherwise use default) and write
                if("VOR" not in z and z[489:495]=='      '):
                    dest.write("81 ")
                elif("VOR" not in z):
                    dest.write(f"{int(10**(math.log10(int(z[489:495]))*0.991130075)):>3} ")

                #write navaid identifier and add a space
                dest.write(z[4:7].strip()+" ")

                #write name and format and append type
                dest.write(z[42:71].strip()+" ")
                dest.write(z[8:15].strip().replace("/","-")+"\n")

#open ILS.txt to parse
with open("ILS.txt") as source:

    #create master data dictionary
    nav = {}

    #parse for each line in ILS.txt
    for z in list(source):

        #add facility ID and ILS# categories to master
        if(z[4:18].strip() not in nav):
            nav[z[4:18].strip()] = {'ILS1':{},'ILS2':{},'ILS3':{},'ILS4':{},'ILS5':{}}

        #create dictionaries for relevant data in ILS1
        if("ILS1" in z):
            nav[z[4:18].strip()]["ILS1"]["ident"] = z[28:33].replace("-","") #ILS identifier
            nav[z[4:18].strip()]["ILS1"]["rwy"] = z[15:18].strip() #runway number
            nav[z[4:18].strip()]["ILS1"]["icao"] = "K"+z[159:162] #airport ICAO
            nav[z[4:18].strip()]["ILS1"]["name"] = 'ILS-cat-'+z[172:176].strip() if z[172:176].strip() else z[18:21]#formatted name of ILS or other directional aid
            nav[z[4:18].strip()]["ILS1"]["crs"] = z[281:288] #approach course

        #create dictionaries for relevant data in ILS2
        if("ILS2" in z):
            nav[z[4:18].strip()]["ILS2"]["coords"] = f"{'-' if z[73]=='S' else ' '}{int(z[60:62])+int(z[63:65])/60+float(z[66:72])/3600:09.6f} {'-' if z[99]=='W' else ' '}{int(z[85:88])+int(z[89:91])/60+float(z[92:98])/3600:010.6f} " #LOC coordinates
            
            #check if elevation is not null
            if(z[126:133].strip() != ""):
                nav[z[4:18].strip()]["ILS2"]["elev"] = str(int(float(z[126:133].strip())/10)) #LOC elevation
            else:
                nav[z[4:18].strip()]["ILS2"]["elev"] = "0" #if elevation is null

            nav[z[4:18].strip()]["ILS2"]["freq"] = z[133:139].replace(".","") #LOC frequency

        #create dictionaries for relevant data in ILS3
        if("ILS3" in z):
            nav[z[4:18].strip()]["ILS3"]["coords"] = f"{'-' if z[73]=='S' else ' '}{int(z[60:62])+int(z[63:65])/60+float(z[66:72])/3600:09.6f} {'-' if z[99]=='W' else ' '}{int(z[85:88])+int(z[89:91])/60+float(z[92:98])/3600:010.6f} " #GS coordinates

            #check if elevation is not null
            if(z[126:133].strip() != ""):
                nav[z[4:18].strip()]["ILS3"]["elev"] = str(int(float(z[126:133].strip())/10)) #GS elevation
            else:
                nav[z[4:18].strip()]["ILS3"]["elev"] = "0" #if elevation is null

            nav[z[4:18].strip()]["ILS3"]["freq"] = z[153:159].replace(".","") #GS frequency
            nav[z[4:18].strip()]["ILS3"]["angle"] = z[148:152].replace(".","") #GS angle

        #create dictionaries for relevant data in ILS4
        if("ILS4" in z):
            nav[z[4:18].strip()]["ILS4"]["coords"] = f"{'-' if z[73]=='S' else ' '}{int(z[60:62])+int(z[63:65])/60+float(z[66:72])/3600:09.6f} {'-' if z[99]=='W' else ' '}{int(z[85:88])+int(z[89:91])/60+float(z[92:98])/3600:010.6f} " #DME coordinates
            
            #check if elevation is not null
            if(z[126:133].strip() != ""):
                nav[z[4:18].strip()]["ILS4"]["elev"] = str(int(float(z[126:133].strip())/10)) #DME elevation
            else:
                nav[z[4:18].strip()]["ILS4"]["elev"] = "0" #if elevation is null

            nav[z[4:18].strip()]["ILS4"]["freq"] = f"{pairing[z[133:137].strip()] if z[133:137].strip() in pairing else (pairing['0'+z[133:137].strip()])} " #DME frequency
            nav[z[4:18].strip()]["ILS4"]["name"] = "DME-ILS" #DME name(always "DME-ILS" for ILS-associated DMEs)

        #create dictionaries for relevant data in ILS5
        if("ILS5" in z):

            #add correct type code for marker type
            if(z[28:30] == "IM"):
                nav[z[4:18].strip()]["ILS5"]["im"] = "9 "
            if(z[28:30] == "MM"):
                nav[z[4:18].strip()]["ILS5"]["mm"] = "8 "
            if(z[28:30] == "OM"):
                nav[z[4:18].strip()]["ILS5"]["om"] = "7 "

            nav[z[4:18].strip()]["ILS5"]["coords"] = f"{'-' if z[75]=='S' else ' '}{int(z[62:64])+int(z[65:67])/60+float(z[68:74])/3600:09.6f} {'-' if z[101]=='W' else ' '}{int(z[87:90])+int(z[91:93])/60+float(z[94:100])/3600:010.6f} " #marker coordinates
            
            #check if elevation is not null
            if(z[129:135].strip() != ""):
                nav[z[4:18].strip()]["ILS5"]["elev"] = str(int(float(z[129:135].strip())/10)) #marker elevation
            else:
                nav[z[4:18].strip()]["ILS5"]["elev"] = "0" #if elevation is null

            #add correct name for marker type
            if("om" in nav[z[4:18].strip()]["ILS5"]):
                nav[z[4:18].strip()]["ILS5"]["omname"] = "OM"
            if("mm" in nav[z[4:18].strip()]["ILS5"]):
                nav[z[4:18].strip()]["ILS5"]["mmname"] = "MM"
            if("im" in nav[z[4:18].strip()]["ILS5"]):
                nav[z[4:18].strip()]["ILS5"]["imname"] = "IM"

#reopen ILS.txt for z index and nav.dat to write, 'a' to append ILS information to previously written information
with open("ILS.txt") as source, open("NavData/nav.dat",'a') as dest:
    
    #for each line in ILS.txt
    for z in list(source):
        
        #write information for ILS2 lines
        if("ILS2" in z):
            dest.write(f"{'5 ' if z[18:21] == 'LOC' else '5 ' if z[18:21] == 'LDA' else '5 ' if z[18:21] == 'SDF' else '4 '}") #correct code for LOC type
            dest.write(nav[z[4:18].strip()]["ILS2"]["coords"]) #LOC coordinates
            dest.write(nav[z[4:18].strip()]["ILS2"]["elev"]+" ") #LOC elevation
            dest.write(nav[z[4:18].strip()]["ILS2"]["freq"]+" ") #LOC frequency
            dest.write("30 ")
            dest.write(nav[z[4:18].strip()]["ILS1"]["crs"]+" ") #ILS approach course
            dest.write(nav[z[4:18].strip()]["ILS1"]["ident"]+" ") #ILS identifier
            dest.write(nav[z[4:18].strip()]["ILS1"]["icao"]+" ") #airport ICAO
            dest.write(nav[z[4:18].strip()]["ILS1"]["rwy"]+" ") #runway number
            dest.write(nav[z[4:18].strip()]["ILS1"]["name"]+"\n") #ILS name

        #write information for ILS3 lines
        if("ILS3" in z):
            dest.write("6 ") #type code for glideslope
            dest.write(nav[z[4:18].strip()]["ILS3"]["coords"]) #GS coordinates
            dest.write(nav[z[4:18].strip()]["ILS3"]["elev"]+" ") #GS elevation
            dest.write(nav[z[4:18].strip()]["ILS3"]["freq"]+" ") #GS frequency
            dest.write("30 ")
            dest.write(nav[z[4:18].strip()]["ILS3"]["angle"]+nav[z[4:18].strip()]["ILS1"]["crs"]+" ") #GS angle and ILS approach course in combined format
            dest.write(nav[z[4:18].strip()]["ILS1"]["ident"]+" ") #ILS identifier
            dest.write(nav[z[4:18].strip()]["ILS1"]["icao"]+" ") #airport ICAO
            dest.write(nav[z[4:18].strip()]["ILS1"]["rwy"]+" ") #runway nuber
            dest.write("GS\n") #universal name for glideslopes
        
        #write information for ILS4 lines
        if("ILS4" in z):
            dest.write("12") #type code for DME component of ILS
            dest.write(nav[z[4:18].strip()]["ILS4"]["coords"]) #DME coordinates
            dest.write(nav[z[4:18].strip()]["ILS4"]["elev"]+" ") #DME elevation
            dest.write(nav[z[4:18].strip()]["ILS4"]["freq"]+" ") #DME frequency
            dest.write("30 ")
            dest.write(nav[z[4:18].strip()]["ILS1"]["ident"]+" ") #ILS identifier
            dest.write(nav[z[4:18].strip()]["ILS1"]["icao"]+" ") #airport ICAO
            dest.write(nav[z[4:18].strip()]["ILS1"]["rwy"]+" ") #runway number
            dest.write("DME-ILS\n") #universal name for DME associated with ILS

        #write information for ILS5 lines
        if("ILS5" in z):
            
            #write the correct type code for marker type
            if(z[28:30] == "IM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["im"]) #type code for inner marker
            if(z[28:30] == "MM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["mm"]) #type code for middle marker
            if(z[28:30] == "OM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["om"]) #type code for outer marker
            
            dest.write(nav[z[4:18].strip()]["ILS5"]["coords"]) #marker coordinates
            dest.write(nav[z[4:18].strip()]["ILS5"]["elev"]+" ") #marker elevation
            dest.write(nav[z[4:18].strip()]["ILS1"]["crs"]+" ") #ILS approach course
            dest.write(nav[z[4:18].strip()]["ILS1"]["icao"]+" ") #airport ICAO
            dest.write(nav[z[4:18].strip()]["ILS1"]["rwy"]+" ") #runway number

            #write the correct name for marker type
            if(z[28:30] == "IM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["imname"]+"\n") #name for inner marker
            if(z[28:30] == "MM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["mmname"]+"\n") #name for middle marker
            if(z[28:30] == "OM"):
                dest.write(nav[z[4:18].strip()]["ILS5"]["omname"]+"\n") #name for outer marker

    #terminate file with "99"
    dest.write("99")
