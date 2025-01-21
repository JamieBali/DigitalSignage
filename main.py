import tkinter as tk
import random
import os
import time
from PIL import Image, ImageTk

def flash_image():
    root.deiconify()
    # Randomly select an image path
    image_path = random.choice(os.listdir())

    print(image_path)

    # Load the image using PIL
    image = Image.open(image_path)
    iw = image.width
    ih = image.height
    h = root.winfo_screenheight()
    ratio = iw / ih
    w = int(ratio * h)
    image = image.resize((w, h))  # Resize the image if needed
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.pack()

    # Display the image for 2 seconds
    root.update()
    time.sleep(2)

    # Remove the image label
    image_label.destroy()

    root.withdraw()

    # Schedule the next flash after 10 seconds
    root.after(1, flash_image)

# Create the main window
root = tk.Tk()
root.title("Image Flasher")
root.geometry("400x300")
root.attributes('-fullscreen', True)

# Start the flashing process
flash_image()

# Keep the window open
root.mainloop()
