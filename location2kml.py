import httplib, json

resolver_cache = {}

def toll( gsm_location ):

	global resolver_cache
	
	if gsm_location in resolver_cache:
		return resolver_cache[ gsm_location ]

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
	
	retval = json.loads( response )
	
	resolver_cache[ gsm_location ] = retval
	
	return retval


def parse( line ):
	import re
	match = re.match(r"(\S+)\s\((\d+), (\d+), (\d+), (\d+)\)", line )
	if match:
		return ( float( match.group( 1 ) ), ( int( match.group( 2 ) ), int( match.group( 3 ) ), int( match.group( 4 ) ), int( match.group( 5 ) ) ) )
	else:
		return None


if __name__ == '__main__':
	import time

	print '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>'

	lines = open( 'location_db.txt' ).readlines()
	previous = None
	for line in lines:
		tl = parse( line )
		if not tl:
			continue
		if tl[ 1 ] == previous: continue
		tt = str( time.ctime( tl[ 0 ] ) )
		llc = toll( tl[ 1 ] )
		if llc:
			ll = llc['location']
			print "<Placemark>\n<name>{0}</name>\n<Point>\n<coordinates>{longitude},{latitude}</coordinates>\n</Point>\n</Placemark>".format( tt, **ll )
		previous = tl[ 1 ]
		
	print '</Document>\n</kml>'
