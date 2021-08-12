# import the following libraries
# will convert the image to text string
import pytesseract      
import numpy as np  
# adds image processing capabilities
from PIL import Image    
from pytesseract import Output  
import cv2

img = Image.open('c:/Users/manya/Desktop/Prescription.jpg')
### describes image format in the output
print(img)                          
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
custom_config = r'--oem 3 --psm 6'
#pytesseract.image_to_string(img, config=custom_config)  
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img,config=custom_config )   
# write text in a text file and save it to source path   
with open('converted.txt',mode ='w') as file:     
    file.write(result)
    print(result)


