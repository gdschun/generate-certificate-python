import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import os

def generate_certificate(names, positions, position_of_name, position_of_rule, font_of_name, font_of_rule, image):
     i = 0
     os.chdir(r"C:\Users\victo\OneDrive\Desktop\certificate_generator_python\output")
     for n, p in zip(names, positions):
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        draw.text((221, 412), n, font=font_of_name, fill=(0, 0, 0))
        # draw.text((position_of_rule[0], position_of_rule[1]), p, font=font_of_rule, fill=(0, 0, 0))
        image_new = np.array(img_pil)
        cv2.imwrite(f"certificate for {n}.jpg", image_new)
        cv2.waitKey(2000)
        i += 1

        

  
image = cv2.imread(r"C:\Users\victo\OneDrive\Desktop\certificate-generator\certificate teamplate\certificate.png")
sheet = pd.read_excel(r"C:\Users\victo\OneDrive\Desktop\certificate_generator_python\excel\mobile bootcamp.xlsx")
names = list(sheet["name"])
positions = list(sheet["position"])

position_of_name = cv2.selectROI("select name of participant", image)
# position_of_rule = cv2.selectROI("select rule of participant", image)
cv2.destroyAllWindows()

font_of_name = ImageFont.truetype(r"C:\Users\victo\OneDrive\Desktop\certificate_generator_python\fonts\times new roman bold italic.ttf", 30)
font_of_rule = ImageFont.truetype(r"C:\Users\victo\OneDrive\Desktop\certificate_generator_python\fonts\times new roman.ttf", 20)

generate_certificate(names, positions, position_of_name, position_of_rule, font_of_name, font_of_rule, image)
