from tkinter import * #Imports the Tkinter module which is used for developing GUI
from translate import Translator #imports the Translator Module package
# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

text = "ذهب الطالب الى المدرسة"
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction

#Initializes the window
Screen = Tk() #Root window developed from the Tk() class
Screen.title("Language Translator by - Dumilani Konyani") #Displays the title
InputLanguage = StringVar() #The variable InputLanguage stores the text that is going to be translated to another language.
TranslateTo = StringVar()   #This variable stores the text to be translated.

''''A tuple for choosing languages to translate'''
LanguageChoices = {'Arabic','English','Nyanja','French','German','Spanish'}
InputLanguage.set('English')
TranslateTo.set('Nyanja')
#The set() sets the value of the variable

#A function to translate the text
def Translate():
    translator = Translator(from_lang= InputLanguage.get(),to_lang=TranslateTo.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)
'''This function is created to translate the text.
 OutputVar is a variable that stores the translated text.
 TextVar is a variable that contains the text that is to be translated.
 Translator(): It helps to translate the text.
from_lang : It is the language of the text that is being translated.
to_lang: It is the language of the text in which the text is to be translated.
get(): Value of the item is returned with the help of this method.'''	

#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguage,*LanguageChoices)
Label(Screen,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
 
#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateTo,*LanguageChoices)
Label(Screen,text="Translate to").grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)	

'''InputLanguageChoiceMenu provides a choice of input languages. 
NewLanguageChoiceMenu provides a choice of languages in which translation of text is possible.

OptionMenu(): It provides the options that are available to the user.
Label(): This widget helps to implement display boxes where the text can be placed.
grid(): Widgets are arranged on the screen with the help of grid.'''

#Input and Output text 
Label(Screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
 
Label(Screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
 
#Button for calling function
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)
 
mainloop()

'''
Entry(): This widget helps to enter or display a single line text on the screen.
Button(): This widget creates a button.
relief: It helps to provide 3-D effects around the outside of the widget.
mainloop(): It helps to run the tkinter event loop.
'''