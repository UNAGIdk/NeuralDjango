import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

fig, axes = plt.subplots(1, 2)
fig.set_figheight(5)
fig.set_figwidth(10)

fig.tight_layout()
plt.subplot(121)
plt.title('EDSR Source Image')
plt.imshow('resources/Source Image EDSR')
plt.axis("off")

plt.subplot(122)
fig.tight_layout()
plt.title('EDSR Super Resolution')
plt.imshow('resources/Super Image EDSR')
plt.axis("off")

fig.tight_layout()
plt.subplot(131)
plt.title('WDSR Source Image')
plt.imshow('resources/Source Image WDSR')
plt.axis("off")

plt.subplot(132)
fig.tight_layout()
plt.title('WDSR Super Resolution')
plt.imshow('resources/Super Image WDSR')
plt.axis("off")

fig.tight_layout()
plt.subplot(141)
plt.title('SRGAN Source Image')
plt.imshow('resources/Source Image SRGAN')
plt.axis("off")

plt.subplot(142)
fig.tight_layout()
plt.title('SRGAN Super Resolution')
plt.imshow('resources/Super Image SRGAN')
plt.axis("off")

# plt.title('WDSR Super Resolution')
# plt.title('SRGAN Super Resolution')

# plt.savefig(outputPath, bbox_inches="tight")

plt.show()
