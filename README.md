# Flightgear-Navdata-Parser
Project by TOASTER and SkyClan480

To make use of this parser, you will need to have python installed. https://www.python.org/.

Download the correct excutable for your os. The file name says what os the executable is built for.

Linux users:
In order to run the file you will need to make it executable by running `chmod +x fgnavparser-1.1-linux` from the command line in the same directory as the file.

## How to use the parser:

1. Download [the latest NASR cycle](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/). You want either one listed under "Current" or "Preview". It will download as a .zip archive.
2. In the .zip there will be several text files. You will need to extract FIX.txt, NAV.txt, ILS.txt, and AWY.txt and put them in the same folder as the parser.
3. Run the parser. You will be prompted to enter the NASR effective date, which will be printed in the header of each file. The effective date of the data is listed on the website where you downloaded it. Enter the date into the prompt. This will create fix.dat, nav.dat, and awy.dat files.
4. Create a folder called NavData anywhere outside of $FGROOT$ and move the .dat files into it.
5. In the FG launcher, you will need to alter some settings to make Flightgear use the new files. Under "addons", find "additional scenery folders" and add a new one. You'll want to add the folder that NavData is in. For example, if the path to NavData is C:\folder\fgstuff\NavData, you would add C:\folder\fgstuff as the scenery folder. Save this setting and then restart Flightgear for changes to take effect.

You can repeat this process for each new NASR cycle. Simply replace the old .dat files with the new ones.
