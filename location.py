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

import location, e32, time

while True:
		file = open( 'E:\\Python\\location_db.txt', 'a' ) # change the drive to suit your installation 
		file.write( str( time.time() ) + '\t' + str( location.gsm_location() ) + '\n' )
		file.close()
		e32.ao_sleep( 60 )