import os
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
    tree = os.walk('for_recognition')
    for i in tree:
        l.append(list(i))
    l = [f'for_recognition/{i}' for i in l[0][2]]
    return l

print(get_dict_of_samples())
