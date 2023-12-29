from PIL import Image
import pandas as pd
from src.get_df_logins import get_logins_from_text
from src.image_crop import crop_main_image
from src.image_recognition import get_match
from src.delete_old_pics import clear_for_recog
import os
os.chdir(f'CS2-Case-Matcher')



logins = """sgfjr50, philippe2002, du6aetheinge, mabaol, 178013049, shelby65pahl"""
image = Image.open('image.jpg')



df = get_logins_from_text(logins)
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
os.rmdir('for_recognition')
