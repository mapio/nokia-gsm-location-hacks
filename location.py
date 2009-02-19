import location, e32, time

while True:
		file = open( 'E:\\Python\\location_db.txt', 'a' )
		file.write( str( time.time() ) + '\t' + str( location.gsm_location() ) + '\n' )
		file.close()
		e32.ao_sleep( 60 )