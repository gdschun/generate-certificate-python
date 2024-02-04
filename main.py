import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog

def select_file(name_of_window):

        filename = filedialog.askopenfilename(title=f"{name_of_window}")
        return filename
def select_folder():
        foldername = filedialog.askdirectory(title="save locatio")
        return foldername

def generate_certificate(names, positions, font_of_name, image):
     save_location =select_folder()   
     os.chdir(rf"{save_location}")
     for n, p in zip(names, positions):
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        w,h=draw.textsize(n,font_of_name)
        draw.text(((img_pil.width-w)//2, 2200), n, font=font_of_name, fill=(0, 0, 0))
        # draw.text((,), p, font=font_of_rule, fill=(0, 0, 0))
        image_new = np.array(img_pil)
        cv2.imwrite(f"certificate for {n}.png", image_new)

        

certificate_teamplate_path=select_file("select certificate teamplate")
image = cv2.imread(rf"{certificate_teamplate_path}")
Excel_sheet_path=select_file("select Excel sheet")
sheet = pd.read_excel(rf"{Excel_sheet_path}")
names = list(sheet["name"])
positions = list(sheet["position"])

# position_of_name = cv2.selectROI("select name of participant", image)
# position_of_rule = cv2.selectROI("select rule of participant", image)
cv2.destroyAllWindows()
font_path=select_file("select Font")
font_of_name = ImageFont.truetype(rf"{font_path}", 300)
# font_of_rule = ImageFont.truetype(r"C:\Users\victo\OneDrive\Desktop\certificate_generator_python\fonts\times new roman.ttf", 20)

generate_certificate(names, positions, font_of_name, image)
