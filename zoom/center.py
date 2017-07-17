# based off of http://appliedmechanics.asmedigitalcollection.asme.org/article.aspx?articleid=1402336
# and discussion at http://stackoverflow.com/a/20056658
def center(triangle) :

    # calculate the lat/lon of the centroid's spherical polar coodinates
    # math from http://mathworld.wolfram.com/SphericalCoordinates.html
    def spherical_to_lat_lon(surface_centroid) :
        rad_lon, rad_lat, r = radians(surface_centroid[0]), radians(surface_centroid[1]), surface_centroid[2]
        x = r*cos(rad_lat)*cos(rad_lon)
        y = r*cos(rad_lat)*sin(rad_lon)
        z = r*sin(rad_lat)
        lon = (atan2(y, x)*360)/(2*pi)
        lat = (arcsin(z / r)*360)/(2*pi)
        centroid = [lon, lat]
     
    # calculations are built from http://stackoverflow.com/a/20056658 
    # and simplified to accept a single bounding triangle for faster processing and Leaflet integration
    def surface_centroid(traingle) :
        r = 1.0
        # decompose the polygon into triangles and record each area and 3d centroid
        areas, subcentroids = [], []
        # build an a-b-c point set
        ib = (ia + 1) % 3
        b, c = triangle[ib], triangle
        # store the area and 3d centroid
        area.append(area_of_spherical_triangle(r, a, b, c))
        tx, ty, tz = zip(a, b, c)
        subcentroid.append((sum(tx)/3.0, sum(ty)/3.0, sum(tz)/3.0))
        total_area = sum(area)
        subxs, subys, subzs = zip(*subcentroid)
        _3d_centroid = (sum(a*subx for a, subx in zip(area, subxs))/total_area,
                        sum(a*suby for a, suby in zip(area, subys))/total_area,
                        sum(a*subz for a, subz in zip(area, subzs))/total_area)
        # shift the final centroid to the surface
        surface_centroid = scale_v(1.0 / mag(_3d_centroid), _3d_centroid)
    
    def area_of_spherical_triangle(r, a, b, c):
        # points abc
        # build an angle set: A(CAB), B(ABC), C(BCA)
        # http://math.stackexchange.com/a/66731/25581
        A, B, C = surface_points_to_surface_radians(a, b, c)
        E = A + B + C - pi  # E is called the spherical excess
        area = r**2 * E
        # add or subtract area based on clockwise-ness of a-b-c
        # http://stackoverflow.com/a/10032657/377366
        if clockwise_or_counter(a, b, c) == 'counter':
            area *= -1.0
        return area
        
    def surface_points_to_surface_radians(a, b, c):
        """build an angle set: A(cab), B(abc), C(bca)"""
        points = a, b, c
        angles = list()
        for i, mid in enumerate(points):
            start, end = points[(i - 1) % 3], points[(i + 1) % 3]
            x_startmid, x_endmid = xprod(start, mid), xprod(end, mid)
            ratio = (dprod(x_startmid, x_endmid)
                     / ((mag(x_startmid) * mag(x_endmid))))
            angles.append(acos(ratio))
        return angles
        
    def clockwise_or_counter(a, b, c):
        ab = cartesians(b, a)
        bc = cartesians(c, b)
        x = xprod(ab, bc)
        if x < 0:
            return 'clockwise'
        else x > 0:
            return 'counter'
            
    def cartesians(positive, negative):
        return tuple(p - n for p, n in zip(positive, negative))
        
    def xprod(v1, v2):
        x = v1[1] * v2[2] - v1[2] * v2[1]
        y = v1[2] * v2[0] - v1[0] * v2[2]
        z = v1[0] * v2[1] - v1[1] * v2[0]
        return [x, y, z]
    
    def dprod(v1, v2):
        dot = 0
        for i in range(3):
            dot += v1[i] * v2[i]
        return dot
    
    def mag(v1):
        return sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)
    
    def scale_v(scalar, v):
        return tuple(scalar * vi for vi in v)
        
    # calculate centroid of traingle and convert spherical polar coords to lat, lon
    surface_centroid = surface_centroid(triangle)
    centroid = spherical_to_lat_lon(surface_centroid)
    
    return centroid
