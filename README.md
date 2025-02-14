# Flightgear Navdata Parser
Project by TOASTER and SkyClan480

To make use of this parser, you will need to have python installed. https://www.python.org/.

Download the correct excutable for your os. The file name says what os the executable is built for.

If you are on linux, you will need to make the file executable by running `chmod +x` on the file from the command line.

## How to use the parser:

1. Download [the latest NASR cycle](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/). You want either one listed under "Current" or "Preview". It will download as a .zip archive.
2. In the .zip there will be several text files. You will need to extract FIX.txt, NAV.txt, ILS.txt, and AWY.txt and put them in the same folder as the parser.
3. Run the parser. You will be prompted to enter the NASR effective date, which will be printed in the header of each file. The effective date of the data is listed on the website where you downloaded it. Enter the date into the prompt. This will create a folder called NavData.
5. Move the NavData folder wherever you want. In the FG launcher, you will need to alter some settings to make Flightgear use the new files. Under "addons", find "additional scenery folders" and add a new one. You'll want to add the folder that you put NavData in. For example, if you put NavData at C:\folder\fgstuff\NavData, you would add C:\folder\fgstuff as the scenery folder. Save this setting and then restart Flightgear for changes to take effect.

You can repeat this process for each new NASR cycle. Simply replace the old NavData folder with the new one. After the first time, you will not need to change flightgear settings in the future, as it will remember the directory and will automatically read the new files.

CIFP UPDATE:
It's 2025 and I've spontaneously decided to stop being lazy and revive this project by finally putting in actual effort to write the CIFP version. I honestly don't even remember why the project stalled before, probably because I didn't really understand the AIRINC 424 format, but dumb stupid past me forgot that you can literally look up the specification for that file format online and the actual company that created it has a PDF that spells out everything we need in one idiot proof place. All that remains is to write the parsing code for it which should be no different than the NASR, and that's what I'm setting out to do now. Perhaps we can properly get this project in position as a free alternative to Navigraph for navigation data in countries that publish their CIFP like the US does.
