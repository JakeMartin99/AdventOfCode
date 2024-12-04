import numpy as np
file = open("day8.txt")
rows = file.read().split("\n")
file.close()
heights = np.array([[int(c) for c in r] for r in rows])
ydim, xdim = len(heights), len(heights[0])
visible = np.array([[i == 0 or i == xdim-1 or j == 0 or j == ydim-1 for i in range(xdim)] for j in range(ydim)])
ymaxs = np.array([h for h in heights[0]])
for y in range(1, ydim-1):
    xmax = heights[y,0]
    for x in range(1, xdim-1):
        h = heights[y,x]
        if h > xmax:
            xmax = h
            visible[y,x] = True
        if h > ymaxs[x]:
            ymaxs[x] = h
            visible[y,x] = True
ymaxs = np.array([h for h in heights[ydim-1]])
for y in range(ydim-2, 0, -1):
    xmax = heights[y,xdim-1]
    for x in range(xdim-2, 0, -1):
        h = heights[y,x]
        if h > xmax:
            xmax = h
            visible[y,x] = True
        if h > ymaxs[x]:
            ymaxs[x] = h
            visible[y,x] = True
print(sum([sum([1 if v else 0 for v in r]) for r in visible]))

left_scores, right_scores = np.zeros(heights.shape, dtype=np.int32), np.zeros(heights.shape, dtype=np.int32)
up_scores, down_scores = np.zeros(heights.shape, dtype=np.int32), np.zeros(heights.shape, dtype=np.int32)
for y in range(0, ydim):
    dist_to_left_of_at_least, dist_to_right_of_at_least = np.zeros(10, dtype=np.int32), np.zeros(10, dtype=np.int32)
    for x in range(0, xdim):
        h = heights[y,x]
        left_scores[y,x] = dist_to_left_of_at_least[h]
        for i in range(10):
            if i <= h:
                dist_to_left_of_at_least[i] = 1 
            else:
                dist_to_left_of_at_least[i] += 1 
        
        xr = (xdim-1)-x
        hr = heights[y,xr]
        right_scores[y,xr] = dist_to_right_of_at_least[hr]
        for i in range(10):
            if i <= hr:
                dist_to_right_of_at_least[i] = 1 
            else:
                dist_to_right_of_at_least[i] += 1
for x in range(0, xdim):
    dist_above_of_at_least, dist_below_of_at_least = np.zeros(10, dtype=np.int32), np.zeros(10, dtype=np.int32)
    for y in range(0, ydim):
        h = heights[y,x]
        up_scores[y,x] = dist_above_of_at_least[h]
        for i in range(10):
            if i <= h:
                dist_above_of_at_least[i] = 1 
            else:
                dist_above_of_at_least[i] += 1 
        
        yu = (ydim-1)-y
        hu = heights[yu,x]
        down_scores[yu,x] = dist_below_of_at_least[hu]
        for i in range(10):
            if i <= hu:
                dist_below_of_at_least[i] = 1 
            else:
                dist_below_of_at_least[i] += 1
prod = left_scores * right_scores * up_scores * down_scores
print(np.amax(prod))
import matplotlib.pyplot as plt
fig, axs = plt.subplots(3,3)
axs[1,1].imshow(heights, cmap="hot", interpolation=None)
axs[1,1].set_title("Heights")
axs[1,0].imshow(left_scores, cmap="hot", interpolation=None)
axs[1,0].set_title("Left")
axs[1,2].imshow(right_scores, cmap="hot", interpolation=None)
axs[1,2].set_title("Right")
axs[0,1].imshow(up_scores, cmap="hot", interpolation=None)
axs[0,1].set_title("Up")
axs[2,1].imshow(down_scores, cmap="hot", interpolation=None)
axs[2,1].set_title("Down")
axs[0,0].imshow(prod, cmap="hot", interpolation=None)
axs[0,0].set_title("Product")
axs[2,0].axis('off')
axs[0,2].axis('off')
axs[2,2].axis('off')
plt.show()