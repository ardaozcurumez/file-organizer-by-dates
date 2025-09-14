import os
from datetime import datetime

def date_organize():

    folder = input("Enter your folder path: ")
    files = list()
    dates = list()

    def list_dir():

        for file in os.listdir(folder):

            if os.path.isdir(os.path.join(folder,file)):
                continue
            elif file.startswith("."):
                continue
            else:
                files.append(file)

    list_dir()

    for file in files:

        date_stamp = os.stat(os.path.join(folder,file)).st_birthtime
        date = datetime.fromtimestamp(date_stamp).strftime("%d-%m-%Y")    

        if date in dates:
            continue
        else:
            dates.append(date)

    for dt in dates:

        if os.path.isdir(os.path.join(folder,dt)):
            continue
        else:
            os.mkdir(os.path.join(folder,dt))

    for file in files:

        date_stamp = os.stat(os.path.join(folder,file)).st_birthtime
        date = datetime.fromtimestamp(date_stamp).strftime("%d-%m-%Y")
        
        os.rename(os.path.join(folder,file),os.path.join(folder,date,file))

if __name__ == "__main__":
    date_organize()




                        