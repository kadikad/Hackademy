from PIL import Image
import code

def rotate_box(an_image):
    box =(100,100,400,400)
    region = an_image.crop(box)   
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed,box)
    return an_image


def to_grayscale(an_image):#convert to grey color 
    grayscale_im = an_image.convert("L")
    return grayscale_im



im=Image.open("C:\\Users\\kadira\\Desktop\\Pictures\\picture2.jpg")
im=rotate_box(im)
im.save("C:\\Users\\kadira\\Desktop\\Pictures\\greyscale\\picture2.jpg")



rotate_all_images = code.get_filenames("C:\\Users\\kadira\\Desktop\\Pictures")
for pic_name in rotate_all_images:
    im = Image.open(pic_name)
    im = rotate_box(im)
    im.show()


im = Image.open("C:\\Users\\kadira\\Desktop\\Pictures\\picture1.jpg")
print(im.size)
format(im.size)

im=rotate_box(im)

im2 = Image.open("C:\\Users\\kadira\\Desktop\\Pictures\\picture2.jpg") #give source for each picture 
im2 = rotate_box(im2)

im.show()
im2.show()
#list all images you want to open 


