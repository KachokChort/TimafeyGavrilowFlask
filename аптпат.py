from PIL import Image, ImageFilter

def motion_blur(n):
    im = Image.open('image.jpg')
    im1 = im.transpose(Image.Rotate_90)
    im2 = im1.filter(ImageFilter.GaussianBlur(radius=n))
    im2.save('res.jpg')
