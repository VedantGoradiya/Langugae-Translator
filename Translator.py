from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
root = Tk()
root.geometry('500x400')
root.title('Translator')
root.resizable(False,False)
root.configure(bg='Grey')
lang_dict = {'afrikaans': 'af', 'albanian' : 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
def click(event=None):
    try:
        word1 = TextBlob(varname1.get())
        lan = word1.detect_language()
        lan_todict = languages.get()
        lan_to = lang_dict[lan_todict]
        word1 = word1.translate(from_lang=lan,to=lan_to)
        varname2.set(word1)
    except:
        varname2.set('try in another keyword')
def main_exit():
    rr = messagebox.askyesnocancel('Notification','Do you want to exit',parent=root)
    if(rr==True):
        root.destroy()

def clear():
    varname1.set('')
    varname2.set('')


#################################### combo box
languages = StringVar()
font_box = Combobox(root,width=30,textvariable=languages,state ='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

########################################################################  entry
varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable = varname1,font=('times',15,'italic bold'))
entry1.place(x=150,y=40)

varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable = varname2,font=('times',15,'italic bold'))
entry2.place(x=150,y=100)

############################################# lable
label1 = Label(root,text = 'Enter Words',font=('times',15,'italic bold'),bg='Grey')
label1.place(x=5,y=40)

label2 = Label(root,text = 'Translated',font=('times',15,'italic bold'),bg='Grey')
label2.place(x=5,y=100)

###################################################### buttons
bt1 = Button(root,text='Translate',bd='10',width=10,font=('times',15,'italic bold'),command = click)
bt1.place(x=30,y=170)

bt2 = Button(root,text='Exit',bd='10',width=10,font=('times',15,'italic bold'),command =main_exit)
bt2.place(x=350,y=170)

bt3 = Button(root,text='Clear Fields',bd ='10',width=10,font=('times',15,'italic bold'),command = clear)
bt3.place(x=190,y=170)

root.bind('<Return>',click)


root.mainloop()
