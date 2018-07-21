from PIL import Image
def crop(img_path):
    img_before = Image.open(img_path)
    area = (0, 0, 150, 150)
    cropped_img = img_before.crop(area)
    cropped_img.show()
    cropped_img.save()

crop("C:\\Users\\train916.ADRICE\\Desktop\\Week 2\\Day 4\\Lab 8\\dukelogo.png")
