"""
    This function will exclude
    any channel from any given RGB image,
    if the image is grayscale, the image
    will be directly returned as rgbExclusion
    cannot be applied to it
    channel value 
    0=red
    1=blue
    2=green
"""

def rgbExclusion(image, channel):
  if(len(image.shape) == 3):
    image[:,:,channel] = np.zeros([image.shape[0], image.shape[1]])
  return image

def convolveImage(image,kernel):
  # kernel = np.flipud(np.fliplr(kernel))
  output = np.zeros_like(image)
  image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
  image_padded[1:-1, 1:-1] = image
  for x in range(image.shape[1]):
    for y in range(image.shape[0]):
      output[y, x]=(kernel * image_padded[y: y+3, x: x+3]).sum()
  return output