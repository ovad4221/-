def find_delta(data):
    x = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    y = x["boundedBy"]["Envelope"]
    lower_corner = [float(i) for i in y['lowerCorner'].split()]
    upper_corner = [float(i) for i in y['upperCorner'].split()]

    return [str(abs(round(lower_corner[0] - upper_corner[0], 6))),
            str(abs(round(lower_corner[1] - upper_corner[1], 6)))]