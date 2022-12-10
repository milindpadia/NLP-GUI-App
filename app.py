from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):

        # Database object
        self.dbo = Database()

        # API object
        self.apio = API()

        # load login GUI
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap('resources/favicon.ico')
        self.bg_color = "#030039"
        self.root.geometry('400x600')
        self.root.configure(bg=self.bg_color)

        self.login_gui()

        self.root.mainloop()
    
    def login_gui(self):
        # clear previous gui
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # enter email
        label1 = Label(self.root, text='Enter email', bg = self.bg_color, fg = 'white')
        label1.configure(font=('Open Sans', 11))
        label1.pack(pady=(10,5))
        
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=4)

        # enter password
        label2 = Label(self.root, text='Enter password', bg = self.bg_color, fg = 'white')
        label2.configure(font=('Open Sans', 11))
        label2.pack(pady=(10,5))
        
        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5,10), ipady=4)
        
        # login button
        login_button = Button(self.root, text='Login', width=10, height=1, command=self.perform_login)
        login_button.configure(font=('Open Sans', 10))
        login_button.pack(pady=(10,20))

        # not registered? register now
        label3 = Label(self.root, text='Not a member?', bg = self.bg_color, fg = 'white')
        label3.configure(font=('Open Sans', 9))
        label3.pack(pady=(10,5))

        # register now button
        register_button = Button(self.root, text='Register now', width=12, height=1, command=self.register_gui)
        register_button.configure(font=('Open Sans', 10))
        register_button.pack(pady=(10,10))
    
    def register_gui(self):
        # clear existing gui
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # enter name
        label0 = Label(self.root, text='Enter name', bg = self.bg_color, fg = 'white')
        label0.configure(font=('Open Sans', 11))
        label0.pack(pady=(10,5))
        
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady=4)

        # enter email
        label1 = Label(self.root, text='Enter email', bg = self.bg_color, fg = 'white')
        label1.configure(font=('Open Sans', 11))
        label1.pack(pady=(10,5))
        
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5,10), ipady=4)

        # enter password
        label2 = Label(self.root, text='Enter password', bg = self.bg_color, fg = 'white')
        label2.configure(font=('Open Sans', 11))
        label2.pack(pady=(10,5))
        
        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5,10), ipady=4)
        
        # register button
        register_button = Button(self.root, text='Register', width=10, height=1, command=self.perform_registration)
        register_button.configure(font=('Open Sans', 10))
        register_button.pack(pady=(10,20))

        # already a member?
        label3 = Label(self.root, text='Already a member?', bg = self.bg_color, fg = 'white')
        label3.configure(font=('Open Sans', 9))
        label3.pack(pady=(10,5))

        # login button
        login_button = Button(self.root, text='Login', width=12, height=1, command=self.login_gui)
        login_button.configure(font=('Open Sans', 10))
        login_button.pack(pady=(10,10))
        
    def clear_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch data from GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful')
        else:
            messagebox.showerror('Error', 'User already exists')

    def perform_login(self):

        # fetch data from GUI
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email/password')

    def home_gui(self):
        # clear previous GUI
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,30))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # sentiment analysis
        sentiment_button = Button(self.root, text='Sentiment Analysis', width=30, height=2, command=self.sentiment_gui)
        sentiment_button.configure(font=('Open Sans', 12))
        sentiment_button.pack(pady=(10,20))

        # named entity recognition
        ner_button = Button(self.root, text='Named Entity Recognition', width=30, height=2, command=self.named_entity_recognition)
        ner_button.configure(font=('Open Sans', 12))
        ner_button.pack(pady=(10,20))

        # emotion prediction
        emotion_button = Button(self.root, text='Emotion Prediction', width=30, height=2, command=self.emotion_prediction)
        emotion_button.configure(font=('Open Sans', 12))
        emotion_button.pack(pady=(10,20))

        # logout button
        logout_button = Button(self.root, text='Logout', width=12, height=1, command=self.login_gui)
        logout_button.configure(font=('Open Sans', 10))
        logout_button.pack(pady=(10,10))

    def sentiment_gui(self):
        # clear previous GUI
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,5))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # heading2
        heading2 = Label(self.root, text = 'Sentiment Analysis', bg = self.bg_color, fg = 'white')
        heading2.pack(pady=(30,10))
        heading2.configure(font=('Open Sans', 20))
        heading2.pack()

        # enter text
        label1 = Label(self.root, text='Enter text', bg = self.bg_color, fg = 'white')
        label1.configure(font=('Open Sans', 12))
        label1.pack(pady=(10,5))
        #entry box
        self.sentiment_text = Entry(self.root, width=50)
        self.sentiment_text.pack(pady=(5,10), ipady=4)

        # analyze sentiment button
        sentiment_button = Button(self.root, text='Analyse', width=12, height=1, command=self.do_sentiment_analysis)
        sentiment_button.configure(font=('Open Sans', 10))
        sentiment_button.pack(pady=(10,10))

        # result label
        self.sentiment_result = Label(self.root, text='', bg = self.bg_color, fg = 'white')
        self.sentiment_result.configure(font=('Open Sans', 12))
        self.sentiment_result.pack(pady=(10,0))

        # back button
        sentiment_button = Button(self.root, text='Back', width=7, height=1, command=self.home_gui)
        sentiment_button.configure(font=('Open Sans', 10))
        sentiment_button.pack(pady=(5,10))

    def do_sentiment_analysis(self):
        text = self.sentiment_text.get()
        result = self.apio.sentiment_analysis(text)
        
        txt = ''
        for sentiment in result['sentiment']:
            txt += "{}: {}%\n\n".format(sentiment.title(), round(result['sentiment'][sentiment]*100, 2))

        self.sentiment_result['text'] = txt
    
    def named_entity_recognition(self):
        # clear previous GUI
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,5))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # heading2
        heading2 = Label(self.root, text = 'Named Entity Recognition', bg = self.bg_color, fg = 'white')
        heading2.pack(pady=(30,10))
        heading2.configure(font=('Open Sans', 20))
        heading2.pack()

        # enter text
        label1 = Label(self.root, text='Enter text', bg = self.bg_color, fg = 'white')
        label1.configure(font=('Open Sans', 12))
        label1.pack(pady=(10,5))
        #entry box
        self.ner_text = Entry(self.root, width=50)
        self.ner_text.pack(pady=(5,10), ipady=4)

        # analyze ner button
        ner_button = Button(self.root, text='Analyse', width=12, height=1, command=self.do_named_entity_recognition)
        ner_button.configure(font=('Open Sans', 10))
        ner_button.pack(pady=(10,10))

        # result label
        self.ner_result = Label(self.root, text='', bg = self.bg_color, fg = 'white')
        self.ner_result.configure(font=('Open Sans', 12))
        self.ner_result.pack(pady=(10,0))

        # back button
        ner_button = Button(self.root, text='Back', width=7, height=1, command=self.home_gui)
        ner_button.configure(font=('Open Sans', 10))
        ner_button.pack(pady=(5,10))
    
    def do_named_entity_recognition(self):
        text = self.ner_text.get()
        response = self.apio.named_entity_recognition(text)
        string = ''
        for enity in response['entities']:
            string += 'Name - {}'.format(enity['name']) + '\n' + 'Category - {}'.format(enity['category']) + '\n' + '\n'
        self.ner_result['text'] = string
    
    def emotion_prediction(self):
        # clear previous GUI
        self.clear_gui()

        # heading
        heading = Label(self.root, text = 'NLP App', bg = self.bg_color, fg = 'white')
        heading.pack(pady=(30,5))
        heading.configure(font=('Open Sans', 24, 'bold'))
        heading.pack()

        # heading2
        heading2 = Label(self.root, text = 'Emotion Prediction', bg = self.bg_color, fg = 'white')
        heading2.pack(pady=(30,10))
        heading2.configure(font=('Open Sans', 20))
        heading2.pack()

        # enter text
        label1 = Label(self.root, text='Enter text', bg = self.bg_color, fg = 'white')
        label1.configure(font=('Open Sans', 12))
        label1.pack(pady=(10,5))
        #entry box
        self.emotion_prediction_text = Entry(self.root, width=50)
        self.emotion_prediction_text.pack(pady=(5,10), ipady=4)

        # analyze emotion prediction button
        emotion_prediction_button = Button(self.root, text='Analyse', width=12, height=1, command=self.do_emotion_prediction)
        emotion_prediction_button.configure(font=('Open Sans', 10))
        emotion_prediction_button.pack(pady=(10,10))

        # result label
        self.emotion_prediction_result = Label(self.root, text='', bg = self.bg_color, fg = 'white')
        self.emotion_prediction_result.configure(font=('Open Sans', 12))
        self.emotion_prediction_result.pack(pady=(10,0))

        # back button
        emotion_prediction_button = Button(self.root, text='Back', width=7, height=1, command=self.home_gui)
        emotion_prediction_button.configure(font=('Open Sans', 10))
        emotion_prediction_button.pack(pady=(5,10))

    def do_emotion_prediction(self):
        text = self.emotion_prediction_text.get()
        response = self.apio.emotion_prediction(text)

        to_print = ''
        for emotion in response['emotion']:
            to_print += "{}: {}%\n\n".format(emotion, round(response["emotion"][emotion]*100, 2))
        
        self.emotion_prediction_result['text'] = to_print

nlp = NLPApp()