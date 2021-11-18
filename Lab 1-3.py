import os
import matplotlib.image as mpimg
import matplotlib.pylab as plt

os.system("ffmpeg -i Lenna.png -vf scale=240:240,format=gray LennaBW.png")
im1 = mpimg.imread("Lenna.png")
im2 = mpimg.imread("LennaBW.png")


plt.subplot(121), plt.imshow(im1), plt.axis('off'), plt.title('Original Image', size=20)
plt.subplot(122), plt.imshow(im2), plt.axis('off'), plt.title('BW Image', size=20)
plt.show()