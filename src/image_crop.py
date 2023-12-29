import os
from PIL import Image
from src.delete_old_pics import clear_for_recog
def crop_main_image(image):
    # Обрезаем изображение по количеству пикселей
    # Получаем размеры изображения
    if os.path.exists('for_recognition')!= True:
        os.mkdir('for_recognition')
        k=0
    else:
        os.chdir('for_recognition')
        k = int(sorted(os.listdir(), key=lambda x: int(x.split('.')[0]))[-1].replace(".jpg",""))+1
        os.chdir(os.path.dirname(os.getcwd()))

    width, height = image.size
    i = 0
    while i < height:
        # Обрезаем изображение
        cropped_image = image.crop((15, i, width-240, height-((height-70)-i)-30))

        # Сохраняем обрезанное изображение
        cropped_image.save(f'for_recognition/{k}.jpg')
        i+=70
        k+=1

def get_all_images():
    # os.chdir('CS2-Case-Matcher')
    try:
        clear_for_recog()
        os.rmdir('for_recognition')
    except:
        pass
    tree = os.walk('origin_images')
    for i in tree:
        for j in i[2]:
            os.chdir('origin_images')
            image = Image.open(j)
            os.chdir(os.path.dirname(os.getcwd()))
            crop_main_image(image)
    return 1

