from PIL import Image

img = Image.open("Images/leopard.jpg")

img2 = img.convert("L")

img2.save("Images/black_and_white_pic.jpg")

