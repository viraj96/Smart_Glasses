from pytesser import *
from PIL import  Image

image = 'image_scan.jpg'
file = 'content.txt'
f = open(file,'w')
pic = Image.open(image)
text = image_to_string(pic)
text = image_file_to_string(pic)
text = image_file_to_string(pic, graceful_errors = True)
print text