import qrcode
from PIL import Image, ImageTk
import tkinter as tk

# Create a QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("https://matias.me/nsfw/?fbclid=PAZXh0bgNhZW0CMTEAAaZwzkNkzycQFSD_wxhwTaBsOkaYaUnZnGBd3e1Kn0ht1LDiCLOlrvjfzIo_aem_k4Zpj18rhzISXbgwe6TKPw")
qr.make(fit=True)

# Generate the QR code image with custom colors
img = qr.make_image(fill_color="pink", back_color="black")

# Save the QR code image to a file
img.save("vid_web.png")

# Create a Tkinter window
root = tk.Tk()
root.title("QR Code")

# Convert the image to a Tkinter-compatible format
tk_image = ImageTk.PhotoImage(img)

# Create a label to display the image in the window
label = tk.Label(root, image=tk_image)
label.pack()

# Start the Tkinter event loop
root.mainloop()

print("QR code generated, saved as 'vid_web.png', and displayed in a Tkinter window!")
