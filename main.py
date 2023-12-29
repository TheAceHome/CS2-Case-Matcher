from PIL import Image
import pandas as pd
from src.get_df_logins import get_logins_from_text
from src.image_crop import crop_main_image
from src.image_recognition import get_match
from src.delete_old_pics import clear_for_recog
import os
os.chdir(f'CS2-Case-Matcher')
print(os.getcwd())



text = """[smbdidknw] Selected drops on: login1, login2, login3, login4, login5, login6, login7, login8, login9, login10"""
image = Image.open('image.jpg')




df = get_logins_from_text(text)
crop_main_image(image)
cases = get_match()
df['Кейсы'] = cases
if not os.path.exists("out.xlsx"):
    pass
else:
    old_df = pd.read_excel("out.xlsx")
    df = pd.concat([old_df, df])
df.to_excel("out.xlsx", index=False)
clear_for_recog()
