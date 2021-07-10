import os
os.mkdir("NavData/fix")

with open("FIX.txt") as source, open("NavData/fix/fix.dat",'w') as dest:
    dest.write(f"""I
XP740 compliant for fgfs. Extracted using fix.py by TOASTER from 28-Day NASR Subscriptions effective """+input("NASR effective date >>> ")+""" from FAA.gov\n\n""")
    for z in list(source):
        if "FIX1" in z:
            dest.write(f"{'-' if z[78]=='S' else ' '}{int(z[66:68])+int(z[69:71])/60+float(z[72:78])/3600:09.6f} {'-' if z[93]=='W' else ' '}{int(z[80:83])+int(z[84:86])/60+float(z[87:93])/3600:010.6f} {z[4:9]}\n")
    dest.write("99")
