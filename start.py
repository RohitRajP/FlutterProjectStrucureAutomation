# pyinstaller command
# pyinstaller myfile.py --noupx -y --onefile

# importing packages
import os
import shutil


# function to emulate the functionality of "touch" command
# while being platform independant
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def printMessage(message):
    print("\n#################################################################")
    print(message)
    print("#################################################################\n")


# used to create the flutter application
def createFlutterApp(projectName, projectOrg):
    printMessage("Creating flutter application...")
    # creating fluutter project
    os.system("flutter create -a java -i swift --org com.{} {}".format(
        projectOrg, projectName))

# used to delete the test folder


def deleteTestFolder():
    printMessage("Deleting 'Test' folder...")
    # navigating into the created project
    os.chdir(projectName)
    # deleting the test folder
    shutil.rmtree("./test")


# used to create all the files and folders in the new flutter project
def createFilesAndFolders():
    printMessage(
        "Creating all supplementary folders and files in 'lib' folder...")
    # navigating to the lib folder
    os.chdir("./lib")
    # making folders
    os.mkdir("global")
    os.mkdir("models")
    os.mkdir("pages")
    os.mkdir("services")
    # creating files
    touch("./imports.dart")
    # configuring global
    os.chdir("./global")
    touch("./globalData.dart")
    touch("./globalScaffoldKeys.dart")
    touch("./globalTheme.dart")
    touch("./globalFunctions.dart")
    touch("./globalWidgets.dart")
    os.mkdir("controllers")
    # configuring services
    os.chdir("../services")
    os.mkdir("networkOps")
    touch("./networkOps/networkOps.dart")
    os.mkdir("permissionOps")
    touch("./permissionOps/permissionOps.dart")
    os.mkdir("sharedPrefsOps")
    touch("./sharedPrefsOps/sharedPrefsOps.dart")
    # configuring pages
    os.chdir("../pages")
    os.mkdir("homePage")
    touch("./homePage/homePage.dart")
    touch("./homePage/widgets.dart")
    touch("./homePage/functions.dart")
    # navigating back to the root of the project
    os.chdir("../..")


# used to perform meta operations such as writing data to files
def writeDataToFiles(projectName):

    # opening pubspec file
    with open("./pubspec.yaml", "r+") as f:
        # getting all the lines in the file
        allLines = f.readlines()
        # clearing the contents of the file
        f.seek(0)
        f.truncate()
        # adding normal dependancies
        allLines.insert(25, '  provider: ^4.3.2+1\n')
        allLines.insert(26, '  flash: ^1.3.1\n')
        # adding the pedantic dev dependancies
        allLines.insert(36, '  effective_dart: ^1.2.4\n')
        # writing the new lines to file
        f.writelines(allLines)

    # filling the contents of the analysis file
    with open("analysis_options.yaml", "w") as f:
        # containes the file content to add
        fileContent = ['include: package:effective_dart/analysis_options.1.2.0.yaml\n',
                       'linter:\n', '  rules:\n', '    prefer_relative_imports: false\n', '    file_names: false\n',
                       '    omit_local_variable_types: false\n', '    avoid_setters_without_getters: false\n','    public_member_api_docs: false\n']
        # writing the contents to the file
        f.writelines(fileContent)

    # running pub get
    os.system("flutter pub get")
    # upgrading existing dependancies to latest version
    os.system("flutter pub upgrade")

    # changing directory to go to lib folder
    os.chdir("./lib")
    # filling the contents of the import.dart file
    with open("imports.dart", "w") as f:
        # containes the file content to add
        fileContent = ['// package imports\n', "export 'package:flutter/material.dart';\n", "export 'package:flash/flash.dart';\n","export 'package:provider/provider.dart';\n\n",
                       '// model imports\n\n', '// page imports\n\n', '// global imports\n', f"export 'package:{projectName}/global/globalData.dart';\n",
                       f"export 'package:{projectName}/global/globalFunctions.dart';\n", f"export 'package:{projectName}/global/globalTheme.dart';\n",
                       f"export 'package:{projectName}/global/globalWidgets.dart';\n", f"export 'package:{projectName}/global/globalScaffoldKeys.dart';\n\n",
                       '// service imports']
        # writing the content to the files
        f.writelines(fileContent)


# main function
if __name__ == "__main__":

    # fetching the flutter project name, org name and web support command
    projectName = input("Please enter name of flutter project: ")
    projectOrg = input("Please enter organization name: ")
    isWebEnabled = input("Should web support be enabled? (y/n): ")

    # checking if web support is needed
    if(isWebEnabled == 'y' or isWebEnabled == 'Y'):
        # enabling flutter web
        os.system("flutter config --enable-web")
    else:
        # disabling web
        os.system("flutter config --no-enable-web")

    # creating flutter project
    createFlutterApp(projectName=projectName, projectOrg=projectOrg)

    # deleting the 'test' folder
    deleteTestFolder()

    # creating all the important files and folders
    createFilesAndFolders()

    # writing data to the required files
    writeDataToFiles(projectName=projectName)

    # completion message
    printMessage("Done! Happy Fluttering ;D")
