from math import pi
def sphere_area(radius):
    Area = 4/(3*pi*(radius)**3)
    print (Area)


def sphereVolume (radius):
    Volume = 4*pi*(radius)**2
    return Volume

sphere_area(5)

Volume = sphereVolume(5)
print(f"{Volume}")