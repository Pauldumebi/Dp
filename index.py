import pandas as pd
import numpy as np
import os,shutil

df = pd.read_csv('Radiologists-report_v1.csv')
# Replace missing values with 3
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(3, inplace=True)

cols = ['Patient ID', 'D3', 'D4', 'D5']
df[cols] = df[cols].applymap(np.int64)

# get the path/directory
folder_dir = "Composite_Images/"

def checkFileExistAndMove(id, Disc, status):
    if len(str(id)) == 1:
        id = '000' + str(id)
    elif len(str(id)) == 2:
        id = '00' + str(id)
    elif len(str(id)) == 3:
        id = '0' + str(id)
  
    image = 'C1_'+ id + '_' + Disc +  '.png'
    path = 'Composite_Images/' + image
    isExisting = os.path.exists(path)
    if isExisting:
        if status == 'Issue':
            original = folder_dir + image
            target = "Issue-G/" + image
            shutil.move(original, target)
        elif status == 'No Issue':
            original = folder_dir + image
            target = "No_issue-G/" + image
            shutil.move(original, target)
        elif status == 'Empty':
            original = folder_dir + image
            target = "Empty-G/" + image
            shutil.move(original, target)
            
for i in range(1, 112):
    IDs = df['Patient ID'].tolist()
    if(i in IDs ):
        getRow = df.loc[df['Patient ID'] == i]
        print(getRow, 'getRow')
        if getRow['D3'].to_string(index=False) == str(1):
            checkFileExistAndMove(i, 'D3', 'Issue')
        elif getRow['D3'].to_string(index=False) == str(0):
            checkFileExistAndMove(i, 'D3', "No Issue")
        elif getRow['D3'].to_string(index=False) == str(3):
            checkFileExistAndMove(i, 'D3', "Empty")
        
        if getRow['D4'].to_string(index=False) == str(1):
            checkFileExistAndMove(i, 'D4', 'Issue')
        elif getRow['D4'].to_string(index=False) == str(0):
            checkFileExistAndMove(i, 'D4', "No Issue")
        elif getRow['D4'].to_string(index=False) == str(3):
            checkFileExistAndMove(i, 'D4', "Empty")
        
        if getRow['D5'].to_string(index=False) == str(1):
            checkFileExistAndMove(i, 'D5', 'Issue')
        elif getRow['D5'].to_string(index=False) == str(0):
            checkFileExistAndMove(i, 'D5', "No Issue")
        elif getRow['D5'].to_string(index=False) == str(3):
            checkFileExistAndMove(i, 'D5', "Empty")