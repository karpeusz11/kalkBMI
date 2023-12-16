import openpyxl
import pandas as pd
import numpy as np

def BMI(waga, wzrost):
    return waga / (wzrost / 100)  2

def main():
        df = pd.read_excel(r"C:\Users\DELL\Downloads\XD (1).xlsx")
        df['BMI'] = df['Waga'] / (df['Wzrost'] / 100)  2
        print(df[['Waga', 'Wzrost', 'BMI']])

main()
