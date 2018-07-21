from PIL import Image
from PIL import ImageFilter
def blurredImage(img_path, r):
    blurred_image = Image.open(img_path)
    blurred_image = blurred_image.filter(ImageFilter.GaussianBlur(radius = r))
    blurred_image.show()
    blurred_image.save()

blurredImage("C:\\Users\\train916.ADRICE\\Desktop\\Week 2\\Day 4\\Lab 8\\vases.png", 50)
