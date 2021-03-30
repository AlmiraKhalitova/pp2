import os

print("This is your current Directory: ", os.getcwd())

def FolderList():
    entries = [*os.listdir()]
    for i in entries:
        print(i)
    pickFolder()

def RenameFolder():
    print("Which Folder you want to rename?")
    s = str(input())

    if os.path.exists(s):
        print("What is the new name of Folder?")
        s1 = str(input())
        os.rename(s,s1)
        print("Folder has been renamed. Dal'she?")
        pickFolder()
    
    else:
        print("Sorry, This Folder does not exist")
        print("One more try? Yes - print F; No - print any key")
        s = str(input())
        if s == 'F':
            RenameFolder()
        else:
            pickFolder()

def AddFolderToFolder():
    print ("Name of new Folder?")
    s = str(input())
    os.mkdir(s)
    print("Folder created. Dal'she?\n")
    pickFolder()

def AddFileToFolder():
    print ("Name of new File?\n")
    s = str(input())

    file = open(s, "w")
    file.close()

    print("File created. Dal'she?\n")
    
    pickFolder()

def GoToHell():
    entries = [*os.listdir()]
    for i in entries:
        print(i)

    print("Which Folder you wanna enter?")
    s = str(input())
    
    if os.path.exists(s):
        d = os.path.join(os.getcwd(), s)
        os.chdir(d)
        print("Folder entered! Dal'she?")
        pickFolder()
    
    else:
        print("Sorry, This File/Folder does not exist\nOne more try? Yes - print F; No - print any key")
        s = str(input())
        if s == 'F':
            GoToHell()
        else:
            pickFolder()

def ChangeFolder():
    print("Type a Folder in which you wanna work...")
    b = str(input())
    if os.path.exists(b):
        os.chdir(b)
        print("Folder Changed! Dal'she?")
        pickFolder()
    else:
        print("There is no such Folder.\nOne more try? Yes - print F; No - print any key")
        s = str(input())
        if s == "F":
            ChangeFolder()
        else:
            pickFolder()



def PrintContent():
    print("Choose file")
    b = str(input())
    s = ""

    if os.path.exists(b):
        file=open(b, "r")
        s = file.read()
        print(s)
        print("\nFile has been read! Dal'she?")
        pickFile()
    else:
        print("Such File does not exist.\nOne more try? Yes - print F; No - print any key")
        d = str(input())

        if d == "F":
            PrintContent()
        
        else:
            pickFile()

def RenameFile():
    print("Type the name of the File...")
    s = str(input())
    if os.path.exists(s):
        print("What is the new name of the File?")
        b = str(input())
        os.rename(s, b)

        print("File has been renamed! Dal'she?")
        pickFile()

    else:
        print("Such File does not exist.\nOne more try? Yes - print F; No - print any key")
        d = str(input())

        if d == "F":
            RenameFile()
        
        else:
            pickFile()

def AddContent():
    print("Type the name of the File...")
    s = str(input())
    if os.path.exists(s):
        print("What you wanna add to the File?")
        c = str(input())
        
        f = open(s, "a")
        f.write(c)
        f.close()

        print("Text has been added to the File! Dal'she?")
        pickFile()

    else:
        print("Such File does not exist.\nOne more try? Yes - print F; No - print any key")
        d = str(input())

        if d == "F":
            AddContent()
        
        else:
            pickFile()

def ReplaceContent():
    print("Type the name of the File...")
    s = str(input())
    if os.path.exists(s):
        print("How do you wanna rewrite the File?")
        c = str(input())
        
        f = open(s, "w")
        f.write(c)
        f.close()

        print("File has been rewritten! Dal'she?")
        pickFile()

    else:
        print("Such File does not exist.\nOne more try? Yes - print F; No - print any key")
        d = str(input())

        if d == "Y":
            ReplaceContent()
        
        else:
            pickFile()

def DeleteFile():
    print("Which File you wanna delete?")
    s = str(input())

    if os.path.exists(s):
        os.remove(s)
        print("File has been removed! Dal'she?")
        pickFile()

    else:
        print("Such File does not exist.\nOne more try? Yes - print F; No - print any key")
        d = str(input())

        if d == "F":
            DeleteFile()
        else:
            pickFile()



def pickFolder():
    print('''What you like to do:
    1. List of Subfolders
    2. Rename Folder
    3. Add Folder
    4. Add File
    5. Go To(File/Folder) in current Folder
    6. Change Folder
    7. Work with Files
    (Any Other Key). End Programm''')

    num = str(input())

    if num == "1":
        FolderList()

    elif num == "2":
        RenameFolder()

    elif num == "3":
        AddFolderToFolder()

    elif num == "4":
        AddFileToFolder()

    elif num == "5":
        GoToHell()

    elif num == "6":
        ChangeFolder()

    elif num == "7":
        pickFile()

    else:
        print("See ya next time :)")

def pickFile():
    print('''What you like to do:
    1. Print Containing
    2. Rename File
    3. Add content to File
    4. Replace content in File
    5. Delete File
    6. Work with Folders
    (Any Other Key). End Programm''')

    num = str(input())

    if num == "1":
        PrintContent()

    elif num == "2":
        RenameFile()

    elif num == "3":
        AddContent()

    elif num == "4":
        ReplaceContent()

    elif num == "5":
        DeleteFile()

    elif num == "6":
        pickFolder()

    else:
        print("See ya next time :)")
        


def KettkEngine():
    print('''Would you like to work with files or folders?
    -If Files, print 'Files'
    -If Folders, print 'Folders'
    -Type any Key to end programm''')
    
    s = str(input())

    if s == 'Folders' or s == "Folders " or s == "folders " or s == "folders":
        pickFolder()
    elif s == 'Files' or s == "Files " or s == "files" or s == "files ":
        pickFile()
    else:
        print("See ya next time :)")

KettkEngine()