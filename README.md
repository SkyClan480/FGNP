# Flightgear-Navdata-Parser
Project by puku-777 and SkyClan480

To make use of these scripts, you will need to have python installed. https://www.python.org/

How to use the parsing scripts:

1. Download the latest NASR cycle from https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/. You want either one listed under "Current" or "Preview". It will download as a .zip archive.
2. In the .zip there will be several text files. You will need to extract FIX.txt, NAV.txt, ILS.txt, and AWY.txt and put them in the same folder as the python scripts.
3. Run fix.py, nav.py, and awy.py with python. This will create fix.dat, nav.dat, and awy.dat.
4. Create a folder called NavData anywhere outside of $FGROOT$, and inside that folder create three folders called "fix", "nav", and "awy" respectively.
5. Move the .dat files from before into the correctly named folder (fix for fix.dat, nav for nav.dat, and awy for awy.dat)
6. In the FG launcher, you will need to alter some settings to make Flightgear use the new files. Under "addons", find "additional scenery folders" and add a new one. You'll want to add the folder that NavData is in. For example, if the path to NavData is C:\folder\fgstuff\NavData, you would add C:\folder\fgstuff as the scenery folder. Save this setting and then restart Flightgear for changes to take effect.

You can repeat this process for each new NASR cycle. Simply replace the old .dat files with the new ones.
