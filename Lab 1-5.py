from scipy.fftpack import dct, idct
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


import matplotlib.image as mpimg
import numpy as np
import matplotlib.pylab as plt

# read lena RGB image
im = mpimg.imread("Lenna.png")
imF = dct2(im)
im1 = idct2(imF)



# plot original and reconstructed images with matplotlib.pylab
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Original Image', size=10)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('Reconstructed Rmage (DCT+IDCT)', size=10)
plt.show()
