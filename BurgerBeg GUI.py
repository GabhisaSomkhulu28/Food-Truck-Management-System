from tkinter import *
import customtkinter 
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import ImageTk, Image
import customtkinter as ctk 
import random
import string
import sqlite3
from tkinter import messagebox, simpledialog
from datetime import datetime




def main():
    win = customtkinter.CTk()
    app = LoginPage(win)
    win.mainloop()

with sqlite3.connect("Burger Inventory.py") as db:
    cur = db.cursor 

class LoginPage():
    def __init__(self, win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Food Truck Manangement System")
        main_image = customtkinter.CTkImage(Image.open("Food Tuck MS/Bckgr.png"), size = (1600, 850))

        password1 = StringVar()
        password2 = StringVar()
        total_price = StringVar()

        def exitbtn():
            self.mainord_frame.destroy()
            self.ord_frame.destroy()
            self.mainord_frame = customtkinter.CTkFrame(self.win, fg_color="white", bg_color="white", corner_radius=0)
            self.mainord_frame.pack(fill = BOTH,expand = TRUE)
            self.ord_frame = customtkinter.CTkFrame(self.mainord_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
            self.ord_frame.pack(expand = True)

            self.pasword2_entry.delete(0, customtkinter.END)
    
            self.admin_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Admin", font = ("Areal", 50))
            self.admin_lbl.place(relx = 0.44, rely = 0.05)
            self.admin_lbl.configure(text_color = "white")

            image_3 = customtkinter.CTkImage(Image.open("Food Tuck MS/Icon.png"), size = (80, 80))

            self.invbtn = customtkinter.CTkButton(self.ord_frame,image = image_3, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = inventory)
            self.invbtn.place(relx = 0.2, rely = 0.5)
            self.invbtn.configure(image = image_3)

            self.inv_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Inventory", font = ("Areal", 18))
            self.inv_lbl.place(relx = 0.228, rely = 0.645)
            self.inv_lbl.configure(text_color = "white")

            image_4 = customtkinter.CTkImage(Image.open("Food Tuck MS/icon3.png"), size = (80,80))

            self.mntly_rprts = customtkinter.CTkButton(self.ord_frame, image = image_4, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = GenerateMonthlyReports)
            self.mntly_rprts.place(relx = 0.7, rely = 0.5)
            self.mntly_rprts.configure(image = image_4)

            image_5 = customtkinter.CTkImage(Image.open("Food Tuck MS/istockphoto-1331044109-612x612.jpg"), size = (80, 80))

            self.aboutus_lbl = customtkinter.CTkLabel(self.ord_frame, text = "About Us",  font = ("Areal", 18))
            self.aboutus_lbl.place(relx =  0.48, rely = 0.645)
            self.aboutus_lbl.configure(text_color = "white")

            self.aboutus_btn = customtkinter.CTkButton(self.ord_frame, image = image_5,  text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = about)
            self.aboutus_btn.place(relx = 0.45, rely = 0.5)
            self.aboutus_btn.configure(image = image_5)

            self.mntly_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Montly Reports",  font = ("Areal", 18))
            self.mntly_lbl.place(relx = 0.71, rely = 0.645)
            self.mntly_lbl.configure(text_color = "white")


        def goback(): 
            self.updt_frame.destroy()
            self.mainord_frame = customtkinter.CTkFrame(self.win, fg_color="white", bg_color="white", corner_radius=0)
            self.mainord_frame.pack(fill = BOTH,expand = TRUE)
            self.ord_frame = customtkinter.CTkFrame(self.mainord_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
            self.ord_frame.pack(expand = True)

            self.pasword2_entry.delete(0, customtkinter.END)

            self.admin_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Admin", font = ("Areal", 50))
            self.admin_lbl.place(relx = 0.44, rely = 0.05)
            self.admin_lbl.configure(text_color = "white")

            image_3 = customtkinter.CTkImage(Image.open("Food Tuck MS/Icon.png"), size = (80, 80))

            self.invbtn = customtkinter.CTkButton(self.ord_frame,image = image_3, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = inventory)
            self.invbtn.place(relx = 0.2, rely = 0.5)
            self.invbtn.configure(image = image_3)

            self.inv_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Inventory", font = ("Areal", 18))
            self.inv_lbl.place(relx = 0.228, rely = 0.645)
            self.inv_lbl.configure(text_color = "white")

            image_4 = customtkinter.CTkImage(Image.open("Food Tuck MS/icon3.png"), size = (80,80))

            self.mntly_rprts = customtkinter.CTkButton(self.ord_frame, image = image_4, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = GenerateMonthlyReports)
            self.mntly_rprts.place(relx = 0.7, rely = 0.5)
            self.mntly_rprts.configure(image = image_4)

            image_5 = customtkinter.CTkImage(Image.open("Food Tuck MS/istockphoto-1331044109-612x612.jpg"), size = (80, 80))

            self.aboutus_lbl = customtkinter.CTkLabel(self.ord_frame, text = "About Us",  font = ("Areal", 18))
            self.aboutus_lbl.place(relx =  0.48, rely = 0.645)
            self.aboutus_lbl.configure(text_color = "white")

            self.aboutus_btn = customtkinter.CTkButton(self.ord_frame, image = image_5,  text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = about)
            self.aboutus_btn.place(relx = 0.45, rely = 0.5)
            self.aboutus_btn.configure(image = image_5)

            self.mntly_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Montly Reports",  font = ("Areal", 18))
            self.mntly_lbl.place(relx = 0.71, rely = 0.645)
            self.mntly_lbl.configure(text_color = "white")

        def logout():
            self.label1 = customtkinter.CTkLabel(self.win, text = "", bg_color= "grey")
            self.label1.place(relx = 0, rely = 0)
            self.label1.configure(image = main_image)

            self.main_frame = customtkinter.CTkFrame(self.win,border_width= 5, width = 700, height = 600, fg_color= "#efbcbc", bg_color="white", border_color="white", corner_radius=4)
            self.main_frame.place(x = 355, y = 100)

            self.login_lbl = customtkinter.CTkLabel(self.main_frame, text = "Login As ?", bg_color = "#efbcbc", font = ("Areal", 40))
            self.login_lbl.place(relx=0.5, rely=0.2, anchor=CENTER)
            self.login_lbl.configure(text_color = "white")

            self.orr_lbl = customtkinter.CTkLabel(self.main_frame, text = "OR", font = ("Areal", 15), bg_color="#efbcbc")
            self.orr_lbl.place(relx = 0.4855, rely = 0.53)
            self.orr_lbl.configure(text_color = "white")

            image_1 = customtkinter.CTkImage(Image.open("Food Tuck MS/1.png"), size = (80, 80))

            self.employee_btn = customtkinter.CTkButton(self.main_frame,image = image_1,text = "", bg_color="#efbcbc",corner_radius = 30, width=70, height=70, fg_color="white", hover_color="white", command = employee) 
            self.employee_btn.place(relx = 0.1, rely = 0.5) 
            self.employee_btn.configure(image = image_1)

            image_2 = customtkinter.CTkImage(Image.open("Food Tuck MS/2.png"), size = (80, 80))

            self.employer_btn = customtkinter.CTkButton(self.main_frame, image = image_2, text = "",bg_color="#efbcbc", corner_radius = 30, width = 70, height = 70, fg_color = "white", hover_color = "white", command = employer)
            self.employer_btn.place(relx = 0.7, rely = 0.5)
        
        

        def employer():
            self.main_frame.destroy()
            self.password2_frame = customtkinter.CTkFrame(self.win, border_width = 5, width = 500, height = 300, fg_color = "#efbcbc", bg_color="white", border_color="white", corner_radius=4 )
            self.password2_frame.place(x = 530, y = 100)

            self.employer_lbl = customtkinter.CTkLabel(master=self.password2_frame, text = "Admin Login", font = ("Areal bold", 30))
            self.employer_lbl.place(relx = 0.31, rely = 0.05)
            self.employer_lbl.configure(text_color = "white")

            self.entr2 = customtkinter.CTkLabel(self.password2_frame, text = "Enter Password : ", font = ("Areal", 15))
            self.entr2.place(relx = 0.1, rely = 0.4)
            self.entr2.configure(text_color = "white")

            self.pasword2_entry = customtkinter.CTkEntry(self.password2_frame, width = 200, textvariable = password2, corner_radius=4, fg_color="white", font = ("Areal", 20))
            self.pasword2_entry.place(relx = 0.39, rely = 0.4)
            self.pasword2_entry.configure(text_color = "black", show = "*")

            self.btn = customtkinter.CTkButton(self.password2_frame,width=100, text="Login", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command=login2)
            self.btn.place(relx = 0.39, rely = 0.6)
            self.rsbtun = customtkinter.CTkButton(self.password2_frame,width=100, text="Reset", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = reset2)
            self.rsbtun.place(relx = 0.66, rely = 0.6)

            self.logoutbtn = customtkinter.CTkButton(self.win, text = "Back",  fg_color = "#efbcbc", bg_color="white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = logout)
            self.logoutbtn.place(x = 50, rely = 0.020)

        def login2():
            if password2.get() != "87654321":
                messagebox.showerror("Login", "Your password is incorrect\nTry Again")
            else:
                password2.get() == "87654321"
                messagebox.showinfo("Login", "Login Succesfull\n Password is correct ")
                self.order_frame = customtkinter.CTkFrame(self.win, border_width = 5, width = 500, height = 300, fg_color = "#efbcbc", bg_color="white", border_color="white", corner_radius=4)
                self.order_frame.place(x = 530, y = 400)

                self.order_lbl = customtkinter.CTkLabel(self.order_frame, text = "Is there an order?", font = ("Areal bold", 25))
                self.order_lbl.configure(text_color = "white")
                self.order_lbl.place(relx = 0.31, rely = 0.05)

                self.yes_order = customtkinter.CTkButton(self.order_frame, text = "Yes order", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = ordr2_btn_clicked)
                self.yes_order.place(relx = 0.39, rely = 0.3)

                self.no_order = customtkinter.CTkButton(self.order_frame, text = "No order",  fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = no_order_btnClkd)
                self.no_order.place(relx = 0.39, rely = 0.5)

        def fries_clckd():
            self.order_frame = customtkinter.CTkScrollableFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 550, height = 150)
            self.order_frame.place(rely = 0.66, relx = 0.53 )
            self.frsaddbtn = customtkinter.CTkButton(self.order_frame, text = "Order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", width = 10, height = 10, command = frsbtn1)
            self.frsaddbtn.configure(text_color = "black")
            self.frsaddbtn.place(relx = 0.02)
                
            self.frsadd1btn = customtkinter.CTkButton(self.order_frame, text = "Order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc",  width = 10, height = 10, command = frsbtn2)
            self.frsadd1btn.configure(text_color = "black")
            self.frsadd1btn.pack()
            self.frsadd1btn.place(relx = 0.02, rely = 0.505)

            try:
                    with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()
                    cur.execute("SELECT item_name FROM Ingredients WHERE id BETWEEN 104 AND 105")
                    fetched_burgers = cur.fetchall()

                    if fetched_burgers:
                        for row in fetched_burgers:
                            self.burger_ing = customtkinter.CTkLabel(self.order_frame, text = row)
                            self.burger_ing.pack()
                            self.burger_ing.configure(text_color="black", text = row)
                    else:
                        print("I don't have items")

            except sqlite3.Error as e:
                    print(f"An error occurred: {e}")

        def frsbtn1():
            try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()

                            cur.execute("SELECT item_name FROM Ingredients WHERE id = 104")
                            fetched_prd = cur.fetchone()
                            cur.execute("SELECT quantity FROM Ingredients WHERE id = 104")
                            fetched_qnty = cur.fetchone()

                            if fetched_qnty:
                                for packs_available in fetched_qnty:
                                    packs_available = fetched_qnty[0]
                                    self.available_entry.delete(0, customtkinter.END)
                                    self.available_entry.insert(0, str(packs_available))
                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                            if fetched_prd:
                                        for product_name in fetched_prd:
                                            product_name = fetched_prd[0]
                                            self.textbox.delete("end",  customtkinter.END)
                                            self.textbox.insert("end", f"{product_name}\n")
                            else:
                                print("I dont have it")

            except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

            try:
                        with sqlite3.connect("burger_inventory.db") as db:
                                cur = db.cursor()
                                cur.execute("SELECT price FROM Ingredients WHERE id = 104")
                                fetched_prc = cur.fetchone()
                                if fetched_prc:
                                    selling_prices1 = fetched_prc[0]
                                    self.textbox2.delete("end", customtkinter.END)
                                    self.textbox2.insert("end", f"{selling_prices1}\n")

                                    self.total_prc += selling_prices1
                                    self.prc_entry.delete(0, customtkinter.END)
                                    self.prc_entry.insert(0, str(self.total_prc))
                                else:
                                    print("I dont have item")

            except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

        def frsbtn2():
            try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()

                            cur.execute("SELECT item_name FROM Ingredients WHERE id = 105")
                            fetched_prd = cur.fetchone()
                            cur.execute("SELECT quantity FROM Ingredients WHERE id = 105")
                            fetched_qnty = cur.fetchone()

                            if fetched_qnty:
                                for packs_available in fetched_qnty:
                                    packs_available = fetched_qnty[0]
                                    self.available_entry.delete(0, customtkinter.END)
                                    self.available_entry.insert(0, str(packs_available))

                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                            if fetched_prd:
                                        for product_name in fetched_prd:
                                            product_name = fetched_prd[0]
                                            self.textbox.delete("end",  customtkinter.END)
                                            self.textbox.insert("end", f"{product_name}\n")
                            else:
                                print("I dont have it")

            except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

            try:
                        with sqlite3.connect("burger_inventory.db") as db:
                                cur = db.cursor()
                                cur.execute("SELECT price FROM Ingredients WHERE id = 105")
                                fetched_prc = cur.fetchone()

                                if fetched_prc:
                                    selling_prices1 = fetched_prc[0]
                                    self.textbox2.delete("end", customtkinter.END)
                                    self.textbox2.insert("end", f"{selling_prices1}\n")

                                    self.total_prc += selling_prices1
                                    self.prc_entry.delete(0, customtkinter.END)
                                    self.prc_entry.insert(0, str(self.total_prc))
                                else:
                                    print("I dont have item")

            except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

        def burger_clkd():
                self.order_frame = customtkinter.CTkScrollableFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 550, height = 150)
                self.order_frame.place(rely = 0.66, relx = 0.53 )
                self.addbtn = customtkinter.CTkButton(self.order_frame, text = "Order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", width = 10, height = 10, command = btn_pressed)
                self.addbtn.configure(text_color = "black")
                self.addbtn.place(relx = 0.02)
                
                self.add1btn = customtkinter.CTkButton(self.order_frame, text = "Order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc",  width = 10, height = 10, command = btn2_pressed)
                self.add1btn.configure(text_color = "black")
                self.add1btn.pack()
                self.add1btn.place(relx = 0.02, rely = 0.325)

                self.add2btn = customtkinter.CTkButton(self.order_frame, text = "Order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc",  width = 10, height = 10, command = btn3_pressed)
                self.add2btn.configure(text_color = "black")
                self.add2btn.pack()
                self.add2btn.place(relx = 0.02, rely = 0.65)

                try:
                    with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()
                    cur.execute("SELECT item_name FROM Ingredients WHERE id BETWEEN 101 AND 103")
                    fetched_burgers = cur.fetchall()

                    if fetched_burgers:
                        for row in fetched_burgers:
                            self.burger_ing = customtkinter.CTkLabel(self.order_frame, text = row)
                            self.burger_ing.pack()
                            self.burger_ing.configure(text_color="black", text = row)
                        
                    else:
                        print("I don't have items")

                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")

        def btn_pressed():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()

                            cur.execute("SELECT item_name FROM Ingredients WHERE id = 101")
                            fetched_prd = cur.fetchone()
                            cur.execute("SELECT quantity FROM Ingredients WHERE id = 101")
                            fetched_qnty = cur.fetchone()

                            if fetched_qnty:
                                for packs_available in fetched_qnty:
                                    packs_available = fetched_qnty[0]
                                    self.available_entry.delete(0, customtkinter.END)
                                    self.available_entry.insert(0, str(packs_available))

                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))
                        
                            if fetched_prd:
                                        for product_name in fetched_prd:
                                            product_name = fetched_prd[0]
                                            self.textbox.delete("end",  customtkinter.END)
                                            self.textbox.insert("end", f"{product_name}\n")
                            else:
                                print("I dont have it")

                    except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                                cur = db.cursor()
                                cur.execute("SELECT price FROM Ingredients WHERE id = 101")
                                fetched_prc = cur.fetchone()

                                if fetched_prc:
                                    selling_prices1 = fetched_prc[0]
                                    self.textbox2.delete("end", customtkinter.END)
                                    self.textbox2.insert("end", f"{selling_prices1}\n")

                                    self.total_prc += selling_prices1
                                    self.prc_entry.delete(0, customtkinter.END)
                                    self.prc_entry.insert(0, str(self.total_prc))
                                else:
                                    print("I dont have item")

                    except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

        def btn2_pressed():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("SELECT item_name FROM Ingredients WHERE id = 102")
                            fetched_prd = cur.fetchone()
                            cur.execute("SELECT quantity FROM Ingredients WHERE id = 102")
                            fetched_qnty = cur.fetchone()

                            if fetched_qnty:
                                for packs_available in fetched_qnty:
                                    packs_avaliable = fetched_qnty[0]
                                    self.available_entry.delete(0, customtkinter.END)
                                    self.available_entry.insert(0, str(packs_available))

                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                            if fetched_prd:
                                        for product_name in fetched_prd:
                                            product_name = fetched_prd[0]
                                    
                                            self.textbox.delete("end", customtkinter.END)
                                            self.textbox.insert("end", f"{product_name}\n")
                            else:
                                print("I dont have it")

                    except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                                cur = db.cursor()

                                cur.execute("SELECT price FROM Ingredients WHERE id = 102")
                                fetched_prc = cur.fetchone()

                                if fetched_prc:
                                    selling_prices1 = fetched_prc[0]
                                    self.textbox2.delete("end", customtkinter.END)
                                    self.textbox2.insert("end", f"{selling_prices1}\n")

                                    self.total_prc += selling_prices1
                                    self.prc_entry.delete(0, customtkinter.END)
                                    self.prc_entry.insert(0, str(self.total_prc))

                                else:
                                    print("I dont have item")

                    except sqlite3.Error as e:
                        print(f"An error ocuured: {e} ")

        def btn3_pressed():
                        try:
                            with sqlite3.connect("burgers_inventory.db") as db:
                                cur = db.cursor()

                                cur.execute("SELECT item_name FROM Ingredients WHERE id = 103")
                                fetched_prd = cur.fetchone()
                                cur.execute("SELECT quantity FROM Ingredients WHERE id = 103")
                                fetched_qnty = cur.fetchone()

                                if fetched_qnty:
                                    for packs_available in fetched_qnty:
                                            packs_available = fetched_qnty[0]
                                            self.available_entry.delete(0, customtkinter.END)
                                            self.available_entry.insert(0, str(packs_available))

                                self.clckd_count += 1
                                self.qnty_entry.delete(0, customtkinter.END)
                                self.qnty_entry.insert(0, str(self.clckd_count))

                                if fetched_prd:
                                            for product_name in fetched_prd:
                                                product_name = fetched_prd[0]
                                                self.textbox.delete("end",  customtkinter.END)
                                                self.textbox.insert("end", f"{product_name}\n")
                                                
                                else:
                                    print("I dont have it")

                        except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

                        try:
                            with sqlite3.connect("burger_inventory.db") as db:
                                    cur = db.cursor()
                                

                                    cur.execute("SELECT price FROM Ingredients WHERE id = 103")
                                    fetched_prc = cur.fetchone()

                                    if fetched_prc:
                                        selling_prices1 = fetched_prc[0]
                                        self.textbox2.delete("end", customtkinter.END)
                                        self.textbox2.insert("end", f"{selling_prices1}\n")

                                        self.total_prc += selling_prices1
                                        self.prc_entry.delete(0, customtkinter.END)
                                        self.prc_entry.insert(0, str(self.total_prc))

                                    else:
                                        print("I dont have item")

                        except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def ddbtn():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()

                    cur.execute("SELECT item_name FROM Ingredients WHERE id = 106")
                    fetched_prd = cur.fetchone()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 106")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_entry.delete(0, customtkinter.END)
                            self.available_entry.insert(0, str(packs_available))

                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                    if fetched_prd:
                        for product_name in fetched_prd:
                                product_name = fetched_prd[0]
                                self.textbox.delete("end",  customtkinter.END)
                                self.textbox.insert("end", f"{product_name}\n")
                        else:
                            print("I dont have it")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()

                        cur.execute("SELECT price FROM Ingredients WHERE id = 106")
                        fetched_prc = cur.fetchone()

                        if fetched_prc:
                                selling_prices1 = fetched_prc[0]
                                self.textbox2.delete("end", customtkinter.END)
                                self.textbox2.insert("end", f"{selling_prices1}\n")

                                self.total_prc += selling_prices1
                                self.prc_entry.delete(0, customtkinter.END)
                                self.prc_entry.insert(0, str(self.total_prc))

                        else:
                                print("I dont have item")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")
        def dd1btn():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()

                    cur.execute("SELECT item_name FROM Ingredients WHERE id = 107")
                    fetched_prd = cur.fetchone()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 107")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_entry.delete(0, customtkinter.END)
                            self.available_entry.insert(0, str(packs_available))

                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                    if fetched_prd:
                        for product_name in fetched_prd:
                                product_name = fetched_prd[0]
                                self.textbox.delete("end",  customtkinter.END)
                                self.textbox.insert("end", f"{product_name}\n")
                        else:
                            print("I dont have it")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()
                        cur.execute("SELECT price FROM Ingredients WHERE id = 107")
                        fetched_prc = cur.fetchone()

                        if fetched_prc:
                                selling_prices1 = fetched_prc[0]
                                self.textbox2.delete("end", customtkinter.END)
                                self.textbox2.insert("end", f"{selling_prices1}\n")

                                self.total_prc += selling_prices1
                                self.prc_entry.delete(0, customtkinter.END)
                                self.prc_entry.insert(0, str(self.total_prc))
                        else:
                                print("I dont have item")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dd2btn():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()

                    cur.execute("SELECT item_name FROM Ingredients WHERE id = 108")
                    fetched_prd = cur.fetchone()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 108")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_entry.delete(0, customtkinter.END)
                            self.available_entry.insert(0, str(packs_available))

                            
                            self.clckd_count += 1
                            self.qnty_entry.delete(0, customtkinter.END)
                            self.qnty_entry.insert(0, str(self.clckd_count))

                    if fetched_prd:
                        for product_name in fetched_prd:
                                product_name = fetched_prd[0]
                                self.textbox.delete("end",  customtkinter.END)
                                self.textbox.insert("end", f"{product_name}\n")
                                                
                        else:
                            print("I dont have it")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()
                        
                        cur.execute("SELECT price FROM Ingredients WHERE id = 108")
                        fetched_prc = cur.fetchone()

                        if fetched_prc:
                                selling_prices1 = fetched_prc[0]
                                self.textbox2.delete("end", customtkinter.END)
                                self.textbox2.insert("end", f"{selling_prices1}\n")

                                self.total_prc += selling_prices1
                                self.prc_entry.delete(0, customtkinter.END)
                                self.prc_entry.insert(0, str(self.total_prc))

                        else:
                                print("I dont have item")

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def ice_cream_clkd():
                
                self.order2_frame = customtkinter.CTkScrollableFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 550, height = 150)
                self.order2_frame.place(rely = 0.66, relx = 0.53)
                self.addbtn = customtkinter.CTkButton(self.order2_frame, text = "order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", width = 10, height = 10, command = ddbtn)
                self.addbtn.configure(text_color = "black")
                self.addbtn.place(relx = 0.02)
                
                self.add1btn = customtkinter.CTkButton(self.order2_frame, text = "order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc",  width = 10, height = 10, command = dd1btn )
                self.add1btn.configure(text_color = "black")
                self.add1btn.pack()
                self.add1btn.place(relx = 0.02, rely = 0.325)

                self.add2btn = customtkinter.CTkButton(self.order2_frame, text = "order",  corner_radius = 13, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc",  width = 10, height = 10, command = dd2btn)
                self.add2btn.configure(text_color = "black")
                self.add2btn.pack()
                self.add2btn.place(relx = 0.02, rely = 0.65)

                try:
                    with sqlite3.connect("burger_inventory.db") as db:
                        cur = db.cursor()
                    cur.execute("SELECT item_name FROM Ingredients WHERE id BETWEEN 106 AND 108")
                    fetched_ice_cream = cur.fetchall()

                    if fetched_ice_cream:
                        for row in fetched_ice_cream:
                            self.ice_cream_ing = customtkinter.CTkLabel(self.order2_frame, text = row)
                            self.ice_cream_ing.pack()
                            self.ice_cream_ing.configure(text_color = "black", text = row)
                    else:
                        print("I don't have items")

                except sqlite3.Error as e:
                    print(f"An error occured: {e}")

        def generate_bill_number():
                name = self.cust_name_entry.get()
                phone = self.cust_num_entry.get()
                seed = name + phone
                random.seed(seed)
                bill_number = random.randint(0, 9999999999)
                formatted_bill_number = f"{bill_number:010d}"

                self.bill_no_entry.configure(text = f"{formatted_bill_number}")
                self.cust_bill_num_entry.configure(text = f"{formatted_bill_number}")

        def cash():
                messagebox.showinfo("Done", "Payment received Thank You!")
                receipt_lines = []

                
                

                with open("receipt.txt", "a") as file:
                    file.write("\nBurgerberg Order Receipt:\n")
                    file.write("\n".join(receipt_lines))
                    file.write(f"\nTotal: R{self.total_prc:}\n")
                    
                    file.write("-" * 30 + "\n")
                    self.prc_entry.delete(0, ctk.END)
                    self.available_entry.delete(0, ctk.END)
                    self.total_prc = 0
                    self.clckd_count = 0
                    self.qnty_entry.delete(0, ctk.END)
                    self.textbox.delete("1.0", ctk.END)
                    self.textbox2.delete("1.0", ctk.END)

        def card_payment():
                self.method_lbl.destroy()
                self.cash_btn.destroy()
                self.card_btn.destroy()

                self.card_lbl = customtkinter.CTkLabel(self.method_frame, text = "Card Number : ",text_color="black")
                self.card_lbl.place(relx = 0.02, rely = 0.25)
                self.card_number = customtkinter.CTkEntry(self.method_frame,fg_color = "white", bg_color = "white", border_width = 2)
                self.card_number.place(relx = 0.225, rely = 0.25)
                self.card_number.configure(text_color = "black")

                self.cvv_number_lbl = customtkinter.CTkLabel(self.method_frame, text = "CVV Number : ", text_color = "black")
                self.cvv_number_lbl.place(relx = 0.02, rely = 0.35)
                self.cvv_number = customtkinter.CTkEntry(self.method_frame, fg_color = "white", bg_color = "white", border_width = 2)
                self.cvv_number.place(relx = 0.225, rely = 0.35)
                self.cvv_number.configure(text_color = "black")

                self.xpry_date_lbl = customtkinter.CTkLabel(self.method_frame, text = "Expiry Date (MM) : ", text_color = "black")
                self.xpry_date_lbl.place(relx = 0.02, rely = 0.45)
                self.xpry_date = customtkinter.CTkEntry(self.method_frame,   fg_color = "white", bg_color = "white", border_width = 2)
                self.xpry_date.place(relx = 0.225, rely = 0.45)
                self.xpry_date.configure(text_color = "black")
                self.xpry_dateYr_lbl = customtkinter.CTkLabel(self.method_frame, text = "Expiry Date(YY) : ", text_color = "black")
                self.xpry_dateYr_lbl.place(relx = 0.02, rely = 0.55)
                self.xpry_dateYr = customtkinter.CTkEntry(self.method_frame,  fg_color = "white", bg_color = "white", border_width = 2)
                self.xpry_dateYr.place(relx = 0.225, rely = 0.55)
                self.xpry_dateYr.configure(text_color = "black")

                def confirm():
                        messagebox.showinfo("Done", "Order Confirmed Thank you")

                self.confirm = customtkinter.CTkButton(self.method_frame, text = "Confirm order", command = confirm)
                self.confirm.place(relx = 0.02, rely = 0.80)

                receipt_lines = []

                        
                

                with open("receipt.txt", "a") as file:
                    file.write("\nBurgerberg Order Receipt:\n")
                    file.write("\n".join(receipt_lines))
                    file.write(f"\nTotal: R{self.total_prc:}\n")
                    
                    file.write("-" * 30 + "\n")

                    self.prc_entry.delete(0, ctk.END)
                    self.available_entry.delete(0, ctk.END)
                    self.total_prc = 0
                    self.clckd_count = 0
                    self.qnty_entry.delete(0, ctk.END)
                    self.textbox.delete("1.0", ctk.END)
                    self.textbox2.delete("1.0", ctk.END)


        def place_order():
                payment_win = ctk.CTkToplevel()
                payment_win.title("Payment")
                payment_win.geometry("1350x850+0+0")
                
                self.bg_payment_frame = customtkinter.CTkFrame(payment_win, fg_color="#efbcbc", bg_color="#efbcbc", corner_radius=0)
                self.bg_payment_frame.pack(fill = BOTH,expand = TRUE)
                self.payment_frame = customtkinter.CTkFrame(self.bg_payment_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
                self.payment_frame.pack(expand = True)

                self.payment_lbl = customtkinter.CTkLabel(self.payment_frame, text = "Payment",  font = ("Areal", 50, "bold"), text_color = "black")
                self.payment_lbl.place(relx = 0.3, rely = 0.02)

                self.method_frame = customtkinter.CTkFrame(self.payment_frame,corner_radius= 10,fg_color="white", bg_color= "#efbcbc", width = 450, height = 250)
                self.method_frame.pack(expand = True)
                self.method_lbl = customtkinter.CTkLabel(self.method_frame, text = "Select Payment Method", font = ("Areal", 15, "bold"), text_color = "black")
                self.method_lbl.place(relx = 0.25, rely = 0.02)
                self.cash_btn = customtkinter.CTkButton(self.method_frame, text="Cash", command = cash)
                self.cash_btn.place(relx = 0.285, rely = 0.3)
                self.card_btn = customtkinter.CTkButton(self.method_frame, text="Card", command = card_payment)
                self.card_btn.place(relx = 0.285, rely = 0.5)

        def ordr2_btn_clicked():
                self.password2_frame.destroy()
                self.mainord_frame = customtkinter.CTkFrame(self.win, fg_color="#efbcbc", bg_color="#efbcbc", corner_radius=0)
                self.mainord_frame.pack(fill = BOTH,expand = TRUE)
                self.ord_frame = customtkinter.CTkFrame(self.mainord_frame, corner_radius= 4,fg_color="white", bg_color= "#efbcbc", width = 1300, height = 800)
                self.ord_frame.pack(expand = True)

                customer_name = StringVar()
                customer_number = StringVar()

                self.ordlbl = customtkinter.CTkLabel(self.ord_frame, text = "Take an order", font = ("Areal", 40))
                self.ordlbl.place(x = 550, rely = 0.098)
                self.ordlbl.configure(text_color = "black")

                self.logotbtn = customtkinter.CTkButton(self.ord_frame, text = "Logout", fg_color = "#efbcbc", bg_color="white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = logout)
                self.logotbtn.place(x = 50, rely = 0.098)

                self.cust_frame = customtkinter.CTkFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 1170, height = 100)
                self.cust_frame.place(rely = 0.19999, relx = 0.06 )

                self.cust_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Details", font = ("Areal", 20) )
                self.cust_lbl.configure(text_color = "black")
                self.cust_lbl.place(relx = 0.43, rely = 0.028)

                self.bill_no_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Bill Number", font = ("Areal", 15))
                self.bill_no_lbl.configure(text_color = "black")
                self.bill_no_lbl.place(relx = 0.02 , rely = 0.31)

                self.bill_no_entry = customtkinter.CTkLabel(self.cust_frame,text = "", fg_color = "white", bg_color = "white")
                self.bill_no_entry.place(relx = 0.1, rely = 0.31)
                self.bill_no_entry.configure(font = ("Areal", 12), text_color = "black")

                self.srch_bill_btn = customtkinter.CTkButton(self.cust_frame, text = "Search", width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = generate_bill_number)
                self.srch_bill_btn.place(relx = 0.23, rely = 0.31)

                self.cust_name_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Name", font = ("Areal", 15))
                self.cust_name_lbl.configure(text_color = "black")
                self.cust_name_lbl.place(relx = 0.41, rely = 0.31)

                self.cust_name_entry = customtkinter.CTkEntry(self.cust_frame,textvariable = customer_name, fg_color = "white", bg_color = "white")
                self.cust_name_entry.place(relx = 0.52, rely = 0.31)
                self.cust_name_entry.configure(font = ("Areal", 12), text_color = "black")

                self.cust_num_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Number", font = ("Areal", 15))
                self.cust_num_lbl.configure(text_color = "black")
                self.cust_num_lbl.place(relx = 0.68, rely = 0.31)

                self.cust_num_entry = customtkinter.CTkEntry(self.cust_frame,textvariable = customer_number, fg_color = "white", bg_color = "white")
                self.cust_num_entry.place(relx = 0.80, rely = 0.31)
                self.cust_num_entry.configure(font = ("Areal", 12), text_color = "black")

                self.prd_frame = customtkinter.CTkFrame(self.ord_frame,  border_width=2, fg_color="white", border_color="black", width = 555, height = 220 )
                self.prd_frame.place(rely = 0.3555, relx = 0.53 )

                self.prd_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Product Order", font = ("Areal", 20))
                self.prd_lbl.configure(text_color = "black")
                self.prd_lbl.place(relx = 0.41, rely = 0.028)

                self.ctgry_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Select Category", font = ("Areal", 15))
                self.ctgry_lbl.configure(text_color = "black")
                self.ctgry_lbl.place(relx = 0.02 , rely = 0.28)

                self.ctgry1_btn = customtkinter.CTkButton(self.prd_frame, text = "Burgers", corner_radius = 0, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = burger_clkd)
                self.ctgry1_btn.place(relx = 0.02, rely = 0.45)
                self.ctgry1_btn.configure(text_color = "black")

                self.ctgry2_btn = customtkinter.CTkButton(self.prd_frame, text = "Ice Cream", corner_radius = 0, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = ice_cream_clkd)
                self.ctgry2_btn.place(relx = 0.02, rely = 0.65)
                self.ctgry2_btn.configure(text_color = "black")

                self.order_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Product",  font = ("Areal", 15))
                self.order_lbl.configure(text_color = "black")
                self.order_lbl.place(relx = 0.68 , rely = 0.28)

                self.order_btn = customtkinter.CTkButton(self.prd_frame,corner_radius = 0,text = "Fries",  fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = fries_clckd)
                self.order_btn.place(relx = 0.68, rely = 0.45)
                self.order_btn.configure(text_color = "black")

                self.bill_frame = customtkinter.CTkFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 585, height = 480)
                self.bill_frame.place(rely = 0.355, relx = 0.06 )

                self.bill_win_lbl = customtkinter.CTkLabel(self.bill_frame, text = "Bill Window", font = ("rockwell", 12))
                self.bill_win_lbl.configure(text_color = "black")
                self.bill_win_lbl.place(relx = 0.45, rely = 0.02)

                self.cmpny_name = customtkinter.CTkLabel(self.bill_frame, text = "BURGERBEG TRUCK SHOP\n UWC MAIN CAMPUS\n TEL NO. 079 333 4543", font = ("rockwell", 12))
                self.cmpny_name.configure(text_color = "black")
                self.cmpny_name.place(relx = 0.36, rely = 0.1)

                self.cust_bill_name = customtkinter.CTkLabel(self.bill_frame, text = "Customer Name:", font = ("rockwell", 11))
                self.cust_bill_name.configure(text_color = "black")
                self.cust_bill_name.place(relx = 0.02, rely = 0.25)

                self.cust_bill_name_entry = customtkinter.CTkEntry(self.bill_frame,textvariable = customer_name, fg_color = "white", bg_color = "white", border_width = 0)
                self.cust_bill_name_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_bill_name_entry.place(relx = 0.165, rely = 0.253)

                self.cust_bill_num = customtkinter.CTkLabel(self.bill_frame, text = "Bill Number:", font = ("rockwell", 11))
                self.cust_bill_num.configure(text_color = "black")
                self.cust_bill_num.place(relx = 0.02, rely = 0.309)

                self.cust_bill_num_entry = customtkinter.CTkLabel(self.bill_frame,text = "", fg_color = "white", bg_color = "white")
                self.cust_bill_num_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_bill_num_entry.place(relx = 0.135, rely = 0.309)

                self.cust_phn = customtkinter.CTkLabel(self.bill_frame, text = "Phone Number:", font = ("rockwell", 11))
                self.cust_phn.configure(text_color = "black")
                self.cust_phn.place(relx = 0.59, rely = 0.25)

                self.cust_phn_entry = customtkinter.CTkEntry(self.bill_frame,textvariable = customer_number, fg_color = "white", bg_color = "white", border_width = 0)
                self.cust_phn_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_phn_entry.place(relx = 0.74, rely = 0.253)

                self.date_lbl = customtkinter.CTkLabel(self.bill_frame, text = "Date:", font = ("rockwell", 11))
                self.date_lbl.configure(text_color = "black")
                self.date_lbl.place(relx = 0.59, rely = 0.309)

                current_date = StringVar()
                current_date = datetime.now().strftime("%Y-%m-%d") 

                self.date_entry = customtkinter.CTkLabel(self.bill_frame,text = current_date, fg_color = "white", bg_color = "white")
                self.date_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.date_entry.place(relx = 0.65, rely = 0.309)

                self.products_frame = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 450, height = 190)
                self.products_frame.place(relx = 0.0231, rely = 0.405)

                self.qnty_frame = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 110, height = 80)
                self.qnty_frame.place(relx = 0.8, rely = 0.405)

                self.prc_frame = customtkinter.CTkFrame(self.products_frame,  border_width=2, fg_color="white", border_color="black", width = 180, height = 170)
                self.prc_frame.place(relx = 0.58, rely = 0.05)

                self.prd_name = customtkinter.CTkLabel(self.products_frame, text = "Products Ordered", font = ("rockwell", 11))
                self.prd_name.configure(text_color = "black")
                self.prd_name.place(relx = 0.35, rely = 0.01)

                self.total = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 110, height = 90)
                self.total.place(relx = 0.8, rely = 0.60)

                self.total_price = customtkinter.CTkLabel(self.total, text = "Total Price", font = ("rockwell", 11))
                self.total_price.place(relx = 0.22, rely = 0.02)
                self.total_price.configure(text_color = "black", font = ("rockwell", 11))

                self.qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Total Quantity",font = ("rockwell", 11))
                self.qnty_lbl.configure(text_color = "black")
                self.qnty_lbl.place(relx = 0.22, rely = 0.02)

                self.qnty_entry = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "white", border_width = 0, width = 40)
                self.qnty_entry.configure(text_color = "black", font = ("rockwell", 11))
                self.qnty_entry.place(relx = 0.35, rely = 0.4)

                self.order_frame = customtkinter.CTkScrollableFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 550, height = 150)
                self.order_frame.place(rely = 0.66, relx = 0.53 )

                self.textbox = customtkinter.CTkTextbox(self.products_frame, width = 200, height = 150, fg_color = "white", font = ("rockwell", 11))
                self.textbox.place(relx = 0.01 , rely = 0.15)
                self.textbox.configure(text_color = "black")

                self.textbox2 = customtkinter.CTkTextbox(self.prc_frame,  width = 150, height = 140, fg_color = "white", font = ("rockwell", 11))
                self.textbox2.place(relx = 0.01 , rely = 0.12)
                self.textbox2.configure(text_color = "black")

                

                self.prc_entry = customtkinter.CTkEntry(self.total,textvariable = total_price,fg_color = "white", bg_color = "white", border_width = 0,  width = 70)
                self.prc_entry.configure(text_color = "black", font = ("rockwell", 11))
                self.prc_entry.place(relx = 0.30, rely = 0.4)

                self.total_prc = 0
                
                self.clckd_count = 0

                self.available_lbl = customtkinter.CTkLabel(self.bill_frame, text = "In Stock(Packs): ", font = ("rockwell", 11))
                self.available_lbl.place(relx = 0.0231, rely = 0.80)
                self.available_lbl.configure(text_color = "black")

                self.available_entry = customtkinter.CTkEntry(self.bill_frame, fg_color = "white", bg_color = "white", border_width = 0, width = 40)
                self.available_entry.place(relx = 0.16, rely = 0.805)
                self.available_entry.configure(text_color = "black", font = ("rockwell", 11))

                self.preview_pricebtn = customtkinter.CTkButton(self.bill_frame, text = "Place Order",  width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = place_order)
                self.preview_pricebtn.place(relx = 0.83, rely = 0.795)

                self.cancel_order_btn = customtkinter.CTkButton(self.bill_frame, text = "Cancel Order", width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = cancel_order)
                self.cancel_order_btn.place(relx = 0.83, rely = 0.85)

        def cancel_order():
                self.prc_entry.delete(0, ctk.END)
                self.available_entry.delete(0, ctk.END)
                self.total_prc = 0
                self.clckd_count = 0
                self.qnty_entry.delete(0, ctk.END)
                self.textbox.delete("1.0", ctk.END)
                self.textbox2.delete("1.0", ctk.END)


        def GenerateMonthlyReports():
            global txtReport
            width = 140
            headingss = "Monthly Report for Food Truck"
            head = f"{headingss:^{width}}"
            Date_of_Report = datetime.now().strftime("%Y-%m-%d")

            Sales = simpledialog.askfloat("Sales", "Enter the sales amount for the current month")
            Sales_Value = str(int(Sales))

            Multiplier = 100 / 120
            Cost_Of_Sales = float(Sales * Multiplier)
            Cost_Of_Sales_Value = str(int(Cost_Of_Sales))

            Gross_Profit = Sales - Cost_Of_Sales
            Gross_Profit_Value = str(int(Gross_Profit))

            Maintainance_Value_Yes = 1500
            Maintainance_Value_No = 0

            Truck_Maintainance = messagebox.askquestion("Does the truck need maintenance?")
            Truck_Maintainance_Value = str(Maintainance_Value_Yes if Truck_Maintainance == 'yes' else Maintainance_Value_No)

            Salaries_And_Wages = simpledialog.askfloat("Salaries And Wages", "Enter the salaries and wages amount for the current month")
            Salaries_And_Wages_Value = str(int(Salaries_And_Wages))

            Labour_Costs = simpledialog.askfloat("Labour Costs", "Enter the labour costs amount for the current month")
            Labour_Costs_Value = str(int(Labour_Costs))

            Operating_Expenses = float(Truck_Maintainance_Value) + float(Salaries_And_Wages_Value) + float(Labour_Costs_Value)
            Operating_Expenses_Value = str(int(Operating_Expenses))

            Total_Expenses = float(Operating_Expenses_Value) + float(Cost_Of_Sales_Value)
            Total_Expenses_Value = str(int(Total_Expenses))

            Net_Profit = Sales - Total_Expenses
            Net_Profit_Value = str(int(Net_Profit))

            txtReport = f"""
            {head}
            Report Date: {Date_of_Report}
            Sales Value: R{Sales_Value}
            Cost Of Sales: R{Cost_Of_Sales_Value}
            Gross Profit: R{Gross_Profit_Value}
            Truck Maintainance: R{Truck_Maintainance_Value}
            Salaries And Wages: R{Salaries_And_Wages_Value}
            Labour Costs: R{Labour_Costs_Value}
            Operating Expenses: R{Operating_Expenses_Value}
            Total Expenses: R{Total_Expenses_Value}
            Net Profit: R{Net_Profit_Value}
            """
            show_report()

        def show_report():
            report_window = ctk.CTkToplevel(self.ord_frame)
            report_window.title("Monthly Report")
            report_window.geometry("700x950")
            main_image = customtkinter.CTkImage(Image.open("Food Tuck MS/Bckgr.png"), size = (1600, 850))
            label1 = customtkinter.CTkLabel(report_window, text = "", bg_color= "grey")
            label1.place(relx = 0, rely = 0)
            label1.configure(image = main_image)
            
            report_label = ctk.CTkLabel(report_window, text=txtReport, justify="left")
            report_label.pack(pady=10)

        def inventory():
            self.admin_lbl.destroy()
            self.invbtn.destroy()
            self.inv_lbl.destroy()
            self.mntly_rprts.destroy()
            self.mntly_lbl.destroy()

            self.menu_frame = customtkinter.CTkFrame(self.ord_frame, border_width = 2, fg_color = "#efbcbc", bg_color = "#efbcbc", width = 400, height = 500) 
            self.menu_frame.place(relx = 0.01, rely = 0.3)

            self.menu_lbl = customtkinter.CTkLabel(self.menu_frame, text = "Menu", font = ("Areal", 20), bg_color = "white", width = 390, corner_radius= 4)
            self.menu_lbl.place(relx = 0.016, rely = 0.02)
            self.menu_lbl.configure(text_color = "black")

            #self.prdct_id = customtkinter.CTkLabel(self.menu_frame, text = "Product ID", font = ("Areal", 15))
            #self.prdct_id.place(relx = 0.03, rely = 0.12)
            #self.prdct_id.configure(text_color = "white")

            #self.prdct_id_Entry = customtkinter.CTkEntry(self.menu_frame, fg_color = "#efbcbc", bg_color = "#efbcbc")
            #self.prdct_id_Entry.place(relx = 0.03, rely = 0.19)
            #self.prdct_id_Entry.configure(text_color = "black")

            #self.srch_prdct = customtkinter.CTkButton(self.ord_frame, text = "Search",  fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", corner_radius = 10)
            #self.srch_prdct.place(relx = 0.15, rely = 0.425)

            self.prdct_optn = customtkinter.CTkLabel(self.menu_frame, text = "Product Options", font = ("Areal", 15))
            self.prdct_optn.place(relx = 0.03, rely = 0.25)
            self.prdct_optn.configure(text_color = "white")

            self.add_prdct = customtkinter.CTkButton(self.menu_frame, text = "Add Product", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", corner_radius = 10, width = 200, command = add_item)
            self.add_prdct.place(relx = 0.03, rely = 0.34)

            self.updt_prdct = customtkinter.CTkButton(self.menu_frame, text = "Update Product", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", corner_radius = 10, width = 200, command = updt_prdcts)
            self.updt_prdct.place(relx = 0.03, rely = 0.45)

            self.dlt_prdct = customtkinter.CTkButton(self.menu_frame, text = "Delete Product",  fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", corner_radius = 10, width = 200, command = delete_prdcts)
            self.dlt_prdct.place(relx = 0.03, rely = 0.55)

            self.exit = customtkinter.CTkButton(self.menu_frame, text = "Exit",fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", corner_radius = 10, width = 95, command = exitbtn)
            self.exit.place(relx = 0.35, rely = 0.90)

            self.prdcts_frame = customtkinter.CTkScrollableFrame(self.ord_frame,  border_width = 2, fg_color = "white", bg_color = "#efbcbc", width = 700, height = 500)
            self.prdcts_frame.place(relx = 0.4, rely = 0.3)

            self.inv_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Inventory Management", font = ("Areal", 50, "bold"), text_color = "white")
            self.inv_lbl.place(relx = 0.3, rely = 0.02)

            load_prdcts()

        def load_prdcts():
            
            try:
                combined_inv = []
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT id, item_name, price, quantity FROM Ingredients")
                    fetched_inv = cur.fetchall()
                    combined_inv.extend(fetched_inv)

                if combined_inv:
                    headers = ["id", "item_name", "price", "quantity"]
                    for col, header in enumerate(headers):
                        customtkinter.CTkLabel(self.prdcts_frame, text = header, font = ("Areal", 12, "bold"), text_color = "black", width = 150, anchor = "w", padx = 5).grid(row = 0, column = col, sticky = "w", padx = (5, 10))
                    for row_index, row in enumerate(combined_inv, start = 1):
                        for col_index, value in enumerate(row):
                            customtkinter.CTkLabel(self.prdcts_frame, text = str(value), text_color = "black", width = 150, anchor = "w", padx = 5).grid(row = row_index,column = col_index, sticky = "w", padx = (5, 10))

                else:
                    print("I dont have")

            except sqlite3.Error as e:
                print(f"An error occcured: {e}")

        
            

        def add1_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Chicken Burger",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 101")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 20

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 20 WHERE id = 101", (20, 101))
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add2_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Beef Burger",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 102")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 20

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 20 WHERE id = 102")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add3_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Vegan Burger",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 103")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 15

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 15 WHERE id = 103")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add4_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Sweet Potato Chips",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 104")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 25

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 25 WHERE id = 104")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add5_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Regular Potato Chips",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 105")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 30

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 30 WHERE id = 105")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add6_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Vanilla Ice Cream",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 106")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 40

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 40 WHERE id = 106")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add7_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Chocolate Ice Cream",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 107")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 40

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 40 WHERE id = 107")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def add8_quantity():
            self.pls1_frame = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.pls1_frame.place(relx = 0.22, rely = 0.3)

            self.pls1_lbl = customtkinter.CTkLabel(self.pls1_frame, text = "Mix(C&V+) Ice Cream",  font = ("Areal", 30, "bold"), text_color = "white")
            self.pls1_lbl.place(relx = 0.35, rely = 0.05)

            self.qnty_frame = customtkinter.CTkFrame(self.pls1_frame, border_width=2, fg_color="#efbcbc", border_color="black", width = 300, height = 180)
            self.qnty_frame.place(relx = 0.305, rely = 0.45)

            self.available_qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Available In Stock", font = ("Areal", 15, "bold"), text_color = "white")
            self.available_qnty_lbl.place(relx = 0.30,rely = 0.05)

            self.available_qnty = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "#efbcbc", border_width = 2, width = 40, text_color = "black")
            self.available_qnty.place(relx = 0.45, rely = 0.205)

            self.sfcnt_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "", text_color="white")
            self.sfcnt_lbl.place(relx = 0.25, rely = 0.35)

            self.pls1 = customtkinter.CTkButton(self.pls1_frame, text = "Add item",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = pls1_btn)
            self.pls1.place(relx = 0.43, rely = 0.35)

            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("SELECT quantity FROM Ingredients WHERE id = 108")
                    fetched_qnty = cur.fetchone()

                if fetched_qnty:
                    for packs_available in fetched_qnty:
                            packs_available = fetched_qnty[0]
                            self.available_qnty.delete(0, customtkinter.END)
                            self.available_qnty.insert(0, str(packs_available))

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

            required_stock = 40

            if packs_available == required_stock:
                self.sfcnt_lbl.configure(text = "The Stock available is sufficient")
                self.pls1.configure(state = DISABLED)
            else:
                self.sfcnt_lbl.configure(text = "Stock needs to be ordered insufficient")

        def pls1_btn():
                    try:
                        with sqlite3.connect("burger_inventory.db") as db:
                            cur = db.cursor()
                            cur.execute("UPDATE Ingredients SET quantity = 40 WHERE id = 108")
                            messagebox.showinfo("Stock", "The Stock is now Sufficient")
                            self.pls1_frame.destroy()
        
                    except sqlite3.Error as e:
                            print(f"An error ocuured: {e} ")

        def updt_prdcts():
            self.updt_frame = customtkinter.CTkFrame(self.ord_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
            self.updt_frame.pack(expand = True)

            self.updt_prdct_lbl = customtkinter.CTkLabel(self.updt_frame, text = "Update Product", font = ("Areal", 50, "bold"), text_color = "white")
            self.updt_prdct_lbl.place(relx = 0.33, rely = 0.02)

            self.updt_prdct_frm = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.updt_prdct_frm.place(relx = 0.22, rely = 0.3)

            self.prdct_name = customtkinter.CTkLabel(self.updt_prdct_frm, text = "Select Product",  font = ("Areal", 20, "bold"))
            self.prdct_name.place(relx = 0.04, rely = 0.20)
            self.prdct_name.configure(text_color = "white")

            self.prd1 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Chicken Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add1_quantity)
            self.prd1.place(relx = 0.04, rely = 0.38)

            self.prd2 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Beef Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add2_quantity)
            self.prd2.place(relx = 0.34, rely = 0.38)

            self.prd3 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Vegan Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add3_quantity)
            self.prd3.place(relx = 0.04, rely = 0.45)

            self.prd4 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Sweet Potato Fries", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add4_quantity)
            self.prd4.place(relx = 0.34, rely = 0.45)

            self.prd5 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Regular Potato Chips", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add5_quantity)
            self.prd5.place(relx = 0.04, rely = 0.52)

            self.prd6 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Vanilla Ice Cream", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add6_quantity)
            self.prd6.place(relx = 0.34, rely = 0.52)

            self.prd7 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Chocolate Ice Cream", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add7_quantity)
            self.prd7.place(relx = 0.04, rely = 0.59)

            self.prd8 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Mix(Choco and Vanilla) Ice Cream",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = add8_quantity)
            self.prd8.place(relx = 0.34, rely = 0.59)

        def dltprdcts1():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 101")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts2():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 102")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts3():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 103")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts4():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 104")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts5():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 105")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts6():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 106")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts7():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 107")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def dltprdcts8():
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("DELETE * FROM Ingredients WHERE id = 108")
                    fetched_qnty = cur.fetchone()

            except sqlite3.Error as e:
                    print(f"An error ocuured: {e} ")

        def delete_prdcts():
            self.updt_frame = customtkinter.CTkFrame(self.ord_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
            self.updt_frame.pack(expand = True)

            self.updt_prdct_lbl = customtkinter.CTkLabel(self.updt_frame, text = "Remove Products", font = ("Areal", 50, "bold"), text_color = "white")
            self.updt_prdct_lbl.place(relx = 0.33, rely = 0.02)

            self.updt_prdct_frm = customtkinter.CTkFrame(self.updt_frame,  border_width=2, fg_color="#efbcbc", border_color="black", width = 680, height = 500)
            self.updt_prdct_frm.place(relx = 0.22, rely = 0.3)

            self.prdct_name = customtkinter.CTkLabel(self.updt_prdct_frm, text = "Select Product",  font = ("Areal", 20, "bold"))
            self.prdct_name.place(relx = 0.04, rely = 0.20)
            self.prdct_name.configure(text_color = "white")

            self.prd1 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Chicken Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts1)
            self.prd1.place(relx = 0.04, rely = 0.38)

            self.prd2 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Beef Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts2)
            self.prd2.place(relx = 0.34, rely = 0.38)

            self.prd3 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Vegan Burger", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts3)
            self.prd3.place(relx = 0.04, rely = 0.45)

            self.prd4 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Sweet Potato Fries", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts4)
            self.prd4.place(relx = 0.34, rely = 0.45)

            self.prd5 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Regular Potato Chips", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts5)
            self.prd5.place(relx = 0.04, rely = 0.52)

            self.prd6 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Vanilla Ice Cream", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts6)
            self.prd6.place(relx = 0.34, rely = 0.52)

            self.prd7 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Chocolate Ice Cream", fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts7)
            self.prd7.place(relx = 0.04, rely = 0.59)

            self.prd8 = customtkinter.CTkButton(self.updt_prdct_frm, text = "Mix(Choco and Vanilla) Ice Cream",  fg_color = "#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = dltprdcts8)
            self.prd8.place(relx = 0.34, rely = 0.59)


        def add(added_item, added_qnty, added_prc):
            try:
                with sqlite3.connect("burger_inventory.db") as db:
                    cur = db.cursor()
                    cur.execute("INSERT INTO Ingredients (item_name, quantity, price) VALUES (?, ?, ?)",
                                (added_item.get(), added_qnty.get(), added_prc.get()))
                    db.commit() 

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")

        def add_item():
            self.updt_frame = customtkinter.CTkFrame(self.ord_frame, corner_radius=4, fg_color="#efbcbc", bg_color="white", width=1300, height=800)
            self.updt_frame.pack(expand=True)

            self.updt_prdct_lbl = customtkinter.CTkLabel(self.updt_frame, text="Add an Item", font=("Areal", 50, "bold"), text_color="white")
            self.updt_prdct_lbl.place(relx=0.33, rely=0.02)

            self.additem_lbl = customtkinter.CTkLabel(self.updt_frame, text="Enter the name of the item", font=("Areal", 15, "bold"), text_color="white")
            self.additem_lbl.place(relx=0.05, rely=0.3)

            added_item = StringVar()
            added_qnty = StringVar()
            added_prc = StringVar()

            self.additem_entry = customtkinter.CTkEntry(self.updt_frame, textvariable=added_item, width=200, corner_radius=4, fg_color="white", font=("Areal", 15))
            self.additem_entry.place(relx=0.05, rely=0.35)
            self.additem_entry.configure(text_color="black")

            self.additem_btn = customtkinter.CTkButton(self.updt_frame, text="Add Item", fg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white",
                                                        command=lambda: add(added_item, added_qnty, added_prc))
            self.additem_btn.place(relx=0.05, rely=0.65)

            self.additem_qnty_lbl = customtkinter.CTkLabel(self.updt_frame, text="Enter the quantity", font=("Areal", 15, "bold"), text_color="white")
            self.additem_qnty_lbl.place(relx=0.05, rely=0.40)

            self.additem_qnty_entry = customtkinter.CTkEntry(self.updt_frame, textvariable=added_qnty, width=200, corner_radius=4, fg_color="white", font=("Areal", 15))
            self.additem_qnty_entry.place(relx=0.05, rely=0.45)
            self.additem_qnty_entry.configure(text_color="black")

            self.additem_prc_lbl = customtkinter.CTkLabel(self.updt_frame, text="Enter the price", font=("Areal", 15, "bold"), text_color="white")
            self.additem_prc_lbl.place(relx=0.05, rely=0.50)

            self.additem_prc_entry = customtkinter.CTkEntry(self.updt_frame, textvariable=added_prc, width=200, corner_radius=4, fg_color="white", font=("Areal", 15))
            self.additem_prc_entry.place(relx=0.05, rely=0.55)
            self.additem_prc_entry.configure(text_color="black")

            self.gobackbtn = customtkinter.CTkButton(self.updt_frame, text = "Back", fg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = goback)
            self.gobackbtn.place(relx = 0.01, rely = 0.05)

        def chckupdts():
            messagebox.showinfo("Updates", "There are no updtes available \n Up to date")
        def about():
                self.admin_lbl.destroy()
                self.invbtn.destroy()
                self.inv_lbl.destroy()
                self.mntly_rprts.destroy()
                self.mntly_lbl.destroy()
                self.aboutus_btn.destroy()
                self.aboutus_lbl.destroy()

                self.menu_frame = customtkinter.CTkFrame(self.ord_frame, border_width = 2, fg_color = "white", bg_color = "#efbcbc", width = 400, height = 300) 
                self.menu_frame.place(relx = 0.01, rely = 0.3)

                self.authors_lbl = customtkinter.CTkLabel(self.menu_frame, text = "Burgerberg would like to acknowledge \n the following as its AUTHORS" + "\n" +
                    "1. Hluma Mahlasela" + "\n" + "2. Lathitha Russia" + "\n" + "3. Ngcebo Ngubane" + "\n" + "4. Vongai Vafana" + "\n" + 
                    "5. Masingta Maswanganye" + "\n" + "6. Nkcubeko Dibela" + "\n", text_color = "black", font = ('Areal', 15, "bold"))
                self.authors_lbl.place(relx = 0.15, rely = 0.09)

                imgFt = customtkinter.CTkImage(Image.open("Food Tuck MS/Pic_for_FT.png"), size = (500, 400))

                self.abtuslbl = customtkinter.CTkLabel(self.ord_frame, text = "About Us", text_color = "white", font = ("Areal", 50, "bold"))
                self.abtuslbl.place(relx = 0.45, rely = 0.05)

                self.imglbl = customtkinter.CTkLabel(self.ord_frame, text = "", corner_radius=10)
                self.imglbl.place(relx = 0.5, rely = 0.2)
                self.imglbl.configure(image =  imgFt)

                self.aboutBB = customtkinter.CTkLabel(self.ord_frame, text = "BurgerBeg has been with customers since 2024 \n Delivering the best meals  puting a smile on peoples face \n We made it our job to do so and we make sure we do our jobe very", font = ("Areal" , 25, "bold"))
                self.aboutBB.place(relx = 0.38, rely = 0.7)
                self.aboutBB.configure(text_color = "white")

                self.chckUpdtsbtn = customtkinter.CTkButton(self.ord_frame, text = "Check for updates", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", width = 150, command = chckupdts)
                self.chckUpdtsbtn.place(relx = 0.11, rely = 0.71)

        def no_order_btnClkd():
            self.password2_frame.destroy()
            self.mainord_frame = customtkinter.CTkFrame(self.win, fg_color="white", bg_color="white", corner_radius=0)
            self.mainord_frame.pack(fill = BOTH,expand = TRUE)
            self.ord_frame = customtkinter.CTkFrame(self.mainord_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
            self.ord_frame.pack(expand = True)

            self.admin_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Admin", font = ("Areal", 50))
            self.admin_lbl.place(relx = 0.44, rely = 0.05)
            self.admin_lbl.configure(text_color = "white")

            image_3 = customtkinter.CTkImage(Image.open("Food Tuck MS/Icon.png"), size = (80, 80))

            self.invbtn = customtkinter.CTkButton(self.ord_frame,image = image_3, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = inventory)
            self.invbtn.place(relx = 0.2, rely = 0.5)
            self.invbtn.configure(image = image_3)

            self.inv_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Inventory", font = ("Areal", 18))
            self.inv_lbl.place(relx = 0.228, rely = 0.645)
            self.inv_lbl.configure(text_color = "white")

            image_4 = customtkinter.CTkImage(Image.open("Food Tuck MS/icon3.png"), size = (80,80))

            self.mntly_rprts = customtkinter.CTkButton(self.ord_frame, image = image_4, text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = GenerateMonthlyReports)
            self.mntly_rprts.place(relx = 0.7, rely = 0.5)
            self.mntly_rprts.configure(image = image_4)

            image_5 = customtkinter.CTkImage(Image.open("Food Tuck MS/istockphoto-1331044109-612x612.jpg"), size = (80, 80))

            self.aboutus_lbl = customtkinter.CTkLabel(self.ord_frame, text = "About Us",  font = ("Areal", 18))
            self.aboutus_lbl.place(relx =  0.48, rely = 0.645)
            self.aboutus_lbl.configure(text_color = "white")

            self.aboutus_btn = customtkinter.CTkButton(self.ord_frame, image = image_5,  text = "", bg_color = "#efbcbc", corner_radius = 30, width = 70, height = 100, fg_color = "white", hover_color = "white", command = about)
            self.aboutus_btn.place(relx = 0.45, rely = 0.5)
            self.aboutus_btn.configure(image = image_5)

            self.mntly_lbl = customtkinter.CTkLabel(self.ord_frame, text = "Montly Reports",  font = ("Areal", 18))
            self.mntly_lbl.place(relx = 0.71, rely = 0.645)
            self.mntly_lbl.configure(text_color = "white")

            self.logoutbtn = customtkinter.CTkButton(self.ord_frame, text = "Logout",  fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = logout)
            self.logoutbtn.place(x = 50, rely = 0.020)

        def reset2():
            password2.set("")

        def employee():
            self.main_frame.destroy()
            self.password_frame = customtkinter.CTkFrame(self.win,border_width= 5, width = 500, height = 300, fg_color= "#efbcbc", bg_color="white", border_color="white", corner_radius=4 )
            self.password_frame.place(x = 530, y = 100)

            self.employee_lbl = customtkinter.CTkLabel(master=self.password_frame, text = "Employee Login", font = ("Areal bold", 30))
            self.employee_lbl.place(relx = 0.31, rely = 0.05)
            self.employee_lbl.configure(text_color = "white")

            self.entr = customtkinter.CTkLabel(self.password_frame, text = "Enter Password : ", font = ("Areal", 15))
            self.entr.place(relx = 0.1, rely = 0.4)
            self.entr.configure(text_color = "white")

            self.pasword_entry = customtkinter.CTkEntry(self.password_frame, width = 200, textvariable = password1, corner_radius=4, fg_color="white", font = ("Areal", 20))
            self.pasword_entry.place(relx = 0.39, rely = 0.4)
            self.pasword_entry.configure(text_color = "black", show = "*")   

            self.logoutbtn = customtkinter.CTkButton(self.win, text = "Back",  fg_color = "#efbcbc", bg_color="white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = logout)
            self.logoutbtn.place(x = 50, rely = 0.020)       

            def reset1():
                password1.set("")

            customer_name = StringVar()
            customer_number = StringVar()

            def generate_bill_number():
                name = self.cust_name_entry.get()
                phone = self.cust_num_entry.get()
                seed = name + phone
                random.seed(seed)
                bill_number = random.randint(0, 9999999999)
                formatted_bill_number = f"{bill_number:010d}"

                self.bill_no_entry.configure(text = f"{formatted_bill_number}")
                self.cust_bill_num_entry.configure(text = f"{formatted_bill_number}")

            def ordbtn_clicked():
                self.password_frame.destroy()
                self.mainord_frame = customtkinter.CTkFrame(self.win, fg_color="#efbcbc", bg_color="#efbcbc", corner_radius=0)
                self.mainord_frame.pack(fill = BOTH,expand = TRUE)
                self.ord_frame = customtkinter.CTkFrame(self.mainord_frame, corner_radius= 4,fg_color="white", bg_color= "#efbcbc", width = 1300, height = 800)
                self.ord_frame.pack(expand = True)

                customer_name = StringVar()
                customer_number = StringVar()

                self.ordlbl = customtkinter.CTkLabel(self.ord_frame, text = "Take an order", font = ("Areal", 40))
                self.ordlbl.place(x = 550, rely = 0.098)
                self.ordlbl.configure(text_color = "black")

                self.logotbtn = customtkinter.CTkButton(self.ord_frame, text = "Logout", fg_color = "#efbcbc", bg_color="white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = logout)
                self.logotbtn.place(x = 50, rely = 0.098)

                self.cust_frame = customtkinter.CTkFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 1170, height = 100)
                self.cust_frame.place(rely = 0.19999, relx = 0.06 )

                self.cust_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Details", font = ("Areal", 20) )
                self.cust_lbl.configure(text_color = "black")
                self.cust_lbl.place(relx = 0.43, rely = 0.028)

                self.bill_no_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Bill Number", font = ("Areal", 15))
                self.bill_no_lbl.configure(text_color = "black")
                self.bill_no_lbl.place(relx = 0.02 , rely = 0.31)

                self.bill_no_entry = customtkinter.CTkLabel(self.cust_frame,text = "", fg_color = "white", bg_color = "white")
                self.bill_no_entry.place(relx = 0.1, rely = 0.31)
                self.bill_no_entry.configure(font = ("Areal", 12), text_color = "black")

                self.srch_bill_btn = customtkinter.CTkButton(self.cust_frame, text = "Search", width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = generate_bill_number)
                self.srch_bill_btn.place(relx = 0.23, rely = 0.31)

                self.cust_name_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Name", font = ("Areal", 15))
                self.cust_name_lbl.configure(text_color = "black")
                self.cust_name_lbl.place(relx = 0.41, rely = 0.31)

                self.cust_name_entry = customtkinter.CTkEntry(self.cust_frame,textvariable = customer_name, fg_color = "white", bg_color = "white")
                self.cust_name_entry.place(relx = 0.52, rely = 0.31)
                self.cust_name_entry.configure(font = ("Areal", 12), text_color = "black")

                self.cust_num_lbl = customtkinter.CTkLabel(self.cust_frame, text = "Customer Number", font = ("Areal", 15))
                self.cust_num_lbl.configure(text_color = "black")
                self.cust_num_lbl.place(relx = 0.68, rely = 0.31)

                self.cust_num_entry = customtkinter.CTkEntry(self.cust_frame,textvariable = customer_number, fg_color = "white", bg_color = "white")
                self.cust_num_entry.place(relx = 0.80, rely = 0.31)
                self.cust_num_entry.configure(font = ("Areal", 12), text_color = "black")

                self.prd_frame = customtkinter.CTkFrame(self.ord_frame,  border_width=2, fg_color="white", border_color="black", width = 555, height = 220 )
                self.prd_frame.place(rely = 0.3555, relx = 0.53 )

                self.prd_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Product Order", font = ("Areal", 20))
                self.prd_lbl.configure(text_color = "black")
                self.prd_lbl.place(relx = 0.41, rely = 0.028)

                self.ctgry_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Select Category", font = ("Areal", 15))
                self.ctgry_lbl.configure(text_color = "black")
                self.ctgry_lbl.place(relx = 0.02 , rely = 0.28)

                self.ctgry1_btn = customtkinter.CTkButton(self.prd_frame, text = "Burgers", corner_radius = 0, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = burger_clkd)
                self.ctgry1_btn.place(relx = 0.02, rely = 0.45)
                self.ctgry1_btn.configure(text_color = "black")

                self.ctgry2_btn = customtkinter.CTkButton(self.prd_frame, text = "Ice Cream", corner_radius = 0, fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = ice_cream_clkd)
                self.ctgry2_btn.place(relx = 0.02, rely = 0.65)
                self.ctgry2_btn.configure(text_color = "black")

                self.order_lbl = customtkinter.CTkLabel(self.prd_frame, text = "Product",  font = ("Areal", 15))
                self.order_lbl.configure(text_color = "black")
                self.order_lbl.place(relx = 0.68 , rely = 0.28)

                self.order_btn = customtkinter.CTkButton(self.prd_frame,corner_radius = 0,text = "Fries",  fg_color = "lightgrey", bg_color = "white", hover_color = "#efbcbc", command = fries_clckd)
                self.order_btn.place(relx = 0.68, rely = 0.45)
                self.order_btn.configure(text_color = "black")

                self.bill_frame = customtkinter.CTkFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 585, height = 480)
                self.bill_frame.place(rely = 0.355, relx = 0.06 )

                self.bill_win_lbl = customtkinter.CTkLabel(self.bill_frame, text = "Bill Window", font = ("rockwell", 12))
                self.bill_win_lbl.configure(text_color = "black")
                self.bill_win_lbl.place(relx = 0.45, rely = 0.02)

                self.cmpny_name = customtkinter.CTkLabel(self.bill_frame, text = "BURGERBEG TRUCK SHOP\n UWC MAIN CAMPUS\n TEL NO. 079 333 4543", font = ("rockwell", 12))
                self.cmpny_name.configure(text_color = "black")
                self.cmpny_name.place(relx = 0.36, rely = 0.1)

                self.cust_bill_name = customtkinter.CTkLabel(self.bill_frame, text = "Customer Name:", font = ("rockwell", 11))
                self.cust_bill_name.configure(text_color = "black")
                self.cust_bill_name.place(relx = 0.02, rely = 0.25)

                self.cust_bill_name_entry = customtkinter.CTkEntry(self.bill_frame,textvariable = customer_name, fg_color = "white", bg_color = "white", border_width = 0)
                self.cust_bill_name_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_bill_name_entry.place(relx = 0.165, rely = 0.253)

                self.cust_bill_num = customtkinter.CTkLabel(self.bill_frame, text = "Bill Number:", font = ("rockwell", 11))
                self.cust_bill_num.configure(text_color = "black")
                self.cust_bill_num.place(relx = 0.02, rely = 0.309)

                self.cust_bill_num_entry = customtkinter.CTkLabel(self.bill_frame,text = "", fg_color = "white", bg_color = "white")
                self.cust_bill_num_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_bill_num_entry.place(relx = 0.135, rely = 0.309)

                self.cust_phn = customtkinter.CTkLabel(self.bill_frame, text = "Phone Number:", font = ("rockwell", 11))
                self.cust_phn.configure(text_color = "black")
                self.cust_phn.place(relx = 0.59, rely = 0.25)

                self.cust_phn_entry = customtkinter.CTkEntry(self.bill_frame,textvariable = customer_number, fg_color = "white", bg_color = "white", border_width = 0)
                self.cust_phn_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.cust_phn_entry.place(relx = 0.74, rely = 0.253)

                self.date_lbl = customtkinter.CTkLabel(self.bill_frame, text = "Date:", font = ("rockwell", 11))
                self.date_lbl.configure(text_color = "black")
                self.date_lbl.place(relx = 0.59, rely = 0.309)

                current_date = StringVar()
                current_date = datetime.now().strftime("%Y-%m-%d") 

                self.date_entry = customtkinter.CTkLabel(self.bill_frame,text = current_date, fg_color = "white", bg_color = "white")
                self.date_entry.configure(font = ("rockwell", 11), text_color = "black")
                self.date_entry.place(relx = 0.65, rely = 0.309)

                self.products_frame = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 450, height = 190)
                self.products_frame.place(relx = 0.0231, rely = 0.405)

                self.qnty_frame = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 110, height = 80)
                self.qnty_frame.place(relx = 0.8, rely = 0.405)

                self.prc_frame = customtkinter.CTkFrame(self.products_frame,  border_width=2, fg_color="white", border_color="black", width = 180, height = 170)
                self.prc_frame.place(relx = 0.58, rely = 0.05)

                self.prd_name = customtkinter.CTkLabel(self.products_frame, text = "Products Ordered", font = ("rockwell", 11))
                self.prd_name.configure(text_color = "black")
                self.prd_name.place(relx = 0.35, rely = 0.01)

                self.total = customtkinter.CTkFrame(self.bill_frame,  border_width=2, fg_color="white", border_color="black", width = 110, height = 90)
                self.total.place(relx = 0.8, rely = 0.60)

                self.total_price = customtkinter.CTkLabel(self.total, text = "Total Price", font = ("rockwell", 11))
                self.total_price.place(relx = 0.22, rely = 0.02)
                self.total_price.configure(text_color = "black", font = ("rockwell", 11))

                self.qnty_lbl = customtkinter.CTkLabel(self.qnty_frame, text = "Total Quantity",font = ("rockwell", 11))
                self.qnty_lbl.configure(text_color = "black")
                self.qnty_lbl.place(relx = 0.22, rely = 0.02)

                self.qnty_entry = customtkinter.CTkEntry(self.qnty_frame, fg_color = "white", bg_color = "white", border_width = 0, width = 40)
                self.qnty_entry.configure(text_color = "black", font = ("rockwell", 11))
                self.qnty_entry.place(relx = 0.35, rely = 0.4)

                self.order_frame = customtkinter.CTkScrollableFrame(self.ord_frame, border_width=2, fg_color="white", border_color="black", width = 550, height = 150)
                self.order_frame.place(rely = 0.66, relx = 0.53 )

                self.textbox = customtkinter.CTkTextbox(self.products_frame, width = 200, height = 150, fg_color = "white", font = ("rockwell", 11))
                self.textbox.place(relx = 0.01 , rely = 0.15)
                self.textbox.configure(text_color = "black")

                self.textbox2 = customtkinter.CTkTextbox(self.prc_frame,  width = 150, height = 140, fg_color = "white", font = ("rockwell", 11))
                self.textbox2.place(relx = 0.01 , rely = 0.12)
                self.textbox2.configure(text_color = "black")

                self.prc_entry = customtkinter.CTkEntry(self.total,fg_color = "white", bg_color = "white", border_width = 0,  width = 70)
                self.prc_entry.configure(text_color = "black", font = ("rockwell", 11))
                self.prc_entry.place(relx = 0.30, rely = 0.4)

                self.total_prc = 0
                self.clckd_count = 0

                self.available_lbl = customtkinter.CTkLabel(self.bill_frame, text = "In Stock(Packs): ", font = ("rockwell", 11))
                self.available_lbl.place(relx = 0.0231, rely = 0.80)
                self.available_lbl.configure(text_color = "black")

                self.available_entry = customtkinter.CTkEntry(self.bill_frame, fg_color = "white", bg_color = "white", border_width = 0, width = 40)
                self.available_entry.place(relx = 0.16, rely = 0.805)
                self.available_entry.configure(text_color = "black", font = ("rockwell", 11))

                self.available2_lbl = customtkinter.CTkLabel(self.bill_frame, text = "In Stock(Pieces per pack): ", font = ("rockwell", 11))
                self.available2_lbl.place(relx = 0.0231, rely = 0.85)
                self.available2_lbl.configure(text_color = "black")

                self.available2_entry = customtkinter.CTkEntry(self.bill_frame,  fg_color = "white", bg_color = "white", border_width = 0, width = 40)
                self.available2_entry.place(relx = 0.255, rely = 0.855)
                self.available2_entry.configure(text_color = "black", font = ("rockwell", 11))

                self.preview_pricebtn = customtkinter.CTkButton(self.bill_frame, text = "Place Order",  width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = place_order)
                self.preview_pricebtn.place(relx = 0.83, rely = 0.795)

                self.cancel_order_btn = customtkinter.CTkButton(self.bill_frame, text = "Cancel Order", width = 20, fg_color = "#efbcbc", bg_color = "white", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = cancel_order)
                self.cancel_order_btn.place(relx = 0.83, rely = 0.85)

            def cancel_order():
                self.prc_entry.delete(0, ctk.END)
                self.available_entry.delete(0, ctk.END)
                self.total_prc = 0
                self.clckd_count = 0
                self.qnty_entry.delete(0, ctk.END)
                self.textbox.delete("1.0", ctk.END)
                self.textbox2.delete("1.0", ctk.END)




            def cash():
                messagebox.showinfo("Done", "Payment received Thank You!")
                receipt_lines = []

                
                

                with open("receipt.txt", "a") as file:
                    file.write("\nBurgerberg Order Receipt:\n")
                    file.write("\n".join(receipt_lines))
                    file.write(f"\nTotal: R{self.total_prc:}\n")
                    
                    file.write("-" * 30 + "\n")
                    self.prc_entry.delete(0, ctk.END)
                    self.available_entry.delete(0, ctk.END)
                    self.total_prc = 0
                    self.clckd_count = 0
                    self.qnty_entry.delete(0, ctk.END)
                    self.textbox.delete("1.0", ctk.END)
                    self.textbox2.delete("1.0", ctk.END)

            def card_payment():
                self.method_lbl.destroy()
                self.cash_btn.destroy()
                self.card_btn.destroy()

                self.card_lbl = customtkinter.CTkLabel(self.method_frame, text = "Card Number : ",text_color="black")
                self.card_lbl.place(relx = 0.02, rely = 0.25)
                self.card_number = customtkinter.CTkEntry(self.method_frame,fg_color = "white", bg_color = "white", border_width = 2)
                self.card_number.place(relx = 0.225, rely = 0.25)
                self.card_number.configure(text_color = "black")

                self.cvv_number_lbl = customtkinter.CTkLabel(self.method_frame, text = "CVV Number : ", text_color = "black")
                self.cvv_number_lbl.place(relx = 0.02, rely = 0.35)
                self.cvv_number = customtkinter.CTkEntry(self.method_frame, fg_color = "white", bg_color = "white", border_width = 2)
                self.cvv_number.place(relx = 0.225, rely = 0.35)
                self.cvv_number.configure(text_color = "black")

                self.xpry_date_lbl = customtkinter.CTkLabel(self.method_frame, text = "Expiry Date (MM) : ", text_color = "black")
                self.xpry_date_lbl.place(relx = 0.02, rely = 0.45)
                self.xpry_date = customtkinter.CTkEntry(self.method_frame,   fg_color = "white", bg_color = "white", border_width = 2)
                self.xpry_date.place(relx = 0.225, rely = 0.45)
                self.xpry_date.configure(text_color = "black")
                self.xpry_dateYr_lbl = customtkinter.CTkLabel(self.method_frame, text = "Expiry Date(YY) : ", text_color = "black")
                self.xpry_dateYr_lbl.place(relx = 0.02, rely = 0.55)
                self.xpry_dateYr = customtkinter.CTkEntry(self.method_frame,  fg_color = "white", bg_color = "white", border_width = 2)
                self.xpry_dateYr.place(relx = 0.225, rely = 0.55)
                self.xpry_dateYr.configure(text_color = "black")

                def confirm():
                        messagebox.showinfo("Done", "Order Confirmed Thank you")

                self.confirm = customtkinter.CTkButton(self.method_frame, text = "Confirm order", command = confirm)
                self.confirm.place(relx = 0.02, rely = 0.80)

                receipt_lines = []

                
                

                with open("receipt.txt", "a") as file:
                    file.write("\nBurgerberg Order Receipt:\n")
                    file.write("\n".join(receipt_lines))
                    file.write(f"\nTotal: R{self.total_prc:}\n")
                    
                    file.write("-" * 30 + "\n")
                    self.prc_entry.delete(0, ctk.END)
                    self.available_entry.delete(0, ctk.END)
                    self.total_prc = 0
                    self.clckd_count = 0
                    self.qnty_entry.delete(0, ctk.END)
                    self.textbox.delete("1.0", ctk.END)
                    self.textbox2.delete("1.0", ctk.END)

            def place_order():
                payment_win = ctk.CTkToplevel()
                payment_win.title("Payment")
                payment_win.geometry("1350x850+0+0")
                
                self.bg_payment_frame = customtkinter.CTkFrame(payment_win, fg_color="#efbcbc", bg_color="#efbcbc", corner_radius=0)
                self.bg_payment_frame.pack(fill = BOTH,expand = TRUE)
                self.payment_frame = customtkinter.CTkFrame(self.bg_payment_frame, corner_radius= 4,fg_color="#efbcbc", bg_color= "white", width = 1300, height = 800)
                self.payment_frame.pack(expand = True)

                self.payment_lbl = customtkinter.CTkLabel(self.payment_frame, text = "Payment",  font = ("Areal", 50, "bold"), text_color = "black")
                self.payment_lbl.place(relx = 0.3, rely = 0.02)

                self.method_frame = customtkinter.CTkFrame(self.payment_frame,corner_radius= 10,fg_color="white", bg_color= "#efbcbc", width = 450, height = 250)
                self.method_frame.pack(expand = True)
                self.method_lbl = customtkinter.CTkLabel(self.method_frame, text = "Select Payment Method", font = ("Areal", 15, "bold"), text_color = "black")
                self.method_lbl.place(relx = 0.25, rely = 0.02)
                self.cash_btn = customtkinter.CTkButton(self.method_frame, text="Cash", command = cash)
                self.cash_btn.place(relx = 0.285, rely = 0.3)
                self.card_btn = customtkinter.CTkButton(self.method_frame, text="Card", command = card_payment)
                self.card_btn.place(relx = 0.285, rely = 0.5)

            


            def login1():
                if password1.get() != "12345678":
                    messagebox.showerror("Login", "The password is incorrect\nTry Again")
                else:
                    password1.get() == "12345678"
                    messagebox.showinfo("Login", "Password is correct")
                    
                    self.ordbtn = customtkinter.CTkButton(self.password_frame, text = "Order",width = 150,fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = ordbtn_clicked )
                    self.ordbtn.place(relx = 0.39, rely = 0.755)

            self.btn = customtkinter.CTkButton(self.password_frame,width=100, text="Login", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command=login1)
            self.btn.place(relx = 0.39, rely = 0.6)
            self.rsbtun = customtkinter.CTkButton(self.password_frame,width=100, text="Reset", fg_color = "#efbcbc", bg_color="#efbcbc", border_color="white", border_width=2, hover_color="#fcf186", text_color="white", command = reset1)
            self.rsbtun.place(relx = 0.66, rely = 0.6)

        self.label1 = customtkinter.CTkLabel(self.win, text = "", bg_color= "grey")
        self.label1.place(relx = 0, rely = 0)
        self.label1.configure(image = main_image)

        self.main_frame = customtkinter.CTkFrame(self.win,border_width= 5, width = 700, height = 600, fg_color= "#efbcbc", bg_color="white", border_color="white", corner_radius=4)
        self.main_frame.place(x = 355, y = 100)        

        self.login_lbl = customtkinter.CTkLabel(self.main_frame, text = "Login As ?", bg_color = "#efbcbc", font = ("Areal", 40))
        self.login_lbl.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.login_lbl.configure(text_color = "white")

        self.orr_lbl = customtkinter.CTkLabel(self.main_frame, text = "OR", font = ("Areal", 15), bg_color="#efbcbc")
        self.orr_lbl.place(relx = 0.4855, rely = 0.53)
        self.orr_lbl.configure(text_color = "white")

        image_1 = customtkinter.CTkImage(Image.open("Food Tuck MS/1.png"), size = (80, 80))

        self.employee_btn = customtkinter.CTkButton(self.main_frame,image = image_1,text = "", bg_color="#efbcbc",corner_radius = 30, width=70, height=70, fg_color="white", hover_color="white", command = employee) 
        self.employee_btn.place(relx = 0.1, rely = 0.5) 
        self.employee_btn.configure(image = image_1)

        image_2 = customtkinter.CTkImage(Image.open("Food Tuck MS/2.png"), size = (80, 80))

        self.employer_btn = customtkinter.CTkButton(self.main_frame, image = image_2, text = "",bg_color="#efbcbc", corner_radius = 30, width = 70, height = 70, fg_color = "white", hover_color = "white", command = employer)
        self.employer_btn.place(relx = 0.7, rely = 0.5)

if __name__ == "__main__":
    main()    

