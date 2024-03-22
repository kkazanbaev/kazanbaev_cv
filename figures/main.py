from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

mask1 = np.array([
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0],
        [1,1,0,0],
        [1,1,1,1],
        [1,1,1,1]])

mask2 = np.array([
        [1,1,1,1],
        [1,1,1,1],
        [0,0,1,1],
        [0,0,1,1],
        [1,1,1,1],
        [1,1,1,1]])

mask3 =  np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1]])

mask4 = np.array([
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])

mask5 = np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])


LB = np.load("figures\ps.npy.txt")

labeled = label(LB)

total_obj = labeled.max()
print(f"Total objects = {total_obj}")

print(label(binary_erosion(LB, mask1)).max())
print(label(binary_erosion(LB, mask2)).max())
print(label(binary_erosion(LB, mask3)).max() - label(binary_erosion(LB, mask5)).max())
print(label(binary_erosion(LB, mask4)).max() - label(binary_erosion(LB, mask5)).max())
print(label(binary_erosion(LB, mask5)).max())


plt.imshow(labeled)
plt.show()