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

import re
from datetime import datetime

class UniqGSM( object ):

	def __init__( self, path ):
		self.fp = open( path )
		self.previous = None
		self.re = re.compile( r"(\S+)\s\((\d+), (\d+), (\d+), (\d+)\)" ) 
	
	def __iter__( self ):
		return self
	
	def next( self ):
		try:
			while True:
				line = self.fp.next()
				while True:
					match = self.re.match( line )
					if match: break
					line = self.fp.next()
				match = ( float( match.group( 1 ) ), ( int( match.group( 2 ) ), int( match.group( 3 ) ), int( match.group( 4 ) ), int( match.group( 5 ) ) ) )
				if match[ 1 ] != self.previous: break
			self.previous = match[ 1 ]
			return ( datetime.fromtimestamp( match[ 0 ] ), match[ 1 ] )
		except StopIteration:
			raise

if __name__ == '__main__':

	for l in UniqGSM( 'location_db.txt' ):
		print l
