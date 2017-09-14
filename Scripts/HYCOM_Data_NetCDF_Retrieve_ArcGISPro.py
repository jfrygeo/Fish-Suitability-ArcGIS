#-------------------------------------------------------------------------------
# Name:        HYCOM_Data_NetCDF_Retrieve
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

import datetime, time, sys, os, arcpy

scriptPath = sys.path[0]

# local folder where wanting to download data
downloadfolder = arcpy.GetParameterAsText(0)

##Base Urls where data resides
baseurl = "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_91.2/2017/"

datachoice = arcpy.GetParameterAsText(1)

#Intermediate file names
front = "archv.2017_"
back = "_00_3z"

if datachoice == "mlt/":
    product = "mlt/"
    type = "mlt"
if datachoice == "salt/":
    product = "salt/"
    type = "s"
if datachoice == "temp/":
    product = "temp/"
    type = "t"
if datachoice == "uvel/":
    product = "uvel/"
    type = "u"
if datachoice == "vvel/":
    product = "vvel/"
    type = "v"

#Calculate local time of today
arcpy.AddMessage("Calculating today's date")
todaysdoy = str(datetime.datetime.now())
print (todaysdoy)

#Calculate local time's day of year
formattime = time.strftime("%j",time.strptime(todaysdoy,"%Y-%m-%d %H:%M:%S.%f"))
print (formattime)

#Add 7 days to local time's day of year
arcpy.AddMessage("Getting Most Current Data (Today + 7 Days)")
doy7 = int(formattime) + 7
print (doy7)


#Format download location with file name
downloadlocationSalt = str(os.path.join(downloadfolder) + "\\" + front + str(doy7) + back + type + ".nc")
print (downloadlocationSalt)

#Format string request for Sea Surface Temperature
dlHYCOMSalt= str(baseurl + product + front + str(doy7) + back + type + ".nc")
print (dlHYCOMSalt)

# Format string request for download
arcpy.AddMessage("Making Request for Data")
arcpy.AddMessage("Downloading Data")

arcpy.AddMessage(dlHYCOMSalt)


if sys.version_info[0]== 3:
    import urllib.request
    #What Python
    sysver = sys.version
    print (sysver)
    urllib.request.urlretrieve(dlHYCOMSalt, downloadlocationSalt)
    print ("Downloaded HYCOM Data")

else:
    if sys.version_info[0]== 2:
        import urllib
        sysver = sys.version
        print (sysver)
        urllib.request.urlretrieve(dlHYCOMSalt, downloadlocationSalt)
        print ("Downloaded HYCOM Data")


arcpy.AddMessage("Data Downloaded" + " " + str(downloadfolder) + "\\")