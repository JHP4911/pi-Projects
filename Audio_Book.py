'''
Write a python script that can be used to convert a pdf into an audiobook
'''
import pyttsx3,PyPDF2
pdfreader = PyPDF2.pdfFileReader(open('file.pdf','rb'))
speaker = pyttsx3.init()
for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
