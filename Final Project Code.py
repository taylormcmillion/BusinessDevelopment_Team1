from tkinter import *


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("TCU Login")
       
        # Create frame for page 1
        self.page1_frame = Frame(self.master)
        self.page1_frame.pack()
       
        # Load initial image and create label for page 1
        self.page1_photo = PhotoImage(file=r'TcuFirstPage.png')
        self.page1_label = Label(self.page1_frame, image=self.page1_photo)
        self.page1_label.pack()
       
        # Create entry fields for page 1
        self.username_label = Label(self.page1_frame, text="Username", font=("Arial", 14), width=19)
        self.username_label.place(x=215, y=519, height=55)
        self.username_entry = Entry(self.page1_frame, font=("Arial", 14), width=40,)
        self.username_entry.place(x=600, y=642, height=55)
        self.password_label = Label(self.page1_frame, text="Password", font=("Arial", 14), width=19)
        self.password_label.place(x=215, y=645, height=55)
        self.password_entry = Entry(self.page1_frame, font=("Arial", 14), width=40,)
        self.password_entry.place(x=600, y=528, height=55)


        # Create login button for page 1
        self.login_button = Button(self.page1_frame, text="Login", bg="red", fg="white", width=10, height=2, command=self.login)
        self.login_button.place(x=785, y=740)
       
        # Create frame for page 2
        self.page2_frame = Frame(self.master)
       
        # Load image and create label for page 2
        self.page2_photo = PhotoImage(file=r'Page2.png')
        self.page2_label = Label(self.page2_frame, image=self.page2_photo)
        self.page2_label.pack()


    # Function for handling login button press
    def login(self):
        # Get username and password values from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
       
        # Perform login validation here
        # ...
       
        # Remove widgets from page 1
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()
        self.page1_label.pack_forget()
        self.page1_frame.pack_forget()
       
        # Add widgets for page 2
        self.page2_frame.pack()
        self.page2_label.pack()


     # Create entry fields for page 2
        self.go_label = Label(self.master, text="Go!", font=("Arial", 20), width=8)
        self.go_label.place(x=150, y=688, height=30)
        self.field1_entry = Entry(root, font=("Arial", 14), width=15,)
        self.field1_entry.place(x=342, y=510, height=36)
        self.field2_entry = Entry(root, font=("Arial", 14), width=38,)
        self.field2_entry.place(x=344, y=457, height=38)


     # Create "Go" button
        self.go = Button(self.master, text="Go!", font=("Arial", 20), width=8, command=self.go_button_press)
        self.go.place(x=150, y=688, height=30)


     # Clear entry fields
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)


     # Function for handling "Go" button press
    def go_button_press(self):
     # Get values from entry fields
      field1_value = self.field1_entry.get()
      field2_value = self.field2_entry.get()


     # Do something with the values, e.g. print them
      print("Field 1 value:", field1_value)
      print("Field 2 value:", field2_value)


     # Create frame for page 3
      self.page3_frame = Frame(self.master)
      self.page3_frame.pack()


     # Load image and create label for page 3
      self.page3_photo = PhotoImage(file=r'Page3.png')
      self.page3_label = Label(self.page3_frame, image=self.page3_photo)
      self.page3_label.pack()


     # Remove widgets from page 2
      self.go_label.place_forget()
      self.field1_entry.place_forget()
      self.field2_entry.place_forget()
      self.go.place_forget()
      self.page2_label.pack_forget()
      self.page2_frame.pack_forget()


     # Create "Favorites" button
      self.favorites = Button(self.master, text="Save to Favorites", font=("Arial", 14), width=13, command=self.favorites_button_press)
      self.favorites.place(x=160, y=755, height=30)


     # Function for handling "Favorites" button press
    def favorites_button_press(self):
     # Get values from entry fields
      field1_value = self.field1_entry.get()
      field2_value = self.field2_entry.get()


      # Create frame for page 4
      self.page4_frame = Frame(self.master)
      self.page4_frame.pack()


     # Load image and create label for page 4
      self.page4_photo = PhotoImage(file=r'Page4.png')
      self.page4_label = Label(self.page4_frame, image=self.page4_photo)
      self.page4_label.pack()


     # Remove widgets from page 3
      self.page3_label.pack_forget()
      self.page3_frame.pack_forget()


     # Create "Help" button
      self.help = Button(self.master, text="Help!", font=("Arial", 20), width=13, command=self.help_button_press)
      self.help.place(x=302, y=635, height=30)
     # Function for handling "Help" button press
    def help_button_press(self):
     # Get values from entry fields
      field1_value = self.field1_entry.get()
      field2_value = self.field2_entry.get()


root = Tk()
app = LoginWindow(root)
root.mainloop()