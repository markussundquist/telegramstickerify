from PIL import Image
import os
import shutil

def check_os(): #Checks operating system
    if os.name == "nt":
        directory = "ImageBin\\"
    elif os.name == "posix":
        directory = "ImageBin/"
    else:
        raise Exception('Unsupported OS.')

    return directory

def new_folder():
    if os.name == "nt":
        directory = "ImagesReady\\"
    elif os.name == "posix":
        directory = "ImagesReady/"
    else:
        raise Exception('Unsupported OS.')

    return directory

def choose_bigger_axis(s_image): #Checks which axis is the largersti one and then resizes it to be 300px. "remember //"
    x, y = s_image.size
    if x > y:       
        return 300, round(((300*y)/x))            #dodgy scaling function, that makes sure that the largest axis is 300px long
    else:
        return round(((300*x)/y)), 300

### Main program starts here ############################
#Iterate through directory and resize every .jpg or .png
i = 0
old_folder = check_os()
working_folder = new_folder()


saved_filenames = input("Save new images as: ")
print(f'Converting images in: {old_folder}\nPlease wait...')


for filename in os.listdir(old_folder):
    print("Processing: "+ str(i)+"/"+str((len(os.listdir(old_folder)))), end='\r')
    if filename.endswith((".jpg",  ".jpeg", ".png", ".gif", ".tif", ".tiff")):
        save = (saved_filenames+str(i)+".png")
        #print(f'converting {filename}') #debug
        modify_file = Image.open(os.path.join(old_folder, filename))
        x_axis, y_axis = choose_bigger_axis(modify_file)
        #print(f'Changing resolution from {modify_file.size} to ({x_axis}, {y_axis})') #debug
        modify_file = modify_file.resize((x_axis, y_axis))
        modify_file.save(save ,"PNG")
        shutil.move(save, working_folder)
        i += 1
  
