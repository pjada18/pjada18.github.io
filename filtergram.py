import filters

def main():
    la=input("Choose a File to show and save.")
    im = filters.load_img(la)
    filters.save_img("read.jpeg")
    im = filters.obamicon(im)
    im.show()


main()
