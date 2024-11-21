
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import random
leaves=random.choice(['has been sanctioned ','has been rejected'])
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tns"
)
mycursor=mydb.cursor()

#first page structure

class MyLabel(tk.Label):
    def __init__(self, master, filename):
        im = Image.open("v.gif")
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('CMYK')
        self.frames = [ImageTk.PhotoImage(first)]

        tk.Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)



root =tk.Tk()
anim = MyLabel(root, 'animated.gif')
anim.pack()
global im10
global i60

#background image
im10=Image.open(r'Title_proj (1).jpg')
i60=ImageTk.PhotoImage(im10)
lb120=tk.Label(root, image=i60).place(x=0,y=0)


#page for login for admin

def admin(q):
    root.destroy()
    
       
    class MyLabel(tk.Label):
        def __init__(self, master, filename):
            im = Image.open("fourcolors7.gif")
            seq =  []
            try:
                while 1:
                    seq.append(im.copy())
                    im.seek(len(seq)) # skip to next frame
            except EOFError:
                pass # we're done

            try:
                self.delay = im.info['duration']
            except KeyError:
                self.delay = 100

            first = seq[0].convert('CMYK')
            self.frames = [ImageTk.PhotoImage(first)]

            tk.Label.__init__(self, master, image=self.frames[0])

            temp = seq[0]
            for image in seq[1:]:
                temp.paste(image)
                frame = temp.convert('RGBA')
                self.frames.append(ImageTk.PhotoImage(frame))

            self.idx = 0

            self.cancel = self.after(self.delay, self.play)

        def play(self):
            self.config(image=self.frames[self.idx])
            self.idx += 1
            if self.idx == len(self.frames):
                self.idx = 0
            self.cancel = self.after(self.delay, self.play)



    b=tk.Tk()
    anim = MyLabel(b, 'animated.gif')
    anim.pack()
  
    b.geometry("512x288")
    un=tk.StringVar()
    pw=tk.StringVar()
    x=tk.Frame(b,width=290,height=250,).place(x=130,y=20)
    L1=tk.Label(b,text="User Name",font=('BankGothic Md BT',16),bg='grey',).place(x=130,y=50)
    E1=tk.Entry(b,textvariable=un,relief=tk.GROOVE,bd=3,width=10,font=('BankGothic Md BT',15)).place(x=260,y=50)
    L2=tk.Label(b,text="Password",font=('BankGothic Md BT',16),bg='grey',).place(x=130,y=100)
    E2=tk.Entry(b,textvariable=pw,show="*",relief=tk.GROOVE,bd=3,width=10,font=('BankGothic Md BT',15)).place(x=260,y=100)
    def login(f):
        x=un.get()
        mycursor.execute("select username from loginpage1 where username='"+x+"'")
        mr=mycursor.fetchone()
        
        if mr==None:
            tk.messagebox.showinfo('info', ' no user found')
        
        z=pw.get()
        mycursor.execute("select password from loginpage1 where username='"+x+"'")
        mv=mycursor.fetchall()
        
        if x=="" or z=="":
            tk.messagebox.showinfo('info','enter the fields')
        
        for i in mv:
           
            a=list(i)
            if z=="":
                tk.messagebox.showinfo('info', 'type the Password')
                break
            elif a[0]==str(z):
                b.destroy()
                d=tk.Tk()
                global im4
                global i5
                global im5
                global i6
                #global im6
                #global i7
                global im7
                global i8
                global im8
                global i9
                global im9
                global i10
                global im10
                global i11
                global im200
                global i500
                #background image
                im200=Image.open(r'rafale1_edit.jpg')
                i500=ImageTk.PhotoImage(im200)
                lb8=tk.Label(d, image=i500)
                
               
               
               
                lb8.pack()
                d.geometry("1707x1024")
               
                x5=tk.Frame(d,width=1550,height=300,bg='#19273D').place(x=0,y=600)
                
                def news(j):
                    y=tk.Toplevel()
                    global im25
                    global i55
                    #background image
                    im25=Image.open(r'cf631c01a5cbba253032a04dc1b80cdc.jpg')
                    i55=ImageTk.PhotoImage(im25)
                    lb12=tk.Label(y, image=i55).place(x=0,y=0)
                    y.geometry("564x639")
                    x3=tk.Frame(y,width=400,height=500,).place(x=80,y=50)
                    L8=tk.Label(y,text=
"""1)Rajnath Singh witnesses para
dropping exercise of Indian
Armed Forces in Leh’s Stakna
2)Indian, Chinese militaries to
carry out verification ofdiseng
-agement process in easternLadakh
3)US aerospace major Boeing compl
-etes delivery of 37 military heli
-copters to India
4)Complete disengagement process
in eastern Ladakh intricate: Indian
Army after talks
5)India asks China to sincerely impl
-ement the understanding reached at
Military Talks
6)US military to stand with India in
conflict with China,indicates White
House official
7)China's light tanks won't survive in
battle with T-90s, say Indian tank comm
-anders
8)After laser-guided anti-tank missile,
India successfully tests new version of
Shaurya Missile
9)We recognise Arunachal Pradesh as Indian
territoryand oppose any claims over it, says
US slamming China indirectly
""",font=('BankGothic Md BT',12),).place(x=80,y=60)
                    
                    
                
                def aboutus(m):
                    x=tk.Toplevel()
                    global im250
                    global i550
                    #background image
                    im250=Image.open(r'9aaedbaad989a90c8bec61b2d7744f16.jpg')
                    i550=ImageTk.PhotoImage(im250)
                    lb12=tk.Label(x, image=i550).place(x=0,y=0)
                    
                    x.geometry("700x900")
                    #table
                    #x153=tk.Frame(x,width=551,height=551,bg="black").place(x=200,y=0)
                                      
                    #table
                    x13=tk.Frame(x,width=377,height=840).place(x=150,y=30)
                    L75=tk.Label(x,text=
'''Founder-1st April
1898;125 years ago
Country	 India
Type	Army
Role	Land warfare
Size	1,237,117
active personnel
960,000 reserve
personnel
Part of	Indian
Armed Forces
Headquarters
Integrated Defence
Headquarters
, Ministry of
Defence, New Delhi
Motto(s)
Service Before Self
Colours	Gold,
red and black

March	Quick:
Qadam Qadam Badhaye Ja
(Keep stepping
forward)
Slow: Samman
Guard (The Guard of Honour)
Anniversaries
Army Day: 15 January
Aircraft315[3]
Commanders
Commander-in-Chief
President Ram Nath Kovind
Chief of Defence Staff (CDS)
General Bipin Rawat
PVSM, UYSM, AVSM, YSM, SM,
VSM, ADC
Chief of the Army Staff
(COAS)	General Manoj
''',font=('BankGothic Md BT',15)).place(x=150,y=40)
                
                    
                def soldiers(e):
                    
                    e=tk.Toplevel()
                    global im16
                    global i15
                    im16=Image.open(r'download.png')
                    i15=ImageTk.PhotoImage(im16)
                    lb17=tk.Label(e, image=i15)
                    lb17.pack()
                    e.geometry("250x150")
        #page for list of soldiers from the options of soldiers
        #-------------------------------------------------------------soldiers------------------------------
                    def maryrs(v):
                        k =tk.Toplevel()
                        global im
                        global i1

                        global lbl1
                        global l1

                        global im2
                        global i2

                        global lbl3
                        global l3

                        global im3
                        global i3

                        global im4
                        global i4

                        #------------------------------------------------------------------------------------
                       


                        im=Image.open("m1.jpg")
                        i1=ImageTk.PhotoImage(im)
                        l2=tk.Label(k,image=i1,height=220,width=180).place(x=0,y=100) 
                        #-----------------------------------------------------------------------------------
                        im2=Image.open("m2.jpg")
                        i2=ImageTk.PhotoImage(im2)
                        lb2=tk.Label(k,image=i2,height=240,width=180).place(x=520,y=80)
                        #------------------------------------------------------------------------------------

                        #lbl3=Image.open("C:\\Users\\Admin\\Desktop\\Python programs\\tkinter-photos\\bg4.jpg")
                        #l3=ImageTk.PhotoImage(lbl3)
                        #lb=tk.Label(a,image=l3)
                        #lb.pack()

                        im3=Image.open("m3.jpg")
                        i3=ImageTk.PhotoImage(im3)
                        lb2=tk.Label(k,image=i3,height=220,width=180).place(x=0,y=340)
                        #--------------------------------------------------------------------------------------
                        im4=Image.open("m5.jpg")
                        i4=ImageTk.PhotoImage(im4)
                        lb1=tk.Label(k,image=i4,height=0,width=180).place(x=520,y=340) 
                        #---------------------------------------------------------------------------------------------------------------------
                        k.title("Martyrs' List")
                        k.geometry("1000x600")
                        x1=tk.Frame(k,width=1000,height=10).place(x=0,y=320)
                        x2=tk.Frame(k,width=1000,height=100).place(x=320,y=570)

                        l1=tk.Label(k,text="List Of Martyrs Who Valiantly Fought At Galwan Valley",font=("Times New Roman",24)).place(x=120,y=10)
                        l2=tk.Label(k,text="Take a moment to pay respects to these bravehearts.",font=("Franklin Gothic",20)).place(x=150,y=60)

                        #----------------------------------------------------------------------------------------------------------------------
                        a1=tk.Label(k,text="1) Name : ",font=("Arial",10)).place(x=190,y=120)
                        a2=tk.Label(k,text="Bikumalla Santosh Babu",font=("Arial",10)).place(x=340,y=120)

                        a3=tk.Label(k,text="2) Place Of Birth : ",font=("Arial",10)).place(x=190,y=160)
                        a4=tk.Label(k,text="Suryapet (Telangana)",font=("Arial",10)).place(x=340,y=160)

                        a5=tk.Label(k,text="3) Post : ",font=("Arial",10)).place(x=190,y=200)
                        a6=tk.Label(k,text="Colonel",font=("Arial",10)).place(x=340,y=200)

                        a7=tk.Label(k,text="4) Regiment Name : ",font=("Arial",10)).place(x=190,y=240)
                        a8=tk.Label(k,text="Bihar 16",font=("Arial",10)).place(x=340,y=240)

                        a9=tk.Label(k,text="5) Service number : ",font=("Arial",10)).place(x=190,y=280)
                        a10=tk.Label(k,text="IC-64405M",font=("Arial",10)).place(x=340,y=280)

                        #-----------------------------------------------------------------------------------


                        l3=tk.Label(k,text="1) Name : ",font=("Arial",10)).place(x=710,y=120)
                        l4=tk.Label(k,text="Mandeep Singh",font=("Arial",10)).place(x=850,y=120)

                        l5=tk.Label(k,text="2) Place Of Birth : ",font=("Arial",10)).place(x=710,y=160)
                        l6=tk.Label(k,text="Patiala Dist(Punjab)",font=("Arial",10)).place(x=850,y=160)

                        l7=tk.Label(k,text="2) Post : ",font=("Arial",10)).place(x=710,y=200)
                        l8=tk.Label(k,text="Naib Subedar",font=("Arial",10)).place(x=850,y=200)

                        l9=tk.Label(k,text="3) Regiment Name : ",font=("Arial",10)).place(x=710,y=240)
                        l10=tk.Label(k,text="Regiment of Artillery",font=("Arial",10)).place(x=850,y=240)

                        l11=tk.Label(k,text="4) Service number : ",font=("Arial",10)).place(x=710,y=280)
                        l12=tk.Label(k,text="JC 280111M",font=("Arial",10)).place(x=850,y=280)

                        #-----------------------------------------------------------------------------------

                        l13=tk.Label(k,text="1) Name : ",font=("Arial",10)).place(x=190,y=370)
                        l14=tk.Label(k,text="Sunil Kumar",font=("Arial",10)).place(x=340,y=370)

                        l15=tk.Label(k,text="2) Place Of Birth : ",font=("Arial",10)).place(x=190,y=410)
                        l16=tk.Label(k,text="Patna dist (Bihar)",font=("Arial",10)).place(x=340,y=410)

                        l17=tk.Label(k,text="2) Post : ",font=("Arial",10)).place(x=190,y=450)
                        l18=tk.Label(k,text="Havildar",font=("Arial",10)).place(x=340,y=450)

                        l19=tk.Label(k,text="3) Regiment Name : ",font=("Arial",10)).place(x=190,y=490)
                        l20=tk.Label(k,text="16 Bihar",font=("Arial",10)).place(x=340,y=490)

                        l21=tk.Label(k,text="4) Service number : ",font=("Arial",10)).place(x=190,y=530)
                        l22=tk.Label(k,text="4282958N",font=("Arial",10)).place(x=340,y=530)

                        #-----------------------------------------------------------------------------------

                        l3=tk.Label(k,text="1) Name : ",font=("Arial",10)).place(x=710,y=370)
                        l4=tk.Label(k,text="Kundan Kumar Ojha",font=("Arial",10)).place(x=850,y=370)

                        l5=tk.Label(k,text="2) Date Of Birth : ",font=("Arial",10)).place(x=710,y=410)
                        l6=tk.Label(k,text="18 Jun 1993",font=("Arial",10)).place(x=850,y=410)

                        l7=tk.Label(k,text="3) Post : ",font=("Arial",10)).place(x=710,y=450)
                        l8=tk.Label(k,text="Sepoy",font=("Arial",10)).place(x=850,y=450)

                        l9=tk.Label(k,text="4) Regiment Name : ",font=("Arial",10)).place(x=710,y=490)
                        l10=tk.Label(k,text="The Bihar Regiment",font=("Arial",10)).place(x=850,y=490)

                        l11=tk.Label(k,text="5) Service number : ",font=("Arial",10)).place(x=710,y=530)
                        l12=tk.Label(k,text="4292067Y",font=("Arial",10)).place(x=850,y=530)


                    def listofsoldiers(r):
                        e.destroy()
                        root=tk.Tk()
                        root.title("soldier Data")
                        root.geometry("600x500")

                        #label12=Label(root,image=photo).grid(row=8,column=5)
                        label1=tk.Label(root,text="Service_number",width=20,height=2,bg="grey").grid(row=0,column=0)
                        label2=tk.Label(root,text="Full_Name",width=20,height=2,bg="grey").grid(row=1,column=0)
                        label3=tk.Label(root,text="Position",width=20,height=2,bg="grey").grid(row=2,column=0)
                        label4=tk.Label(root,text="Phone_Number",width=20,height=2,bg="grey").grid(row=3,column=0)
                        label5=tk.Label(root,text="City",width=20,height=2,bg="grey").grid(row=4,column=0)
                        label6=tk.Label(root,text="State",width=20,height=2,bg="grey").grid(row=5,column=0)
                        label7=tk.Label(root,text="Age",width=20,height=2,bg="grey").grid(row=6,column=0)
                        label8=tk.Label(root,width=10,height=2).grid(row=7,column=2)
                        label9=tk.Label(root,width=10,height=2).grid(row=7,column=4)
                        label10=tk.Label(root,width=10,height=2).grid(row=7,column=6)
                        label11=tk.Label(root,width=10,height=2).grid(row=7,column=8)
                        e1=tk.Entry(root,width=30,borderwidth=8)
                        e1.grid(row=0,column=1)
                        e2=tk.Entry(root,width=30,borderwidth=8)
                        e2.grid(row=1,column=1)
                        e3=tk.Entry(root,width=30,borderwidth=8)
                        e3.grid(row=2,column=1)
                        e4=tk.Entry(root,width=30,borderwidth=8)
                        e4.grid(row=3,column=1)
                        e5=tk.Entry(root,width=30,borderwidth=8)
                        e5.grid(row=4,column=1)
                        e6=tk.Entry(root,width=30,borderwidth=8)
                        e6.grid(row=5,column=1)
                        e7=tk.Entry(root,width=30,borderwidth=8)
                        e7.grid(row=6,column=1)
                        def Register():
                            RollNo=e1.get()
                            dbRollNo=""
                            Select="select RollNo from soldier where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            for i in result:
                                dbRollNo=i[0]
                            if(RollNo == dbRollNo):
                                messagebox.askokcancel("Information","Record Already exists")
                            else:
                                Insert="Insert into soldier(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Full_Name=e2.get()
                                Position=e3.get()
                                Phone_Number=e4.get()   
                                City=e5.get()
                                State=e6.get()
                                Age=e7.get()
                                if(Full_Name !="" and Position !="" and Phone_Number !="" and City !="" and State !="" and Age !=""):
                                    Value=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    mycursor.execute(Insert,Value)
                                    mydb.commit()
                                    messagebox.askokcancel("Information","Record inserted")
                                    e1.delete(0,tk.END)
                                    e2.delete(0,tk.END)
                                    e3.delete(0,tk.END)
                                    e4.delete(0,tk.END)
                                    e5.delete(0,tk.END)
                                    e6.delete(0,tk.END)
                                    e7.delete(0,tk.END)
                                else:
                                    if (Full_Name == "" and Position == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
                                        messagebox.askokcancel("Information","New Entery Fill All Details")
                                    else:
                                         messagebox.askokcancel("Information", "Some fields left blank")
                        def ShowRecord():
                            RollNo=e1.get()
                            dbRollNo=""
                            Select="select RollNo from soldier where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select)
                            result1=mycursor.fetchall()
                            for i in result1:
                                dbRollNo=i[0]
                            Select1="select Full_Name,Position,Phone_Number,City,State,Age from soldier where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select1)
                            result2=mycursor.fetchall()
                            Full_Name=""
                            Position=""
                            Phone_Number=""
                            City=""
                            State=""
                            Age=""
                            if(RollNo == dbRollNo):
                                for i in result2:
                                    Full_Name=i[0]
                                    Position=i[1]
                                    Phone_Number=i[2]
                                    City=i[3]
                                    State=i[4]
                                    Age=i[5]
                                e2.insert(0,Full_Name)
                                e3.insert(0, Position)
                                e4.insert(0, Phone_Number)
                                e5.insert(0, City)
                                e6.insert(0, State)
                                e7.insert(0, Age)
                                
                            else:
                                messagebox.askokcancel("Information","No Record exists")
                        def Delete():
                            RollNo=e1.get()
                            Delete="delete from soldier where RollNo='%s'" %(RollNo)
                            mycursor.execute(Delete)
                            mydb.commit()
                            messagebox.showinfo("Information","Record Deleted")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def Update():
                            RollNo=e1.get()
                            Full_Name=e2.get()
                            Position=e3.get()
                            Phone_Number=e4.get()
                            City=e5.get()
                            State=e6.get()
                            Age=e7.get()
                            Update="Update soldier set Full_Name='%s', Position='%s', Phone_Number='%s', City='%s', State='%s', Age='%s' where RollNo='%s'" %(Full_Name,Position,Phone_Number,City,State,Age,RollNo)
                            mycursor.execute(Update)
                            mydb.commit()
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                            messagebox.showinfo("Info","Record Update")
                           

                        def Showall():
                            class A(tk.Frame):
                                def __init__(self, parent):
                                    tk.Frame.__init__(self, parent)
                                    self.CreateUI()
                                    self.LoadTable()
                                    self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    parent.grid_rowconfigure(0, weight=1)
                                    parent.grid_columnconfigure(0, weight=1)
                                def CreateUI(self):
                                    tv=ttk.Treeview(root)
                                    tv['columns']=('RollNo', 'Full_Name', 'Position', 'Phone_Number', 'City', 'State', 'Age')
                                    tv.heading('#0',text='RollNo',anchor='center')
                                    tv.column('#0',anchor='center')
                                    tv.heading('#1', text='Full_Name', anchor='center')
                                    tv.column('#1', anchor='center')
                                    tv.heading('#2', text='Position', anchor='center')
                                    tv.column('#2', anchor='center')
                                    tv.heading('#3', text='Phone_Number', anchor='center')
                                    tv.column('#3', anchor='center')
                                    tv.heading('#4', text='City', anchor='center')
                                    tv.column('#4', anchor='center')
                                    tv.heading('#5', text='State', anchor='center')
                                    tv.column('#5', anchor='center')
                                    tv.heading('#6', text='Age', anchor='center')
                                    tv.column('#6', anchor='center')
                                    tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    self.treeview =tv
                                    self.grid_rowconfigure(0,weight=1)
                                    self.grid_columnconfigure(0,weight=1)
                                def LoadTable(self):
                                    Select="Select * from soldier"
                                    mycursor.execute(Select)
                                    result=mycursor.fetchall()
                                    RollNo=""
                                    Full_Name=""
                                    Position=""
                                    Phone_Number=""
                                    City=""
                                    State=""
                                    Age=""
                                    for i in result:
                                        RollNo=i[0]
                                        Full_Name=i[1]
                                        Position=i[2]
                                        Phone_Number=i[3]
                                        City=i[4]
                                        State=i[5]
                                        Age=i[6]
                                        self.treeview.insert("",'end',text=RollNo,values=(Full_Name,Position,Phone_Number,City,State,Age))
                            root=tk.Tk()
                            root.title("Overview Page")
                            A(root)
                        def Clear():
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def team():
                            RollNo=e1.get()
                            dbRollNo=""
                            Select="select RollNo from team where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            for i in result:
                                dbRollNo=i[0]
                            if(RollNo == dbRollNo):
                                messagebox.askokcancel("Information","Record Already exists")
                            else:
                                Insert="Insert into team(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Insert1="Insert into teamC(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Full_Name=e2.get()
                                Position=e3.get()
                                Phone_Number=e4.get()
                                City=e5.get()
                                State=e6.get()
                                Age=e7.get()
                                if(Full_Name !="" and Position !="" and Phone_Number !="" and City !="" and State !="" and Age !=""):
                                    Value=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    Value1=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    mycursor.execute(Insert,Value)
                                    mydb.commit()
                                    mycursor.execute(Insert1,Value1)
                                    mydb.commit()
                                    messagebox.askokcancel("Information","Added to team")
                                    e1.delete(0,tk.END)
                                    e2.delete(0,tk.END)
                                    e3.delete(0,tk.END)
                                    e4.delete(0,tk.END)
                                    e5.delete(0,tk.END)
                                    e6.delete(0,tk.END)
                                    e7.delete(0,tk.END)
                                else:
                                    if (Full_Name == "" and Position == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
                                        messagebox.askokcancel("Information","New Entery Fill All Details")
                                    else:
                                         messagebox.askokcancel("Information", "Some fields left blank")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def teamA():
                            RollNo=e1.get()
                            dbRollNo=""
                            Select="select RollNo from teamA where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            for i in result:
                                dbRollNo=i[0]
                            if(RollNo == dbRollNo):
                                messagebox.askokcancel("Information","Record Already exists")
                            else:
                                Insert="Insert into teamA(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Insert1="Insert into teamC(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Full_Name=e2.get()
                                Position=e3.get()
                                Phone_Number=e4.get()
                                City=e5.get()
                                State=e6.get()
                                Age=e7.get()
                                if(Full_Name !="" and Position !="" and Phone_Number !="" and City !="" and State !="" and Age !=""):
                                    Value=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    Value1=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    mycursor.execute(Insert,Value)
                                    mydb.commit()
                                    mycursor.execute(Insert1,Value1)
                                    mydb.commit()
                                    messagebox.askokcancel("Information","Added to team")
                                    e1.delete(0,tk.END)
                                    e2.delete(0,tk.END)
                                    e3.delete(0,tk.END)
                                    e4.delete(0,tk.END)
                                    e5.delete(0,tk.END)
                                    e6.delete(0,tk.END)
                                    e7.delete(0,tk.END)
                                else:
                                    if (Full_Name == "" and Position == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
                                        messagebox.askokcancel("Information","New Entery Fill All Details")
                                    else:
                                         messagebox.askokcancel("Information", "Some fields left blank")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def teamB():
                            RollNo=e1.get()
                            dbRollNo=""
                            Select="select RollNo from teamB where RollNo='%s'" %(RollNo)
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            for i in result:
                                dbRollNo=i[0]
                            if(RollNo == dbRollNo):
                                messagebox.askokcancel("Information","Record Already exists")
                            else:
                                Insert="Insert into teamB(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Insert1="Insert into teamB(RollNo,Full_Name,Position,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
                                Full_Name=e2.get()
                                Position=e3.get()
                                Phone_Number=e4.get()
                                City=e5.get()
                                State=e6.get()
                                Age=e7.get()
                                if(Full_Name !="" and Position !="" and Phone_Number !="" and City !="" and State !="" and Age !=""):
                                    Value=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)
                                    Value1=(RollNo,Full_Name,Position,Phone_Number,City,State,Age)

                                    mycursor.execute(Insert,Value)
                                    mydb.commit()
                                    mycursor.execute(Insert1,Value1)
                                    mydb.commit()
                                    messagebox.askokcancel("Information","Added to team")
                                    e1.delete(0,tk.END)
                                    e2.delete(0,tk.END)
                                    e3.delete(0,tk.END)
                                    e4.delete(0,tk.END)
                                    e5.delete(0,tk.END)
                                    e6.delete(0,tk.END)
                                    e7.delete(0,tk.END)
                                else:
                                    if (Full_Name == "" and Position == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
                                        messagebox.askokcancel("Information","New Entery Fill All Details")
                                    else:
                                         messagebox.askokcancel("Information", "Some fields left blank")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)        


                        def delete():
                            RollNo=e1.get()
                            Delete="delete from team where RollNo='%s'" %(RollNo)
                            mycursor.execute(Delete)
                            mydb.commit()
                            messagebox.showinfo("Information","Record Deleted")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def deleteA():
                            RollNo=e1.get()
                            Delete="delete from teamA where RollNo='%s'" %(RollNo)
                            mycursor.execute(Delete)
                            mydb.commit()
                            messagebox.showinfo("Information","Record Deleted")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)
                        def deleteB():
                            RollNo=e1.get()
                            Delete="delete from teamB where RollNo='%s'" %(RollNo)
                            mycursor.execute(Delete)
                            mydb.commit()
                            messagebox.showinfo("Information","Record Deleted")
                            e1.delete(0,tk.END)
                            e2.delete(0,tk.END)
                            e3.delete(0,tk.END)
                            e4.delete(0,tk.END)
                            e5.delete(0,tk.END)
                            e6.delete(0,tk.END)
                            e7.delete(0,tk.END)

                        def showteam():
                            class A(tk.Frame):
                                def __init__(self, parent):
                                    tk.Frame.__init__(self, parent)
                                    self.CreateUI()
                                    self.LoadTable()
                                    self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    parent.grid_rowconfigure(0, weight=1)
                                    parent.grid_columnconfigure(0, weight=1)
                                def CreateUI(self):
                                    tv=ttk.Treeview(root)
                                    tv['columns']=('RollNo', 'Full_Name', 'Position', 'Phone_Number', 'City', 'State', 'Age')
                                    tv.heading('#0',text='RollNo',anchor='center')
                                    tv.column('#0',anchor='center')
                                    tv.heading('#1', text='Full_Name', anchor='center')
                                    tv.column('#1', anchor='center')
                                    tv.heading('#2', text='Position', anchor='center')
                                    tv.column('#2', anchor='center')
                                    tv.heading('#3', text='Phone_Number', anchor='center')
                                    tv.column('#3', anchor='center')
                                    tv.heading('#4', text='City', anchor='center')
                                    tv.column('#4', anchor='center')
                                    tv.heading('#5', text='State', anchor='center')
                                    tv.column('#5', anchor='center')
                                    tv.heading('#6', text='Age', anchor='center')
                                    tv.column('#6', anchor='center')
                                    tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    self.treeview =tv
                                    self.grid_rowconfigure(0,weight=1)
                                    self.grid_columnconfigure(0,weight=1)
                                def LoadTable(self):
                                    Select="Select * from team"
                                    mycursor.execute(Select)
                                    result=mycursor.fetchall()
                                    RollNo=""
                                    Full_Name=""
                                    Position=""
                                    Phone_Number=""
                                    City=""
                                    State=""
                                    Age=""
                                    for i in result:
                                        RollNo=i[0]
                                        Full_Name=i[1]
                                        Position=i[2]
                                        Phone_Number=i[3]
                                        City=i[4]
                                        State=i[5]
                                        Age=i[6]
                                        self.treeview.insert("",'end',text=RollNo,values=(Full_Name,Position,Phone_Number,City,State,Age))
                            root=tk.Tk()
                            root.title("Team-A")
                            A(root)
                        def showteamA():
                            class A(tk.Frame):
                                def __init__(self, parent):
                                    tk.Frame.__init__(self, parent)
                                    self.CreateUI()
                                    self.LoadTable()
                                    self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    parent.grid_rowconfigure(0, weight=1)
                                    parent.grid_columnconfigure(0, weight=1)
                                def CreateUI(self):
                                    tv=ttk.Treeview(root)
                                    tv['columns']=('RollNo', 'Full_Name', 'Position', 'Phone_Number', 'City', 'State', 'Age')
                                    tv.heading('#0',text='RollNo',anchor='center')
                                    tv.column('#0',anchor='center')
                                    tv.heading('#1', text='Full_Name', anchor='center')
                                    tv.column('#1', anchor='center')
                                    tv.heading('#2', text='Position', anchor='center')
                                    tv.column('#2', anchor='center')
                                    tv.heading('#3', text='Phone_Number', anchor='center')
                                    tv.column('#3', anchor='center')
                                    tv.heading('#4', text='City', anchor='center')
                                    tv.column('#4', anchor='center')
                                    tv.heading('#5', text='State', anchor='center')
                                    tv.column('#5', anchor='center')
                                    tv.heading('#6', text='Age', anchor='center')
                                    tv.column('#6', anchor='center')
                                    tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    self.treeview =tv
                                    self.grid_rowconfigure(0,weight=1)
                                    self.grid_columnconfigure(0,weight=1)
                                def LoadTable(self):
                                    Select="Select * from teamA"
                                    mycursor.execute(Select)
                                    result=mycursor.fetchall()
                                    RollNo=""
                                    Full_Name=""
                                    Position=""
                                    Phone_Number=""
                                    City=""
                                    State=""
                                    Age=""
                                    for i in result:
                                        RollNo=i[0]
                                        Full_Name=i[1]
                                        Position=i[2]
                                        Phone_Number=i[3]
                                        City=i[4]
                                        State=i[5]
                                        Age=i[6]
                                        self.treeview.insert("",'end',text=RollNo,values=(Full_Name,Position,Phone_Number,City,State,Age))
                            root=tk.Tk()
                            root.title("Team-B")
                            A(root)
                        def showteamB():
                            class A(tk.Frame):
                                def __init__(self, parent):
                                    tk.Frame.__init__(self, parent)
                                    self.CreateUI()
                                    self.LoadTable()
                                    self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    parent.grid_rowconfigure(0, weight=1)
                                    parent.grid_columnconfigure(0, weight=1)
                                def CreateUI(self):
                                    tv=ttk.Treeview(root)
                                    tv['columns']=('RollNo', 'Full_Name', 'Position', 'Phone_Number', 'City', 'State', 'Age')
                                    tv.heading('#0',text='RollNo',anchor='center')
                                    tv.column('#0',anchor='center')
                                    tv.heading('#1', text='Full_Name', anchor='center')
                                    tv.column('#1', anchor='center')
                                    tv.heading('#2', text='Position', anchor='center')
                                    tv.column('#2', anchor='center')
                                    tv.heading('#3', text='Phone_Number', anchor='center')
                                    tv.column('#3', anchor='center')
                                    tv.heading('#4', text='City', anchor='center')
                                    tv.column('#4', anchor='center')
                                    tv.heading('#5', text='State', anchor='center')
                                    tv.column('#5', anchor='center')
                                    tv.heading('#6', text='Age', anchor='center')
                                    tv.column('#6', anchor='center')
                                    tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                    self.treeview =tv
                                    self.grid_rowconfigure(0,weight=1)
                                    self.grid_columnconfigure(0,weight=1)
                                def LoadTable(self):
                                    Select="Select * from teamB"
                                    mycursor.execute(Select)
                                    result=mycursor.fetchall()
                                    RollNo=""
                                    Full_Name=""
                                    Position=""
                                    Phone_Number=""
                                    City=""
                                    State=""
                                    Age=""
                                    for i in result:
                                        RollNo=i[0]
                                        Full_Name=i[1]
                                        Position=i[2]
                                        Phone_Number=i[3]
                                        City=i[4]
                                        State=i[5]
                                        Age=i[6]
                                        self.treeview.insert("",'end',text=RollNo,values=(Full_Name,Position,Phone_Number,City,State,Age))
                            root=tk.Tk()
                            root.title("Overview Page")
                            A(root)                 

            

                        button1=tk.Button(root,text="Register",width=15,height=2,command=Register).grid(row=0,column=2)
                        button2=tk.Button(root,text="Delete",width=15,height=2,command=Delete).grid(row=1,column=2)
                        button3=tk.Button(root,text="Update",width=15,height=2,command=Update).grid(row=2,column=2)
                        button4=tk.Button(root,text="Show record",width=15,height=2,command=ShowRecord).grid(row=3,column=2)
                        button5=tk.Button(root,text="Show All",width=15,height=2,command=Showall).grid(row=4,column=2)
                        button6=tk.Button(root,text="Clear",width=15,height=2,command=Clear).grid(row=5,column=2)
                        
                        
                        button7=tk.Button(root,text="Add to team-A",width=15,height=2,command=team).grid(row=7,column=0)
                        button10=tk.Button(root,text="Add to team-B",width=15,height=2,command=teamA).grid(row=7,column=1)
                        button11=tk.Button(root,text="Add to team-C",width=15,height=2,command=teamB).grid(row=7,column=2)
                        button2=tk.Button(root,text="Delete member from team-A",width=25,height=2,command=delete).grid(row=8,column=0)
                        button2=tk.Button(root,text="Delete member from team-B",width=25,height=2,command=deleteA).grid(row=8,column=1)
                        button2=tk.Button(root,text="Delete member from team-C",width=25,height=2,command=deleteB).grid(row=8,column=2)
                        button8=tk.Button(root,text="show team-A",width=15,height=2,command=showteam).grid(row=9,column=0)
                        button8=tk.Button(root,text="show team-B",width=15,height=2,command=showteamA).grid(row=9,column=1)
                        button8=tk.Button(root,text="show team-C",width=15,height=2,command=showteam).grid(row=9,column=2)


                       



                        
                        
            
            
                    
                                            
                    def hover4(r):
                        buttonsoldierslist["bg"]="#ffffff"
                        buttonsoldierslist["fg"]="#000000"
                    def leave4(r):
                        buttonsoldierslist["bg"]="#000000"
                        buttonsoldierslist["fg"]="#ffffff"


                    buttonsoldierslist=tk.Button(e,text="soldier",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)

                    buttonsoldierslist.bind("<Enter>", hover4)
                    buttonsoldierslist.bind("<Button-1>",listofsoldiers)
                    buttonsoldierslist.bind("<Button-3>",listofsoldiers)
                    buttonsoldierslist.bind("<Return>",listofsoldiers)
                    buttonsoldierslist.bind("<Leave>",leave4)
                    buttonsoldierslist.place(x=55,y=20)
                    def hover4(v):
                        buttonmartyrs["bg"]="#ffffff"
                        buttonmartyrs["fg"]="#000000"
                    def leave4(v):
                        buttonmartyrs["bg"]="#000000"
                        buttonmartyrs["fg"]="#ffffff"


                    buttonmartyrs=tk.Button(e,text="Martyrs",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)

                    buttonmartyrs.bind("<Enter>", hover4)
                    buttonmartyrs.bind("<Button-1>",maryrs)
                    buttonmartyrs.bind("<Button-3>",maryrs)
                    buttonmartyrs.bind("<Return>",maryrs)
                    buttonmartyrs.bind("<Leave>",leave4)
                    buttonmartyrs.place(x=65,y=75)

                    #buttonsoldierslist=tk.Button(e,text="soldier",bg='grey',font=('BankGothic Md BT',19),relief=tk.RAISED,command=listofsoldiers ).place(x=55,y=20)
                    #buttonmartyrs=tk.Button(e,text="Martyrs",bg='grey',font=('BankGothic Md BT',19),relief=tk.RAISED,command=maryrs).place(x=65,y=75)
                    

        #------------------------------------------------------WEAPONS-----------------------------------------------------------------------
                def weapons(e):
                    root=tk.Tk()
                    root.title("weapon Data")
                    root.geometry("600x500")

                    #label12=Label(root,image=photo).grid(row=8,column=5)
                    label1=tk.Label(root,text="serial_no",width=20,height=2,bg="grey").grid(row=0,column=0)
                    label2=tk.Label(root,text="weapon_name",width=20,height=2,bg="grey").grid(row=1,column=0)
                    label3=tk.Label(root,text="manufactured_by",width=20,height=2,bg="grey").grid(row=2,column=0)
                    label4=tk.Label(root,text="numbers",width=20,height=2,bg="grey").grid(row=3,column=0)
                    label5=tk.Label(root,text="bullet_size",width=20,height=2,bg="grey").grid(row=4,column=0)
                    label6=tk.Label(root,text="type_of_weapon",width=20,height=2,bg="grey").grid(row=5,column=0)
                    label8=tk.Label(root,width=10,height=2).grid(row=7,column=2)
                    label9=tk.Label(root,width=10,height=2).grid(row=7,column=4)
                    label10=tk.Label(root,width=10,height=2).grid(row=7,column=6)
                    label11=tk.Label(root,width=10,height=2).grid(row=7,column=8)
                    e1=tk.Entry(root,width=30,borderwidth=8)
                    e1.grid(row=0,column=1)
                    e2=tk.Entry(root,width=30,borderwidth=8)
                    e2.grid(row=1,column=1)
                    e3=tk.Entry(root,width=30,borderwidth=8)
                    e3.grid(row=2,column=1)
                    e4=tk.Entry(root,width=30,borderwidth=8)
                    e4.grid(row=3,column=1)
                    e5=tk.Entry(root,width=30,borderwidth=8)
                    e5.grid(row=4,column=1)
                    e6=tk.Entry(root,width=30,borderwidth=8)
                    e6.grid(row=5,column=1)
                    
                    def Register():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from weapons where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into weapons(S_no,weapon_name,Manufactured_by,numbers,bullet_size,Type_of_weapons) values(%s,%s,%s,%s,%s,%s)"
                            weapon_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            bullet_size=e5.get()
                            type_of_weapon=e6.get()
                            
                            if(weapon_name !="" and manufactured_by !="" and numbers !="" and  bullet_size !="" and type_of_weapon !="" ):
                                Value=(serial_no,weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                
                            else:
                                if (weapon_name == "" and manufactured_by == "" and numbers == "" and bullet_size == "" and type_of_weapon == "" ):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def ShowRecord():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from weapons where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        Select1="select weapon_name,Manufactured_by,numbers,bullet_size,Type_of_weapons from weapons where S_no='%s'" %(serial_no)
                        mycursor.execute(Select1)
                        result2=mycursor.fetchall()
                        weapon_name=""
                        manufactured_by=""
                        numbers=""
                        bullet_size=""
                        type_of_weapon=""
                        if(serial_no == dbserial_no):
                            for i in result2:
                                weapon_name=i[0]
                                manufactured_by=i[1]
                                numbers=i[2]
                                bullet_size=i[3]
                                type_of_weapon=i[4]
                                
                            e2.insert(0,weapon_name)
                            e3.insert(0, manufactured_by)
                            e4.insert(0, numbers)
                            e5.insert(0, bullet_size)
                            e6.insert(0, type_of_weapon)
                            
                            
                        else:
                            messagebox.askokcancel("Information","No Record exists")

                   
                    def Update():
                        serial_no=e1.get()
                        weapon_name=e2.get()
                        manufactured_by=e3.get()
                        numbers=e4.get()
                        bullet_size=e5.get()
                        type_of_weapon=e6.get()
                        
                        Update="Update weapons set weapon_name='%s', Manufactured_by='%s', numbers='%s', bullet_size='%s', Type_of_weapons='%s' where S_no='%s'" %( weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon,serial_no)
                        mycursor.execute(Update)
                        mydb.commit()
                        messagebox.showinfo("Info","Record Update")
                        

                    def Showall():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'weapon_name', 'manufactured_by', 'numbers', 'bullet_size', 'type_of_weapon')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='weapon_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='bullet_size', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_weapon', anchor='center')
                                tv.column('#5', anchor='center')
                               
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from weapons"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                weapon_name=""
                                manufactured_by=""
                                numbers=""
                                bullet_size=""
                                type_of_weapon=""
                                
                                for i in result:
                                    serial_no=i[0]
                                    weapon_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    bullet_size=i[4]
                                    type_of_weapon=i[5]
                                    
                                    self.treeview.insert("",'end',text=serial_no,values=(weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def Clear():
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        
                    def weaponteamA():
                        
                        serial_no=e1.get()
                        
                        dbserial_no=""
                        Select="select S_no from weapon_tean where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into weapon_tean(S_no,weapon_name,Manufactured_by,numbers,bullet_size,Type_of_weapons) values(%s,%s,%s,%s,%s,%s)"
                            weapon_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update weapons set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            bullet_size=e5.get()
                            type_of_weapon=e6.get()
                            
                            if(weapon_name !="" and manufactured_by !="" and numbers !="" and  bullet_size !="" and type_of_weapon !="" ):
                                Value=(serial_no,weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                
                            else:
                                if (weapon_name == "" and manufactured_by == "" and numbers == "" and bullet_size == "" and type_of_weapon == "" ):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def weaponteamB():
                        serial_no=e1.get()
                        
                        dbserial_no=""
                        Select="select S_no from weapon_teanA where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into weapon_teanA(S_no,weapon_name,Manufactured_by,numbers,bullet_size,Type_of_weapons) values(%s,%s,%s,%s,%s,%s)"
                            weapon_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update weapons set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            bullet_size=e5.get()
                            type_of_weapon=e6.get()
                            
                            if(weapon_name !="" and manufactured_by !="" and numbers !="" and  bullet_size !="" and type_of_weapon !="" ):
                                Value=(serial_no,weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                
                            else:
                                if (weapon_name == "" and manufactured_by == "" and numbers == "" and bullet_size == "" and type_of_weapon == "" ):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def weaponteamC():
                        serial_no=e1.get()
                        
                        dbserial_no=""
                        Select="select S_no from weapon_teanB where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into weapon_teanB(S_no,weapon_name,Manufactured_by,numbers,bullet_size,Type_of_weapons) values(%s,%s,%s,%s,%s,%s)"
                            weapon_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update weapons set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            bullet_size=e5.get()
                            type_of_weapon=e6.get()
                            
                            if(weapon_name !="" and manufactured_by !="" and numbers !="" and  bullet_size !="" and type_of_weapon !="" ):
                                Value=(serial_no,weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                
                            else:
                                if (weapon_name == "" and manufactured_by == "" and numbers == "" and bullet_size == "" and type_of_weapon == "" ):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")            
                    def deleteA():
                        serial_no=e1.get()
                        Delete="delete from weapon_tean where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                    def deleteB():
                        serial_no=e1.get()
                        Delete="delete from weapon_teanA where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                    def deleteC():
                        serial_no=e1.get()
                        Delete="delete from weapon_teanB where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        

                    def showteamA():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'weapon_name', 'manufactured_by', 'numbers', 'bullet_size', 'type_of_weapon')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='weapon_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='bullet_size', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_weapon', anchor='center')
                                tv.column('#5', anchor='center')
                               
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from weapon_tean"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                weapon_name=""
                                manufactured_by=""
                                numbers=""
                                bullet_size=""
                                type_of_weapon=""
                                
                                for i in result:
                                    serial_no=i[0]
                                    weapon_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    bullet_size=i[4]
                                    type_of_weapon=i[5]
                                    
                                    self.treeview.insert("",'end',text=serial_no,values=(weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def showteamB():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'weapon_name', 'manufactured_by', 'numbers', 'bullet_size', 'type_of_weapon')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='weapon_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='bullet_size', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_weapon', anchor='center')
                                tv.column('#5', anchor='center')
                               
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from weapon_teanA"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                weapon_name=""
                                manufactured_by=""
                                numbers=""
                                bullet_size=""
                                type_of_weapon=""
                                
                                for i in result:
                                    serial_no=i[0]
                                    weapon_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    bullet_size=i[4]
                                    type_of_weapon=i[5]
                                    
                                    self.treeview.insert("",'end',text=serial_no,values=(weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def showteamC():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'weapon_name', 'manufactured_by', 'numbers', 'bullet_size', 'type_of_weapon')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='weapon_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='bullet_size', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_weapon', anchor='center')
                                tv.column('#5', anchor='center')
                               
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from weapon_teanB"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                weapon_name=""
                                manufactured_by=""
                                numbers=""
                                bullet_size=""
                                type_of_weapon=""
                                
                                for i in result:
                                    serial_no=i[0]
                                    weapon_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    bullet_size=i[4]
                                    type_of_weapon=i[5]
                                    
                                    self.treeview.insert("",'end',text=serial_no,values=(weapon_name,manufactured_by,numbers,bullet_size,type_of_weapon))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                
                    button1=tk.Button(root,text="Add",width=15,height=2,command=Register).grid(row=0,column=2)
                   
                    button3=tk.Button(root,text="Update",width=15,height=2,command=Update).grid(row=1,column=2)
                    button4=tk.Button(root,text="Show record",width=15,height=2,command=ShowRecord).grid(row=2,column=2)
                    button5=tk.Button(root,text="Show All",width=15,height=2,command=Showall).grid(row=3,column=2)
                    button6=tk.Button(root,text="Clear",width=15,height=2,command=Clear).grid(row=4,column=2)
                   
                    button7=tk.Button(root,text="Add to weapon team-A",width=20,height=2,command=weaponteamA).grid(row=7,column=0)
                    button10=tk.Button(root,text="Add to weapon team-B",width=20,height=2,command=weaponteamB).grid(row=7,column=1)
                    button11=tk.Button(root,text="Add to weapon team-C",width=20,height=2,command=weaponteamC).grid(row=7,column=2)
                    button2=tk.Button(root,text="Delete weapon from team-A",width=25,height=2,command=deleteA).grid(row=8,column=0)
                    button2=tk.Button(root,text="Delete weapon from team-B",width=25,height=2,command=deleteB).grid(row=8,column=1)
                    button2=tk.Button(root,text="Delete weapon from team-C",width=25,height=2,command=deleteC).grid(row=8,column=2)
                    button8=tk.Button(root,text="show the weapons in team-A",width=25,height=2,command=showteamA).grid(row=9,column=0)
                    button8=tk.Button(root,text="show the weapons in team-B",width=25,height=2,command=showteamB).grid(row=9,column=1)
                    button8=tk.Button(root,text="show the weapons in team team-C",width=25,height=2,command=showteamC).grid(row=9,column=2)
                   
                    
                
        #-----------------------------------------------------VEHICLES-----------------------------------------------------------------------------------------------            
                def vehicles(g):
                    
                    root=tk.Tk()
                    root.title("Vehicles Data")
                    root.geometry("600x500")

                    #label12=Label(root,image=photo).grid(row=8,column=5)
                    labell1=tk.Label(root,text="serial_no",width=20,height=2,bg="grey").grid(row=0,column=0)
                    label2=tk.Label(root,text="vehicle_name",width=20,height=2,bg="grey").grid(row=1,column=0)
                    label3=tk.Label(root,text="manufactured_by",width=20,height=2,bg="grey").grid(row=2,column=0)
                    label4=tk.Label(root,text="numbers",width=20,height=2,bg="grey").grid(row=3,column=0)
                    label5=tk.Label(root,text="weight",width=20,height=2,bg="grey").grid(row=4,column=0)
                    label6=tk.Label(root,text="type_of_vehicle",width=20,height=2,bg="grey").grid(row=5,column=0)
                    label7=tk.Label(root,text="purpose",width=20,height=2,bg="grey").grid(row=6,column=0)
                    label8=tk.Label(root,width=10,height=2).grid(row=7,column=2)
                    label9=tk.Label(root,width=10,height=2).grid(row=7,column=4)
                    label10=tk.Label(root,width=10,height=2).grid(row=7,column=6)
                    label11=tk.Label(root,width=10,height=2).grid(row=7,column=8)
                    e1=tk.Entry(root,width=30,borderwidth=8)
                    e1.grid(row=0,column=1)
                    e2=tk.Entry(root,width=30,borderwidth=8)
                    e2.grid(row=1,column=1)
                    e3=tk.Entry(root,width=30,borderwidth=8)
                    e3.grid(row=2,column=1)
                    e4=tk.Entry(root,width=30,borderwidth=8)
                    e4.grid(row=3,column=1)
                    e5=tk.Entry(root,width=30,borderwidth=8)
                    e5.grid(row=4,column=1)
                    e6=tk.Entry(root,width=30,borderwidth=8)
                    e6.grid(row=5,column=1)
                    e7=tk.Entry(root,width=30,borderwidth=8)
                    e7.grid(row=6,column=1)
                    def Register():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from vehicles where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into vehicles(S_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose) values(%s,%s,%s,%s,%s,%s,%s)"
                            vehicle_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            weight=e5.get()
                            type_of_vehicle=e6.get()
                            purpose=e7.get()
                            if(vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                Value=(serial_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                e7.delete(0,tk.END)
                            else:
                                if (vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def ShowRecord():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from vehicles where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        Select1="select vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose from vehicles where S_no='%s'" %(serial_no)
                        mycursor.execute(Select1)
                        result2=mycursor.fetchall()
                        vehicle_name=""
                        manufactured_by=""
                        numbers=""
                        weight=""
                        type_of_vehicle=""
                        purpose=""
                        if(serial_no == dbserial_no):
                            for i in result2:
                                vehicle_name=i[0]
                                manufactured_by=i[1]
                                numbers=i[2]
                                weight=i[3]
                                type_of_vehicle=i[4]
                                purpose=i[5]
                            e2.insert(0,vehicle_name)
                            e3.insert(0, manufactured_by)
                            e4.insert(0, numbers)
                            e5.insert(0, weight)
                            e6.insert(0, type_of_vehicle)
                            e7.insert(0, purpose)
                            
                        else:
                            messagebox.askokcancel("Information","No Record exists")
                   
                    def Update():
                        serial_no=e1.get()
                        vehicle_name=e2.get()
                        manufactured_by=e3.get()
                        numbers=e4.get()
                        weight=e5.get()
                        type_of_vehicle=e6.get()
                        purpose=e7.get()
                        Update="Update vehicles set vehicle_name='%s', manufactured_by='%s', numbers='%s', weight='%s', type_of_vehicle='%s', purpose='%s' where S_no='%s'" %(vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose,serial_no)
                        mycursor.execute(Update)
                        mydb.commit()
                        messagebox.showinfo("Info","Record Update")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        e7.delete(0,tk.END)

                    def Showall():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'vehicle_name', 'manufactured_by', 'numbers', 'weight', 'type_of_vehicle', 'purpose')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='vehicle_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='weight', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_vehicle', anchor='center')
                                tv.column('#5', anchor='center')
                                tv.heading('#6', text='purpose', anchor='center')
                                tv.column('#6', anchor='center')
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from vehicles"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                vehicle_name=""
                                manufactured_by=""
                                numbers=""
                                weight=""
                                type_of_vehicle=""
                                purpose=""
                                for i in result:
                                    serial_no=i[0]
                                    vehicle_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    weight=i[4]
                                    type_of_vehicle=i[5]
                                    purpose=i[6]
                                    self.treeview.insert("",'end',text=serial_no,values=(vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def Clear():
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        e7.delete(0,tk.END)
                    def teamA():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from vehicle_team where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into vehicle_team(S_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose) values(%s,%s,%s,%s,%s,%s,%s)"
                            vehicle_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update vehicles set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            weight=e5.get()
                            type_of_vehicle=e6.get()
                            purpose=e7.get()
                            if(vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                Value=(serial_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                e7.delete(0,tk.END)
                            else:
                                if (vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def teamB():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from vehicle_teamA where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into vehicle_teamA(S_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose) values(%s,%s,%s,%s,%s,%s,%s)"
                            vehicle_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update vehicles set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            weight=e5.get()
                            type_of_vehicle=e6.get()
                            purpose=e7.get()
                            if(vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                Value=(serial_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                e7.delete(0,tk.END)
                            else:
                                if (vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def teamC():
                        serial_no=e1.get()
                        dbserial_no=""
                        Select="select S_no from vehicle_teamB where S_no='%s'" %(serial_no)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbserial_no=i[0]
                        if(serial_no == dbserial_no):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into vehicle_teamB(S_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose) values(%s,%s,%s,%s,%s,%s,%s)"
                            vehicle_name=e2.get()
                            manufactured_by=e3.get()
                            numbers=e4.get()
                            mycursor.execute("update vehicles set numbers=numbers-'"+numbers+"' where S_no ='"+serial_no+"' ")
                            weight=e5.get()
                            type_of_vehicle=e6.get()
                            purpose=e7.get()
                            if(vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                Value=(serial_no,vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Record inserted")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                e7.delete(0,tk.END)
                            else:
                                if (vehicle_name !="" and manufactured_by !="" and numbers !="" and  weight !="" and type_of_vehicle !=""  and purpose!=""):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    def deleteA():
                        serial_no=e1.get()
                        Delete="delete from vehicle_team where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        e7.delete(0,tk.END)
                    def deleteB():
                        serial_no=e1.get()
                        Delete="delete from vehicle_teamA where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        e7.delete(0,tk.END)
                    def deleteC():
                        serial_no=e1.get()
                        Delete="delete from vehicle_teamB where S_no='%s'" %(serial_no)
                        mycursor.execute(Delete)
                        mydb.commit()
                        messagebox.showinfo("Information","Record Deleted")
                        e1.delete(0,tk.END)
                        e2.delete(0,tk.END)
                        e3.delete(0,tk.END)
                        e4.delete(0,tk.END)
                        e5.delete(0,tk.END)
                        e6.delete(0,tk.END)
                        e7.delete(0,tk.END)

                    def showteamA():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'vehicle_name', 'manufactured_by', 'numbers', 'weight', 'type_of_vehicle', 'purpose')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='vehicle_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='weight', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_vehicle', anchor='center')
                                tv.column('#5', anchor='center')
                                tv.heading('#6', text='purpose', anchor='center')
                                tv.column('#6', anchor='center')
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from vehicle_team"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                vehicle_name=""
                                manufactured_by=""
                                numbers=""
                                weight=""
                                type_of_vehicle=""
                                purpose=""
                                for i in result:
                                    serial_no=i[0]
                                    vehicle_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    weight=i[4]
                                    type_of_vehicle=i[5]
                                    purpose=i[6]
                                    self.treeview.insert("",'end',text=serial_no,values=(vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def showteamB():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'vehicle_name', 'manufactured_by', 'numbers', 'weight', 'type_of_vehicle', 'purpose')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='vehicle_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='weight', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_vehicle', anchor='center')
                                tv.column('#5', anchor='center')
                                tv.heading('#6', text='purpose', anchor='center')
                                tv.column('#6', anchor='center')
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from vehicle_teamA"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                vehicle_name=""
                                manufactured_by=""
                                numbers=""
                                weight=""
                                type_of_vehicle=""
                                purpose=""
                                for i in result:
                                    serial_no=i[0]
                                    vehicle_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    weight=i[4]
                                    type_of_vehicle=i[5]
                                    purpose=i[6]
                                    self.treeview.insert("",'end',text=serial_no,values=(vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)
                    def showteamC():
                        class A(tk.Frame):
                            def __init__(self, parent):
                                tk.Frame.__init__(self, parent)
                                self.CreateUI()
                                self.LoadTable()
                                self.grid(column=0, row=0, columnspan=3, rowspan=3)
                                parent.grid_rowconfigure(0, weight=1)
                                parent.grid_columnconfigure(0, weight=1)
                            def CreateUI(self):
                                tv=ttk.Treeview(root)
                                tv['columns']=('serial_no', 'vehicle_name', 'manufactured_by', 'numbers', 'weight', 'type_of_vehicle', 'purpose')
                                tv.heading('#0',text='serial_no',anchor='center')
                                tv.column('#0',anchor='center')
                                tv.heading('#1', text='vehicle_name', anchor='center')
                                tv.column('#1', anchor='center')
                                tv.heading('#2', text='manufactured_by', anchor='center')
                                tv.column('#2', anchor='center')
                                tv.heading('#3', text='numbers', anchor='center')
                                tv.column('#3', anchor='center')
                                tv.heading('#4', text='weight', anchor='center')
                                tv.column('#4', anchor='center')
                                tv.heading('#5', text='type_of_vehicle', anchor='center')
                                tv.column('#5', anchor='center')
                                tv.heading('#6', text='purpose', anchor='center')
                                tv.column('#6', anchor='center')
                                tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                                self.treeview =tv
                                self.grid_rowconfigure(0,weight=1)
                                self.grid_columnconfigure(0,weight=1)
                            def LoadTable(self):
                                Select="Select * from vehicle_teamB"
                                mycursor.execute(Select)
                                result=mycursor.fetchall()
                                serial_no=""
                                vehicle_name=""
                                manufactured_by=""
                                numbers=""
                                weight=""
                                type_of_vehicle=""
                                purpose=""
                                for i in result:
                                    serial_no=i[0]
                                    vehicle_name=i[1]
                                    manufactured_by=i[2]
                                    numbers=i[3]
                                    weight=i[4]
                                    type_of_vehicle=i[5]
                                    purpose=i[6]
                                    self.treeview.insert("",'end',text=serial_no,values=(vehicle_name,manufactured_by,numbers,weight,type_of_vehicle,purpose))
                        root=tk.Tk()
                        root.title("Overview Page")
                        A(root)


                    button1=tk.Button(root,text="Add",width=15,height=2,command=Register).grid(row=0,column=2)
                   
                    button3=tk.Button(root,text="Update",width=15,height=2,command=Update).grid(row=1,column=2)
                    button4=tk.Button(root,text="Show record",width=15,height=2,command=ShowRecord).grid(row=2,column=2)
                    button5=tk.Button(root,text="Show All",width=15,height=2,command=Showall).grid(row=3,column=2)
                    button6=tk.Button(root,text="Clear",width=15,height=2,command=Clear).grid(row=4,column=2)
           
                    button7=tk.Button(root,text="Add to vehicles team-A",width=20,height=2,command=teamA).grid(row=7,column=0)
                    button10=tk.Button(root,text="Add to vehicles team-B",width=20,height=2,command=teamB).grid(row=7,column=1)
                    button11=tk.Button(root,text="Add to vehicles team-C",width=20,height=2,command=teamC).grid(row=7,column=2)
                    button2=tk.Button(root,text="Delete vehicle from team-A",width=25,height=2,command=deleteA).grid(row=8,column=0)
                    button2=tk.Button(root,text="Delete vehicle from team-B",width=25,height=2,command=deleteB).grid(row=8,column=1)
                    button2=tk.Button(root,text="Delete vehicle from team-C",width=25,height=2,command=deleteC).grid(row=8,column=2)
                    button8=tk.Button(root,text="show the vehicle in team-A",width=25,height=2,command=showteamA).grid(row=9,column=0)
                    button8=tk.Button(root,text="show the vehicle in team-B",width=25,height=2,command=showteamB).grid(row=9,column=1)
                    button8=tk.Button(root,text="show the vehicle in team team-C",width=25,height=2,command=showteamC).grid(row=9,column=2)
                   

                    
        #-------------------------------------------------LEAVES--------------------------------------------------------------------
        #RollNo, name, absence,going ,coming, place, purpose
                def leaves_applied(f):
                    class A(tk.Frame):
                        def __init__(self, parent):
                            tk.Frame.__init__(self, parent)
                            self.CreateUI()
                            self.LoadTable()
                            self.grid(column=0, row=0, columnspan=3, rowspan=3)
                            parent.grid_rowconfigure(0, weight=1)
                            parent.grid_columnconfigure(0, weight=1)
                        def CreateUI(self):
                            tv=ttk.Treeview(root)
                            tv['columns']=('RollNo', 'name', 'absence', 'going', 'coming', 'place', 'purpose')
                            tv.heading('#0',text='RollNo',anchor='center')
                            tv.column('#0',anchor='center')
                            tv.heading('#1', text='name', anchor='center')
                            tv.column('#1', anchor='center')
                            tv.heading('#2', text='absence', anchor='center')
                            tv.column('#2', anchor='center')
                            tv.heading('#3', text='going', anchor='center')
                            tv.column('#3', anchor='center')
                            tv.heading('#4', text='coming', anchor='center')
                            tv.column('#4', anchor='center')
                            tv.heading('#5', text='place', anchor='center')
                            tv.column('#5', anchor='center')
                            tv.heading('#6', text='purpose', anchor='center')
                            tv.column('#6', anchor='center')
                            tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                            self.treeview =tv
                            self.grid_rowconfigure(0,weight=1)
                            self.grid_columnconfigure(0,weight=1)
                        def LoadTable(self):
                            Select="Select * from leaved"
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            RollNo=""
                            name=""
                            absence=""
                            going=""
                            coming=""
                            place=""
                            purpose=""
                            for i in result:
                                RollNo=i[0]
                                name=i[1]
                                absence=i[2]
                                going=i[3]
                                coming=i[4]
                                place=i[5]
                                purpose=i[6]
                                self.treeview.insert("",'end',text=RollNo,values=( name, absence,going ,coming, place, purpose))
                    root=tk.Tk()
                    root.title("Leaves Applied")
                    A(root)

                            
                global im15
                global i7   
                im5=Image.open(r'Soldier_butt_edit.png')
                i5=ImageTk.PhotoImage(im5)
                lb8=tk.Label(d, image=i5)
                im5=Image.open(r'Weapon_butt_edit.png')
                i6=ImageTk.PhotoImage(im5)
                lb8=tk.Label(d, image=i6)
                im15=Image.open(r'Vehicle_butt_.png')
                i7=ImageTk.PhotoImage(im15)
                lb8=tk.Label(d, image=i7)
                im5=Image.open(r'Leave_app_butt_edit.png')
                i8=ImageTk.PhotoImage(im5)
                lb8=tk.Label(d, image=i8)
             
                def hover(e):
                    buttonsoldiers["bg"]="#F79D3B"
                    buttonsoldiers["fg"]="#19273D"
                def leave(e):
                    buttonsoldiers["bg"]="#19273D"
                    buttonsoldiers["fg"]="#F79D3B"


                buttonsoldiers=tk.Button(d,image=i5,text="SOLDIERS",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0) 

                buttonsoldiers.bind("<Enter>", hover)
                buttonsoldiers.bind("<Button-1>",soldiers)
                buttonsoldiers.bind("<Button-3>",soldiers)
                buttonsoldiers.bind("<Return>",soldiers)
                buttonsoldiers.bind("<Leave>",leave)
                buttonsoldiers.place(x=50,y=600)

                def hover1(e):
                    buttonweapon["bg"]="#F79D3B"
                    buttonweapon["fg"]="#19273D"
                def leave1(e):
                    buttonweapon["bg"]="#19273D"
                    buttonweapon["fg"]="#F79D3B"


                buttonweapon=tk.Button(d,image=i6,text="WEAPONS",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0)
                buttonweapon.bind("<Enter>", hover1)
                buttonweapon.bind("<Button-1>",weapons)
                buttonweapon.bind("<Button-3>",weapons)
                buttonweapon.bind("<Return>",weapons)
                buttonweapon.bind("<Leave>",leave1)
                buttonweapon.place(x=350,y=600)
                def hover2(g):
                    buttonvehicles["bg"]="#F79D3B"
                    buttonvehicles["fg"]="#19273D"
                def leave2(g):
                    buttonvehicles["bg"]="#19273D"
                    buttonvehicles["fg"]="#F79D3B"


                buttonvehicles=tk.Button(d,image=i7,text="VEHICLES",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0)
                buttonvehicles.bind("<Enter>", hover2)
                buttonvehicles.bind("<Button-1>",vehicles)
                buttonvehicles.bind("<Button-3>",vehicles)
                buttonvehicles.bind("<Return>",vehicles)
                buttonvehicles.bind("<Leave>",leave2)
                buttonvehicles.place(x=650,y=600)
                def hover3(f):
                    buttonteam["bg"]="#F79D3B"
                    buttonteam["fg"]="#19273D"
                def leave3(f):
                    buttonteam["bg"]="#19273D"
                    buttonteam["fg"]="#F79D3B"


                buttonteam=tk.Button(d,image=i8,text="Leaves Applied",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0)
                buttonteam.bind("<Enter>", hover3)
                buttonteam.bind("<Button-1>",leaves_applied)
                buttonteam.bind("<Button-3>",leaves_applied)
                buttonteam.bind("<Return>",leaves_applied)
                buttonteam.bind("<Leave>",leave3)
                buttonteam.place(x=950,y=600)

                def hover4(m):
                    buttonaboutus["bg"]="#ffffff"
                    buttonaboutus["fg"]="#000000"
                def leave4(m):
                    buttonaboutus["bg"]="#000000"
                    buttonaboutus["fg"]="#ffffff"


                buttonaboutus=tk.Button(d,text="about us",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)
                buttonaboutus.bind("<Enter>", hover4)
                buttonaboutus.bind("<Button-1>",aboutus)
                buttonaboutus.bind("<Button-3>",aboutus)
                buttonaboutus.bind("<Return>",aboutus)
                buttonaboutus.bind("<Leave>",leave4)
                buttonaboutus.place(x=900,y=50)
                
                def hover4(j):
                    buttonnews["bg"]="#ffffff"
                    buttonnews["fg"]="#000000"
                def leave4(j):
                    buttonnews["bg"]="#000000"
                    buttonnews["fg"]="#ffffff"


                buttonnews=tk.Button(d,text="news",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)
                buttonnews.bind("<Enter>", hover4)
                buttonnews.bind("<Button-1>",news)
                buttonnews.bind("<Button-3>",news)
                buttonnews.bind("<Return>",news)
                buttonnews.bind("<Leave>",leave4)
                buttonnews.place(x=1100,y=50)
               
               

                                    

              

            else:
                messagebox.showerror('error','wrong password')
    def hover4(f):
        buttonenter["bg"]="#ffffff"
        buttonenter["fg"]="#000000"
    def leave4(f):
        buttonenter["bg"]="#000000"
        buttonenter["fg"]="#ffffff"


    buttonenter=tk.Button(b,text="Enter",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0 )
    buttonenter.bind("<Enter>", hover4)
    buttonenter.bind("<Button-1>",login)
    buttonenter.bind("<Button-3>",login)
    buttonenter.bind("<Return>",login)
    buttonenter.bind("<Leave>",leave4)
    buttonenter.place(x=230,y=150)
   
    

def hover4(q):
    buttonadmin["bg"]="#ffffff"
    buttonadmin["fg"]="#000000"
def leave4(q):
    buttonadmin["bg"]="#000000"
    buttonadmin["fg"]="#ffffff"


buttonadmin=tk.Button(root,text="admin",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0 )
buttonadmin.bind("<Enter>", hover4)
buttonadmin.bind("<Button-1>",admin)
buttonadmin.bind("<Button-3>",admin)
buttonadmin.bind("<Return>",admin)
buttonadmin.bind("<Leave>",leave4)
buttonadmin.place(x=350,y=550)

#im5=Image.open(r'C:/Users/JOHN/Desktop/25237577-speaker-icon.jpg')
#i5=ImageTk.PhotoImage(im5)
#lb8=tk.Label(root, image=i5)
#buttonadmin=tk.Button(root,image=i5,bg='grey', font=('BankGothic Md BT',19),relief=tk.RAISED ,command=music).place(x=550,y=150)
#im5=Image.open(r'C:/Users/JOHN/Desktop/istockphoto-909364766-1024x1024.jpg')
#i11=ImageTk.PhotoImage(im5)
#lb8=tk.Label(root, image=i11)
#buttonadmin=tk.Button(root,image=i11,bg='grey',font=('BankGothic Md BT',19),relief=tk.RAISED ,command=stop).place(x=550,y=450)







#----------------------------------------------USER------------------------------------------------------------------------
#login page for user
def user(i):
    root.destroy()
    
    class MyLabel(tk.Label):
        def __init__(self, master, filename):
            im = Image.open("fourcolors7.gif")
            seq =  []
            try:
                while 1:
                    seq.append(im.copy())
                    im.seek(len(seq)) # skip to next frame
            except EOFError:
                pass # we're done

            try:
                self.delay = im.info['duration']
            except KeyError:
                self.delay = 100

            first = seq[0].convert('CMYK')
            self.frames = [ImageTk.PhotoImage(first)]

            tk.Label.__init__(self, master, image=self.frames[0])

            temp = seq[0]
            for image in seq[1:]:
                temp.paste(image)
                frame = temp.convert('RGBA')
                self.frames.append(ImageTk.PhotoImage(frame))

            self.idx = 0

            self.cancel = self.after(self.delay, self.play)

        def play(self):
            self.config(image=self.frames[self.idx])
            self.idx += 1
            if self.idx == len(self.frames):
                self.idx = 0
            self.cancel = self.after(self.delay, self.play)



    c =tk.Tk()
    anim = MyLabel(c, 'animated.gif')
    anim.pack()
  
    c.geometry("512x288")
    un=tk.StringVar()
    pw=tk.StringVar()
    x=tk.Frame(c,width=290,height=250,).place(x=130,y=20)
    L1=tk.Label(c,text="User Name",font=('BankGothic Md BT',16),bg='grey',).place(x=130,y=50)
    E1=tk.Entry(c,textvariable=un,relief=tk.GROOVE,bd=3,width=10,font=('BankGothic Md BT',15)).place(x=260,y=50)
    L2=tk.Label(c,text="Password",font=('BankGothic Md BT',16),bg='grey',).place(x=130,y=100)
    E2=tk.Entry(c,textvariable=pw,show="*",relief=tk.GROOVE,bd=3,width=10,font=('BankGothic Md BT',15)).place(x=260,y=100)
    def login(x):
        x=un.get()
        mycursor.execute("select username from loginpage2 where username='"+x+"'")
        mr=mycursor.fetchone()
        
        if mr==None:
            tk.messagebox.showinfo('info', ' no user found')
        
        z=pw.get()
        mycursor.execute("select password from loginpage2 where username='"+x+"'")
        mv=mycursor.fetchall()
        
        if x=="" or z=="":
            tk.messagebox.showinfo('info','enter the fields')
        
        for i in mv:
           
            a=list(i)
            if z=="":
                tk.messagebox.showinfo('info', 'type the Password')
                break
            elif a[0]==str(z):
                c.destroy()
                f=tk.Tk()
                global im4
                global i5
                global im5
                global i6
                #global im6
                #global i7
                global im7
                global i8
                global im8
                global i9
                global im9
                global i10
                global im10
                global i11
                global im200
                global i500
                #background image
                im200=Image.open(r'rafale1_edit.jpg')
                i500=ImageTk.PhotoImage(im200)
                lb8=tk.Label(f, image=i500)
                
               
               
               
                lb8.pack()
                f.geometry("1707x1024")
               
                x5=tk.Frame(f,width=1550,height=300,bg='#19273D').place(x=0,y=600)
                def news(j1):
                    y=tk.Toplevel()
                    global im25
                    global i55
                    #background image
                    im25=Image.open(r'cf631c01a5cbba253032a04dc1b80cdc.jpg')
                    i55=ImageTk.PhotoImage(im25)
                    lb12=tk.Label(y, image=i55).place(x=0,y=0)
                    y.geometry("564x639")
                    x3=tk.Frame(y,width=400,height=500,).place(x=80,y=50)
                    L8=tk.Label(y,text=
"""1)Rajnath Singh witnesses para
dropping exercise of Indian
Armed Forces in Leh’s Stakna
2)Indian, Chinese militaries to
carry out verification ofdiseng
-agement process in easternLadakh
3)US aerospace major Boeing compl
-etes delivery of 37 military heli
-copters to India
4)Complete disengagement process
in eastern Ladakh intricate: Indian
Army after talks
5)India asks China to sincerely impl
-ement the understanding reached at
Military Talks
6)US military to stand with India in
conflict with China,indicates White
House official
7)China's light tanks won't survive in
battle with T-90s, say Indian tank comm
-anders
8)After laser-guided anti-tank missile,
India successfully tests new version of
Shaurya Missile
9)We recognise Arunachal Pradesh as Indian
territoryand oppose any claims over it, says
US slamming China indirectly
""",font=('BankGothic Md BT',12),).place(x=80,y=60)
                    
                    
                
                def aboutus(m1):
                    x=tk.Toplevel()
                    global im250
                    global i550
                    #background image
                    im250=Image.open(r'9aaedbaad989a90c8bec61b2d7744f16.jpg')
                    i550=ImageTk.PhotoImage(im250)
                    lb12=tk.Label(x, image=i550).place(x=0,y=0)
                    
                    x.geometry("700x900")
                    #table
                    #x153=tk.Frame(x,width=551,height=551,bg="black").place(x=200,y=0)
                                      
                    #table
                    x13=tk.Frame(x,width=377,height=840).place(x=150,y=30)
                    L75=tk.Label(x,text=
'''Founder-1st April
1898;125 years ago
Country	 India
Type	Army
Role	Land warfare
Size	1,237,117
active personnel
960,000 reserve
personnel
Part of	Indian
Armed Forces
Headquarters
Integrated Defence
Headquarters
, Ministry of
Defence, New Delhi
Motto(s)
Service Before Self
Colours	Gold,
red and black

March	Quick:
Qadam Qadam Badhaye Ja
(Keep stepping
forward)
Slow: Samman
Guard (The Guard of Honour)
Anniversaries
Army Day: 15 January
Aircraft315[3]
Commanders
Commander-in-Chief
President Ram Nath Kovind
Chief of Defence Staff (CDS)
General Bipin Rawat
PVSM, UYSM, AVSM, YSM, SM,
VSM, ADC
Chief of the Army Staff
(COAS)	General Manoj
''',font=('BankGothic Md BT',15)).place(x=150,y=40)
                
                
                def team_created(k):
                    class A(tk.Frame):
                        def __init__(self, parent):
                            tk.Frame.__init__(self, parent)
                            self.CreateUI()
                            self.LoadTable()
                            self.grid(column=0, row=0, columnspan=3, rowspan=3)
                            parent.grid_rowconfigure(0, weight=1)
                            parent.grid_columnconfigure(0, weight=1)
                        def CreateUI(self):
                            tv=ttk.Treeview(root)
                            tv['columns']=('RollNo', 'Full_Name', 'Position', 'Phone_Number', 'City', 'State', 'Age')
                            tv.heading('#0',text='RollNo',anchor='center')
                            tv.column('#0',anchor='center')
                            tv.heading('#1', text='Full_Name', anchor='center')
                            tv.column('#1', anchor='center')
                            tv.heading('#2', text='Position', anchor='center')
                            tv.column('#2', anchor='center')
                            tv.heading('#3', text='Phone_Number', anchor='center')
                            tv.column('#3', anchor='center')
                            tv.heading('#4', text='City', anchor='center')
                            tv.column('#4', anchor='center')
                            tv.heading('#5', text='State', anchor='center')
                            tv.column('#5', anchor='center')
                            tv.heading('#6', text='Age', anchor='center')
                            tv.column('#6', anchor='center')
                            tv.grid(column=0, row=0, columnspan=3, rowspan=3)
                            self.treeview =tv
                            self.grid_rowconfigure(0,weight=1)
                            self.grid_columnconfigure(0,weight=1)
                        def LoadTable(self):
                            Select="Select * from teamC"
                            mycursor.execute(Select)
                            result=mycursor.fetchall()
                            RollNo=""
                            Full_Name=""
                            Position=""
                            Phone_Number=""
                            City=""
                            State=""
                            Age=""
                            for i in result:
                                RollNo=i[0]
                                Full_Name=i[1]
                                Position=i[2]
                                Phone_Number=i[3]
                                City=i[4]
                                State=i[5]
                                Age=i[6]
                                self.treeview.insert("",'end',text=RollNo,values=(Full_Name,Position,Phone_Number,City,State,Age))
                    root=tk.Tk()
                    root.title("Overview Page")
                    A(root)                 
        #--------------------------------------------LEAVE APPLICATION--------------------------------------------------------------------------    
        #Roll no, name, duration of absence, date of going ,date of coming, place of visit, purpose for visit
                def leave(o):

                    root=tk.Tk()
                    label1=tk.Label(root,text="Service number",width=20,height=2,bg="grey").grid(row=0,column=0)
                    label2=tk.Label(root,text="Name",width=20,height=2,bg="grey").grid(row=1,column=0)
                    label3=tk.Label(root,text="duration of absence",width=20,height=2,bg="grey").grid(row=2,column=0)
                    label4=tk.Label(root,text="date of going",width=20,height=2,bg="grey").grid(row=3,column=0)
                    label5=tk.Label(root,text="date of coming",width=20,height=2,bg="grey").grid(row=4,column=0)
                    label6=tk.Label(root,text="place of visit",width=20,height=2,bg="grey").grid(row=5,column=0)
                    label7=tk.Label(root,text="purpose for visit",width=20,height=2,bg="grey").grid(row=6,column=0)
                    label8=tk.Label(root,width=10,height=2).grid(row=7,column=2)
                    label9=tk.Label(root,width=10,height=2).grid(row=7,column=4)
                    label10=tk.Label(root,width=10,height=2).grid(row=7,column=6)
                    label11=tk.Label(root,width=10,height=2).grid(row=7,column=8)
                    e1=tk.Entry(root,width=30,borderwidth=8)
                    e1.grid(row=0,column=1)
                    e2=tk.Entry(root,width=30,borderwidth=8)
                    e2.grid(row=1,column=1)
                    e3=tk.Entry(root,width=30,borderwidth=8)
                    e3.grid(row=2,column=1)
                    e4=tk.Entry(root,width=30,borderwidth=8)
                    e4.grid(row=3,column=1)
                    e5=tk.Entry(root,width=30,borderwidth=8)
                    e5.grid(row=4,column=1)
                    e6=tk.Entry(root,width=30,borderwidth=8)
                    e6.grid(row=5,column=1)
                    e7=tk.Entry(root,width=30,borderwidth=8)
                    e7.grid(row=6,column=1)
                    def Register():
                        RollNo=e1.get()
                        dbRollNo=""
                        Select="select RollNo from leaved where RollNo='%s'" %(RollNo)
                        mycursor.execute(Select)
                        result=mycursor.fetchall()
                        for i in result:
                            dbRollNo=i[0]
                        if(RollNo == dbRollNo):
                            messagebox.askokcancel("Information","Record Already exists")
                        else:
                            Insert="Insert into leaved(RollNo, name, absence,going ,coming, place, purpose) values(%s,%s,%s,%s,%s,%s,%s)"
                            name=e2.get()
                            absence=e3.get()
                            going=e4.get()   
                            coming=e5.get()
                            place=e6.get()
                            purpose=e7.get()
                            if(name !="" and absence !="" and going !="" and coming !="" and place !="" and purpose !=""):
                                Value=(RollNo, name, absence,going ,coming, place, purpose)
                                mycursor.execute(Insert,Value)
                                mydb.commit()
                                messagebox.askokcancel("Information","Your leave application "+str(leaves)+" by higher authorities")
                                e1.delete(0,tk.END)
                                e2.delete(0,tk.END)
                                e3.delete(0,tk.END)
                                e4.delete(0,tk.END)
                                e5.delete(0,tk.END)
                                e6.delete(0,tk.END)
                                e7.delete(0,tk.END)
                            else:
                                if (name == "" and absence == "" and going == "" and coming == "" and place == "" and purpose == ""):
                                    messagebox.askokcancel("Information","New Entery Fill All Details")
                                else:
                                     messagebox.askokcancel("Information", "Some fields left blank")
                    button1=tk.Button(root,text="Register",width=15,height=2,command=Register).grid(row=0,column=2)
                    
                global im15
                global i7
                im5=Image.open(r'Team_butt_edit.png')
                i6=ImageTk.PhotoImage(im5)
                lb8=tk.Label(f, image=i6)
                im15=Image.open(r'Leave_app_user_butt_edit.png')
                i7=ImageTk.PhotoImage(im15)
                lb8=tk.Label(f, image=i7)
                def hover1(k):
                    buttonweapon["bg"]="#F79D3B"
                    buttonweapon["fg"]="#19273D"
                def leave1(k):
                    buttonweapon["bg"]="#19273D"
                    buttonweapon["fg"]="#F79D3B"


                buttonweapon=tk.Button(f,image=i6,text="WEAPONS",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0)
                buttonweapon.bind("<Enter>", hover1)
                buttonweapon.bind("<Button-1>",team_created)
                buttonweapon.bind("<Button-3>",team_created)
                buttonweapon.bind("<Return>",team_created)
                buttonweapon.bind("<Leave>",leave1)
                buttonweapon.place(x=200,y=600)
                def hover2(o):
                    buttonvehicles["bg"]="#F79D3B"
                    buttonvehicles["fg"]="#19273D"
                def leave2(o):
                    buttonvehicles["bg"]="#19273D"
                    buttonvehicles["fg"]="#F79D3B"


                buttonvehicles=tk.Button(f,image=i7,text="VEHICLES",bg='#19273D',font=('BankGothic Md BT',15),borderwidth=0)
                buttonvehicles.bind("<Enter>", hover2)
                buttonvehicles.bind("<Button-1>",leave)
                buttonvehicles.bind("<Button-3>",leave)
                buttonvehicles.bind("<Return>",leave)
                buttonvehicles.bind("<Leave>",leave2)
                buttonvehicles.place(x=800,y=600)
                def hover4(m1):
                    buttonaboutus["bg"]="#ffffff"
                    buttonaboutus["fg"]="#000000"
                def leave4(m):
                    buttonaboutus["bg"]="#000000"
                    buttonaboutus["fg"]="#ffffff"


                buttonaboutus=tk.Button(f,text="about us",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)
                buttonaboutus.bind("<Enter>", hover4)
                buttonaboutus.bind("<Button-1>",aboutus)
                buttonaboutus.bind("<Button-3>",aboutus)
                buttonaboutus.bind("<Return>",aboutus)
                buttonaboutus.bind("<Leave>",leave4)
                buttonaboutus.place(x=900,y=50)
                
                def hover4(j1):
                    buttonnews["bg"]="#ffffff"
                    buttonnews["fg"]="#000000"
                def leave4(j):
                    buttonnews["bg"]="#000000"
                    buttonnews["fg"]="#ffffff"


                buttonnews=tk.Button(f,text="news",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)
                buttonnews.bind("<Enter>", hover4)
                buttonnews.bind("<Button-1>",news)
                buttonnews.bind("<Button-3>",news)
                buttonnews.bind("<Return>",news)
                buttonnews.bind("<Leave>",leave4)
                buttonnews.place(x=1100,y=50)
                
               
            else:
                messagebox.showerror('error','wrong password')
    def hover4(x):
        buttonenter["bg"]="#ffffff"
        buttonenter["fg"]="#000000"
    def leave4(x):
        buttonenter["bg"]="#000000"
        buttonenter["fg"]="#ffffff"


    buttonenter=tk.Button(c,text="Enter",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0 )
    buttonenter.bind("<Enter>", hover4)
    buttonenter.bind("<Button-1>",login)
    buttonenter.bind("<Button-3>",login)
    buttonenter.bind("<Return>",login)
    buttonenter.bind("<Leave>",leave4)
    buttonenter.place(x=230,y=150)



   
def hover4(i):
    buttonuser["bg"]="#ffffff"
    buttonuser["fg"]="#000000"
def leave4(i):
    buttonuser["bg"]="#000000"
    buttonuser["fg"]="#ffffff"


buttonuser=tk.Button(root,text="user",bg='#000000',fg="#ffffff",font=('BankGothic Md BT',19),borderwidth=0)
buttonuser.bind("<Enter>", hover4)
buttonuser.bind("<Button-1>",user)
buttonuser.bind("<Button-3>",user)
buttonuser.bind("<Return>",user)
buttonuser.bind("<Leave>",leave4)
buttonuser.place(x=500,y=550)




