#https://www.codingame.com/ide/puzzle/2nd-degree-polynomial---simple-analysis

import math

def round_to_meaningful(x):
    """Round to at most 2 decimal places, removing trailing zeros."""
    return '{:.2f}'.format(x).rstrip('0').rstrip('.')

def find_intersections(a, b, c):
    points = []
    
    if a == 0 and b == 0 and c == 0:
        # y = 0
        return ["(0,0)"]
    
    # Y-axis intersection
    y_intersect = c
    points.append((0, y_intersect))
    
    if a == 0:
        if b != 0:
            # Linear function
            x = -c / b
            points.append((x, 0))
    else:
        # Quadratic function
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            points.extend([(x1, 0), (x2, 0)])
        elif delta == 0:
            x = -b / (2*a)
            points.append((x, 0))
    
    # Sort points from left to right
    points.sort(key=lambda p: p[0])
    
    # Format points
    formatted_points = [f"({round_to_meaningful(x)},{round_to_meaningful(y)})" for x, y in points]
    
    return formatted_points

# Read input
a, b, c = map(float, input().split())

# Calculate and print intersections
result = find_intersections(a, b, c)
print(','.join(result))