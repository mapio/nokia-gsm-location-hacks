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
