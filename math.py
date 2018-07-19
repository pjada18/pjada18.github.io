from PIL import Image
im = Image.open("pic2.jpg", mode='r')
im.show()
print(im.size)
