import os

def save_csv(name, df):
    directory_path = r'C:\Users\Aadya Dewangan\Desktop\sql projects\csv_files'
    
    file_path = os.path.join(directory_path, f'{name}.csv')

    df.to_csv(file_path, index=False)

    print(f'DataFrame has been saved to {file_path}')
