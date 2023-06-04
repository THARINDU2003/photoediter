from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;.pdf*")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((500, 500))  # Resize the image to fit within a 500x500 window
        photo = ImageTk.PhotoImage(image)
        canvas.config(width=image.width, height=image.height)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.image = photo


def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
    if file_path:
        canvas.postscript(file=file_path + '.eps')
        image = Image.open(file_path + '.eps')
        image.save(file_path)
        image.close()


# Create the main window
window = Tk()
window.title("Photo Editor")

# Create a canvas to display the image
canvas = Canvas(window, bg="white")
canvas.pack(fill=BOTH, expand=YES)

# Create "Open" and "Save" buttons
open_button = Button(window, text="Open", command=open_image)
open_button.pack(side=LEFT, padx=10, pady=10)

save_button = Button(window, text="Save", command=save_image)
save_button.pack(side=LEFT, padx=10, pady=10)

edit_button = Button(window, text="edit", command=save_image)
edit_button.pack(side=LEFT, padx=10, pady=10)

crop_button = Button(window, text="crop", command=save_image)
crop_button.pack(side=LEFT, padx=10, pady=10)

filter_button = Button(window, text="filter", command=save_image)
filter_button.pack(side=LEFT, padx=10, pady=10)

# Run the application
window.mainloop()