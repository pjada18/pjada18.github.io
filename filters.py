from PIL import Image

def load_img(la):
    im = Image.open(la, mode="r")
    return im

def show_img(la):
    im.show()

def save_img(la):
    im = load_img(la)
    im.save(la, format = None)
    #show_img(im)

def obamicon(im):
    darkBlue = (0,51,96)      #intensity<182,
    red = (217,26,33)         #182<insentsity<364
    lightBlue = (112,150,158) #364<intensity<546
    yellow = (252,227,166)    #intensity<546
    new_pixels = []
    pixels = im.getdata()
    for p in pixels: #p is a place holder in the tulpe
        intensity = p[0] + p[1] + p[2]
        if intensity<182:
            new_pixels.append(darkBlue)
        elif intensity>=182 and intensity<=364:
            new_pixels.append(red)
        elif intensity>364 and intensity<=546:
            new_pixels.append(lightBlue)
        else:
            new_pixels.append(yellow)
    newim= Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim
