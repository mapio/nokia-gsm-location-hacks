## Install Py60 and (signed) shell on the phone ##

First of all you need to install the Py60 interpreter on the phone. Go to http://sourceforge.net/projects/pys60/ and download the `PythonForS60` SIS and install it (it will suffice to send it to the phone via Bluetooth). Pick the version accoding to the Symbian OS release you have on your phone.

Then download the **unsgned** `PythonScriptShell` SIS file (the filename should contain `unsigned_testrange`) that you'll need to sign yourself. To tho that, get the IMEI of the phone (on my model I just typed `*#06#` on the numpad) and go to [Open Signed Online](https://www.symbiansigned.com/app/page/public/openSignedOnline.do), fill the form, be sure to check `[Select all]` in the `Capability information` section, upload the `PythonScriptShell` SIS and follow the instruction on how to get the signed version. Once you have it, install it on the phone.

It is _very important_ that you sign the shell with all the capabilities, otherwise the phone will not let you access GSM location information.

## Install and run the location script ##

Once you have `PythonForS60` and `PythonScriptShell` SISs installed on the phone, create a `Python` folder on the phone and place there the `location.py` script of this project. The code assumes that you place the `Python` folder  on drive `E:` (usually corresponding to the additional memory card in the phone), the drive is hardcoded in  the `location.py`and `getdb.py`scripts.

You can than start to collect the GSM location information simply activating the `PythonScriptShell` and choosing "Run Script" from the list of its available options (and, obviously, running the `location.py`script).

## Fetch the location data from the phone ##

You can fetch the data via Bluetooh, they are located in a file named `location_db.txt` in the `Python` folder of the phone. If you want to automate that task you can use the `getdb.py` script of this project that is based on LightBlue. To use the script you need to determine the address and channel of your phone OBEX service. You can do that using the `obex_ftp_client.py` script provided as an example in the LightBlue source distribution.


## Map location data to geographical coordinates ##

The `location_db.txt` contains data in the following format
```
 timetsamp ( mobile_country_code, mobile_network_code, location_area_code, cell_id )
```
you can use the Gears GeolocationAPI to map such information to latitude and longitude.

You can find an usage example of such API in the `gsm2ll.py` script of this project that translates the raw data obtained from the phone in latitue and longitude informations. Once you have such a map, you can use the`ll2kml.py` script of this project to obtain  a (very simple) KML file that can be used with Google Earth, or Google Maps.