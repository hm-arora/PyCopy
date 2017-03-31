PyCopy
===================

Python script to copy music , movies , images , pdf etc . to their specified folder
It reduces the effort of copying  one type of files at a time and paste in a folder
(eg : copying music files from usb and paste in a music folder and again go to usb folder
and copying all movies and then paste in a movies folder)

Grab the latest version of Python at https://www.python.org/downloads/.

### Usage:

#### Linux : with Nautilus file manager(Tested on Debian Based with nautilus as file manager):
* Go to ~/.local/share/nautilus/scripts/ (Ubuntu 13.04 or above) OR ~/.gnome2/nautilus-scripts/ (Ubuntu 12.10 and below) folder and add Movefiles.sh in the folder.

* for ubuntu 13.04 or above 
```
chmod +x ~/.local/share/nautilus/scripts/MoveFiles.sh
```
* for ubuntu 12.10 and below
```
chmod +x ~/.gnome2/nautilus-scripts/MoveFiles.sh
```
* The path for file.py is hardcoded to Desktop ...U can change it accordingly.

* Add more extenstion in the *exten.txt* file with name specified of 

* Add folder path in the *folder.txt* file

* Make sure above files have same name in left side

* Now Right Click on the selected files you want to copying from that path to specified path . Right Click ->  Scripts -> Movefiles.sh
