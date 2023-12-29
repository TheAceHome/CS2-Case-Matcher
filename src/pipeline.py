from PIL import Image
import pandas as pd
from src.get_df_logins import get_logins_from_text
from src.image_crop import crop_main_image, get_all_images
from src.image_recognition import get_match
from src.delete_old_pics import clear_for_recog
import os

def full_pipeline():
    print(os.getcwd())
    try:
        os.chdir('CS2-Case-Matcher')
        get_all_images()
        df = get_logins_from_text()
        cases = get_match()
        try:
            df['Кейсы'] = cases
            if not os.path.exists("out.txt"):
                pass
            else:
                old_df = pd.read_csv("out.txt", sep=' ')
                df = pd.concat([old_df, df])
            df.to_csv("out.txt", index=False, sep=' ')
            # clear_for_recog()
            # os.rmdir('for_recognition')
        except:
            print("Найдены новые варианты кейсов, добавьте папки")
    except:
        # os.rmdir('for_recognition')
        print("Found error. Delete try, except and look for it")