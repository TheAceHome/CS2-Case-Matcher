import pandas as pd
def get_logins_from_text(txt):
    text = txt.split(", ")  # разделить по запятым и превратить в список
    df = pd.DataFrame(text, columns=['logins'])

    # Вывод таблицы
    return df

