import lightblue

FILE = 'location_db.txt'
FTP_TARGET_UUID = '\xf9\xec{\xc4\x95<\x11\xd2\x98NRT\x00\xdc\x9e\t'

# change the following two lines to suit your phone, see the Howto in the wiki 

ADDRESS = '00:1B:AF:C5:EF:4F' 
CHANNEL = 11

DIR = 'E:\Python' # change the drive to suit your installation

client = lightblue.obex.OBEXClient( ADDRESS, CHANNEL )

response = client.connect( { 'target': FTP_TARGET_UUID } )

response = client.setpath( {'name': DIR } )

f = file( FILE , 'w' )

response = client.get( { 'name': FILE }, f )

f.close()

response = client.disconnect()
