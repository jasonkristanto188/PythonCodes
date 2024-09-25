import pandas as pd
import os

def get_data(userinput):
    if int(userinput) == 1:
        sheetname = 'CCC'
    elif int(userinput) == 2:
        sheetname = 'BS'

    path = r"D:\Users\jason.kristanto\PycharmProjects\CondaProjects\chatbot\functions\panduan_treasury\List Pertanyaan Finance Treasury.xlsx"
    df = pd.read_excel(path, sheet_name=sheetname)
    df.columns = df.iloc[1]
    df = df.iloc[2:]
    df.reset_index(drop=True, inplace=True)
    return df

def generate_panduan_treasury_questions(userinput):
    os.system('cls') if os.name == 'nt' else os.system('clear')

    df = get_data(userinput)

    questionstr = f'Tekan angka 1-{len(df)} untuk mendapatkan jawaban yang diinginkan\n'
    for index, row in df.iterrows():
        questionstr += f"{row['No']}. {row['Pertanyaan']}\n"
    return questionstr + 'Enter: '

def generate_panduan_treasury_response(userinput, answer):
    os.system('cls') if os.name == 'nt' else os.system('clear')
    df = get_data(userinput)
    
    return f"{df.loc[int(answer) - 1, 'Pertanyaan']}\n\n{df.loc[int(answer) - 1, 'Jawaban']}\n\n"

