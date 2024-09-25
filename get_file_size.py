import os 
import pandas as pd

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    
    index = 0
    while total_size / 1024 > 1:
        total_size /= 1024
        index += 1
    
    return round(total_size, 2), index

def main():

    quit = False
    current_path = None
    previous_path = None
    prevdf = None
    while not quit:
        if not current_path:
            additional_message = 'Enter folder path: '
            prevdf = None
        
        inputmessage = f"\nPress 'q' to quit\n{additional_message}"
        userinput = input(inputmessage)
        userinput = userinput.strip()
        os.system('cls') if os.name == 'nt' else os.system('clear')

        if userinput.lower() == 'q':
            break
        else:
            if not previous_path:
                current_path = userinput
            else:
                if not userinput.isdigit():
                    if userinput == '-1':
                        if '\\' not in previous_path:
                            current_path = None
                        else:
                            break_past_directory = previous_path.split('\\')
                            current_path = '\\'.join(break_past_directory[:-1])
                    else:
                        current_path = userinput
                else:
                    if 0 <= int(userinput) and int(userinput) < len(prevdf):
                        current_path = os.path.join(previous_path, prevdf['File Name'].values.tolist()[int(userinput)])
                    else:
                        current_path = None

        if current_path:
            print('calculating file/folder sizes in directory:', current_path)
            mainlist = []
            for x in os.listdir(current_path):
                folder_size, index = get_folder_size(os.path.join(current_path, x))
                if folder_size > 0:
                    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
                    unit = units[index]

                    item_type = 'Folder' if os.path.isdir(os.path.join(current_path, x)) else 'File'
                    mainlist.append([x, item_type, folder_size, index, unit])
            
            df = pd.DataFrame(mainlist)
            df.columns = ['File Name', 'Type', 'Size', 'Index', 'Unit']
            df = df.sort_values(by=["Index", "Size", "File Name"], ascending=[False, False, True], ignore_index=True)
            df = df[['File Name', 'Type', 'Size', 'Unit']]

            os.system('cls') if os.name == 'nt' else os.system('clear')
            print(f"Directory: {current_path}\n")
            print(df)

            prevdf = df
            previous_path = current_path
            additional_message = f'Press 0 to {len(df) - 1} to check one of the directories above\nEnter -1 to go back to prev directory'
            additional_message += "\nYou can also enter the folder path manually\nEnter: "

if __name__ == '__main__':
    main()
