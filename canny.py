import cv2
import numpy as np
from matplotlib import pyplot as plt

def is_safe(img, i, j):
    return i>=0 and i<len(img) and j>=0 and j<len(img[0])

def nearest_one(img, i, j):
    
    queue = []
    queue.append((i, j))
    while len(queue) > 0:
        cell = queue[0]
        queue.pop(0)
        if img[cell[0]][cell[1]] == 1:
            return cell
        if is_safe(img, cell[0]+1, cell[1]):
            queue.append((cell[0]+1, cell[1]))
        if is_safe(img, cell[0], cell[1]+1):
            queue.append((cell[0], cell[1]+1))
        if is_safe(img, cell[0]-1, cell[1]):
            queue.append((cell[0]-1, cell[1]))
        if is_safe(img, cell[0], cell[1]-1):
            queue.append((cell[0], cell[1]-1))
            
        if is_safe(img, cell[0]+1, cell[1]+1):
            queue.append((cell[0]+1, cell[1]+1))
        if is_safe(img, cell[0]+1, cell[1]-1):
            queue.append((cell[0]+1, cell[1]-1))
        if is_safe(img, cell[0]-1, cell[1]+1):
            queue.append((cell[0]-1, cell[1]))
        if is_safe(img, cell[0]-1, cell[1]-1):
            queue.append((cell[0]-1, cell[1]-1))

img = cv2.imread('eye1.jpeg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
#print(edges.shape)

i, j = nearest_one(edges,50,100)
print(i)
print(j)

