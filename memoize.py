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

import pickle

class Memoized( object ):

	def __init__( self, func ):
		self.path = func.__name__ + ".pickle"
		try:
			f = open( self.path )
			self.cache = pickle.load( f )
			f.close()
		except IOError:
			self.cache = {}
		self.func = func

	def __enter__( self ):
		def _memoized( *args, **kwargs ):
			ha = list( args )
			ha.extend( sorted( kwargs.items() ) )
			ha = tuple( ha )
			if ha in self.cache: return self.cache[ ha ]
			val = self.func( *args, **kwargs )
			self.cache[ ha ] = val
			return val
		return _memoized

	def __exit__(self, type, value, traceback):
		f = open( self.path, 'w' )
		pickle.dump( self.cache, f )
		f.close()


if __name__ == '__main__':
		
	def myf( x, k1 = 3, k2 = 4 ):
		import time
		time.sleep( 1 )
		return x * 2 
			
	with Memoized( myf ) as myf_m:
		print myf_m( 2 )
		print myf_m( 3 )