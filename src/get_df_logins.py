import pandas as pd
def get_logins_from_text():
    with open('logins.txt', 'r') as file:
        logins = file.read()
    text = logins.split(", ")  # разделить по запятым и превратить в список
    df = pd.DataFrame(text, columns=['logins.txt'])

    # Вывод таблицы
    return df

