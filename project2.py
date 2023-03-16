pi = 3.14

def checkPositiveFloat(num):
  try:
    given = float(num)
    if given < 0:
      return False
    return True
  except ValueError:
    return False

def area(radius: float):
  return pow(radius, 2) * pi

def volume(radius: float, length: float):
  return area(radius) * length

def printCylinder():
  radius = input("Radius of the cylinder: ")

  if checkPositiveFloat(radius) == False:
    return print("Given radius is not an positive number.")

  length = input("Length of the cylinder: ")

  if checkPositiveFloat(length) == False:
    return print("Given length is not an positive number.")

  cRadius = float(radius)
  cLength = float(length)

  cArea = area(cRadius)
  cVolume = volume(cRadius, cLength)

  return print(f"Area: {cArea}, Volume: {cVolume}")

printCylinder()