parse(geo, df) :
    latDict, lonDict = dict(), dict()

    # identify extreme most latitude and longitude coordinate pairs in each state
    # save coordinate pair of most extreme points for autozoom
    for count in range(0,len(usStates['features'])) :
        if geo['key'] in [code for code in statePctChange['code']] :
            for coords in geo['key']['coordinates'][0] :
                # collect lat, lon data in either geoJSON format
                # lat, lon data will either be in list (coords) or a list of lists (pairs) 
                try :
                    latDict[coords[1]] = coords
                    lonDict[coords[0]] = coords
                except :
                    for pair in coords :
                        latDict[pair[1]] = pair
                        lonDict[pair[0]] = pair
    
    bounds = [list(reversed(l)) for l in [latDict[max([key for key in latDict.keys()])], latDict[min([key for key in latDict.keys()])],
                                          lonDict[max([key for key in lonDict.keys()])], lonDict[min([key for key in lonDict.keys()])]]]
    # keep most extreme bounds to save maximum bounding triangle
    triangle = bounds.remove(min([abs(max([key for key in latDict.keys()])), abs(min([key for key in latDict.keys()])), 
                                  abs(max([key for key in lonDict.keys()])), abs(min([key for key in lonDict.keys()]))]))

    return bounds, triangle
