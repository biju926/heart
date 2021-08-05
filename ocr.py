# import the following libraries
# will convert the image to text string
import pytesseract      
  
# adds image processing capabilities
from PIL import Image    
  
 # converts the text to speech  
import pyttsx3           
  
#translates into the mentioned language
from googletrans import Translator
import pywhatkit as kit
  
 # opening an image from the source path
img = Image.open('C:\\Users\\manya\\Desktop\\Prescription.jpg')     
  
# describes image format in the output
print(img)                          
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   
#img = Image.open('medicalprescriptionocr.png')    
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)   
# write text in a text file and save it to source path   
with open('abc.txt',mode ='w') as file:     
      
    file.write(result)
    print(result)


