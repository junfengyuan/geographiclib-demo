
from geographiclib.geodesic import Geodesic
import math

geod = Geodesic.WGS84  # define the WGS84 ellipsoid

#Consider the geodesic between Beijing Airport (40.1N, 116.6E) and San Fransisco Airport (37.6N, 122.4W). 
# Compute waypoints and azimuths at intervals of 1000 km 
l = geod.InverseLine(40.1, 116.6, 37.6, -122.4)
ds = 1000e3; n = int(math.ceil(l.s13 / ds))
for i in range(n + 1):
   if i == 0:
     print("distance latitude longitude azimuth")
   s = min(ds * i, l.s13)
   g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
   print("{:.0f} {:.5f} {:.5f} {:.5f}".format(g['s12'], g['lat2'], g['lon2'], g['azi2']))

#Solve direct geodetic problem with geographiclib.
#return: coordinates (lat, lon) of second point on a WGS84 globe
def direct_geodetic(latlon, azi, dist):
#param tuple latlon: coordinates of first point
#param azi: azimuth of direction
#param dist: distance in km
    coords = Geodesic.WGS84.Direct(latlon[0], latlon[1], azi, dist * 1000)
    return coords['lat2'], coords['lon2']

latlon = (42.63055, 126.25757)
coords = direct_geodetic(latlon, 30.0, 100)
print("{:.7f} {:.7f}".format(coords[0], coords[1]))
