A collection of hacks written in Python to make Nokia phones running Symbian 60 record (and report) the [GSM](http://en.wikipedia.org/wiki/GSM) cell information and their geographical equivalent.

This software is based on
  * Py60
  * Python
  * LightBlue
  * Google Gears

The data (such as [MCC](http://en.wikipedia.org/wiki/Mobile_Country_Code), [MNC](http://en.wikipedia.org/wiki/Mobile_network_code), [LAC](http://en.wikipedia.org/wiki/Mobility_management#Location_area) and [Cell ID](http://en.wikipedia.org/wiki/GSM_localization#Examples_of_LBS_technologies)) are collected by the phone using Py60,  then moved to a internet connected computer via LightBlue and finally geographically mapped using GeolocationAPI.

The code is quite unpolished and the deployment/usage requires several manual steps. But it is simple enough that you should be able to customize it to suit your needs.

Please see the [Howto](Howto.md) for more instructions on installing and using the hacks.