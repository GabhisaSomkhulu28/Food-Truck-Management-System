from tkinter import *
import tkinter as tk
from tkinter import messagebox

root =Tk()
root.title("About")
root.geometry("550x500")
root.resizable(False, False)
root.configure(background= "Light Pink")



def Show_Help():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    txtReport.destroy()
    Head1.destroy()
    btnCheckForUpdates.destroy()



    txtHelp=Text(root, width= 46, height = 20, bg="White", border=None, font=('Times New Roman' , 14,))
    txtHelp.place(relx=0.21, rely=0.05)

     txtHelp.insert(tk.INSERT ,"Welcome to Burgerberg Help" + "\n" + "Documentation" + "\n" +
                    "If you are a newcomer to Burgerberg, please read the introduction to Burgerberg." +  "\n" + 
                    "You will find some information on how to use nurgerberg in the link: ." +  "\n" + 
                    "If you are unsure about terminology, please consult the knowledge base." + "\n" + 
                    "Help" +  "\n" + "Before asking any question, please refer yourself to the FAQ." + "\n" +
                    "You might then get (and give) help on the Forums, the mailing-lists." + "\n" + 
                    "Contribute to the project" + "\n" + "You can help the Burgerberg program by purchasing some of its products")

def Update_Info():
     messagebox.showinfo("Update Info" , "There are no new updates available.")

def Show_About():
        
        txtHelp=Text(root, width= 50, height = 20,highlightthickness=0,relief="raised", bg="light pink",bd=0,font=('Times New Roman' , 14,), fg="light pink", )
        txtHelp.place(relx=0.21, rely=0.05)
        Head1= Frame(root,width=140,height=140,bg="White")
        Head1.place(x=245 , y=10)

        Head2= Frame(root,width=100,height=480,bg="Sky Blue")
        Head2.place(x=10 , y=10)

        Head3= Frame(root,width=70,height=70,bg="White")
        Head3.place(x= 20 , y=15)

        Head4 = Frame(root,width=70,height=70,bg="White")
        Head4.place(x= 20 , y=100)

        Head4 = Frame(root,width=70,height=70,bg="White")
        Head4.place(x= 20 , y=185)

        label1 = tk.Label(root, text="Burgerberg" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
        label1.place(relx=0.48 , rely=0.3)

        label2 = tk.Label(root , text="Version - 12.11.28.304" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
        label2.place(relx=0.38 , rely=0.35)

        label3 = tk.Label(root , text="Copyroght 2024 Burgerberg" + "\n" + "All Rights Reserved" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
        label3.place(relx=0.34 , rely=0.4)

        txtReport =Text(root, width= 46, height = 10, bg="White",font=('Times New Roman' , 14,))
        txtReport.place(relx=0.21, rely=0.53)


        btnHelp = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "Help" , command= Show_Help)
        btnHelp.place( x=25 , y= 110)

        btnAbout = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "About" , command= Show_About)
        btnAbout.place( x=25 , y= 22)

        btnCheckUpdates = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "Updates" , command= Update_Info)
        btnCheckUpdates.place( x=25 , y= 190)


        

        txtReport.insert(tk.INSERT ,"Burgerberg would like to acknowledge the following as its AUTHORS" + "\n" +
                        "1. Hluma Mahlasela" + "\n" + "2. Lathitha Russia" + "\n" + "3. Ngcebo Ngubane" + "\n" + "4. Vongai Vafana" + "\n" + 
                        "5. Masingta Maswanganye" + "\n" + "6. Nkcubeko Dibela" + "\n")
        



Head1= Frame(root,width=140,height=140,bg="White")
Head1.place(x=245 , y=10)

Head2= Frame(root,width=100,height=480,bg="Sky Blue")
Head2.place(x=10 , y=10)

Head3= Frame(root,width=70,height=70,bg="White")
Head3.place(x= 20 , y=15)

Head4 = Frame(root,width=70,height=70,bg="White")
Head4.place(x= 20 , y=100)

Head4 = Frame(root,width=70,height=70,bg="White")
Head4.place(x= 20 , y=185)



label1 = tk.Label(root, text="Burgerberg" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
label1.place(relx=0.48 , rely=0.3)

label2 = tk.Label(root , text="Version - 12.11.28.304" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
label2.place(relx=0.38 , rely=0.35)

label3 = tk.Label(root , text="Copyroght 2024 Burgerberg" + "\n" + "All Rights Reserved" , fg="Black" , bg= "Light Pink",font=('Times New Roman' , 15, 'bold'))
label3.place(relx=0.34 , rely=0.4)

txtReport =Text(root, width= 46, height = 10, bg="White",font=('Times New Roman' , 14,))
txtReport.place(relx=0.21, rely=0.53)

btnAbout = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "About" , command= Show_About)
btnAbout.place( x=25 , y= 22)

btnHelp = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "Help" , command= Show_Help)
btnHelp.place( x=25 , y= 110)

btnCheckUpdates = tk.Button(root ,width=7, height=3 , font=('Times New Roman' , 10,),text = "Updates" , command= Update_Info)
btnCheckUpdates.place( x=25 , y= 190)

txtReport.insert(tk.INSERT ,"Burgerberg would like to acknowledge the following as its AUTHORS" + "\n" +
                 "1. Hluma Mahlasela" + "\n" + "2. Lathitha Russia" + "\n" + "3. Ngcebo Ngubane" + "\n" + "4. Vongai Vafana" + "\n" + 
                 "5. Masingta Maswanganye" + "\n" + "6. Nkcubeko Dibela" + "\n")

btnCheckForUpdates = tk.Button(root ,width=36, height=3, font=('Times New Roman' , 14,),text = "Check For Updates" , command=Update_Info)
btnCheckForUpdates.place(relx=0.25 ,rely=0.53 )
btnCheckForUpdates.destroy()

txtHelp=Text(root, width= 46, height = 20, bg="White",font=('Times New Roman' , 14,))
txtHelp.place(relx=0.21, rely=0.05)

txtHelp.insert(tk.INSERT ,"Welcome to Burgerberg Help" + "\n" + "Documentation" + "\n" +
                "If you are a newcomer to Burgerberg, please read the introduction to Burgerberg." +  "\n" + 
                "You will find some information on how to use nurgerberg in the link: ." +  "\n" + 
                "If you are unsure about terminology, please consult the knowledge base." + "\n" + 
                "Help" +  "\n" + "Before asking any question, please refer yourself to the FAQ." + "\n" +
                "You might then get (and give) help on the Forums, the mailing-lists." + "\n" + 
                "Contribute to the project" + "\n" + "You can help the Burgerberg program by purchasing some of its products")
txtHelp.destroy()


root.mainloop()

def about():
     