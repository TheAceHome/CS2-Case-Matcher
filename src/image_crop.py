import os
def crop_main_image(image):
    # Обрезаем изображение по количеству пикселей
    # Получаем размеры изображения
    width, height = image.size
    i = 0
    k=0
    while i < 700:

        # Обрезаем изображение
        cropped_image = image.crop((15, i, width-240, height-(630-i)-30))

        # Сохраняем обрезанное изображение
        cropped_image.save(f'for_recognition/{k}.jpg')
        i+=70
        k+=1

