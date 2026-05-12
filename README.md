# massArchiver
Create a list of and batch export DRA file's out of [BlackMagic's DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/)

## Installing Script
### Steps
1. In Resolve open the Fusion page, in the toolbar click “Fusion > Fusion Settings”
2. Click “Path Map” in the Fusion drop down of the settings window, and make sure “Scripts” is set to “UserPaths:Scripts”. If not, hit the “Reset” button.
3. Click "Script" in the Fusion drop down of the settings window, change selection from python 2.7 to python 3
   - This step is only Resolve version 18.1.4 or later
4. Hit the save button to update all of your changes
5. [Download this repository's latest release](https://github.com/MokshC/massArchiver/releases)
6. Add it to your scripts path. These paths can also be found by clicking the folder icon at the bottom right of "Path Map" from step 2.
   - **LINUX**: `~/.local/share/DaVinciResolve/Fusion/Scripts/Deliver`
     - Hint: if you can’t find .local try hitting Ctrl+H to show hidden folders
   - **WINDOWS**: `C:\Users\{NAME}\AppData\Roaming\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Deliver`
     - Hint: if you can’t find AppData try going to View > Hidden items in file explorer and hitting the checkbox 
   - **MAC**: `/Library/Application Support/Blackmagic Design/Fusion/Scripts/Deliver`
7. Restart Resolve
8. Now when you go open Resolve and, in the toolbar, click “Workspace > Scripts” several scripts should be available.

## Using the script
### Steps
1. Open a timeline in your resolve project
2. Click “Workspace > Scripts > massArchiver”
3. Select the project database you want to archive projects from, and close the database folder pop up once the database loads
4. Select the folders or projects you want to archive with ctrl + click or shift + clcik, it will go 1 deep in selected folders.
5. Click "Add Selected" and you'll see selected projects populate on the left panel.
6. Click "Clear" to start over or click "Archive" to begin.
7. Choose a folder to which the archives will be saved.
8. Select the settings of what you want archived.
9. Hit "Ok" to start archiving, the process will stop if there are any error pop ups and wait for your response.
