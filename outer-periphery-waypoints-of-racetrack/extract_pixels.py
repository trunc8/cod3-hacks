#!/usr/bin/env python
import argparse
import csv
import cv2
from itertools import product
import numpy as np

parser = argparse.ArgumentParser(description="Output outer periphery waypoints given a closed loop track image")
parser.add_argument('-i', help="input image path", default="")
args = parser.parse_args()

if args.i == "":
  img = np.zeros((600,600), dtype=np.float64)
  cv2.circle(img, (img.shape[0]//2, img.shape[1]//2), 200, 1., 10)
else:
  img = cv2.imread(args.i, 0)/255.

height, width = img.shape

cv_img = (img*255).astype(np.uint8)
cv2.imshow("Original image", cv_img)
# sys.exit(0)

# Ensure that the starting point lies on outer periphery
y_start, x_start = 0, 0
for row, col in product(range(height), range(width)):
  if img[row, col] == 1:
    y_start, x_start = row, col
    break


# TASK: Move anti-clockwise along the outer periphery
y_curr, x_curr = y_start, x_start
y_next, x_next = -1, -1
# CONVENTION: movement_direction = delta_y, delta_x
dirn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

waypoints = []
waypoints.append((y_curr, x_curr))

while y_next!=y_start or x_next!=x_start:
  offset = 0
  for i in range(len(dirn)):
    row, col = tuple(map(sum, zip((y_curr, x_curr), dirn[i])))
    if img[row, col] == 0:
      offset = i
      break
  for i in range(len(dirn)-1):
    row, col = tuple(map(sum, zip((y_curr, x_curr), dirn[(i+offset)%len(dirn)])))
    if img[row, col] == 1:
      y_next, x_next = row, col
      break
  y_curr, x_curr = y_next, x_next
  waypoints.append((y_curr, x_curr))

with open('waypoints.txt', 'w') as out:
  csv_out = csv.writer(out)
  csv_out.writerows(waypoints)

# VERIFICATION CODE
pixel_img = np.zeros((600,600), dtype=np.float64)
for coord in waypoints:
  pixel_img[coord] = 1
pixel_cv_img = (pixel_img*255).astype(np.uint8)
cv2.imshow("Single pixel width Image", pixel_cv_img)
cv2.waitKey(0)