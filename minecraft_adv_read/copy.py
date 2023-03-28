import shutil

#print(dir(shutil))
def copy_raw_files():
    shutil.copy('/AppData/Roaming/.minecraft/saves/WORLD/advancements/FILENAME1.json','/minecraft_adv_read/raw_data_file1.json')
    shutil.copy('/AppData/Roaming/.minecraft/saves/WORLD/advancements/FILENAME2.json','/minecraft_adv_read/raw_data_file2.json')
    
