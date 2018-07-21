from PIL import Image
from PIL import ImageFilter

img_path = input("What file? ")
method = input("Press 1 for blurring, 2 for sharpening, or 3 for cropping (VERY BUGGY). ")
print(img_path)

def blurredImage(img_path, r):
    blurred_image = Image.open(img_path)
    blurred_image = blurred_image.filter(ImageFilter.GaussianBlur(radius = r))
    blurred_image.show()
    blurred_image.save("processed.png")

def SharperImage(img_path, r, p, th):
    sharper_image = Image.open(img_path)
    sharper_image = sharper_image.filter(ImageFilter.UnsharpMask(radius = r, percent = p, threshold = th))
    sharper_image.show()
    sharper_image.save("processed.png")

def crop(img_path, x1, y1, x2, y2):
    img_before = Image.open(img_path)
    area = (x1, y1, x2, y2)
    cropped_img = img_before.crop(area)
    cropped_img.show()
    cropped_img.save("processed.png")

if int(method) == 1:
    r = input("How blurry do you want you photo? Please put in a value greater than 2. ")
    r = int(r)
    blurredImage(img_path, r)

if int(method) == 2:
    r = input("How many pixels do you wants to sharpen? ")
    p = input("What percentage sharper do you want them? ")
    th = input("What is your threshold for sharpening? ")
    r = int(r)
    p = int(p)
    th = int(th)
    SharperImage(img_path, r, p, th)

if int(method) == 3:
    x1, y1, x2, y2 = input("Ök, I warned you. What points do you want to crop?")
    crop(img_path, x1, y1, x2, y2)
