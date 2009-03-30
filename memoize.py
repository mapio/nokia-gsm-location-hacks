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