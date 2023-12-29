import os
def clear_for_recog():
    tree = os.walk('for_recognition')
    for i in tree:
        for j in i[2]:
            os.chdir(f'for_recognition')
            os.remove(f"{j}")
            os.chdir(os.path.dirname(os.getcwd()))
    return print("Folder for_recongition cleared")