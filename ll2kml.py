#!/usr/bin/env python2.6

from gsm2ll import toll
from memoize import Memoized
from uniqgsm import UniqGSM

if __name__ == '__main__':

	with Memoized( toll ) as mtoll:
		print '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>'
		for gsmll in UniqGSM( 'location_db.txt' ):
			ll = mtoll( gsmll[ 1 ] )
			if ll: print "<Placemark>\n<name>{0[0]}</name>\n<Point>\n<coordinates>{longitude},{latitude}</coordinates>\n</Point>\n</Placemark>".format( gsmll, **ll[ 'location' ] )
		print '</Document>\n</kml>'
