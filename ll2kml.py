#!/usr/bin/env python2.6

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

from gsm2ll import toll
from memoize import Memoized
from uniqgsm import UniqGSM

if __name__ == '__main__':

	with Memoized( toll ) as mtoll:
		print '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n<Document>'
		for gsmll in UniqGSM( 'location_db.txt' ):
			ll = mtoll( gsmll[ 1 ] )
			if ll: print "<Placemark>\n<name>{0[0]}</name>\n<Point>\n<coordinates>{longitude},{latitude}</coordinates>\n</Point>\n</Placemark>".format( gsmll, **ll[ 'location' ] )
		print '</Document>\n</kml>'
