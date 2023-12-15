from tkinter import *

def create_dashboard():
    window = Tk()
    window.title("Dashboard Monitoring")
    window.geometry('500x440')  # Width, Height
    window.resizable(False, False)  # Width, Height
    window.configure(bg="white")

    # Header image
    canvas_header = Canvas(window, width=500, height=100)
    canvas_header.place(x=0, y=0)
    img_header = PhotoImage(file="head_img.png")
    canvas_header.create_image(0, 0, anchor=NW, image=img_header)

    # Lamp image
    canvas_lamp = Canvas(window, width=200, height=200)
    canvas_lamp.place(x=150, y=100)
    img_lamp = PhotoImage(file="lamp_img.png")
    canvas_lamp.create_image(0, 0, anchor=NW, image=img_lamp)

    # Temperature image
    canvas_temp = Canvas(window, width=200, height=200)
    canvas_temp.place(x=50, y=250)
    img_temp = PhotoImage(file="temp_img.png")
    canvas_temp.create_image(0, 0, anchor=NW, image=img_temp)

    # Humidity image
    canvas_humidity = Canvas(window, width=200, height=200)
    canvas_humidity.place(x=250, y=250)
    img_humidity = PhotoImage(file="humidity_img.png")
    canvas_humidity.create_image(0, 0, anchor=NW, image=img_humidity)

    # Label °C
    temp_label = Label(window,
        text=" °C",
        bg="white",
        fg="black",
        font=("Helvetica", 20))
    temp_label.place(x=150, y=400)

    # Label %
    humidity_label = Label(window,
        text="%",
        bg="white",
        fg="black",
        font=("Helvetica", 20))
    humidity_label.place(x=350, y=400)

    window.mainloop()

if __name__ == "__main__":
    create_dashboard()
