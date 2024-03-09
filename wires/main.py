from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

image = np.load("wires6npy.txt")

labeled_image = label(image)

for i in range(1, labeled_image.max()+1):
    wire = labeled_image==i
    eros_wire = binary_erosion(wire)
    labeled_eros_wire = label(eros_wire)
    wires_cnt = labeled_eros_wire.max()


    if (wires_cnt) == 1:
        print("Провод цельный")
    elif (wires_cnt) == 0:
        print("Провод анигиллирован")
    else:
        print(f"Провол порван на {wires_cnt} частей")



# plt.subplot(121)
# plt.imshow(image)
# plt.subplot(122)
# plt.imshow(labeled_image)
# plt.show()