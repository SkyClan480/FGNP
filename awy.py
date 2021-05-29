with open('AWY.txt') as source, open('awy.dat','w') as dest:#, input("NASR effective date >>> ") as effdate:
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
XP640 compliant for fgfs. Extracted using awy.py by TOASTER from 28-Day NASR Subscriptions effective """+input("NASR effective date >>> ")+' from FAA.gov\n\n')
    #iterate over airways, and in each airway iterate over point and its neighbour.
    for z in awys:
        for x,y in zip(list(awys[z]),list(awys[z])[1:]):
            dest.write(f"{awys[z][x]['ident']:5} {awys[z][x]['lat']:>10.6f} {awys[z][x]['lon']:>11.6f} {awys[z][y]['ident']:5} {awys[z][y]['lat']:>10.6f} {awys[z][y]['lon']:>11.6f} {awys[z][x]['altclass']} {awys[z][x]['minalt']:03} {awys[z][x]['maxalt']:03} {z}\n")
    dest.write('99')
