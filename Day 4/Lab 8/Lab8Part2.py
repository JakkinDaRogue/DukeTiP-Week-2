from PIL import Image
# alternatively, try the line below
#import Image    # standard python image library


def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    nim.putdata(pixels)
    return nim

def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


'''
During this lab a pixel is a tuple of 3 values (R, G, B)
representing the red, green, and blue components of a color
that each range from [0-255] inclusive.
The filter functions:
    - take one pixel as an argument,
    - modify the channels of the pixel and
    - return the transformed pixel
'''
def identity(pixel):
    r,g,b = pixel
    return (r,g,b)


def invert(pixel):
    r,g,b = pixel
    return (255-r, 255-g, 255-b)

def darken(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    return(int(r * (9/10)), int(g * (9/10)), int(b * (9/10)))

def brighten(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    return(int(r * (11/10)), int(g * (11/10)), int(b * (11/10)))

def gray_scale(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    grey = (r + g + b) / 3
    return (int (grey), int(grey), int(grey))


def posterize(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    if r >= 0 and r <= 63:
        r = 50
    if r >= 64 and r <= 127:
        r = 100
    if r >= 128 and r <= 191:
        r = 150
    if r >= 192 and r <= 255:
        r = 200
    if g >= 0 and g <= 63:
        g = 50
    if g >= 64 and g <= 127:
        g = 100
    if g >= 128 and g <= 191:
        g = 150
    if g >= 192 and g <= 255:
        g = 200
    if b >= 0 and b <= 63:
        b = 50
    if b >= 64 and b <= 127:
        b = 100
    if b >= 128 and b <= 191:
        b = 150
    if b >= 192 and b <= 255:
        b = 200
    return(r, g, b)
def solarize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - if the value is less than 128, set it to 255 - the original value.
     - if the value is 128 or greater, don't change it.
    """
    # TODO: students fill this in
    r, g, b = pixel
    if r < 128:
        r = 255
    if g < 128:
        g = 255
    if b < 128:
        b = 255
    return(r, g, b)
def denoise(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    g = 0
    b = 0
    r = r*10
    return(r, g, b)

def denoise2(pixel):
    # TODO: students fill this in
    r, g, b = pixel
    r = 0
    g = g * 20
    b = b * 20
    return(r, g, b)

def denoise3(pixel):
    '''
    take noise out of a pixel
    '''
    # TODO: Students fill this in
    r, g, b = pixel
    if r == 255 and g == 0 and b == 0:
        r = 0
        g = 0
        b = 0
    if r == 255 and g == 255 and b == 255:
        r = 0
        g = 0
        b = 0
    return(r, g, b)
def load_and_go(fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")


if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "C:\\Users\\train916.ADRICE\\Desktop\\Week 2\\Day 4\\Lab 8\\clue2.bmp"
    load_and_go(input_file, denoise3)
