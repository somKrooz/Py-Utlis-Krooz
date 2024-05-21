from PIL import Image, ImageDraw, ImageFont

def CreateThumbnail(file, title, size):
    # Open the image
    img = Image.open(file)
    draw = ImageDraw.Draw(img)
    font_path = "arial.ttf"  
    font_size = size * 5  
    font = ImageFont.truetype(font_path, font_size)
    
    text_bbox = draw.textbbox((0, 0), title, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    image_width, image_height = img.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2
    # Draw the text on the image
    draw.text((x, y), title, font=font, fill="white")
    
    return img