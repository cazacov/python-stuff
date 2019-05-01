import math


def vect(fromPoint, toPoint):
    return [toPoint[0] - fromPoint[0],
            toPoint[1] - fromPoint[1],
            toPoint[2] - fromPoint[2]]


def scale(vector, scale_factor):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    return [x * scale_factor,
            y * scale_factor,
            z * scale_factor]


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
            x2 * z1 - x1 * z2,
            x1 * y2 - x2 * y1]


def rotate_x(vertices, angle):
    for point in vertices:
        x = point[0]
        y = point[1]
        z = point[2]
        point[1] = y * math.cos(angle) - z * math.sin(angle)
        point[2] = y * math.sin(angle) + z * math.cos(angle)


def rotate_y(vertices, angle):
    for point in vertices:
        x = point[0]
        y = point[1]
        z = point[2]
        point[0] = x * math.cos(angle) - z * math.sin(angle)
        point[2] = x * math.sin(angle) + z * math.cos(angle)


def rotate_z(vertices, angle):
    for point in vertices:
        x = point[0]
        y = point[1]
        z = point[2]
        point[0] = x * math.cos(angle) - y * math.sin(angle)
        point[1] = x * math.sin(angle) + y * math.cos(angle)


def length(vector):
    return math.sqrt(dot_product(vector, vector))


def cos_angle(vector1, vector2):
    return dot_product(vector1, vector2) / (length(vector1) * length(vector2))
