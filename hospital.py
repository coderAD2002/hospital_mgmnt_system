from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as ms

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablets=StringVar()
        self.Ref=StringVar()
        self.Dose=StringVar()
        self.NoOfTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.BloodPressure=StringVar()
        self.Storage=StringVar()
        self.Medicine=StringVar()
        self.PatientId=StringVar()
        self.NhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DOB=StringVar()
        self.Address=StringVar()
        
 



        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #=========================Dataframe====================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)


        #=================================Button's Frame========================
       
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #===========================Details frame=============================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)


        #========================DataframeLeft==========================

        lblNameOfTablets=Label(DataframeLeft,text="Names of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameOfTablets.grid(row=0,column=0)
        
        comNameOfTablets=ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablets,font=("times new roman",12,"bold"),width=30,)                                                                                
        comNameOfTablets["values"]=("Nice","Corona","Vaccine","Acetomorphin","Adderall","Amlodopine","Atvian")
        comNameOfTablets.grid(row=0,column=1)

        lblRef=Label(DataframeLeft,text="Referrence No.",font=("times new roman",12,"bold"),padx=2)
        lblRef.grid(row=1,column=0,sticky=W)
        txtRef=Entry(DataframeLeft,textvariable=self.Ref,font=("times new roman",12,"bold"),width=35)
        txtRef.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,text="Dose:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("times new roman",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets=Label(DataframeLeft,text="No. Of Tablets:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets=Entry(DataframeLeft,textvariable=self.NoOfTablets,font=("times new roman",12,"bold"),width=35)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,text="Lot:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=("times new roman",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(DataframeLeft,text="Date of Issue",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=("times new roman",12,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,text="Expiry Date:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=("times new roman",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,text="Daily Dose:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("times new roman",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,text="Side Effect:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,textvariable=self.SideEffects,font=("times new roman",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataframeLeft,text="Further Information:",font=("times new roman",12,"bold"),padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("times new roman",12,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,text="Blood Pressure:",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.BloodPressure,font=("times new roman",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,text="Storage:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,textvariable=self.Storage,font=("times new roman",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,text="Medicine:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,textvariable=self.Medicine,font=("times new roman",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,text="Patient's Id:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,textvariable=self.PatientId,font=("times new roman",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,text="NHS Number:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,textvariable=self.NhsNumber,font=("times new roman",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,text="Name of Patient:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,textvariable=self.PatientName,font=("times new roman",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        lblDOB=Label(DataframeLeft,text="Date Of Birth:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB=Entry(DataframeLeft,textvariable=self.DOB,font=("times new roman",12,"bold"),width=35)
        txtDOB.grid(row=7,column=3)

        lblAddress=Label(DataframeLeft,text="Patient's Address:",font=("times new roman",12,"bold"),padx=4,pady=6)
        lblAddress.grid(row=8,column=2,sticky=W)
        txtAddress=Entry(DataframeLeft,textvariable=self.Address,font=("times new roman",12,"bold"),width=35)
        txtAddress.grid(row=8,column=3)

        #=======================DataframeRight=========================
        self.txtPrescription=Text(DataframeRight,font=("times new roman",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #=============================Buttons=====================================
        
        btnPrescription=Button(Buttonframe,bg="green",text="Prescription",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.prescription)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,bg="green",text="Prescription Data",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=2)

        btnUpdate=Button(Buttonframe,bg="green",text="Update",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.update)
        btnUpdate.grid(row=0,column=4)

        btnDelete=Button(Buttonframe,bg="green",text="Delete",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.delete)
        btnDelete.grid(row=0,column=6)

        btnClear=Button(Buttonframe,bg="green",text="Clear",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.clear)
        btnClear.grid(row=0,column=8)

        btnExit=Button(Buttonframe,bg="green",text="Exit",fg="white",font=("times new roman",12,"bold"),width=26,height=0,padx=2,pady=4,command=self.exit)
        btnExit.grid(row=0,column=10)

        #========================================Table====================================
        #====================================Scroll-Bar====================================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("name of tablets","ref","dose","no of tablets","lot","issue date","exp date","daily dose","storage","nhs number","p_name","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("name of tablets",text="Names Of Tablets")
        self.hospital_table.heading("ref",text="Referrence No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("no of tablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issue date",text="Date Of Issue")
        self.hospital_table.heading("exp date",text="Expiry Date")        
        self.hospital_table.heading("daily dose",text="Daily Dose")        
        self.hospital_table.heading("storage",text="Stroage")       
        self.hospital_table.heading("nhs number",text="NHS Number")       
        self.hospital_table.heading("p_name",text="Patient Name")       
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("address",text="Address")
        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)
        


        self.hospital_table.column("name of tablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("no of tablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issue date",width=100)
        self.hospital_table.column("exp date",width=100)
        self.hospital_table.column("daily dose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhs number",width=100)
        self.hospital_table.column("p_name",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        self.hospital_table.pack(fill=BOTH,expand=1)
        

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


    #===================================functioanlities================================

    def iPrescriptionData(self):
        if self.NameOfTablets.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            mydb=ms.connect(host="localhost",user="root",password="1234",database="hospital_details")
            mycur=mydb.cursor()
            mycur.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.NameOfTablets.get(),
                                                                                                                self.Ref.get(),
                                                                                                                self.Dose.get(),
                                                                                                                self.NoOfTablets.get(),
                                                                                                                self.Lot.get(),
                                                                                                                self.IssueDate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.DailyDose.get(),
                                                                                                                self.SideEffects.get(),
                                                                                                                self.FurtherInformation.get(),
                                                                                                                self.BloodPressure.get(),
                                                                                                                self.Storage.get(),
                                                                                                                self.Medicine.get(),
                                                                                                                self.PatientId.get(),
                                                                                                                self.NhsNumber.get(),
                                                                                                                self.PatientName.get(),
                                                                                                                self.DOB.get(),
                                                                                                                self.Address.get()
                                                                                                                ))
            mydb.commit()
            self.fetch_data()
            mycur.close()
            mydb.close()
            messagebox.showinfo("Success","Records have been added")


    def update(self):
        mydb=ms.connect(host="localhost",user="root",password="1234",database="hospital_details")
        mycur=mydb.cursor()
        mycur.execute("update hospital set NameOfTablets=%s,Ref=%s,Dose=%s,NoOfTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,SideEffects=%s,FurtherInformation=%s,BloodPressure=%s,Storage=%s,Medicine=%s,PatientId=%s,NhsNumber=%s,PatientName=%s,DOB=%s,Address=%s",(
                                                                                                                                                                                                                                                                                self.NameOfTablets.get(),
                                                                                                                                                                                                                                                                                self.Ref.get(),
                                                                                                                                                                                                                                                                                self.Dose.get(),
                                                                                                                                                                                                                                                                                self.NoOfTablets.get(),
                                                                                                                                                                                                                                                                                self.Lot.get(),
                                                                                                                                                                                                                                                                                self.IssueDate.get(),
                                                                                                                                                                                                                                                                                self.ExpDate.get(),
                                                                                                                                                                                                                                                                                self.DailyDose.get(),
                                                                                                                                                                                                                                                                                self.SideEffects.get(),
                                                                                                                                                                                                                                                                                self.FurtherInformation.get(),
                                                                                                                                                                                                                                                                                self.BloodPressure.get(),
                                                                                                                                                                                                                                                                                self.Storage.get(),
                                                                                                                                                                                                                                                                                self.Medicine.get(),
                                                                                                                                                                                                                                                                                self.PatientId.get(),
                                                                                                                                                                                                                                                                                self.NhsNumber.get(),
                                                                                                                                                                                                                                                                                self.PatientName.get(),
                                                                                                                                                                                                                                                                                self.DOB.get(),
                                                                                                                                                                                                                                                                                self.Address.get()
                                                                                                                                                                                                                                                                                ))
        messagebox.showinfo("Success","Records have been updated")

    
    def fetch_data(self):
        mydb=ms.connect(host="localhost",user="root",password="1234",database="hospital_details")
        mycur=mydb.cursor()
        mycur.execute("select * from hospital")
        rows=mycur.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            mydb.commit()
        mydb.close()



    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameOfTablets.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.SideEffects.set(row[8])
        self.FurtherInformation.set(row[9])
        self.BloodPressure.set(row[10])
        self.Storage.set(row[11])
        self.Medicine.set(row[12])
        self.PatientId.set(row[13])
        self.NhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DOB.set(row[16])
        self.Address.set(row[17])


    def prescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets:\t\t\t"+self.NameOfTablets.get()+"\n")
        self.txtPrescription.insert(END,"Referrence No:\t\t\t"+self.Ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"No Of Tablets:\t\t\t"+self.NoOfTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t\t"+self.SideEffects.get()+"\n")
        self.txtPrescription.insert(END,"Further Info:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"BP:\t\t\t"+self.BloodPressure.get()+"\n")
        self.txtPrescription.insert(END,"Storage:\t\t\t"+self.Storage.get()+"\n")
        self.txtPrescription.insert(END,"Medicine:\t\t\t"+self.Medicine.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"Nhs:\t\t\t"+self.NhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Birth Date:\t\t\t"+self.DOB.get()+"\n")
        self.txtPrescription.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")
     

    def delete(self):
        mydb=ms.connect(host="localhost",user="root",password="1234",database="hospital_details")
        mycur=mydb.cursor()
        query="delete from hospital where Ref=%s"
        value=(self.Ref.get(),)
        mycur.execute(query,value)
        mydb.commit()
        mydb.close()
        self.fetch_data()
        messagebox.showinfo("Success","Records have been deleted successfully")

    def clear(self):
        self.NameOfTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffects.set("")
        self.FurtherInformation.set("")
        self.BloodPressure.set("")
        self.Storage.set("")
        self.Medicine.set("")
        self.PatientId.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")
        self.txtPrescription.delete("1.0",END)



    def exit(self):
        iexit=messagebox.askyesno("Hospital mgmnt system","Are you sure you want to exit?")
        if iexit>0:
            root.destroy()
            return

                                                                                                                                                                                                                                                                                
root=Tk()
ob=Hospital(root)
root.mainloop()