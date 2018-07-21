from PIL import Image
from PIL import ImageFilter
def SharperImage(img_path, r, p, th):
    sharper_image = Image.open(img_path)
    sharper_image = sharper_image.filter(ImageFilter.UnsharpMask(radius = r, percent = p, threshold = th))
    sharper_image.show()
    sharper_image.save()

SharperImage("C:\\Users\\train916.ADRICE\\Desktop\\Week 2\\Day 4\\Lab 8\\vases.png", 2, 150, 3)
