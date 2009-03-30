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
