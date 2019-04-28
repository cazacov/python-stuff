def scale(vector, scaleFactor):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    return [x * scaleFactor,
            y * scaleFactor,
            z * scaleFactor]


def add(v1, v2):
    x1 = v1[0]
    y1 = v1[1]
    z1 = v1[2]
    x2 = v2[0]
    y2 = v2[1]
    z2 = v2[2]
    return [x1 + x2,
            y1 + y2,
            z1 + z2]


def dot_product(v1, v2):
    x1 = v1[0]
    y1 = v1[1]
    z1 = v1[2]
    x2 = v2[0]
    y2 = v2[1]
    z2 = v2[2]
    return x1*x2 + y1*y2 + z1*z2


# Kreuzprodukt
def cross_product(v1, v2):
    x1 = v1[0]
    y1 = v1[1]
    z1 = v1[2]
    x2 = v2[0]
    y2 = v2[1]
    z2 = v2[2]
    return [y1 * z2 - y2 * z1,
            x1 * z2 - x2 * z1,
            x1 * y2 - x2 * y1]

