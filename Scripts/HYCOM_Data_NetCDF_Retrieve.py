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

import datetime, time, sys, os

scriptPath = sys.path[0]

# local folder where wanting to download data
downloadfolder = sys.path[0] + "\\Scratch\\HYCOM\\"

##Base Urls where data resides
baseurl = "ftp://ftp.hycom.org/datasets/GLBa0.08/expt_91.2/2017/salt/"

#Intermediate file names
saltfront = "archv.2017_"
saltback = "_00_3zs.nc"


#Calculate local time of today
todaysdoy = str(datetime.datetime.now())
print (todaysdoy)

#Calculate local time's day of year
formattime = time.strftime("%j",time.strptime(todaysdoy,"%Y-%m-%d %H:%M:%S.%f"))
print (formattime)

#Add 7 days to local time's day of year
doy7 = int(formattime) + 7
print (doy7)


#Format download location with file name
downloadlocationSalt = str(os.path.join(downloadfolder) + saltfront + str(doy7) + saltback)
print (downloadlocationSalt)

#Format string request for Sea Surface Temperature
dlHYCOMSalt= str(baseurl + saltfront + str(doy7) + saltback)
print (dlHYCOMSalt)

# Format string request for download
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


