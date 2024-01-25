# Importing needed modules
import pandas as pd
import os
import shutil

# Reading the CSV file 
csv_path = r'C:\Users\Edward Benjamin\Desktop\AyaData\Task 2-20240123T155023Z-001\Task 2\mask-images\instance_mask_annotations.csv'
mask_table = pd.read_csv(csv_path)

# Defining the paths for the source masks and destination folders
source_folder = r'C:\Users\Edward Benjamin\Desktop\AyaData\Task 2-20240123T155023Z-001\Task 2\mask-images\masks'
humans = r'C:\Users\Edward Benjamin\Desktop\AyaData\Task 2-20240123T155023Z-001\Task 2\mask-images\human'
backgrounds = r'C:\Users\Edward Benjamin\Desktop\AyaData\Task 2-20240123T155023Z-001\Task 2\mask-images\background'


# Looping through each row in the Dataframe
for index, row in mask_table.iterrows():
    # Assigning each value of the column maks_id and class_name to variables
    mask_id = row['mask_id']
    class_name = row['class_name']

    # Constructing the source and destination paths
    source_path = os.path.join(source_folder, f'{mask_id}.png')  
    destination_folder = humans if class_name == 'Human' else backgrounds

    # Moving the mask image to the right destination folder
    destination_path = os.path.join(destination_folder, f'{mask_id}.png')
    shutil.move(source_path, destination_path)  
