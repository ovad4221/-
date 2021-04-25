def find_delta(data):
    x = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    y = x["boundedBy"]["Envelope"]
    lower_corner = [float(i) for i in y['lowerCorner'].split()]
    upper_corner = [float(i) for i in y['upperCorner'].split()]

    return [str(abs(round(lower_corner[0] - upper_corner[0], 6))),
            str(abs(round(lower_corner[1] - upper_corner[1], 6)))]


def find_delta_meters(ad1, ad2):
    coord1 = [float(i) for i in ad1.split(',')]
    coord2 = [float(i) for i in ad2.split(',')]
    return round(((111120 * (coord1[0] - coord2[0])) ** 2
                  + (111120 * (coord1[1] - coord2[1])) ** 2) ** 0.5, 1)
