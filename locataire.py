from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error




#===============================================================Definition de la classe voiture=======================================================================================================================================#
class voiture:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "Gestion des Locataires")
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

        Id_loc = StringVar()
        Nom = StringVar()
        Prenom = StringVar()
        Adresse  = StringVar()
       
#========================================================================DEfinition des fonctions==============================================================================================================================#
        def Exit():
            Exit = tkinter.messagebox.askyesno("locataire","comfirm if you want to exit")
            if Exit > 0:
                root.destroy()
                return
        
        def Reset():
            self.entId_loc.delete(0,END)
            self.entNom.delete(0,END)
            self.entPrenom.delete(0,END)
            self.entAdresse.delete(0,END)
            
            
            
        def AddData():
            if Id_loc.get() == "":
                tkinter.messagebox.showerror("locataire","Not Id_loc entred")
            else:
                
                 conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
                 cur = conn.cursor()
                 cur.execute("insert into locataire(Id_loc,Nom,Prenom,Adresse) values(%s,%s,%s,%s)",(
                         Id_loc.get(),
                         Nom.get(),
                         Prenom.get(),
                         Adresse.get(),
                         
                         ))
                 conn.commit()
                 DisplayData()
                 conn.close()
                 tkinter.messagebox.showinfo("Locataire","Record Entered successfully")
            
        def DisplayData():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("select * from locataire order by nom ASC")
            result = cur.fetchall()
            if len(result) != 0:
                self.locataire_records.delete(*self.locataire_records.get_children())
                for row in result:
                    self.locataire_records.insert('',END,values=row)
                
            conn.commit()
            conn.close()
        
        def ViewInfo(ev):
            Info= self.locataire_records.focus()
            learnerData = self.locataire_records.item(Info)
            row = learnerData['values']
            Id_loc.set(row[0]),
            Nom.set(row[1]),
            Prenom.set(row[2]),
            Adresse.set(row[3])
           
        
        
        def Update():
           conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
           cur = conn.cursor()
           cur.execute("update locataire set Nom=%s,Prenom=%s,Adresse=%s where Id_loc=%s",(
          
           Nom.get(),
           Prenom.get(),
           Adresse.get(),
           Id_loc.get()))
           conn.commit()
           DisplayData()
           conn.close()
            
           tkinter.messagebox.showinfo("Locataire","Record updated successfully")
        
        def DeleteData():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("delete  from locataire where Id_loc=%s"%Id_loc.get())
            
            conn.commit()
            DisplayData()
            conn.close()
            
            tkinter.messagebox.showinfo("locataire","Record successfully Deleted")
            
            
        def SearchDB():
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
                cur = conn.cursor()
                cur.execute("select * from locataire where Id_loc='%s'"%Id_loc.get())
                row = cur.fetchone()
                Id_loc.set(row[0]),
                Nom.set(row[1]),
                Prenom.set(row[2]),
                Adresse.set(row[3]),
                conn.commit()
            except:
                tkinter.messagebox.showinfo("locataire","No such Record found")
                Reset()
            
          
            conn.close() 
                
                 
    
                
#==========================================================================Graphic design============================================================================================================================#      
        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text='Locataire',bd=7)
        self.lbltitle.grid(row=0,column=0,padx=280)
        
        self.lblId_loc=Label(LeftFrame1,font=('arial',12,'bold'),text='Id_loc',bd=7)
        self.lblId_loc.grid(row=0,column=0,sticky=W,padx=5)
        self.entId_loc=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Id_loc)
        self.entId_loc.grid(row=0,column=1,sticky=W,padx=5)
        
        self.lblNom=Label(LeftFrame1,font=('arial',12,'bold'),text='Nom',bd=7)
        self.lblNom.grid(row=1,column=0,sticky=W,padx=5)
        self.entNom=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Nom)
        self.entNom.grid(row=1,column=1,sticky=W,padx=5)
        
        self.lblPrenom=Label(LeftFrame1,font=('arial',12,'bold'),text='Prenom',bd=7)
        self.lblPrenom.grid(row=2,column=0,sticky=W,padx=5)
        self.entPrenom=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Prenom)
        self.entPrenom.grid(row=2,column=1,sticky=W,padx=5)
        
        self.lblAdresse=Label(LeftFrame1,font=('arial',12,'bold'),text='Adresse',bd=7)
        self.lblAdresse.grid(row=3,column=0,sticky=W,padx=5)
        self.entAdresse=Entry(LeftFrame1,font=('arial',12,'bold'),width=44,bd=5,justify='left',textvariable=Adresse)
        self.entAdresse.grid(row=3,column=1,sticky=W,padx=5)
        
        
        
#========================================================Table treeview==============================================================================================================================================#
        scroll_y = Scrollbar(LeftFrame , orient = VERTICAL)
        
        self.locataire_records =ttk.Treeview(LeftFrame,height =12,columns=("Id_loc","Nom","Prenom","Adresse") ,yscrollcommand= scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.locataire_records.heading('Id_loc',text='Id_loc')
        self.locataire_records.heading('Nom',text='Nom')
        self.locataire_records.heading('Prenom',text='Prenom')
        self.locataire_records.heading('Adresse',text='Adresse')
       
        
        self.locataire_records['show']='headings'
        
        
        self.locataire_records.column('Id_loc',width=70)
        self.locataire_records.column('Nom',width=70)
        self.locataire_records.column('Prenom',width=70)
        self.locataire_records.column('Adresse',width=70)

        self.locataire_records.pack(fill=BOTH,expand=1)
        self.locataire_records.bind("<ButtonRelease-1>",ViewInfo)
        
        
                
        
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
