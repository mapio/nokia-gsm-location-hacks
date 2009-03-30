#!/usr/bin/env python2.6

from gsm2ll import toll
from memoize import Memoized
from uniqgsm import UniqGSM

if __name__ == '__main__':

	with Memoized( toll ) as mtoll:
		print '<data>'
		for gsmll in UniqGSM( 'location_db.txt' ):
			ll = mtoll( gsmll[ 1 ] )
			if ll: print '<point lat="{latitude}" lng="{longitude}" />'.format( **ll[ 'location' ] )
		print '</data>'
		
	