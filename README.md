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


Please note that we are currently in the process of transitioning to using the CIFP (Coded Instrument Flight Procedures) instead of NASR as the data source. This is because the CIFP are written in the international standard ARINC 424 format, which is shared by all countries. So, if we write the code to parse that format, it will be compatible with all countries' CIFP. The CIFP version of the parser is available on the "cifp-source" branch of the repository if you want to try it out (do be warned it is very incomplete at this point). The NASR will remain the active method for now, limiting data availability to the USA, but the CIFP conversion will likely be merged with main in the future, once we bring to a workable state.
