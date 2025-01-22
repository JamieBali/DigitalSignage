import tkinter as tk
import random
import os
import time
from PIL import Image, ImageTk

first = True

def get_image():
    # Randomly select an image path
    image_path = random.choice(os.listdir("\\\\[Storage Machine IP]\\Shared\\DigitalSignage\\"))

    # Load the image using PIL
    # We have to append the storage machine path again as the random.choice only returns the file name.
    image = Image.open("\\\\[Storage Machine IP]\\Shared\\DigitalSignage\\" + image_path)
    iw = image.width
    ih = image.height
    h = root.winfo_screenheight()
    ratio = iw / ih                 # Calculate ratio to ensure image doesn't get stretched
    w = int(ratio * h)
    image = image.resize((w, h))    # Resize the image if needed
    photo = ImageTk.PhotoImage(image)

    return photo

def display_image(photo):

    if (photo == False):
        photo = get_image()

    root.deiconify()
    
    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.pack()        

    # Display the image for a given number of seconds (currently 2 mins)
    root.update()
    time.sleep(2) # this is a time in seconds
    
    photo = get_image()

    # Remove the image label
    image_label.destroy()

    # Schedule the display_image immediately, as the last image just got destroyed.
    root.after(0, display_image(photo))

# Create the main window
root = tk.Tk()
root.title("Digital Signage")
root.geometry("400x300")
root.attributes('-fullscreen', True)

# Start signage
display_image(False)

# Keep the window open
root.mainloop()
