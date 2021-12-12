from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from mysql.connector import Error




#===============================================================Definition du classe voiture=======================================================================================================================================#
class Location_voiture:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "Gestion de location")
        self.root.geometry("800x700+300+0")
       
        
        
      
        
        
        
        
        MainFrame = Frame(self.root,bd=10,width=800,height=700,relief=RIDGE,bg='cadet blue')
        MainFrame.grid()
        TitleFrame = Frame(MainFrame,bd=7,width=800,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3 = Frame(MainFrame,bd=5,width=800,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)
        
        LeftFrame = Frame(TopFrame3,bd=5,width=800,height=400,padx=2,relief=RIDGE,bg='cadet blue')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd=5,width=600,height=180,padx=2,pady=4,relief=RIDGE)
        LeftFrame1.pack(side=TOP , padx =0 ,pady=0)
        
        RightFrame1 = Frame(TopFrame3,bd=5,width=100,height=400,padx=2,relief=RIDGE,bg='cadet blue')
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
       
        
        

#======================================================================definition des attributs================================================================================================================================#
        Id =IntVar()
        Num_imma = StringVar()
        Id_loc = IntVar()
        NbJours = IntVar()
        prix_total=IntVar()
        prix_loc=IntVar()
       
        
      
#========================================================================DEfinition des fonctions==============================================================================================================================#
        def Exit():
            Exit = tkinter.messagebox.askyesno("voiture","comfirm if you want to exit")
            if Exit > 0:
                root.destroy()
                return
        
        def Reset():
            self.entId.delete(0,END)
            self.cboNum_imma.delete(0,END)
            self.cboId_loc.delete(0,END)
            self.entNbJours.delete(0,END)
            
       
        
        def Num():
             
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("select Num_imma from voiture where Etat ='Disponible'")
            num = cur.fetchall()
            conn.commit()
            conn.close()
            print(num)
            return num
        
        
        def Id_Loc():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("select Id_loc from locataire")
            idloc = cur.fetchall()
            conn.commit()
            conn.close()
            return idloc
 
        
        def prix_location(event):
            global c
            c = self.cboNum_imma.get() # this will assign the variable c the value of cbox
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            sql = "SELECT prix_location FROM voiture WHERE Num_imma=%s"
            arg = (c,)
            cur.execute(sql, arg)
            num1 = cur.fetchone()
            conn.commit()
            conn.close()
            self.cboprix_location.set(num1)
            prixTotal = int(self.entNbJours.get())*int(self.cboprix_location.get())
            self.cboprix_total.set(prixTotal)
           
            
        
        
        def ViewInfo(ev):
            Info= self.locations_records.focus()
            learnerData = self.locations_records.item(Info)
            row = learnerData['values']
            Id.set(row[0]),
            NbJours.set(row[1]),
            Id_loc.set(row[2]),
            Num_imma.set(row[3]),
            prix_loc.set(row[4]),
            prix_total.set(row[5])
            
        def Display():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("select * from location_voiture")
            result = cur.fetchall()
            if len(result) !=0:
                self.locations_records.delete(*self.locations_records.get_children())
                for row in result:
                    self.locations_records.insert('',END,values=row)
            conn.commit()
            conn.close()

            
        def Add():
            if Num_imma.get() == "" or Id_loc.get() == "":
                tkinter.messagebox.showerror("voiture","no id_loc or num_imma selected")
            else:
                
                
                
                conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
                cur = conn.cursor()
                cur.execute("insert into location_voiture(Id,NbJours,Id_loc,Num_imma,prix_location,prix_total) values(%s,%s,%s,%s,%s,%s)",(
                         Id.get(),
                         NbJours.get(),
                         Id_loc.get(),
                         Num_imma.get(),
                         prix_loc.get(),
                         prix_total.get()))
                
                cur.execute("UPDATE `voiture` SET `Etat`='en cours de location' WHERE `Num_imma`='%s'"%Num_imma.get())
                conn.commit()
                Display()
                conn.close()
                tkinter.messagebox.showinfo("voiture","Record Entered successfully")
                
                
        
                
        def DeleteData():
            conn = mysql.connector.connect(host="localhost",user="root",password="",database="location")
            cur = conn.cursor()
            cur.execute("delete from location_voiture where Id='%s'"%Id.get())
            conn.commit()
            Display()
            conn.close()
            
            tkinter.messagebox.showinfo("voiture","Record successfully Deleted")
#===============================================================================================================
        self.lbltitle=Label(TitleFrame,font=('arial',30,'bold'),text='LOCATION_VOITURE',bd=7)
        self.lbltitle.grid(row=0,column=0,padx=280)
        
        self.lblId=Label(LeftFrame1,font=('arial',12,'bold'),text='ID',bd=7)
        self.lblId.grid(row=0,column=0,sticky=W,padx=5)
        self.cboId=Entry(LeftFrame1,font=('arial',12,'bold'),width=30,justify='left',textvariable=Id)
        self.cboId.grid(row=0,column=1,sticky=W,padx=5)
        
        self.lblNum_imma=Label(LeftFrame1,font=('arial',12,'bold'),text='NUm_imma',bd=7)
        self.lblNum_imma.grid(row=3,column=0,sticky=W,padx=5)
        self.cboNum_imma=ttk.Combobox(LeftFrame1,values=Num(),font=('arial',12,'bold'),width=30,justify='left',textvariable=Num_imma)
        self.cboNum_imma.bind("<<ComboboxSelected>>", prix_location)
        
        self.cboNum_imma.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblId_loc=Label(LeftFrame1,font=('arial',12,'bold'),text='Id_loc',bd=7)
        self.lblId_loc.grid(row=2,column=0,sticky=W,padx=5)
        self.cboId_loc=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=30,justify='left',textvariable=Id_loc)
        self.cboId_loc['values']=Id_Loc()
        
        self.cboId_loc.grid(row=2,column=1,sticky=W,padx=5)
        
        self.lblNbJours=Label(LeftFrame1,font=('arial',12,'bold'),text='NbJours',bd=7)
        self.lblNbJours.grid(row=1,column=0,sticky=W,padx=5)
        self.entNbJours=Entry(LeftFrame1,font=('arial',12,'bold'),width=31,bd=5,justify='left',textvariable=NbJours)
        self.entNbJours.grid(row=1,column=1,sticky=W,padx=5)
        
        self.lblprix_location=Label(LeftFrame1,font=('arial',12,'bold'),text='prix_location/j',bd=7)
        self.lblprix_location.grid(row=4,column=0,sticky=W,padx=5)
        self.cboprix_location=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=31,state='readonly',textvariable=prix_loc)
        self.cboprix_location.grid(row=4,column=1,sticky=W,padx=5)
        

        self.lblprix_total=Label(LeftFrame1,font=('arial',12,'bold'),text='prix_total',bd=7)
        self.lblprix_total.grid(row=5,column=0,sticky=W,padx=5)
        self.cboprix_total=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=31,state='readonly',textvariable=prix_total)
        self.cboprix_total.grid(row=5,column=1,sticky=W,padx=5)
        
        
        
        
        
#========================================================Table treeview==============================================================================================================================================#
        scroll_y = Scrollbar(LeftFrame , orient = VERTICAL)
        
        self.locations_records =ttk.Treeview(LeftFrame,height =12,columns=("Id","NbJours","Id_loc","Num_imma","prix_loc","prix_total") ,yscrollcommand= scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        self.locations_records.heading('Id',text='Id')
        self.locations_records.heading('NbJours',text='NbJours')
        self.locations_records.heading('Id_loc',text='Id_loc')
        self.locations_records.heading('Num_imma',text='Num_imma')
        self.locations_records.heading('prix_loc',text='prix location')
        self.locations_records.heading('prix_total',text='prix total')
       
        
        self.locations_records['show']='headings'
        
        
        self.locations_records.column('Id',width=70)
        self.locations_records.column('NbJours',width=70)
        self.locations_records.column('Id_loc',width=70)
        self.locations_records.column('Num_imma',width=70)
        self.locations_records.column('prix_loc',width=70)
        self.locations_records.column('prix_total',width=70)
     

        self.locations_records.pack(fill=BOTH,expand=1)
        self.locations_records.bind("<ButtonRelease-1>",ViewInfo)




#========================================================================Creation des boutons==============================================================================================================================#
        self.btnAdd=Button(RightFrame1a,font=('arial',16,'bold'),text='louer',bd=4,pady=1,padx=24,width=8,height=2,command=Add).grid(row=0,column=0,padx=1)
        self.btndelete=Button(RightFrame1a,font=('arial',16,'bold'),text='delete',bd=4,pady=1,padx=24,width=8,height=2,command=DeleteData).grid(row=1,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text='display',bd=4,pady=1,padx=24,width=8,height=2,command=Display).grid(row=2,column=0,padx=1)
      
       
          
            

   












#======================================================================================================================================================================================================#

if __name__ == '__main__':
    root = Tk()
    application = Location_voiture(root)
    root.mainloop()