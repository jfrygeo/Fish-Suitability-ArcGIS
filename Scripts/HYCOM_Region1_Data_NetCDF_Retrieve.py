#-------------------------------------------------------------------------------
# Name:        HYCOM_Data_NetCDF_Retrieve from Region 1
# Purpose:     Retrieve latest NetCDF from HYCOM. HYCOM forecasts 7 days so this script downloads the data that is
# 7 days ahead of today's date
#
# Author:      JFry
#
# Created:     7/26/2017
# Edited:
# Copyright:   (c) john6807 2017
# Licence:  Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
#-------------------------------------------------------------------------------

import datetime, time, sys, os

scriptPath = sys.path[0]

# local folder where wanting to download data
downloadfolder = sys.path[0] + "\\Scratch\\HYCOM\\"

##Base Urls where data resides
baseurl = "https://ecowatch.ncddc.noaa.gov/thredds/fileServer/hycom_region1/"

#Intermediate file names
HYCOMFileName = "hycom_glb_regp01_"
#tau indicates the time at which the forecast is for. You may want to add a few more times to download
tau = "t000.nc"

#Calculate local time of today
todaysdate = str(datetime.datetime.now())
print (todaysdate)

#Calculate local time's day of year
formattime = time.strftime("%Y%m%d",time.strptime(todaysdate,"%Y-%m-%d %H:%M:%S.%f"))
print (formattime)

#format date to yesterday
yearmonthdate = str(int(formattime) - 1)
print (yearmonthdate)

#Format download location with file name
downloadlocationReg1 = str(os.path.join(downloadfolder) + HYCOMFileName + yearmonthdate + tau)
print (downloadlocationReg1)

#Format string request for Sea Surface Temperature
dlHYCOMReg1= str(baseurl + yearmonthdate + "/" + HYCOMFileName + yearmonthdate + "00_" + tau)
print (dlHYCOMReg1)

# Format string request for download
if sys.version_info[0]== 3:
    import urllib.request
    #What Python
    sysver = sys.version
    print (sysver)
    urllib.request.urlretrieve(dlHYCOMReg1, downloadlocationReg1)
    print ("Downloaded HYCOM Data")

else:
    if sys.version_info[0]== 2:
        import urllib
        sysver = sys.version
        print (sysver)
        urllib.request.urlretrieve(dlHYCOMReg1, downloadlocationReg1)
        print ("Downloaded HYCOM Data")


