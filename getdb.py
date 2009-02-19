import lightblue

FTP_TARGET_UUID = '\xf9\xec{\xc4\x95<\x11\xd2\x98NRT\x00\xdc\x9e\t'
ADDRESS = '00:1B:AF:C5:EF:4F'
CHANNEL = 11

DIR = 'E:\Python'
FILE = 'location_db.txt'

client = lightblue.obex.OBEXClient( ADDRESS, CHANNEL )

response = client.connect( { 'target': FTP_TARGET_UUID } )

response = client.setpath( {'name': DIR } )

f = file( FILE , 'w' )

response = client.get( { 'name': FILE }, f )

f.close()

response = client.disconnect()
