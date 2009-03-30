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
