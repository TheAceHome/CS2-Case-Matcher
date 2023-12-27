import pandas as pd
import numpy as np
import cv2
import warnings
warnings.simplefilter("ignore", UserWarning)
import os
os.chdir(os.path.dirname(os.getcwd()))
print(os.getcwd())

# img1 = cv2.imread('70.jpg', 0)
# img2 = cv2.imread('140.jpg', 0)


def get_percentage(img1, img2):
    res = cv2.absdiff(img1, img2)
    res = res.astype(np.uint8)
    percentage = (np.count_nonzero(res) * 100)/ res.size
    return percentage

def mse(img1, img2):
    h, w = img1.shape
    diff = cv2.absdiff(img1, img2)
    error = np.sum(diff ** 2) / (h * w)
    return error

def percentage_differ(image1,image2):
    image1 = cv2.resize(image1, (0, 0), fx=0.5, fy=0.5)
    image2 = cv2.resize(image2, (0, 0), fx=0.5, fy=0.5)
    difference = cv2.absdiff(image1, image2)

    _, difference_binary = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    total_pixels = difference_binary.shape[0] * difference_binary.shape[1]
    non_zero_pixels = np.count_nonzero(difference_binary)
    percent_diff = (non_zero_pixels / total_pixels) * 100

    return percent_diff

# error = mse(img1, img2)
# perc = get_percentage(img1, img2)
# percentage_difference = percentage_differ(img1, img2)
# print("Image matching Error between the two images:", error)
# print("Image matching Percentage between the two images:", perc)
# print(f'The percentage of difference is {percentage_differ}%')

def get_dict_of_samples():
    base_wd = os.getcwd()
    l = []
    d = {}
    tree = os.walk('images')
    for i in tree:
        l.append(list(i))

    for i in range(0, len(l)-1):
        name_of_case = l[0][1][i]
        list_os_samples = l[1+i][2]
        if os.getcwd() != base_wd:
            os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
        else:
            pass
        os.chdir(f'images/{l[0][1][i]}')
        d[name_of_case] = list_os_samples
    return d

def get_list_of_recog():
    l = []
    os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    tree = os.walk('for_recognition')
    for i in tree:
        l.append(list(i))
    l = sorted([f'{i}' for i in l[0][2]])
    return l

def get_match():
    list_of_cases=[]
    dict_of_samples = get_dict_of_samples()
    list_of_recog = get_list_of_recog()

    for i in range(0,len(list_of_recog)):
        for j in range(0,len(dict_of_samples)):

            os.chdir(f'for_recognition')
            img1 = cv2.imread(list_of_recog[i], 0)
            f1=list_of_recog[i]
            os.chdir(os.path.dirname(os.getcwd()))

            os.chdir(f'images/{list(dict_of_samples.keys())[j]}')
            for k in dict_of_samples[list(dict_of_samples.keys())[j]]:
                img2 = cv2.imread(k, 0)
                percent_diff = percentage_differ(img1, img2)
                if percent_diff <0.1:
                    list_of_cases.append(list(dict_of_samples.keys())[j])

            os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    return list_of_cases



