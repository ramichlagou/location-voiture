from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error




#===============================================================Definition du classe voiture=======================================================================================================================================#
class voiture:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "Gestion de voiture")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False,height=False)
        
        
        
        
        MainFrame = Frame(self.root,bd=10,width=770,height=700,relief=RIDGE,bg='cadet blue')
        MainFrame.grid()
        TitleFrame = Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3 = Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)
        
        LeftFrame = Frame(TopFrame3,bd=5,width=770,height=400,padx=2,relief=RIDGE,bg='cadet blue')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd=5,width=600,height=180,padx=2,pady=4,relief=RIDGE)
        LeftFrame1.pack(side=TOP , padx =0 ,pady=0)
        
        RightFrame1 = Frame(TopFrame3,bd=5,width=100,height=400,padx=2,relief=RIDGE,bg='cadet blue')
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
       
        

#======================================================================definition des attributs================================================================================================================================#

        Num_imma = StringVar()
        Marque = StringVar()
        Modele = StringVar()
        Kilometrage  = StringVar()
        Etat = StringVar()
        Prix_location =StringVar()
#========================================================================DEfinition des fonctions==============================================================================================================================#
        def Exit():
            Exit = tkinter.messagebox.askyesno("voiture","comfirm if you want to exit")
            if Exit > 0:
                root.destroy()
                return
        
        def Reset():
            self.entNum_imma.delete(0,END)
            self.entMarque.delete(0,END)
            self.entModele.delete(0,END)
            self.entKilometrage.delete(0,END)
            self.cboEtat.delete(0,END)
            self.entPrix_location.delete(0,END)
            
            
        def AddData():
            if Num_imma.get() == "":
                tkinter.messagebox.showerror("voiture","Not Num_imma entred")
            else:
                
                 conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
                 cur = conn.cursor()
                 cur.execute("insert into voiture(Num_imma,Marque,Modele,Kilometrage,Etat,Prix_location) values(%s,%s,%s,%s,%s,%s)",(
                         Num_imma.get(),
                         Marque.get(),
                         Modele.get(),
                         Kilometrage.get(),
                         Etat.get(),
                         Prix_location.get()
                         ))
                 conn.commit()
                 DisplayData()
                 conn.close()
                 tkinter.messagebox.showinfo("voiture","Record Entered successfully")
            
        def DisplayData():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("select * from voiture")
            result = cur.fetchall()
            if len(result) != 0:
                self.voiture_records.delete(*self.voiture_records.get_children())
                for row in result:
                    self.voiture_records.insert('',END,values=row)
                
            conn.commit()
            conn.close()
        
        def ViewInfo(ev):
            Info= self.voiture_records.focus()
            learnerData = self.voiture_records.item(Info)
            row = learnerData['values']
            Num_imma.set(row[0]),
            Marque.set(row[1]),
            Modele.set(row[2]),
            Kilometrage.set(row[3]),
            Etat.set(row[4]),
            Prix_location.set(row[5])
            
        
        
        def Update():
           conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
           cur = conn.cursor()
           cur.execute("update voiture set Marque=%s,Modele=%s,Kilometrage=%s,Etat=%s,Prix_location=%s where Num_imma=%s",(
          
           Marque.get(),
           Modele.get(),
           Kilometrage.get(),
           Etat.get(),
           Prix_location.get(),
           Num_imma.get()))
           conn.commit()
           DisplayData()
           conn.close()
            
           tkinter.messagebox.showinfo("voiture","Record updated successfully")
        
        def DeleteData():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("delete from voiture where Num_imma ='%s'"%Num_imma.get())
            conn.commit()
            DisplayData()
            conn.close()
            
            tkinter.messagebox.showinfo("voiture","Record successfully Deleted")
            
            
        def SearchDB():
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
                cur = conn.cursor()
                cur.execute("select * from voiture where Num_imma='%s'"%Num_imma.get())
                row = cur.fetchone()
                Num_imma.set(row[0]),
                Marque.set(row[1]),
                Modele.set(row[2]),
                Kilometrage.set(row[3]),
                Etat.set(row[4]),
                Prix_location.set(row[5])
                conn.commit()
            except:
                tkinter.messagebox.showinfo("voiture","No such Record found")
                Reset()
            
          
            conn.close() 
                
                 
    
                
#==========================================================================Grafic design============================================================================================================================#      
        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text='voiture',bd=7)
        self.lbltitle.grid(row=0,column=0,padx=280)
        
        self.lblNum_imma=Label(LeftFrame1,font=('arial',12,'bold'),text='Num_imma',bd=7)
        self.lblNum_imma.grid(row=0,column=0,sticky=W,padx=5)
        self.entNum_imma=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Num_imma)
        self.entNum_imma.grid(row=0,column=1,sticky=W,padx=5)
        
        self.lblMarque=Label(LeftFrame1,font=('arial',12,'bold'),text='Marque',bd=7)
        self.lblMarque.grid(row=1,column=0,sticky=W,padx=5)
        self.entMarque=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Marque)
        self.entMarque.grid(row=1,column=1,sticky=W,padx=5)
        
        self.lblModele=Label(LeftFrame1,font=('arial',12,'bold'),text='Modele',bd=7)
        self.lblModele.grid(row=2,column=0,sticky=W,padx=5)
        self.entModele=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Modele)
        self.entModele.grid(row=2,column=1,sticky=W,padx=5)
        
        self.lblKilometrage=Label(LeftFrame1,font=('arial',12,'bold'),text='Kilometrage',bd=7)
        self.lblKilometrage.grid(row=3,column=0,sticky=W,padx=5)
        self.entKilometrage=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Kilometrage)
        self.entKilometrage.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblEtat=Label(LeftFrame1,font=('arial',12,'bold'),text='Etat',bd=7)
        self.lblEtat.grid(row=4,column=0,sticky=W,padx=5)
        self.cboEtat=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=42,state='readonly',textvariable=Etat)
        self.cboEtat['values']=[' ' , 'disponible','en cours de location']
        self.cboEtat.grid(row=4,column=1,sticky=W,padx=5)
        
        self.lblPrix_location=Label(LeftFrame1,font=('arial',12,'bold'),text='Prix_location',bd=7)
        self.lblPrix_location.grid(row=5,column=0,sticky=W,padx=5)
        self.entPrix_location=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Prix_location)
        self.entPrix_location.grid(row=5,column=1,sticky=W,padx=5)
        
#========================================================Table treeview==============================================================================================================================================#
        scroll_y = Scrollbar(LeftFrame , orient = VERTICAL)
        
        self.voiture_records =ttk.Treeview(LeftFrame,height =12,columns=("Num_imma","Marque","Modele","Kilometrage","Etat","Prix_location") ,yscrollcommand= scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.voiture_records.heading('Num_imma',text='Num_imma')
        self.voiture_records.heading('Marque',text='Marque')
        self.voiture_records.heading('Modele',text='Modele')
        self.voiture_records.heading('Kilometrage',text='Kilometrage')
        self.voiture_records.heading('Etat',text='Etat')
        self.voiture_records.heading('Prix_location',text='Prix_location')
        
        self.voiture_records['show']='headings'
        
        
        self.voiture_records.column('Num_imma',width=70)
        self.voiture_records.column('Marque',width=70)
        self.voiture_records.column('Modele',width=70)
        self.voiture_records.column('Kilometrage',width=70)
        self.voiture_records.column('Etat',width=70)
        self.voiture_records.column('Prix_location',width=70)

        self.voiture_records.pack(fill=BOTH,expand=1)
        self.voiture_records.bind("<ButtonRelease-1>",ViewInfo)
        
        
#========================================================================Creation des boutons==============================================================================================================================#
        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text='Add New',bd=4,pady=1,padx=24,width=8,height=2,command=AddData).grid(row=0,column=0,padx=1)
        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text='Delete',bd=4,pady=1,padx=24,width=8,height=2,command=DeleteData).grid(row=1,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text='Update',bd=4,pady=1,padx=24,width=8,height=2,command=Update).grid(row=2,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text='Display',bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData).grid(row=3,column=0,padx=1)
        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text='Search',bd=4,pady=1,padx=24,width=8,height=2,command=SearchDB).grid(row=4,column=0,padx=1)
        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text='Reset',bd=4,pady=1,padx=24,width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)
        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text='Exit',bd=4,pady=1,padx=24,width=8,height=2,command=Exit).grid(row=6,column=0,padx=1)


   












#======================================================================================================================================================================================================#

if __name__ == '__main__':
    root = Tk()
    application = voiture(root)
    root.mainloop()