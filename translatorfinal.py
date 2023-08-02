#Interactive Translator
#Importing libraries
from cProfile import label
import sys 
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from googletrans import Translator
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import pyttsx3 


times = 1
#Global Dictionaries with linked lists 
Widgets = {
    "logo" : [],
    "spanish_logo" :[],
    "italian_logo" :[],
    "portuguese_logo" :[],
    "french_logo" :[],
    "german_logo" :[],
    "lang_buttons" : [], 
    "german_buttons": [],
    "italian_buttons" :[],
    "spanish_buttons":[],
    "french_buttons" :[], 
    "portuguese_buttons": [],
    "testyourknowledge3": [],
    "button":[],
    "textbox" :[],
    "comboBox" : []
}
Labels = {
    "italian_labels": [],
    "german_labels": [],
    "spanish_labels":[],
    "french_labels": [],
    "portuguese_labels": [],
    "other_labels" : []

}


Voice = {
    "voice_buttons" : []
}

#Main frame with grid layout
app = QApplication(sys.argv)
Window = QWidget()
Window.setWindowTitle("Translator")
Window.setStyleSheet("background-color: #BCEE68;")
Window.setGeometry(0,0,5000,1000)
Window.setWindowIcon(QtGui.QIcon('translate.jpeg'))
grid = QGridLayout()
Window.setLayout(grid)

#User defined functions for creating buttons and labels
def clear_widgets():
        for widget in Widgets:
            if Widgets[widget] != []:
                Widgets[widget][-1].hide()
            for i in range(0, len(Widgets[widget])):
                Widgets[widget].pop()

        for i in range(0,len(Labels["other_labels"])) :
            Labels["other_labels"][i].hide()

        for i in range(0,len(Voice["voice_buttons"])) :
            Voice["voice_buttons"][i].hide()
        for i in range(0,len(Labels["italian_labels"])) :
            Labels["italian_labels"][i].hide()
        for i in range(0,len(Labels["spanish_labels"])) :
            Labels["spanish_labels"][i].hide()
        for i in range(0,len(Labels["french_labels"])) :
            Labels["french_labels"][i].hide()
        for i in range(0, len(Labels["portuguese_labels"])):
            Labels["portuguese_labels"][i].hide()
        for i in range(0, len(Labels["german_labels"])):
            Labels["german_labels"][i].hide()

def create_buttons(text) :
    button = QPushButton(text)
    button.setText(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(800)
    button.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")

    return button 

def create_label(text):
    label = QLabel(text)
    label.setText(text)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setFixedWidth(800)
    label.setStyleSheet("*{border: 4px solid '#5D478B';"+
                            "background-color: #BDA0CB; "
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
    return label  

#Label functions
    #German
def hello_german_translated():
    hello_label = create_label("Hallo") 
    Labels["german_labels"].append(hello_label)                        
    grid.addWidget(Labels["german_labels"][-1],1,1,1,1)

def howareyou_german_translated():
    howareyou_label = create_label("Wie ghet es dir") 
    Labels["german_labels"].append(howareyou_label)                        
    grid.addWidget(Labels["german_labels"][-1],2,1,1,1) 

def goodmorning_german_translated():
    goodmorning_label = create_label("Guten morgan/nacht") 
    Labels["german_labels"].append(goodmorning_label)                        
    grid.addWidget(Labels["german_labels"][-1],3,1,1,1) 

def thankyou_german_translated():
    thankyou_label = create_label("Danke") 
    Labels["german_labels"].append(thankyou_label)                        
    grid.addWidget(Labels["german_labels"][-1],4,1,1,1)

def canyouhelpmewith_german_translated():
    canyouhelpmewith_label = create_label("Kannst du mir dabei helfen") 
    Labels["german_labels"].append(canyouhelpmewith_label)                        
    grid.addWidget(Labels["german_labels"][-1],5,1,1,1)                

def sorry_german_translated():
    sorry_label = create_label("Verzeihung") 
    Labels["german_labels"].append(sorry_label)                        
    grid.addWidget(Labels["german_labels"][-1],1,1,1,1)

def mayihavesomewater_german_translated():
    mayihavesomewater_label = create_label("Kann ich etwas wasser haben") 
    Labels["german_labels"].append(mayihavesomewater_label)                        
    grid.addWidget(Labels["german_labels"][-1],2,1,1,1)

def yesno_german_translated():
    yesno_label = create_label("Jawohl/Nein") 
    Labels["german_labels"].append(yesno_label)                        
    grid.addWidget(Labels["german_labels"][-1],3,1,1,1)

def whereareyoufrom_german_translated():
    whereareyoufrom_label = create_label("Woher kommst du") 
    Labels["german_labels"].append(whereareyoufrom_label)                        
    grid.addWidget(Labels["german_labels"][-1],4,1,1,1) 

def excuseme_german_translated():
    excuseme_label = create_label("Verzeihung") 
    Labels["german_labels"].append(excuseme_label)                        
    grid.addWidget(Labels["german_labels"][-1],5,1,1,1)

    #Italian
def hello_italian_translated():
    hello_label_i = create_label("Ciao/Arrivederci") 
    Labels["italian_labels"].append(hello_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],1,1,1,1)

def howareyou_italian_translated():
    howareyou_label_i = create_label("Come Va") 
    Labels["italian_labels"].append(howareyou_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],2,1,1,1)

def goodnight_i() :
    goodnight_label_i = create_label(" Buongiorno/Buonnotte")
    Labels["italian_labels"].append(goodnight_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],3,1,1,1)

def thankyou_i() :
    thankyou_label_i = create_label("Grazie")
    Labels["italian_labels"].append(thankyou_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],4,1,1,1)

def canyouhelpmewiththis_i() :
    canyouhelpmewiththis_label_i = create_label("Puoi aiutarmi con questo")
    Labels["italian_labels"].append(canyouhelpmewiththis_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],5,1,1,1)

def sorry_i() :
    sorry_label_i = create_label("Susate")
    Labels["italian_labels"].append(sorry_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],1,1,1,1)

def canihavesomewater_i() :
    canihavesomewater_label_i = create_label("Posso avere dell'acqua")
    Labels["italian_labels"].append(canihavesomewater_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],2,1,1,1)

def yesno_i() :
    yesno_label_i = create_label("Si/No")
    Labels["italian_labels"].append(yesno_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],3,1,1,1)

def whereareyoufrom_i() :
    whereareyoufrom_label_i = create_label("Di dove sei")
    Labels["italian_labels"].append(whereareyoufrom_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],4,1,1,1)

def excuseme_i() :
    excuseme_label_i = create_label("Scusami")
    Labels["italian_labels"].append(excuseme_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],5,1,1,1)

def name_i() :
    name_label_i = create_label("Come ti chiami?")
    Labels["italian_labels"].append(name_label_i)                        
    grid.addWidget(Labels["italian_labels"][-1],6,1,1,1)


    #Spanish
def hello_s():
    hello_slabel = create_label("Hola!")
    Labels["spanish_labels"].append(hello_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],1,1,1,1)

def howareyou_s():
    howareyou_slabel = create_label("Cómo estás? / Estoy bien")
    Labels["spanish_labels"].append(howareyou_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],5,1,1,1)

def sorry_s():
    sorry_slabel = create_label("Lo siento")
    Labels["spanish_labels"].append(sorry_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],2,1,1,1)

def thankyou_s():
    thankyou_slabel = create_label("Gracias!")
    Labels["spanish_labels"].append(thankyou_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],3,1,1,1)

def gm_s():
    gm_slabel = create_label("Buenos días/Buenes Noches")
    Labels["spanish_labels"].append(gm_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],4,1,1,1)

def canyouhelp_s():
    canyouhelp_slabel = create_label("¿Puedes ayudarme con _____?")
    Labels["spanish_labels"].append(canyouhelp_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],6,1,1,1)

def mayihave_s():
    mayihave_slabel = create_label("¿Me puede dar un poco de agua?")
    Labels["spanish_labels"].append(mayihave_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],1,1,1,1)

def yesno_s():
    yesno_slabel = create_label("Sí / No")
    Labels["spanish_labels"].append(yesno_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],2,1,1,1)

def whereareyoufrom_s():
    whereareyoufrom_slabel = create_label("¿De dónde eres?")
    Labels["spanish_labels"].append(whereareyoufrom_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],3,1,1,1)

def excuseme_s():
    excuseme_slabel = create_label("Discúlpame")
    Labels["spanish_labels"].append(excuseme_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],4,1,1,1)

def name_s():
    name_slabel = create_label("¿Cuál es su nombre? / Mi nombre es ______")
    Labels["spanish_labels"].append(name_slabel)
    grid.addWidget(Labels["spanish_labels"][-1],5,1,1,1)

    #French
def hello_french_translated():
    hello_flabel = create_label("Bonjour/Au revoir") 
    Labels["french_labels"].append(hello_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],1,1,1,1)

def howareyou_french_translated():
    howareyou_flabel = create_label("Comment vas-tu?") 
    Labels["french_labels"].append(howareyou_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],2,1,1,1)

def goodnight_f() :
    goodnight_flabel = create_label("Bonjour/Bonne nuit")
    Labels["french_labels"].append(goodnight_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],3,1,1,1)

def thankyou_f() :
    thankyou_flabel = create_label("Merci")
    Labels["french_labels"].append(thankyou_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],4,1,1,1)

def canyouhelpmewiththis_f() :
    canyouhelpmewiththis_flabel = create_label("Pouvez-vous m'aider avec?")
    Labels["french_labels"].append(canyouhelpmewiththis_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],5,1,1,1)



def sorry_f() :
    sorry_flabel = create_label("Pardon")
    Labels["french_labels"].append(sorry_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],1,1,1,1)

def canihavesomewater_f() :
    canihavesomewater_flabel = create_label("Puis-je avoir de l'eau?")
    Labels["french_labels"].append(canihavesomewater_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],2,1,1,1)

def yesno_f() :
    yesno_flabel = create_label("Oui/Non")
    Labels["french_labels"].append(yesno_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],3,1,1,1)

def whereareyoufrom_f() :
    whereareyoufrom_flabel = create_label("D'où viens-tu?")
    Labels["french_labels"].append(whereareyoufrom_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],4,1,1,1)

def excuseme_f() :
    excuseme_flabel = create_label("Excusez Moi")
    Labels["french_labels"].append(excuseme_flabel)                        
    grid.addWidget(Labels["french_labels"][-1],5,1,1,1)

    


    #Portuguese
def hello_portuguese_translated():
    hello_label = create_label("Olá / Adeus")
    Labels["portuguese_labels"].append(hello_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 1, 1, 1, 1)

def howareyou_portuguese_translated():
    howareyou_label = create_label("Como estás?")
    Labels["portuguese_labels"].append(howareyou_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 2, 1, 1, 1)

def goodnight_p():
    goodnight_label = create_label(" Bom dia/Boa noite ")
    Labels["portuguese_labels"].append(goodnight_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 3, 1, 1, 1)

def thankyou_p():
    thankyou_label = create_label("Obrigado")
    Labels["portuguese_labels"].append(thankyou_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 4, 1, 1, 1)

def canyouhelpmewiththis_p():
    canyouhelpmewiththis_label = create_label("Pode ajudar me com isto?")
    Labels["portuguese_labels"].append(canyouhelpmewiththis_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 5, 1, 1, 1)

def sorry_p():
    sorry_label = create_label("Desculpa")
    Labels["portuguese_labels"].append(sorry_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 1, 1, 1, 1)

def canihavesomewater_p():
    canihavesomewater_label = create_label("Posso ter um pouco de água?")
    Labels["portuguese_labels"].append(canihavesomewater_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 2, 1, 1, 1)

def yesno_p():
    yesno_label = create_label("Sim / Não")
    Labels["portuguese_labels"].append(yesno_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 3, 1, 1, 1)

def whereareyoufrom_p():
    whereareyoufrom_label = create_label("Di dove sei")
    Labels["portuguese_labels"].append(whereareyoufrom_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 4, 1, 1, 1)

def excuseme_p():
    excuseme_label = create_label("De onde és?")
    Labels["portuguese_labels"].append(excuseme_label)
    grid.addWidget(Labels["portuguese_labels"][-1], 5, 1, 1, 1)
#Frames
    #Start frame

def frame1():
    for i in range(0,len(Voice["voice_buttons"])) :
        Voice["voice_buttons"][i].hide()
    clear_widgets()
    #display logo
    image = QPixmap("translation.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    #display button
    button = QPushButton("Start")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("*{border: 4px solid '#C84A6B';" +
                         "border-radius: 45px;" +
                         "font-size: 35px;" +
                         "color: 'black';" +
                         "padding: 25px 0;" +
                         "margin: 100px 200px;}" +
                         "*:hover{background: '#C84A6B';}"
    )
    button.clicked.connect(frame2)
    Widgets["button"].append(button)

    grid.addWidget(Widgets["testyourknowledge3"][-1], 0, 0, 1, 2)
    grid.addWidget(Widgets["button"][-1], 1, 0, 1, 2)

    #Select language frame
def frame2() :
    for i in range(0,len(Voice["voice_buttons"])) :
        Voice["voice_buttons"][i].hide()
    clear_widgets()
    german_btn = QPushButton("German")
    german_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    german_btn.setFixedWidth(800)
    german_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    image = QPixmap("germany (1).png")
    german_logo = QLabel()
    german_logo.setPixmap(image)
    german_logo.setAlignment(QtCore.Qt.AlignCenter)
    german_logo.setStyleSheet("margin-top: 1px;")
    Widgets["german_logo"].append(german_logo)
    grid.addWidget(Widgets["german_logo"][-1],1,1,1,1)                         

    Widgets["lang_buttons"].append(german_btn)                        
    grid.addWidget(Widgets["lang_buttons"][-1],1,0,1,1)
    german_btn.clicked.connect(german_frame1)

    italian_btn = QPushButton("Italian")
    italian_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    italian_btn.setFixedWidth(800)
    italian_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    image = QPixmap("italy (1).png")
    italian_logo = QLabel()
    italian_logo.setPixmap(image)
    italian_logo.setAlignment(QtCore.Qt.AlignCenter)
    italian_logo.setStyleSheet("margin-top: 1px;")
    Widgets["italian_logo"].append(italian_logo)
    grid.addWidget(Widgets["italian_logo"][-1],2,2,1,1)                        

    Widgets["lang_buttons"].append(italian_btn)   
    grid.addWidget(Widgets["lang_buttons"][-1],2,0,1,1)
    italian_btn.clicked.connect(italian_phrases1)

    spanish_btn = QPushButton("Spanish")
    spanish_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    spanish_btn.setFixedWidth(800)
    spanish_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    image = QPixmap("spain.png")
    spanish_logo = QLabel()
    spanish_logo.setPixmap(image)
    spanish_logo.setAlignment(QtCore.Qt.AlignCenter)
    spanish_logo.setStyleSheet("margin-top: 1px;")
    Widgets["spanish_logo"].append(spanish_logo)
    grid.addWidget(Widgets["spanish_logo"][-1],3,1,1,1) 

    Widgets["lang_buttons"].append(spanish_btn)    
    grid.addWidget(Widgets["lang_buttons"][-1],3,0,1,1)
    spanish_btn.clicked.connect(spanish_phrases1)


    french_btn = QPushButton("French")
    french_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    french_btn.setFixedWidth(800)
    french_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    image = QPixmap("france (1).png")
    french_logo = QLabel()
    french_logo.setPixmap(image)
    french_logo.setAlignment(QtCore.Qt.AlignCenter)
    french_logo.setStyleSheet("margin-top: 1px;")
    Widgets["french_logo"].append(french_logo)
    grid.addWidget(Widgets["french_logo"][-1],4,2,1,1)                        

    Widgets["lang_buttons"].append(french_btn)    
    grid.addWidget(Widgets["lang_buttons"][-1],4,0,1,1)
    french_btn.clicked.connect(french_frame1)

    portuguese_btn = QPushButton("Portuguese")
    portuguese_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    portuguese_btn.setFixedWidth(800)
    portuguese_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    image = QPixmap("portugal (1).png")
    portuguese_logo = QLabel()
    portuguese_logo.setPixmap(image)
    portuguese_logo.setAlignment(QtCore.Qt.AlignCenter)
    portuguese_logo.setStyleSheet("margin-top: 1px;")
    Widgets["portuguese_logo"].append(portuguese_logo)
    grid.addWidget(Widgets["portuguese_logo"][-1],5,1,1,1)                        

    Widgets["lang_buttons"].append(portuguese_btn)    
    grid.addWidget(Widgets["lang_buttons"][-1],5,0,1,1)
    portuguese_btn.clicked.connect(portuguese_frame1)

    typeInText_btn = QPushButton("Custom text Translate")
    typeInText_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    typeInText_btn.setFixedWidth(800)
    typeInText_btn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 17px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")

    Widgets["lang_buttons"].append(typeInText_btn)    
    grid.addWidget(Widgets["lang_buttons"][-1],6,0,1,1)
    typeInText_btn.clicked.connect(uni_trans)

def uni_trans() :
    clear_widgets() 
    for i in range(0,len(Widgets["lang_buttons"])) :
        Widgets["lang_buttons"][i].hide()
    
    
  
    titleLabel = QLabel()
    titleLabel.setText('              Custom Text:')
    titleLabel.setAlignment(QtCore.Qt.AlignCenter)
    titleLabel.setStyleSheet("*{border: 4px solid '#BCEE68';" +
                            "font-size: 50px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
                            #"*:hover{background:'#C84A6B';}")

    grid.addWidget(titleLabel,0,0)
    Labels["other_labels"].append(titleLabel) 

  
    
    nameLabel = QLabel()#C84A6B
    nameLabel.setText('Text to be Translated :')
    nameLabel.setAlignment(QtCore.Qt.AlignRight)
    nameLabel.setStyleSheet("*{border: 4px solid '#BCEE68';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
                            #"*:hover{background:'#C84A6B';}")


    line = QLineEdit()
    Widgets["textbox"].append(line)

    line.move(80, 20)
    line.resize(1000, 1000)
    
    nameLabel.move(20, 20)


    line.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
                            #"*:hover{background:'#C84A6B';}")


    pybutton = QPushButton('Translate')
    pybutton.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    Widgets["lang_buttons"].append(pybutton)
    pybutton.resize(200,32)
    pybutton.move(80, 60)
    pybutton.clicked.connect(clickMethod)
    

    combo =  QComboBox()
    Widgets["comboBox"].append(combo)
    langlist= ["","German", "Italian", "Spanish", "Portuguese","French"]
    combo.addItems(langlist)
    combo.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")
    Labels
    
    invi_label1 = QLabel()
    invi_label1.setAlignment(QtCore.Qt.AlignCenter)
    invi_label1.setFixedWidth(800)
    invi_label1.setStyleSheet("*{border: 4px solid '#5D478B';"+
                            "background-color: '#BDA0CB;' "
                            + "border-radius: 15px;" + 
                            "color: '#BDA0CB';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
    grid.addWidget(invi_label1,4,1,3,3)

    Labels["other_labels"].append(invi_label1) 



    invi_label2 = QLabel()
    invi_label2.setAlignment(QtCore.Qt.AlignCenter)
    invi_label2.setFixedWidth(800)
    invi_label2.setStyleSheet("*{border: 4px solid '#5D478B';"+
                            "background-color: '#BDA0CB;' "
                            + "border-radius: 15px;" + 
                            "color: '#BDA0CB';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}")
    grid.addWidget(invi_label2,3,0,3,3)

    Labels["other_labels"].append(invi_label2) 

    exit_btn = create_buttons("Exit")
    Voice["voice_buttons"].append(exit_btn)                        
    grid.addWidget(Voice["voice_buttons"][-1],5,1,1,1)
    exit_btn.clicked.connect(frame2)


    #grid.addWidget(title)
    grid.addWidget(combo,2,0,1,1)
    grid.addWidget(pybutton,2,1,1,1)
    grid.addWidget(line,1,1,1,1)
    grid.addWidget(nameLabel,1,0,1,1)



def clickMethod() :
    text = Widgets["textbox"][-1].text()
    combo_text = Widgets["comboBox"][-1].currentText()
    translator = Translator()
    #print(googletrans.LANGUAGES)
    
    if combo_text == "Italian" :
        result1 = translator.translate(text, src = 'en',dest='it')
        ansText = result1.text
        anslabel = create_label(ansText)
        anslabel.setFixedWidth(800)
        anslabel.setWordWrap(True)
        grid.addWidget(anslabel,3,1,1,1)

        Labels["other_labels"].append(anslabel) 

        saybtn_i = create_voicebtns()
        Voice["voice_buttons"].append(saybtn_i) 
        grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
        saybtn_i.clicked.connect(voice)


    elif combo_text == "Spanish" :
        result2 = translator.translate(text, src = 'en',dest='es')
        ansText = result2.text
        anslabel = create_label(ansText)
        grid.addWidget(anslabel,3,1,1,1)
        Labels["other_labels"].append(anslabel) 

        saybtn_s = create_voicebtns()
        Voice["voice_buttons"].append(saybtn_s) 
        grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
        saybtn_s.clicked.connect(voice)

    elif combo_text == "French" :
        result3 = translator.translate(text, src = 'en',dest='fr')
        ansText = result3.text
        anslabel = create_label(ansText)
        grid.addWidget(anslabel,3,1,1,1)
        Labels["other_labels"].append(anslabel) 

        saybtn_f = create_voicebtns()
        Voice["voice_buttons"].append(saybtn_f) 
        grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
        saybtn_f.clicked.connect(voice)



    elif combo_text == "German" :
        result4 = translator.translate(text, src = 'en',dest='de')
        print(result4.text)
        ansText = result4.text
        anslabel = create_label(ansText)
        grid.addWidget(anslabel,3,1,1,1)
        Labels["other_labels"].append(anslabel) 

        saybtn_g = create_voicebtns()
        Voice["voice_buttons"].append(saybtn_g) 
        grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
        saybtn_g.clicked.connect(voice)

    elif combo_text == "Portuguese" :
        result5 = translator.translate(text, src = 'en',dest='pt')
        ansText = result5.text
        anslabel = create_label(ansText)
        grid.addWidget(anslabel,3,1,1,1)
        Labels["other_labels"].append(anslabel) 

        saybtn_p = create_voicebtns()
        Voice["voice_buttons"].append(saybtn_p) 
        grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
        saybtn_p.clicked.connect(voice)


def create_voicebtns():
    button = QPushButton()
    button.setIcon(QIcon('speaker.png'))
    button.setIconSize(QtCore.QSize(30,30))
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(100)
    button.setStyleSheet("*{border: 4px solid '#BCEE68';"
                            + "border-radius: 15px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#BCEE68';}")

    return button 




def voice() :
    #voice_id = Widgets["voice_ids"]
    text = Widgets["textbox"][-1].text()
    print(text)
    combo_text = Widgets["comboBox"][-1].currentText()
    print(combo_text)
    traslator = Translator()
    


    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    if(combo_text =="Italian"):

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        result_i = traslator.translate(text, src = 'en',dest='it')
        print(result_i.text)
        engine.say(result_i.text) 
        engine.runAndWait() 


    elif(combo_text =="German"):
        print("Ingerman)")

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        result_g = traslator.translate(text, src = 'en',dest='de')
        print(result_g.text)
        engine.say(result_g.text) 
        engine.runAndWait() 

    elif(combo_text =="Portuguese"):

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        result_p = traslator.translate(text, src = 'en',dest='pt')
        print(result_p.text)
        engine.say(result_p.text) 
        engine.runAndWait() 

    elif(combo_text =="French"):

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        result_f = traslator.translate(text, src = 'en',dest='fr')
        print(result_f.text)
        engine.say(result_f.text) 
        engine.runAndWait() 

    elif(combo_text =="Spanish"):

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        result_s = traslator.translate(text, src = 'en',dest='es')
        print(result_s.text)
        engine.say(result_s.text) 
        engine.runAndWait() 
    
    
    #Language frames
def german_frame1():
    clear_widgets()

    hellogoodbye_gbtn = create_buttons("Hello/Goodbye")
    Widgets["german_buttons"].append(hellogoodbye_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 1, 0, 1, 1)
    hellogoodbye_gbtn.clicked.connect(hello_german_translated)
    image = QPixmap("speaker.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    sayhello_g = create_voicebtns()
    Voice["voice_buttons"].append(sayhello_g) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    sayhello_g.clicked.connect(voice_hello_g)
    

    
    howareyou_gbtn = create_buttons("How are you?")
    Widgets["german_buttons"].append(howareyou_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 2, 0, 1, 1)
    howareyou_gbtn.clicked.connect(howareyou_german_translated)

    sayhowareyou_g = create_voicebtns()
    Voice["voice_buttons"].append(sayhowareyou_g) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    sayhowareyou_g.clicked.connect(voice_howareyou_g)

    

    goodnight_gbtn = create_buttons("Good Night/Good Morning")
    Widgets["german_buttons"].append(goodnight_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 3, 0, 1, 1)
    goodnight_gbtn.clicked.connect(goodmorning_german_translated)

    saygoodnight_g = create_voicebtns()
    Voice["voice_buttons"].append(saygoodnight_g) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saygoodnight_g.clicked.connect(voice_goodnight_g)
    
    thankyou_gbtn = create_buttons("Thank You")
    Widgets["german_buttons"].append(thankyou_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 4, 0, 1, 1)
    thankyou_gbtn.clicked.connect(thankyou_german_translated)

    saythankyou_g = create_voicebtns()
    Voice["voice_buttons"].append(saythankyou_g) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saythankyou_g.clicked.connect(voice_thankyou_g)

  
    canyouhelpmewiththis_gbtn = create_buttons("Can you help me with this?")
    Widgets["german_buttons"].append(canyouhelpmewiththis_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 5, 0, 1, 1)
    canyouhelpmewiththis_gbtn.clicked.connect(canyouhelpmewith_german_translated)

    saycanyouhelpmewiththis_g = create_voicebtns()
    Voice["voice_buttons"].append(saycanyouhelpmewiththis_g) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    saycanyouhelpmewiththis_g.clicked.connect(voice_canyouhelpmewiththis_g)

    
    next_gbtn = create_buttons("Next")
    Widgets["german_buttons"].append(next_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 6, 1, 1, 1)
    next_gbtn.clicked.connect(german_frame2)


def german_frame2():
    clear_widgets()

    sorry_gbtn = create_buttons("Sorry")
    Widgets["german_buttons"].append(sorry_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 1, 0, 1, 1)
    sorry_gbtn.clicked.connect(sorry_german_translated)

    saysorry_g = create_voicebtns()
    Voice["voice_buttons"].append(saysorry_g) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    saysorry_g.clicked.connect(voice_sorry_g)

    

    canihavesomewater_gbtn = create_buttons("Can I have some water?")
    Widgets["german_buttons"].append(canihavesomewater_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 2, 0, 1, 1)
    canihavesomewater_gbtn.clicked.connect(mayihavesomewater_german_translated )

    saycanihavesomewater_g = create_voicebtns()
    Voice["voice_buttons"].append(saycanihavesomewater_g) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    saycanihavesomewater_g.clicked.connect(voice_canihavesomewater_g)

    

    yesno_gbtn = create_buttons("Yes / No")
    Widgets["german_buttons"].append(yesno_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 3, 0, 1, 1)
    yesno_gbtn.clicked.connect(yesno_german_translated)

    sayyesno_g = create_voicebtns()
    Voice["voice_buttons"].append(sayyesno_g) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    sayyesno_g.clicked.connect(voice_yesno_g)

   
    whereareyoufrom_gbtn = create_buttons("Where are you from?")
    Widgets["german_buttons"].append(whereareyoufrom_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 4, 0, 1, 1)
    whereareyoufrom_gbtn.clicked.connect(whereareyoufrom_german_translated)

    saywhereareyoufrom_g = create_voicebtns()
    Voice["voice_buttons"].append(saywhereareyoufrom_g) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saywhereareyoufrom_g.clicked.connect(voice_whereareyoufrom_g)

 

   

    excuseme_btn = create_buttons("Excuse me")
    Widgets["german_buttons"].append(excuseme_btn)
    grid.addWidget(Widgets["german_buttons"][-1], 5, 0, 1, 1)
    excuseme_btn.clicked.connect(excuseme_german_translated)

    sayexcuseme_g = create_voicebtns()
    Voice["voice_buttons"].append(sayexcuseme_g ) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayexcuseme_g .clicked.connect(voice_excuseme_g )

   

    exit_gbtn = create_buttons("Exit")
    Widgets["german_buttons"].append(exit_gbtn)
    grid.addWidget(Widgets["german_buttons"][-1], 6, 1, 1, 1)
    exit_gbtn.clicked.connect(frame2)

def voice_hello_g() :
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        engine.say("Hallo ") 
        engine.runAndWait()

def voice_goodnight_g() :
        engine = pyttsx3.init()
        voices = engine.getProperty('voices') 

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        engine.say("Guten morgan / nacht") 
        engine.runAndWait() 
    

 

def voice_thankyou_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Danke") 
    engine.runAndWait() 



def voice_canyouhelpmewiththis_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Kannst du mir dabei helfen?") 
    engine.runAndWait() 

 

def voice_sorry_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Verzeihung") 
    engine.runAndWait() 

 


def voice_canihavesomewater_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Kann ich etwas wasser haben?") 
    engine.runAndWait() 

 

def voice_howareyou_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Wie ghet es dir") 
    engine.runAndWait() 

   



def voice_yesno_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Jawohl/Nein") 
    engine.runAndWait() 

    


def voice_whereareyoufrom_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Woher kommst du?") 
    engine.runAndWait() 


     

def voice_excuseme_g() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Verzeihung") 
    engine.runAndWait() 





def italian_phrases1() :
    clear_widgets()

    hellogoodbye_btn = create_buttons("Hello/Goodbye")
    Widgets["italian_buttons"].append(hellogoodbye_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],1,0,1,1)
    hellogoodbye_btn.clicked.connect(hello_italian_translated)
    image = QPixmap("speaker.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    sayhello_i = create_voicebtns()
    Voice["voice_buttons"].append(sayhello_i) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    sayhello_i.clicked.connect(voice_hello_i)


    howareyou_btn = create_buttons("How are you?")
    Widgets["italian_buttons"].append(howareyou_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],2,0,1,1)
    howareyou_btn.clicked.connect(howareyou_italian_translated)

    sayhowareyou_i = create_voicebtns()
    Voice["voice_buttons"].append(sayhowareyou_i) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    sayhowareyou_i.clicked.connect(voice_howareyou_i)

    goodnight_btn = create_buttons("Good Morning/Night")
    Widgets["italian_buttons"].append(goodnight_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],3,0,1,1)
    goodnight_btn.clicked.connect(goodnight_i)

    saygoodnight_i = create_voicebtns()
    Voice["voice_buttons"].append(saygoodnight_i) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saygoodnight_i.clicked.connect(voice_goodnight_i)

    thankyou_btn = create_buttons("Thank You")
    Widgets["italian_buttons"].append(thankyou_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],4,0,1,1)
    thankyou_btn.clicked.connect(thankyou_i)

    saythankyou_i = create_voicebtns()
    Voice["voice_buttons"].append(saythankyou_i) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saythankyou_i.clicked.connect(voice_thankyou_i)

    canyouhelpmewiththis_ibtn = create_buttons("Can you help me with this?")
    Widgets["italian_buttons"].append(canyouhelpmewiththis_ibtn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],5,0,1,1)
    canyouhelpmewiththis_ibtn.clicked.connect(canyouhelpmewiththis_i)

    saycanyouhelpmewiththis_i = create_voicebtns()
    Voice["voice_buttons"].append(saycanyouhelpmewiththis_i) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    saycanyouhelpmewiththis_i.clicked.connect(voice_canyouhelpmewiththis_i)


    name_ibtn = create_buttons("What is your name?")
    Widgets["italian_buttons"].append(name_ibtn)
    grid.addWidget(Widgets["italian_buttons"][-1],6,0,1,1)
    name_ibtn.clicked.connect(name_i)

    sayname_i = create_voicebtns()
    Voice["voice_buttons"].append(sayname_i) 
    grid.addWidget(Voice["voice_buttons"][-1],6,2,1,1)
    sayname_i.clicked.connect(voice_name_i)


    next_ibtn = create_buttons("Next")
    Widgets["italian_buttons"].append(next_ibtn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],7,1,1,1)
    next_ibtn.clicked.connect(italian_frame2)

def italian_frame2() :
    for i in range(0,len(Widgets["italian_buttons"])) :
        Widgets["italian_buttons"][i].hide()
    clear_widgets()
    
    sorry_btn = create_buttons("Sorry")
    Widgets["italian_buttons"].append(sorry_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],1,0,1,1)
    sorry_btn.clicked.connect(sorry_i)

    saysorry_i = create_voicebtns()
    Voice["voice_buttons"].append(saysorry_i) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    saysorry_i.clicked.connect(voice_sorry_i)

    canihavesomewater_btn = create_buttons("Can I have some water?")
    Widgets["italian_buttons"].append(canihavesomewater_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],2,0,1,1)
    canihavesomewater_btn.clicked.connect(canihavesomewater_i)

    saycanihavesomewater_i = create_voicebtns()
    Voice["voice_buttons"].append(saycanihavesomewater_i) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    saycanihavesomewater_i.clicked.connect(voice_canihavesomewater_i)


    yesno_btn = create_buttons("Yes/No")
    Widgets["italian_buttons"].append(yesno_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],3,0,1,1)
    yesno_btn.clicked.connect(yesno_i)

    sayyesno_i = create_voicebtns()
    Voice["voice_buttons"].append(sayyesno_i) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    sayyesno_i.clicked.connect(voice_yesno_i)

    whereareyoufrom_btn = create_buttons("Where are you from?")
    Widgets["italian_buttons"].append(whereareyoufrom_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],4,0,1,1)
    whereareyoufrom_btn.clicked.connect(whereareyoufrom_i)

    saywhereareyoufrom_i = create_voicebtns()
    Voice["voice_buttons"].append(saywhereareyoufrom_i) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saywhereareyoufrom_i.clicked.connect(voice_whereareyoufrom_i)

    excuseme_btn = create_buttons("Excuse me")
    Widgets["italian_buttons"].append(excuseme_btn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],5,0,1,1)
    excuseme_btn.clicked.connect(excuseme_i)

    sayexcuseme_i = create_voicebtns()
    Voice["voice_buttons"].append(sayexcuseme_i ) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayexcuseme_i .clicked.connect(voice_excuseme_i)

    exit_ibtn = create_buttons("Exit")
    Widgets["italian_buttons"].append(exit_ibtn)                        
    grid.addWidget(Widgets["italian_buttons"][-1],6,1,1,1)
    exit_ibtn.clicked.connect(frame2)  


def voice_hello_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-75)
    engine.say("Ciao/Arrivederci ") 
    engine.runAndWait() 


def voice_goodnight_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-75)
    engine.say("Buona notte / Buon giorno") 
    engine.runAndWait() 
    

 

def voice_thankyou_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Grazie") 
    engine.runAndWait() 



def voice_canyouhelpmewiththis_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Puoi aiutarmi con questo?") 
    engine.runAndWait() 

 

def voice_sorry_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Scusate") 
    engine.runAndWait() 

 


def voice_canihavesomewater_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Posso avere dell'acqua?") 
    engine.runAndWait() 

 

def voice_howareyou_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Come Va") 
    engine.runAndWait() 

   



def voice_yesno_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Si'/No") 
    engine.runAndWait() 

    


def voice_whereareyoufrom_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Di dove sei?") 
    engine.runAndWait() 


     

def voice_excuseme_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Scusami") 
    engine.runAndWait() 

def voice_name_i() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Come ti chiami?") 
    engine.runAndWait()


def spanish_phrases1():
    clear_widgets()

    hello_sbtn = create_buttons("Hello / Goodbye")
    Widgets["spanish_buttons"].append(hello_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],1,0,1,1)
    hello_sbtn.clicked.connect(hello_s)
    image = QPixmap("speaker.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    sayhello_s = create_voicebtns()
    Voice["voice_buttons"].append(sayhello_s) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    sayhello_s.clicked.connect(voice_hello_s)

    sorry_sbtn = create_buttons("Sorry")
    Widgets["spanish_buttons"].append(sorry_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],2,0,1,1)
    sorry_sbtn.clicked.connect(sorry_s)

    saysorry_s = create_voicebtns()
    Voice["voice_buttons"].append(saysorry_s) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    saysorry_s.clicked.connect(voice_sorry_s)

    thankyou_sbtn = create_buttons("Thank you!")
    Widgets["spanish_buttons"].append(thankyou_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],3,0,1,1)
    thankyou_sbtn.clicked.connect(thankyou_s)

    saythankyou_s = create_voicebtns()
    Voice["voice_buttons"].append(saythankyou_s) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saythankyou_s.clicked.connect(voice_thankyou_s)

    gm_sbtn = create_buttons("Good Morning/Night")
    Widgets["spanish_buttons"].append(gm_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],4,0,1,1)
    gm_sbtn.clicked.connect(gm_s)

    saygm_s = create_voicebtns()
    Voice["voice_buttons"].append(saygm_s) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saygm_s.clicked.connect(voice_gm_s)

    howareyou_sbtn = create_buttons("How are you? / I am fine.")
    Widgets["spanish_buttons"].append(howareyou_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],5,0,1,1)
    howareyou_sbtn.clicked.connect(howareyou_s)

    sayhowareyou_s = create_voicebtns()
    Voice["voice_buttons"].append(sayhowareyou_s) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayhowareyou_s.clicked.connect(voice_howareyou_s)

    canyouhelp_sbtn = create_buttons("Can you help me with ______")
    Widgets["spanish_buttons"].append(canyouhelp_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],6,0,1,1)
    canyouhelp_sbtn.clicked.connect(canyouhelp_s)

    saycanyouhelp_s = create_voicebtns()
    Voice["voice_buttons"].append(saycanyouhelp_s) 
    grid.addWidget(Voice["voice_buttons"][-1],6,2,1,1)
    saycanyouhelp_s.clicked.connect(voice_canyouhelp_s)

    next_sbtn = QPushButton("Next")
    next_sbtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    next_sbtn.setFixedWidth(500)
    next_sbtn.setStyleSheet("*{border: 4px solid '#C84A6B';"
                            + "border-radius: 17px;" +
                            "font-size: 25px;"+ 
                            "color: 'black';" +
                            "padding: 15px 0;"+
                            "margin: 25px 150px;}"+
                            "*:hover{background:'#C84A6B';}")

    Widgets["spanish_buttons"].append(next_sbtn)    
    grid.addWidget(Widgets["spanish_buttons"][-1],7,1,1,1)
    next_sbtn.clicked.connect(spanish_phrases2)

def spanish_phrases2():
    for i in range(0,len(Widgets["spanish_buttons"])) :
        Widgets["spanish_buttons"][i].hide()
    clear_widgets()

    mayihave_sbtn = create_buttons("May I have some water?")
    Widgets["spanish_buttons"].append(mayihave_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],1,0,1,1)
    mayihave_sbtn.clicked.connect(mayihave_s)

    saymayihave_s = create_voicebtns()
    Voice["voice_buttons"].append(saymayihave_s) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    saymayihave_s.clicked.connect(voice_mayihave_s)

    yesno_sbtn = create_buttons("Yes/No")
    Widgets["spanish_buttons"].append(yesno_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],2,0,1,1)
    yesno_sbtn.clicked.connect(yesno_s)

    sayyesno_s = create_voicebtns()
    Voice["voice_buttons"].append(sayyesno_s) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    sayyesno_s.clicked.connect(voice_yesno_s)

    whereareyoufrom_sbtn = create_buttons("Where are you from?")
    Widgets["spanish_buttons"].append(whereareyoufrom_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],3,0,1,1)
    whereareyoufrom_sbtn.clicked.connect(whereareyoufrom_s)

    saywhereareyoufrom_s = create_voicebtns()
    Voice["voice_buttons"].append(saywhereareyoufrom_s) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saywhereareyoufrom_s.clicked.connect(voice_whereareyoufrom_s)

    excuseme_sbtn = create_buttons("Excuse me.")
    Widgets["spanish_buttons"].append(excuseme_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],4,0,1,1)
    excuseme_sbtn.clicked.connect(excuseme_s)

    sayexcuseme_s = create_voicebtns()
    Voice["voice_buttons"].append(sayexcuseme_s) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    sayexcuseme_s.clicked.connect(voice_excuseme_s)

    name_sbtn = create_buttons("What is your name? / My name is _____")
    Widgets["spanish_buttons"].append(name_sbtn)
    grid.addWidget(Widgets["spanish_buttons"][-1],5,0,1,1)
    name_sbtn.clicked.connect(name_s)

    sayname_s = create_voicebtns()
    Voice["voice_buttons"].append(sayname_s) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayname_s.clicked.connect(voice_name_s)

    exit_btn = create_buttons("Exit")
    Widgets["spanish_buttons"].append(exit_btn)                        
    grid.addWidget(Widgets["spanish_buttons"][-1],6,1,1,1)
    exit_btn.clicked.connect(frame2)

def voice_hello_s() :
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        engine.say("Hola ") 
        engine.runAndWait() 


def voice_gm_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-75)
    engine.say("Buenos días/Buenes Noches") 
    engine.runAndWait() 
    

 

def voice_thankyou_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Gracias") 
    engine.runAndWait() 



def voice_canyouhelp_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Puedes ayudarme con?") 
    engine.runAndWait() 

 

def voice_sorry_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Lo siento") 
    engine.runAndWait() 

 


def voice_mayihave_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Me puede dar un poco de agua?") 
    engine.runAndWait() 

 

def voice_howareyou_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Cómo estás? / Estoy bien") 
    engine.runAndWait() 

   



def voice_yesno_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Sí / No") 
    engine.runAndWait() 

    


def voice_whereareyoufrom_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("De dónde eres?") 
    engine.runAndWait() 


     

def voice_excuseme_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Discúlpame") 
    engine.runAndWait() 

def voice_name_s() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Cuál es su nombre? / Mi nombre es") 
    engine.runAndWait()



def french_frame1():
    clear_widgets()

    hellogoodbye_btn = create_buttons("Hello/Goodbye")
    Widgets["french_buttons"].append(hellogoodbye_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],1,0,1,1)
    hellogoodbye_btn.clicked.connect(hello_french_translated)
    image = QPixmap("speaker.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    sayhellogoodbye_f = create_voicebtns()
    Voice["voice_buttons"].append(sayhellogoodbye_f) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    sayhellogoodbye_f.clicked.connect(voice_hellogoodbye_f)

    howareyou_btn = create_buttons("How are you?")
    Widgets["french_buttons"].append(howareyou_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],2,0,1,1)
    howareyou_btn.clicked.connect(howareyou_french_translated)

    sayhowareyou_f = create_voicebtns()
    Voice["voice_buttons"].append(sayhowareyou_f) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    sayhowareyou_f.clicked.connect(voice_howareyou_f)

    goodnight_btn = create_buttons("Good Morning/Good Night")
    Widgets["french_buttons"].append(goodnight_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],3,0,1,1)
    goodnight_btn.clicked.connect(goodnight_f)

    saygoodnight_f = create_voicebtns()
    Voice["voice_buttons"].append(saygoodnight_f) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saygoodnight_f.clicked.connect(voice_goodnight_f)

    thankyou_btn = create_buttons("Thank You")
    Widgets["french_buttons"].append(thankyou_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],4,0,1,1)
    thankyou_btn.clicked.connect(thankyou_f)

    saythankyou_f = create_voicebtns()
    Voice["voice_buttons"].append(saythankyou_f) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saythankyou_f.clicked.connect(voice_thankyou_f)
    
    canyouhelpmewiththis_btn = create_buttons("Can you help me with this?")
    Widgets["french_buttons"].append(canyouhelpmewiththis_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],5,0,1,1)
    canyouhelpmewiththis_btn.clicked.connect(canyouhelpmewiththis_f)

    saycanyouhelpmewiththis_f = create_voicebtns()
    Voice["voice_buttons"].append(saycanyouhelpmewiththis_f) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    saycanyouhelpmewiththis_f.clicked.connect(voice_canyouhelpmewiththis_f)

   

   

    next_btn = create_buttons("Next")
    Widgets["french_buttons"].append(next_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],7,1,1,1)
    next_btn.clicked.connect(french_frame2)

def french_frame2() :
    clear_widgets()
    
    sorry_btn = create_buttons("Sorry")
    Widgets["french_buttons"].append(sorry_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],1,0,1,1)
    sorry_btn.clicked.connect(sorry_f)

    saysorry_f = create_voicebtns()
    Voice["voice_buttons"].append(saysorry_f) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    saysorry_f.clicked.connect(voice_sorry_f)

    canihavesomewater_btn = create_buttons("Can I have some water?")
    Widgets["french_buttons"].append(canihavesomewater_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],2,0,1,1)
    canihavesomewater_btn.clicked.connect(canihavesomewater_f)

    saycanihavesomewater_f = create_voicebtns()
    Voice["voice_buttons"].append(saycanihavesomewater_f) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    saycanihavesomewater_f.clicked.connect(voice_canihavesomewater_f)

    yesno_btn = create_buttons("Yes/No")
    Widgets["french_buttons"].append(yesno_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],3,0,1,1)
    yesno_btn.clicked.connect(yesno_f)

    sayyesno_f = create_voicebtns()
    Voice["voice_buttons"].append(sayyesno_f) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    sayyesno_f.clicked.connect(voice_yesno_f)

    whereareyoufrom_btn = create_buttons("Where are you from?")
    Widgets["french_buttons"].append(whereareyoufrom_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],4,0,1,1)
    whereareyoufrom_btn.clicked.connect(whereareyoufrom_f)

    saywhereareyoufrom_f = create_voicebtns()
    Voice["voice_buttons"].append(saywhereareyoufrom_f) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saywhereareyoufrom_f.clicked.connect(voice_whereareyoufrom_f)

    excuseme_btn = create_buttons("Excuse me")
    Widgets["french_buttons"].append(excuseme_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],5,0,1,1)
    excuseme_btn.clicked.connect(excuseme_f)

    sayexcuseme_f = create_voicebtns()
    Voice["voice_buttons"].append(sayexcuseme_f) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayexcuseme_f.clicked.connect(voice_excuseme_f)
   
    exit_btn = create_buttons("Exit")
    Widgets["french_buttons"].append(exit_btn)                        
    grid.addWidget(Widgets["french_buttons"][-1],6,1,1,1)
    exit_btn.clicked.connect(frame2)

def voice_hellogoodbye_f() :
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        engine.say("Bonjour/Au revoir ") 
        engine.runAndWait() 


def voice_goodnight_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-75)
    engine.say("Bonjour/Bonne nuit") 
    engine.runAndWait() 
    

 

def voice_thankyou_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Merci") 
    engine.runAndWait() 



def voice_canyouhelpmewiththis_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Pouvez-vous m'aider avec?") 
    engine.runAndWait() 

 

def voice_sorry_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Pardon") 
    engine.runAndWait() 

 


def voice_canihavesomewater_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Puis-je avoir de l'eau?") 
    engine.runAndWait() 

 

def voice_howareyou_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Comment vas-tu?") 
    engine.runAndWait() 

   



def voice_yesno_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Oui / Non") 
    engine.runAndWait() 

    


def voice_whereareyoufrom_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("D'où viens-tu?") 
    engine.runAndWait() 


     

def voice_excuseme_f() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Excusez Moi") 
    engine.runAndWait() 





def portuguese_frame1():
    clear_widgets()

    hellogoodbye_btn = create_buttons("Hello/Goodbye")
    Widgets["portuguese_buttons"].append(hellogoodbye_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 1, 0, 1, 1)
    hellogoodbye_btn.clicked.connect(hello_portuguese_translated)
    image = QPixmap("speaker.png")
    testyourknowledge3 = QLabel()
    testyourknowledge3.setPixmap(image)
    testyourknowledge3.setAlignment(QtCore.Qt.AlignCenter)
    testyourknowledge3.setStyleSheet("margin-top: 1px;")
    Widgets["testyourknowledge3"].append(testyourknowledge3)

    sayhellogoodbye_p = create_voicebtns()
    Voice["voice_buttons"].append(sayhellogoodbye_p) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    sayhellogoodbye_p.clicked.connect(voice_hellogoodbye_p)


    howareyou_btn = create_buttons("How are you?")
    Widgets["portuguese_buttons"].append(howareyou_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 2, 0, 1, 1)
    howareyou_btn.clicked.connect(howareyou_portuguese_translated)

    sayhowareyou_p = create_voicebtns()
    Voice["voice_buttons"].append(sayhowareyou_p) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    sayhowareyou_p.clicked.connect(voice_howareyou_p)


    goodnight_btn = create_buttons("Good Morning/Good Night")
    Widgets["portuguese_buttons"].append(goodnight_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 3, 0, 1, 1)
    goodnight_btn.clicked.connect(goodnight_p)

    saygoodnight_p = create_voicebtns()
    Voice["voice_buttons"].append(saygoodnight_p) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    saygoodnight_p.clicked.connect(voice_goodnight_p)

    thankyou_btn = create_buttons("Thank You")
    Widgets["portuguese_buttons"].append(thankyou_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 4, 0, 1, 1)
    thankyou_btn.clicked.connect(thankyou_p)

    saythankyou_p = create_voicebtns()
    Voice["voice_buttons"].append(saythankyou_p) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saythankyou_p.clicked.connect(voice_thankyou_p)

    canyouhelpmewiththis_btn = create_buttons("Can you help me with this?")
    Widgets["portuguese_buttons"].append(canyouhelpmewiththis_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 5, 0, 1, 1)
    canyouhelpmewiththis_btn.clicked.connect(canyouhelpmewiththis_p)

    saycanyouhelpmewiththis_p = create_voicebtns()
    Voice["voice_buttons"].append(saycanyouhelpmewiththis_p) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    saycanyouhelpmewiththis_p.clicked.connect(voice_canyouhelpmewiththis_p)

    

    next_btn = create_buttons("Next")
    Widgets["portuguese_buttons"].append(next_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 6, 1, 1, 1)
    next_btn.clicked.connect(portuguese_frame2)


def portuguese_frame2():
    clear_widgets()

    sorry_btn = create_buttons("Sorry")
    Widgets["portuguese_buttons"].append(sorry_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 1, 0, 1, 1)
    sorry_btn.clicked.connect(sorry_p)

    saysorry_p = create_voicebtns()
    Voice["voice_buttons"].append(saysorry_p) 
    grid.addWidget(Voice["voice_buttons"][-1],1,2,1,1)
    saysorry_p.clicked.connect(voice_sorry_p)


    canihavesomewater_btn = create_buttons("Can I have some water?")
    Widgets["portuguese_buttons"].append(canihavesomewater_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 2, 0, 1, 1)
    canihavesomewater_btn.clicked.connect(canihavesomewater_p)

    saycanihavesomewater_p = create_voicebtns()
    Voice["voice_buttons"].append(saycanihavesomewater_p) 
    grid.addWidget(Voice["voice_buttons"][-1],2,2,1,1)
    saycanihavesomewater_p.clicked.connect(voice_canihavesomewater_p)

   


    yesno_btn = create_buttons("Yes / No")
    Widgets["portuguese_buttons"].append(yesno_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 3, 0, 1, 1)
    yesno_btn.clicked.connect(yesno_p)

    sayyesno_p = create_voicebtns()
    Voice["voice_buttons"].append(sayyesno_p) 
    grid.addWidget(Voice["voice_buttons"][-1],3,2,1,1)
    sayyesno_p.clicked.connect(voice_yesno_p)

    whereareyoufrom_btn = create_buttons("Where are you from?")
    Widgets["portuguese_buttons"].append(whereareyoufrom_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 4, 0, 1, 1)
    whereareyoufrom_btn.clicked.connect(whereareyoufrom_p)

    saywhereareyoufrom_p = create_voicebtns()
    Voice["voice_buttons"].append(saywhereareyoufrom_p) 
    grid.addWidget(Voice["voice_buttons"][-1],4,2,1,1)
    saywhereareyoufrom_p.clicked.connect(voice_whereareyoufrom_p)

    

    excuseme_btn = create_buttons("Excuse me")
    Widgets["portuguese_buttons"].append(excuseme_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 5, 0, 1, 1)
    excuseme_btn.clicked.connect(excuseme_p)

    sayexcuseme_p = create_voicebtns()
    Voice["voice_buttons"].append(sayexcuseme_p) 
    grid.addWidget(Voice["voice_buttons"][-1],5,2,1,1)
    sayexcuseme_p.clicked.connect(voice_excuseme_p)

    

    exit_btn = create_buttons("Exit")
    Widgets["portuguese_buttons"].append(exit_btn)
    grid.addWidget(Widgets["portuguese_buttons"][-1], 6, 1, 1, 1)
    exit_btn.clicked.connect(frame2)

def voice_hellogoodbye_p() :
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-75)
        engine.say("Olá / Adeus ") 
        engine.runAndWait() 


def voice_goodnight_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-75)
    engine.say("Bom dia/Boa noite") 
    engine.runAndWait() 
    

 

def voice_thankyou_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Obrigado") 
    engine.runAndWait() 



def voice_canyouhelpmewiththis_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Pode ajudar me com isto ?") 
    engine.runAndWait() 

 

def voice_sorry_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Desculpa") 
    engine.runAndWait() 

 


def voice_canihavesomewater_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Posso ter um pouco de água?") 
    engine.runAndWait() 

 

def voice_howareyou_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Como estás?") 
    engine.runAndWait() 

   



def voice_yesno_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Sim / Não") 
    engine.runAndWait() 

    


def voice_whereareyoufrom_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("Di dove sei?") 
    engine.runAndWait() 


     

def voice_excuseme_p() :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') 

    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say("De onde és?") 
    engine.runAndWait() 


    engine.runAndWait()
#Starting program
frame1()
Window.show()
sys.exit(app.exec_())