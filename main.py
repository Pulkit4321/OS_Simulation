disk = [None] * 1024 # 1024 blocks in the disk
total_blocks = len(disk)
used_blocks = 0

def add_file(name, size):
    global used_blocks
    free_blocks = []
    for i in range(total_blocks):
        if disk[i] == None:
            free_blocks.append(i)
            if len(free_blocks) == size:
                for j in free_blocks:
                    disk[j] = name
                used_blocks += size
                return True
        else:
            free_blocks = []
    return False

def delete_file(name):
    flg = False
    global used_blocks
    for i in range(total_blocks):
        if disk[i] == name:
            flg = True
            disk[i] = None
            used_blocks -= 1
    return flg

def rename_file(old_name, new_name):
    flg = False
    for i in range(total_blocks):
        if disk[i] == old_name:
            flg = True
            disk[i] = new_name
    return flg

def move_file(name, new_location):
    global used_blocks
    size = 0
    old_location = []
    for i in range(total_blocks):
        if disk[i] == name:
            size += 1
            old_location.append(i)
    free_blocks = 0
    for i in range(new_location, total_blocks):
        if disk[i] == None:
            free_blocks += 1
        else:
            free_blocks = 0
        if free_blocks == size:
            for j in old_location:
                disk[j] = None
            for j in range(new_location, new_location+size):
                disk[j] = name
            used_blocks -= size
            return True
    return False

def calculate_fragmentation():
    free_blocks = 0
    for i in range(total_blocks):
        if disk[i] == None:
            free_blocks += 1
    return free_blocks

time = -1
print("==++Choice Menu++==")
print("1) Creating a File\n2) Deleting a File\n3) Renaming a File\n4) Moveing a File\n5) Calculate Fragmentation\n0) Stopping the Simulation")
print("===================")
while(time!=0):
    time = int(input("Enter Choice: "))
    if(time==1):
        name = input("Enter name of file to be added with extention: ")
        size = int(input("Enter size of file in MB: "))
        if add_file(name,size):
            print("The file has been sucessfully added.")
        else:
            print("The file has not been added cause of insufficient space.")
    elif(time==2):
        name = input("Enter name of file to be removed with extention: ")
        if delete_file(name):
            print("The file has been sucessfully removed.")
        else:
            print("The file has not been removed cause it doesnt exist.")
    elif(time==3):
        name1 = input("Enter old name of file to be renamed with extention: ")
        name2 = input("Enter new name of file to be renamed with extention: ")
        if(rename_file(name1,name2)):
            print("The file has been sucessfully renamed.")
        else:
            print("The file wasn't renamed as it did not exist.")
    elif(time==4):
        name = input("Enter name of file to be moved with extention: ")
        location = int(input("Enter the location at which you need to move the file: "))
        if(move_file(name,location)):
            print("The file has been sucessfully moved to the new location")
        else:
            print("The file doesn't exist or not enough space at new location")
    elif(time==5):
        print("No. of Fragmented blocks are: {}".format(calculate_fragmentation()))
