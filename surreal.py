from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

root = Tk()
root.title("Photo Editor")
root.geometry("640x640")

def selected():
    global img_path, img, img1
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    img.thumbnail((350,350))
    img1 = ImageTk.PhotoImage(img)
    canvas.create_image(300,210,image=img1)
    canvas.image=img1
    
def blur(event):
    global img_path, img1, imgg
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    imgg = img.filter(ImageFilter.BoxBlur(float(event)))
    img1 = ImageTk.PhotoImage(imgg) 
    canvas.create_image(300, 210, image=img1)
    canvas.image=img1
    
def brightness(event):
    global img_path, img2, img3
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    imgg = ImageEnhance.Brightness(img)
    img2 = imgg.enhance(float(event))
    img3 = ImageTk.PhotoImage(img2)
    canvas.create_image(300, 210, image=img3)
    canvas.image=img3
    
def flip_img(event):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350,350))
    
    if flip.get() == 'LEFT TO RIGHT':
        img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip.get() == 'TOP TO BOTTOM':
        img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    canvas.create_image(300, 210, image=img9)
    canvas.image = img9
    
def rotate_img(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350,350))
    
    if rotate.get() == '90':
        img10 = img.transpose(Image.ROTATE_90)
    elif rotate.get() == '180':
        img10 = img.transpose(Image.ROTATE_180)
    elif rotate.get() == '270':
        img10 = img.transpose(Image.ROTATE_270)
    img11 = ImageTk.PhotoImage(img10)
    canvas.create_image(300, 210, image=img11)
    canvas.image = img11
    
def border_img(event):
    global img_path, img12, img13
    img = Image.open(img_path)
    img.thumbnail((350,350))
    img12 = ImageOps.expand(img, border = int(addborder.get()))
    img13 = ImageTk.PhotoImage(img12)
    canvas.create_image(300, 210, image=img13)
    canvas.image = img13

def mono(event=0):
    global img_path, img14, img15
    img = Image.open(img_path)
    img.thumbnail((350,350))
    img14 = img.convert('L')
    img15 = ImageTk.PhotoImage(img14)
    canvas.create_image(300, 210, image=img15)
    canvas.image = img15
    
def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    
def placeholder():
    pass

Label(root, text='Blur:', font="ariel 17 bold").place(x=145, y=8)
blur = ttk.Scale(root, from_=0, to=10, variable=IntVar(), orient=HORIZONTAL, command=blur)
blur.place(x=210, y=12)
blur.set(1)

Label(root, text='Brightness:', font="ariel 17 bold").place(x=70, y=50)
brightness = ttk.Scale(root, from_=0, to=10, variable=DoubleVar(), orient=HORIZONTAL, command=brightness)
brightness.place(x=210, y=55)
brightness.set(1)

Label(root, text='Monochromatize:', font="ariel 17 bold").place(x=10, y=92)
mono = Checkbutton(root, variable=IntVar(), command=mono)
mono.place(x=210, y=100)

Label(root, text='Flip:', font="ariel 17 bold").place(x=400, y=8)
flip = ttk.Combobox(root, values=['LEFT TO RIGHT', 'TOP TO BOTTOM'], font="ariel 10 bold")
flip.place(x=460, y=14)
flip.bind("<<ComboboxSelected>>", flip_img)

Label(root, text='Rotate:', font="ariel 17 bold").place(x=370, y=50)
rotate = ttk.Combobox(root, values=[90,180,270], font="ariel 10 bold")
rotate.place(x=460, y=55)
rotate.bind("<<ComboboxSelected>>", rotate_img)

Label(root, text='Add Border:', font="ariel 17 bold").place(x=316, y=92)
addborder = ttk.Combobox(root, values=[10,15,20,25,30,35,40], font="ariel 10 bold")
addborder.place(x=460, y=100)
addborder.bind("<<ComboboxSelected>>", border_img)

canvas = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas.place(x=15, y=150)

Button(root, text="Select Image", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected).place(x=65, y=587)
Button(root, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=placeholder).place(x=245, y=587)
Button(root, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy).place(x=425, y=587)

mainloop()