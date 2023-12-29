import os
def crop_main_image(image):
    # Обрезаем изображение по количеству пикселей
    # Получаем размеры изображения
    os.mkdir('for_recognition')
    width, height = image.size
    i = 0
    k=0
    while i < height:
        # Обрезаем изображение
        cropped_image = image.crop((15, i, width-240, height-((height-70)-i)-30))

        # Сохраняем обрезанное изображение
        cropped_image.save(f'for_recognition/{k}.jpg')
        i+=70
        k+=1




