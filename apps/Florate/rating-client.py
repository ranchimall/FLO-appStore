from tkinter import Tk,END,Button,Label,Frame,Entry,messagebox,Message,Text,NSEW,Scrollbar,Listbox,MULTIPLE ,PhotoImage,VERTICAL
#import CryptTools
import Transaction
import DataCenter
from SF import VerticalScrolledFrame

class Application:
    """The main application GUI Window."""
    def __init__(self,master=None):
    
        self.master = master
        self.Frame = Frame(self.master)
        self.LEVEL ={
            1: 'unsatisfactory',
            2: 'satisfactory',
            3: 'meet expectations',
            4:  'Exceed expectations',
            5:  'Exceptional'
            }
    
    
    def main(self):
        """
        Method name: main.

        Method use: The program starts the main GUI of the Rating System. 
        """
        try:
            self.IS.destroy()
        except:
            pass
        try:
            self.EM.destroy()
        except:
            pass
        self.MF = Frame(self.master)
        self.MF.pack()
        WelcomeLabel = Label(self.MF,text="Choose who you are ?",font=("Arial", 20))
        WelcomeLabel.grid(column = 1, columnspan =2)
        label =Label(self.MF,text=" ")
        label.grid(row = 2, columnspan =2)
        ISButton = Button(self.MF,text="Intern",command=self.internWindow)
        ISButton.grid(row =3,column=1)
        EMButton = Button(self.MF,text="Employee",command=self.employeeWindow)
        EMButton.grid(row =3, column=2)
        contentText = "\n\nWhat is this?\nThis app lets us to rate Interns through the FLO blockchain .\n\nThis is a zero knowledge application.\n\nHow to work ?\n\n Choose if you are an Intern or Employeer\n\n"+"An Intern's work would be to enter the Transaction id in the given field and get rating\n\nAn Empolyee must enter the transaction address and write all the intern data to it "
        Context = Message(self.MF, text = contentText)
        Context.grid(column = 1, columnspan =2)
    
    #Intern Section Starts
    def internWindow(self):
        """
        Method Name: internWindow.

        Method use: Provides a GUI for the Intern Application.
        """


        self.MF.destroy()
        self.IS = Frame(self.master)
        self.IS.pack()
        self.tranLBL = Label(self.IS,text="Enter Trasaction id: ")
        self.tranLBL.grid(row=0,column=0,sticky=NSEW,padx=8,pady=8)
        self.TXE  = Entry(self.IS)
        self.TXE.grid(row=0,column=1,sticky=NSEW,padx=16,pady=8)
        self.Sub = Button(self.IS,text="Fetch Rating",command=self.ratingResults)
        self.Sub.grid(row=1,columnspan=2,pady=16,padx=16,sticky=NSEW)
        self.LBL = Label(self.IS,text="Make a search and results will be displayed here:")
        self.LBL.grid(row=2,columnspan=2)
        self.Text = Text(self.IS,height=30,width=40,state='disabled')
        self.TextScroll = Scrollbar(self.Text,orient=VERTICAL)
        self.Text.config(yscrollcommand=self.TextScroll.set)
        self.TextScroll.config(command=self.Text.yview)
        self.Text.grid(row=3,columnspan=2,padx=16,pady=16)
        self.BackButton = Button(self.IS,text="Back",command=self.main)
        self.BackButton.grid(row=4,column=0)
        self.QUIT = Button(self.IS,command=self.master.destroy,text="QUIT")
        self.QUIT.grid(row=4,column=1)
    
    
    def ratingResults(self):
        """
        Method name: ratingResults.

        Method use: Driver for Intern Window GUI.
        """


        self.txid = self.TXE.get()
        self.TXE.configure(state="normal")
        self.TXE.insert('end',"Attempting to connect to BlockChain Address")
        self.TXE.configure(state="disabled")
        self.Text.configure(state="normal")
        self.Text.insert('end',"Trying to read Data from Block Chain")
        self.Text.configure(state="disabled")
        try:
            if len(self.txid)==0:
                messagebox.showwarning('Txid Error',"Trasaction Id cannot be empty")
                self.TXE.configure(state='normal')
                self.TXE.delete(0,'end')
                self.Text.configure(state='normal')
                self.Text.delete(1.0,'end')
                self.Text.configure(state='disabled')
                return
            recv = Transaction.readDatafromBlockchain(self.txid)
        except:
            messagebox.showwarning("NetworkError","Make Sure FLO-Core is running")
            self.TXE.configure(state='normal')
            self.TXE.delete(0,'end')
            self.Text.configure(state='normal')
            self.Text.delete(1.0,'end')
            self.Text.configure(state='disabled')
        pt = bytes.fromhex(recv).decode()
        lines = pt.split('\n')
        self.Text.configure(state="normal")
        self.Text.delete(1.0,'end')
        for line in lines:
            if line:
                num = line.split()[1]
                num = int(float(num))+1
                self.Text.insert('1.0',line+" "+self.LEVEL[num]+"\n")
        self.Text.configure(state='disabled')
        
    #Intern Section Ends Here

    #Employee Section Starts Here
    
    def employeeWindow(self,text=None):
        """
            Method name: employeeWindow.

            Method use: Provide a GUI for employee Window.

            Positional Arguments:
                
                Arguement Name: text.
                Argument Use: To provide the neccessary details to the GUI about rating data 
                              retrieved from the finalizeRatings method.
        """

        try:
            self.MF.destroy()
            self.RW.destroy() 
        except:
            pass
        self.EM = Frame(self.master)
        self.EM.pack()
        self.IDLBL =  Label(self.EM,text="Enter the Adress: ")
        self.IDLBL.grid(row=0,column=0,sticky=NSEW,padx=8,pady=8)
        self.TRE = Entry(self.EM)
        self.TRE.grid(row=0,column=1,sticky=NSEW,padx=16,pady=8)
        self.pButton = Button(self.EM,text="Create New Ratings",command=self.createRatings)
        self.pButton.grid(row=2,column=0,pady=16,padx=16)
        self.Sub = Button(self.EM,text="Post Rating",command=self.postResults)
        self.Sub.grid(row=2,column=1,pady=16,padx=16,sticky=NSEW)
        self.LBL = Label(self.EM,text="The rating Data is Here:")
        self.LBL.grid(row=3,columnspan=2)
        self.Text = Text(self.EM,height=20,width=30)
        if text:
            self.Text.insert('1.0',text)
        self.Text.grid(row=4,columnspan=2,padx=16,pady=16)
        self.BackButton = Button(self.EM,text="Back",command=self.main)
        self.BackButton.grid(row=5,column=0)
        self.QUIT = Button(self.EM,command=self.master.destroy,text="QUIT")
        self.QUIT.grid(row=5,column=1)
    
    
    def createRatings(self):
        """
            Method name: createRaNSEWtings.

            Method use: Provides a GUI for the Intern Rating.
        """
        try:
            self.EM.destroy()
        except:
            pass
        DataCenter.checkState()
        self.RW = Frame(self.master)
        self.RW.pack()
        self.IDLB = Listbox(self.RW,width=50,height=20,selectmode=MULTIPLE)
        self.scrollbar = Scrollbar(self.IDLB, orient=VERTICAL)
        self.IDLB.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.IDLB.yview)
        self.populateListBox()
        self.IDLB.grid(row=0,column=1,padx=16,pady=16,sticky=NSEW)
        self.loadImg = PhotoImage(file="AddBtn.gif")
        self.remImg = PhotoImage(file="RenmBtn.gif")
        self.removeIntern = Button(self.RW,height=48,width=48,image=self.remImg,command=self.removeData)
        self.removeIntern.grid(row=0,column=2,padx=8,pady=8)
        self.addIntern = Button(self.RW,text="",height=48,width=48,image=self.loadImg,command = self.loadData)
        self.addIntern.grid(row=0,column=3,padx=8,pady=8)
        self.RL = Listbox(self.RW,width=50,height=20,selectmode=MULTIPLE)
        for usr,rat in DataCenter.retrieveRating():
            self.RL.insert(END,usr + " "+str(rat))
        try:
            self.RAT.destroy()
        except:
            pass
        self.RLscroll = Scrollbar(self.RL, orient=VERTICAL)
        self.RL.config(yscrollcommand=self.RLscroll.set)
        self.RLscroll.config(command=self.RL.yview)
        self.RL.grid(row=0,column=4,padx=16,pady=16)
        self.createIntern = Button(self.RW,text="Add a new Intern",command = self.newIntern)
        self.createIntern.grid(row=2,column=1,padx=8,pady=4)
        self.DeleteIntern = Button(self.RW,text="Remove an Existing Intern",command=self.removeExistingIntern)
        self.DeleteIntern.grid(row=3,column=1,padx=8,pady=4)
        self.finalBtn = Button(self.RW,text="Finalize",command = self.finalizeRatings)
        self.finalBtn.grid(row=3,column=4)
    
    
    def newIntern(self):
        """
        Method name: newIntern.
        
        Method use: GUI for the creation of new Intern
        """


        self.RW.destroy()
        self.NE = Frame(self.master)
        self.NE.pack()
        self.newLBL = Label(self.NE,text="Enter the name: ")
        self.newLBL.grid(row=0,column=0,padx=8,pady=8)
        self.newNMEntry = Entry(self.NE)
        self.newNMEntry.grid(row=0,column=1,padx=8,pady=8)
        self.newUser = Label(self.NE,text="Enter the username: ")
        self.newUser.grid(row=1,column=0,padx=8,pady=8)
        self.newUNMEntry = Entry(self.NE)
        self.newUNMEntry.grid(row=1,column=1,padx=8,pady=8)
        self.AddBtn = Button(self.NE,text="Add Intern",command = self.CIB)
        self.AddBtn.grid(row=2,padx=8,pady=8)

    
    def finalizeRatings(self):
        """
            Method Name: finalizeRatings.

            Method Use: Format the rating data into desirable format and return back to the
                        Employee Window.
        """

        Rating_Str = ""
        for usr,rat in DataCenter.retrieveRating():
            Rating_Str += usr+" "+str(rat)+"\n"
        
        if not messagebox.askyesno("Revive Data","Should you want the rating data to be kept"):
            DataCenter.clearRatings()
        self.RW.destroy()
        self.employeeWindow(text = Rating_Str)


    def CIB(self):
        """
        Method name: CIB.

        Method Use: Driver Code to add a new Intern to the DataBase.
        """
        if len(self.newNMEntry.get())<=3 or len(self.newUNMEntry.get())<=3:
            messagebox.showwarning("Invalid Length","The Intern Fields are either empty or under 3 charecters")
            return
        else:
            try:
                DataCenter.write(self.newNMEntry.get(),self.newUNMEntry.get())
            except:
                messagebox.showwarning("Invalid Data","Please Check again")
                return
            messagebox.showinfo("Success","New Intern Sucessfully added")
            self.NE.destroy()
            self.createRatings()
    
    
    def loadData(self,process=None):
        """
        Method name: loadData.

        Method use: GUI to take the Input from the user and load the data to the Rating Data Base.
        """


        self.ratList = []
        self.TMPEN=[]
        if process:
            for name,rating in process:
                DataCenter.insertRating(name,rating.get())
            self.createRatings()
            return
        if not self.IDLB.curselection():
            messagebox.showinfo("Empty Selection","Please make sure to select at least one intern")
            return
        for i in self.IDLB.curselection():
            self.ratList.append(self.IDLB.get(i).split(' ')[2])
        self.RW.destroy()
        self.RAT = VerticalScrolledFrame(self.master)
        self.RAT.pack()
        self.LBL = Label(self.RAT.interior,text="Enter a Rating for the selected interns: ")
        self.LBL.pack()
        for item,row in zip(self.ratList,range(1,len(self.ratList)+1)):
            self.LBx = Label(self.RAT.interior,text=item)
            self.LBx.pack()
            self.TMPEN.append(Entry(self.RAT.interior))
            self.TMPEN[row-1].pack()
        self.Sub = Button(self.RAT.interior,command=lambda :self.loadData(zip(self.ratList,self.TMPEN)),text="submit")
        self.Sub.pack(pady=8)
        

    def removeData(self):
        """
        Method Name: removeData.

        Method use: Driver code to remove an Intern's Rating from the DataBase.
        """

        delList = []
        for item in self.RL.curselection():
            delList.append(self.RL.get(item))
            self.RL.delete(item)
        for item in delList:
            DataCenter.removeRating(item.split(' ')[0])


    def populateListBox(self):
        """
        Method Name: populateListBox

        Method use: To Format the rating Data and Fill it into the Intern's List
        """

        try:
            for data in enumerate(DataCenter.readAll(),1):
                self.IDLB.insert(END,str(data[0])+" "+str(data[1][0])+" "+str(data[1][1]))
        except:
            return

    def removeExistingIntern(self):
        """
        Method Name: removeExistingIntern
        
        Method use: To remove an Existing Intern from the DataBase
        """

        delList = []
        for i in self.IDLB.curselection():
            delList.append(self.IDLB.get(i))
        if messagebox.askyesno("Are you sure to delete ? (This can't be undone)","The following interns data is deleted:\n\n"+"\n".join(delList)):
            for item in delList:
                DataCenter.delete(item.split(' ')[2])
        self.RW.destroy()
        self.createRatings()


    def postResults(self):
        """
        Method Name: postResults

        Method use: To post the results on to the Block Chain
        """
        
        self.addr = self.TRE.get()
        self.ratingData = self.Text.get('1.0', END)
        try:
            if len(self.addr)==0:
                messagebox.showwarning('Adress Error',"Trasaction Address cannot be empty")
                self.TRE.configure(state='normal')
                self.TRE.delete(0,'end')
                self.Text.delete(1.0,'end')
                return
            elif len(self.ratingData)==0:
                messagebox.showwarning('Empty Ratings Error',"Ratings Field cannot be empty")
            hexCoded = self.ratingData.encode()
            hexCoded = hexCoded.hex()
            send = Transaction.writeDatatoBlockchain(hexCoded,self.addr,0.003)
            print(send)
            messagebox.showinfo("Transaction Success","Share this id with your interns:\n"+send)
            f = open("RatingData.txt","w")
            f.write(send)
            f.close()
        except:
            messagebox.showwarning("NetworkError","Make Sure FLO-Core is running")
            self.TRE.configure(state='normal')
            self.TRE.delete(0,'end')
            self.Text.delete(1.0,'end')


root = Tk()
root.title("Flo Rating App")
app = Application(master=root)
app.main()
root.mainloop()

""""
key = CryptTools.keyGen()
ct = CryptTools.encryptMsg("HelloTarun",key)
send = ct.encode().hex()
#txid = Transaction.writeDatatoBlockchain(send,"oPXCQNVnzkLRgHqzhz6kWc8XyErSdVhAdn",0.0003)
#recv = Transaction.readDatafromBlockchain(txid)
ct = bytes.fromhex(recv).decode()
pt = CryptTools.decryptMsg(ct,key)
"""
