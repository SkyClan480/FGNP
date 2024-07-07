import os
import math
os.mkdir("NavData")
os.mkdir("NavData/fix")
effdate = input("NASR effective date >>> ")
with open("FIX.txt") as source, open("NavData/fix/fix.dat",'w') as dest:    
    
    dest.write(f"""I
XP740 compliant for fgfs. Extracted using fix.py by TOASTER from 28-Day NASR Subscriptions effective """+effdate+""" from FAA.gov\n\n""")
    for z in list(source):
        if "FIX1" in z:
            dest.write(f"{'-' if z[78]=='S' else ' '}{int(z[66:68])+int(z[69:71])/60+float(z[72:78])/3600:09.6f} {'-' if z[93]=='W' else ' '}{int(z[80:83])+int(z[84:86])/60+float(z[87:93])/3600:010.6f} {z[4:9]}\n")
    dest.write("99")

#======================================================================================================================================================================================================

#freqency pairing list parsed by TOASTER
pairing = {
"001X":96200,
"001Y":108800,
"002X":96300,
"002Y":108900,
"003X":96400,
"003Y":109000,
"004X":96500,
"004Y":109100,
"005X":96600,
"005Y":109200,
"006X":96700,
"006Y":109300,
"007X":96800,
"007Y":109400,
"008X":96900,
"008Y":109500,
"009X":97000,
"009Y":109600,
"010X":97100,
"010Y":109700,
"011X":97200,
"011Y":109800,
"012X":97300,
"012Y":109900,
"013X":97400,
"013Y":110000,
"014X":97500,
"014Y":110100,
"015X":97600,
"015Y":110200,
"016X":97700,
"016Y":110300,
"017X":10800,
"017Y":10805,
"018X":10810,
"018Y":10815,
"019X":10820,
"019Y":10825,
"020X":10830,
"020Y":10835,
"021X":10840,
"021Y":10845,
"022X":10850,
"022Y":10855,
"023X":10860,
"023Y":10865,
"024X":10870,
"024Y":10875,
"025X":10880,
"025Y":10885,
"026X":10890,
"026Y":10895,
"027X":10900,
"027Y":10905,
"028X":10910,
"028Y":10915,
"029X":10920,
"029Y":10925,
"030X":10930,
"030Y":10935,
"031X":10940,
"031Y":10945,
"032X":10950,
"032Y":10955,
"033X":10960,
"033Y":10965,
"034X":10970,
"034Y":10975,
"035X":10980,
"035Y":10985,
"036X":10990,
"036Y":10995,
"037X":11000,
"037Y":11005,
"038X":11010,
"038Y":11015,
"039X":11020,
"039Y":11025,
"040X":11030,
"040Y":11035,
"041X":11040,
"041Y":11045,
"042X":11050,
"042Y":11055,
"043X":11060,
"043Y":11065,
"044X":11070,
"044Y":11075,
"045X":11080,
"045Y":11085,
"046X":11090,
"046Y":11095,
"047X":11100,
"047Y":11105,
"048X":11110,
"048Y":11115,
"049X":11120,
"049Y":11125,
"050X":11130,
"050Y":11135,
"051X":11140,
"051Y":11145,
"052X":11150,
"052Y":11155,
"053X":11160,
"053Y":11165,
"054X":11170,
"054Y":11175,
"055X":11180,
"055Y":11185,
"056X":11190,
"056Y":11195,
"057X":11200,
"057Y":11205,
"058X":11210,
"058Y":11215,
"059X":11220,
"059Y":11225,
"060X":102100,
"060Y":114700,
"061X":102200,
"061Y":114800,
"062X":102300,
"062Y":114900,
"063X":102400,
"063Y":115000,
"064X":115100,
"064Y":102500,
"065X":115200,
"065Y":102600,
"066X":115300,
"066Y":102700,
"067X":115400,
"067Y":102800,
"068X":115500,
"068Y":102900,
"069X":115600,
"069Y":103000,
"070X":11230,
"070Y":11235,
"071X":11240,
"071Y":11245,
"072X":11250,
"072Y":11255,
"073X":11260,
"073Y":11265,
"074X":11270,
"074Y":11275,
"075X":11280,
"075Y":11285,
"076X":11290,
"076Y":11295,
"077X":11300,
"077Y":11305,
"078X":11310,
"078Y":11315,
"079X":11320,
"079Y":11325,
"080X":11330,
"080Y":11335,
"081X":11340,
"081Y":11345,
"082X":11350,
"082Y":11355,
"083X":11360,
"083Y":11365,
"084X":11370,
"084Y":11375,
"085X":11380,
"085Y":11385,
"086X":11390,
"086Y":11395,
"087X":11400,
"087Y":11405,
"088X":11410,
"088Y":11415,
"089X":11420,
"089Y":11425,
"090X":11430,
"090Y":11435,
"091X":11440,
"091Y":11445,
"092X":11450,
"092Y":11455,
"093X":11460,
"093Y":11465,
"094X":11470,
"094Y":11475,
"095X":11480,
"095Y":11485,
"096X":11490,
"096Y":11495,
"097X":11500,
"097Y":11505,
"098X":11510,
"098Y":11515,
"099X":11520,
"099Y":11525,
"100X":11530,
"100Y":11535,
"101X":11540,
"101Y":11545,
"102X":11550,
"102Y":11555,
"103X":11560,
"103Y":11565,
"104X":11570,
"104Y":11575,
"105X":11580,
"105Y":11585,
"106X":11590,
"106Y":11595,
"107X":11600,
"107Y":11605,
"108X":11610,
"108Y":11615,
"109X":11620,
"109Y":11625,
"110X":11630,
"110Y":11635,
"111X":11640,
"111Y":11645,
"112X":11650,
"112Y":11655,
"113X":11660,
"113Y":11665,
"114X":11670,
"114Y":11675,
"115X":11680,
"115Y":11685,
"116X":11690,
"116Y":11695,
"117X":11700,
"117Y":11705,
"118X":11710,
"118Y":11715,
"119X":11720,
"119Y":11725,
"120X":11730,
"120Y":11735,
"121X":11740,
"121Y":11745,
"122X":11750,
"122Y":11755,
"123X":11760,
"123Y":11765,
"124X":11770,
"124Y":11775,
"125X":11780,
"125Y":11785,
"126X":11790,
"126Y":11795
}

#======================================================================================================================================================================================================
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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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
                if(z[489:495].strip() != ""):
                    dest.write(f"{int(10**(math.log10(int(z[489:495].strip()))*0.991130075)):>3} ")
                else:
                    dest.write("81 ")

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

#======================================================================================================================================================================================================

with open('AWY.txt') as source, open('NavData/awy.dat','w') as dest:#, input("NASR effective date >>> ") as effdate:
    #make a 2d table of airways and points.
    awys = {}
    for z in list(source):
        if z[:4] in ('AWY1','AWY2'):
            if z[4:9].strip() not in awys: awys[z[4:9].strip()]={} #initialise airway in the master dictionary
            #print(awys)
            if z[:4]=='AWY1':
                #create dict entry (another nested dict) by index number, and assign minimum altitude (MOCA) and maximum altitude (max authorised)
                awys[z[4:9].strip()][int(int(z[11:15])/10)]={'minalt':int(int(z[102:106].strip() or 0)/100),'maxalt':int(int(z[97:102].strip() or 60000)/100)}
                #decide altitude class (1=low, 2=high) based on prefix letter
                if z[4] in 'JQ':awys[z[4:9].strip()][int(int(z[11:15].strip())/10)]['altclass']=2
                elif z[4] in 'VTABGR':awys[z[4:9].strip()][int(int(z[11:15].strip())/10)]['altclass']=1
            elif z[:4]=='AWY2':
                #finally we can know the point's name
                if "FIX" in z:
                    awys[z[4:9].strip()][int(int(z[11:15].strip())/10)]['ident']=z[15:20].strip()
                else:
                    awys[z[4:9].strip()][int(int(z[11:15].strip())/10)]['ident']=z[116:119].strip()
                #prune border fixes and just forget about it
                if 'BORDER' in z[:40]:
                    del(awys[z[4:9].strip()][int(int(z[11:15])/10)]);continue
                #parse latitude, then longitude
                awys[z[4:9].strip()][int(int(z[11:15])/10)]['lat']=(-1 if z[94]=='S' else 1)*(int(z[83:85])+int(z[86:88])/60+float(z[89:93])/3600)
                awys[z[4:9].strip()][int(int(z[11:15])/10)]['lon']=(-1 if z[109]=='W' else 1)*(int(z[97:100])+int(z[101:103])/60+float(z[104:108])/3600)
            #print(z[4:9].strip(),int(int(z[11:15])/10),awys[z[4:9].strip()][int(int(z[11:15])/10)])
    #write the front matter for the data file
    dest.write("""I
XP640 compliant for fgfs. Extracted using awy.py by TOASTER from 28-Day NASR Subscriptions effective """+effdate+' from FAA.gov\n\n')
    #iterate over airways, and in each airway iterate over point and its neighbour.
    for z in awys:
        for x,y in zip(list(awys[z]),list(awys[z])[1:]):
            dest.write(f"{awys[z][x]['ident']:5} {awys[z][x]['lat']:>10.6f} {awys[z][x]['lon']:>11.6f} {awys[z][y]['ident']:5} {awys[z][y]['lat']:>10.6f} {awys[z][y]['lon']:>11.6f} {awys[z][x]['altclass']} {awys[z][x]['minalt']:03} {awys[z][x]['maxalt']:03} {z}\n")
    dest.write('99')
