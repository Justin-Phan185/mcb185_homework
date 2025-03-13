import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

with open(colorfile) as fp:
	colors = []
	for line in fp:
		line = line.split('\t')
		name = line[0].strip()
		rgb = line[2].strip()
		r, g, b = rgb.split(',')
		colors.append((name, r,g,b))
		
color_match = ''
distance_match = 1000 #chose a value larger then the potential max distance 
for color in colors:
	name = color[0]
	r = int(color[1])
	g = int(color[2])
	b = int(color[3])
	distance = abs(R-r) + abs(G-g) + abs(B-b)	
	if distance <= distance_match:
		distance_match = distance
		color_match = name
print(color_match)
