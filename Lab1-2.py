import os
import matplotlib.image as mpimg
import matplotlib.pylab as plt


os.system("ffmpeg -i Lenna.png -vf scale=120:120 Lenna_120x120.png")
im1 = mpimg.imread("Lenna.png")
im2 = mpimg.imread("Lenna_120x120.png")


plt.subplot(121), plt.imshow(im1), plt.axis('off'), plt.title('Original Image', size=20)
plt.subplot(122), plt.imshow(im2), plt.axis('off'), plt.title('Resized Image', size=20)
plt.show()


