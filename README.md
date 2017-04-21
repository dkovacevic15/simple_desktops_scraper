# Simple Desktops Wallpaper Downloader

Downloads all wallpapers from simpledesktops.com (requires Python 3.x)

# Guide for Windows:

1) Install [Python 3](https://www.python.org/downloads/) (make sure Python is added to PATH, the installer should help you out here)
2) Open up the command prompt (search for it in the start menu)
3) Type in the following commands (wait for one to finish, then enter the next):
~~~
  pip install beautifulsoup4
  pip install requests
  pip install lxml
~~~
4) Download the .py file from this repository
5) Copy it to the folder where you want to download all the wallpapers
6) Right-click it
7) Press "Open with IDLE"
8) Press F5
9) Wait (Due to the actual website being relatively small, and Python not really being the fastest language there is, expect this step to take a while)

Note:
If the program finds a file already downloaded, it will stop. Because of this, you can use it to update your wallpaper dir whenever a new wallpaper is posted. To disable this, open the py file in notepad and change the first line from 'STOP_IF_FOUND = True' to 'STOP_IF_FOUND = False' (mind the capital F)
