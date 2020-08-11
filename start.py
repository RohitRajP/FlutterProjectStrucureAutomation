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

# function to print message


def printMessage(message):
    print("\n#################################################################")
    print(message)
    print("#################################################################\n")


# main function
if __name__ == "__main__":

    # fetching the flutter project name
    projectName = input("Please enter name of flutter project: ")
    projectOrg = input("Please enter organization name: ")

    # executing commands one by one

    printMessage("Creating flutter application...")
    # creating fluutter project
    os.system("flutter create -a java -i swift --org com.{} {}".format(
        projectOrg, projectName))

    printMessage("Deleting 'Test' folder...")
    # navigating into the created project
    os.chdir(projectName)
    # deleting the test folder
    shutil.rmtree("./test")

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

    # completion message
    printMessage("Done! Happy Fluttering ;D")
    input()
