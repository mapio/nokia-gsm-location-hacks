#!/usr/bin/env python2.6

# nokia-gsm-location-hacks, record GSM location information with Symbian 60 phones
# Copyright (C) 2009 Massimo Santini
#
# This file is part of nokia-gsm-location-hacks.
# 
# nokia-gsm-location-hacks is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# nokia-gsm-location-hacks is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with nokia-gsm-location-hacks.  If not, see <http://www.gnu.org/licenses/>.

import json
import httplib

from memoize import Memoized
from uniqgsm import UniqGSM

def toll( gsm_location ):

	conn = httplib.HTTPConnection( "www.google.com" )
	
	( mcc, mnc, lac, cid ) = gsm_location
	
	req = { \
		'version': '1.1.0', \
		'radio': 'gsm', 
		'request_address': True, \
		'cell_towers': [ { \
			'cell_id' : str( cid ), \
			'location_area_code' : lac, \
			'mobile_country_code' : mcc, \
			'mobile_network_code' : mnc \
			} ] 
		};

	reqs = json.dumps( req )
	
	conn.request( "POST", "/loc/json", reqs )
	response = conn.getresponse().read()
	conn.close()
	
	return json.loads( response )
	

if __name__ == '__main__':

	with Memoized( toll ) as mtoll:
		for gsmll in UniqGSM( 'location_db.txt' ):
			llc = mtoll( gsmll[ 1 ] )
			if llc:
				ll = llc['location']
				print "{0[0]}, {longitude}, {latitude}".format( gsmll, **ll )
