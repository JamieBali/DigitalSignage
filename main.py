import tkinter as tk
import random, os, time, sys
from PIL import Image, ImageTk

first = True

try:
    imgDisplayTime = int(sys.argv[1])
except:
    imgDisplayTime = 120

try:
    datapath = sys.argv[2]
except:
    datapath = ".\\"

photo = False

def get_image():
    # Randomly select an image path
    image_path = random.choice(os.listdir(datapath))

    # Load the image using PIL
    # We have to append the storage machine path again as the random.choice only returns the file name.
    image = Image.open(datapath + image_path)
    iw = image.width
    ih = image.height
    h = root.winfo_screenheight()
    ratio = iw / ih                 # Calculate ratio to ensure image doesn't get stretched
    w = int(ratio * h)
    image = image.resize((w, h))    # Resize the image if needed
    photo = ImageTk.PhotoImage(image)

    return photo

def display_image():
    global photo

    if (photo == False):
        photo = get_image()

    root.deiconify()
    
    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.pack()        

    # Display the image for a given number of seconds (currently 2 mins)
    root.update()
    time.sleep(imgDisplayTime) # this is a time in seconds
    
    photo = get_image()

    # Remove the image label
    image_label.destroy()

    # Schedule the display_image immediately, as the last image just got destroyed.
    root.after(0, display_image)

# Create the main window
root = tk.Tk()
root.title("Digital Signage")
root.geometry("400x300")
root.attributes('-fullscreen', True)

photo = False

# Start signage
display_image()

# Keep the window open
root.mainloop()
