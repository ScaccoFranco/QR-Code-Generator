from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import qrcode

class QRGen:
    def __init__(self):

        self.window = Tk()

        # Set the window title
        self.window.title("QR-Code Generator")

        # Set the window geometry
        self.window.geometry("500x300")

        # Set the window widgets
        self.print_window()
        
        # Print the window 
        self.window.mainloop()

    def save_code(self):
        # This function is called to create and save the qr-code from the variable self.image
         
        try:

            # Ask to the user the path to save the image
            new_file = filedialog.asksaveasfilename(
                        initialfile="Untitled",
                        defaultextension=".png", 
                        filetypes=[("JPEG/JPG", "*.jpg"), 
                        ("PNG", "*.png"),
                        ("Tutti i file", "*.*")])

            
            # Create the qr-code image
            self.create()
            
            # Save the image in the previous path
            self.image.save(new_file)

        except Exception as e:
            # If an error occurs print it in a messagebox
            messagebox.showinfo("Error!(1)", e)

        else:
            # If the image has been successful saved print this message
            messagebox.showinfo("Congratulation!", "Your QR-Code has beeen succesfully created!")


    def create(self):
        # This function get called to create an image and saving it in a variable, self.image

        try:
            # set the qr-code structure using the values passsed by the user in the textboxes
            code = qrcode.QRCode(
                version=int(self.codev.get()), # controls the size of the QR Code, from 1 to 40
                error_correction=qrcode.constants.ERROR_CORRECT_H, # error solving
                box_size=int(self.boxsize.get()), # how many pixels each “box” of the QR code is
                border=int(self.border.get()) # how many boxes thick the border should be
            )

            # Set the qr-code content
            code.add_data(self.subject.get())

            # Create the code
            code.make(fit=True)

            # Save the code as an image in the variable self.image
            self.image = code.make_image(fill_color=self.color.get(), back_color=self.bgcolor.get())

        except Exception as e:
            # If an error occurs print it in a messagebox
            messagebox.showinfo("Error!", e)

    def print_window(self):
        # This function is called to create the window widgets

        text_style = ("Helvetica", 12)

        # create frames orntend in the four directions
        topframe = Frame(self.window)
        topframe.pack(side=TOP)

        leftframe = Frame(self.window)
        leftframe.pack(side=LEFT)

        rightframe = Frame(self.window)
        rightframe.pack(side=RIGHT)

        bottomframe = Frame(self.window)
        bottomframe.pack(side=BOTTOM)

        # create lables
        lab1 = Label(topframe, text="Enter variables:", font=text_style)
        lab1.pack(padx=3, pady=3) 

        lab2 = Label(leftframe, text="Code version (1 to 40):", font=text_style)
        lab2.pack(padx=3, pady=3)

        lab3 = Label(leftframe, text="Box size (pixels in a box):", font=text_style)
        lab3.pack(padx=3, pady=3)

        lab4 = Label(leftframe, text="Border (in boxes):", font=text_style)
        lab4.pack(padx=3, pady=3)

        lab5 = Label(leftframe, text="Content:", font=text_style)
        lab5.pack(padx=3, pady=3)

        lab5 = Label(leftframe, text="Color (es. \"black\"):", font=text_style)
        lab5.pack(padx=3, pady=3)

        lab5 = Label(leftframe, text="Background Color (es. \"white\"):", font=text_style)
        lab5.pack(padx=3, pady=3)


        # create textareas

        # Textarea for the code version
        self.codev = StringVar(self.window, value="1")
        codeversion = Entry(rightframe, width = 6, textvariable=self.codev)
        codeversion.pack(padx = 5, pady = 5)

        # Textarea for the size of the boxes 
        self.boxsize = StringVar(self.window, value="10")
        boxsize = Entry(rightframe, width = 6, textvariable=self.boxsize)
        boxsize.pack(padx = 5, pady = 5)

        # Textarea for the dimension of the border
        self.border = StringVar(self.window, value="0")
        border = Entry(rightframe, width = 6, textvariable=self.border)
        border.pack(padx = 5, pady = 5)

        # Textarea for the code content
        self.subject = StringVar(self.window, value="")
        content = Entry(rightframe, width = 20, textvariable=self.subject)
        content.pack(padx = 5, pady = 5)

        # Textarea for the code color
        self.color = StringVar(self.window, value="black")
        color = Entry(rightframe, width = 10, textvariable=self.color)
        color.pack(padx = 5, pady = 5)

        # Textarea for the background color
        self.bgcolor = StringVar(self.window, value="white")
        bgcolor = Entry(rightframe, width = 10, textvariable=self.bgcolor)
        bgcolor.pack(padx = 5, pady = 5)

        # Create button
        create = Button(bottomframe, text="Generate Code", font=text_style, width=30, command=self.save_code)
        create.pack(padx = 5, pady = 5)

if __name__ == "__main__":
    qr = QRGen()