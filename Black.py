import os
from PIL import Image

def make_white_transparent_and_black(img):
    datas = img.getdata()

    new_data = []
    for item in datas:
        # change all white (also shades of whites) pixels to transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((0, 0, 0, 255))  # change non-white pixels to black

    img.putdata(new_data)
    return img

def resize_and_add_image_to_multiple(bg_img_folder, overlay_img_path):
    try:
        overlay_img = Image.open(overlay_img_path).convert("RGBA")
        overlay_img = make_white_transparent_and_black(overlay_img)

        for bg_img_name in os.listdir(bg_img_folder):
            bg_img_path = os.path.join(bg_img_folder, bg_img_name)

            bg_img = Image.open(bg_img_path).convert("RGBA")

            overlay_img_width = int(bg_img.width / 8)  
            overlay_img_height = int(overlay_img.height * (overlay_img_width / overlay_img.width))

            overlay_img_resized = overlay_img.resize((overlay_img_width, overlay_img_height))

            x_offset = y_offset = 1  # change these values as needed
            position = (bg_img.width - overlay_img_width - x_offset, bg_img.height - overlay_img_height - y_offset)

            temp_img = Image.new('RGBA', bg_img.size)
            temp_img.paste(overlay_img_resized, position)

            bg_img = Image.alpha_composite(bg_img, temp_img)

            bg_img.save(bg_img_path)

            print(f"Image saved at {bg_img_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

resize_and_add_image_to_multiple(r"File Location where you want Images To be Changed", " Signature.png")
