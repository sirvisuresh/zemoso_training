import math
def polysum(n, s):
    
    area = 0.25 * n * s**2 / (math.tan(math.pi/n))
    per = n * s
    return round(area + per**2, 4)