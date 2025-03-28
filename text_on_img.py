from PIL import Image,ImageDraw,ImageFont

image = Image.open("Images/leopard.jpg")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("redisplayed.ttf", 30)

text = "Hello World"

bbox = draw.textbbox((0,0),text,font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
image_width, image_height = image.size
x = (image_width - text_width) / 2
y = (image_height - text_height) / 2

draw.text((x, y), text, fill = "black", font = font)

image.show()
image.save("Images/text_on_img.jpg")