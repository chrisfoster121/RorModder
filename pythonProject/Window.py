from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ModLabel import ModLabel
from zipfile import ZipFile
import shutil
import requests
import os


class Window(QMainWindow):

    def __init__(self, width, height):
        super().__init__()

        # set class instance variables
        self.scroll_area = None

        # setting geometry
        self.setGeometry(100, 100, width, height)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)
        self.setMinimumSize(width, height)

        # calling method
        self.ui_components()

        # showing all the widgets
        self.show()

        self.steam_common_path = "/home/christopher/.local/share/Steam/steamapps/common/Risk of Rain 2/"
        self.temp_download_path = "/tmp/ror_modder/"
        self.mod_ror()
    # method for components
    def ui_components(self):
        # creating a push button
        push = QPushButton("Launch", self)

        # determine button x location
        button_width = 300
        width_percentage = button_width/self.width()
        button_x = (1 - width_percentage) / 2
        print(button_x)

        # determine button Y location
        button_height = 40
        height_percentage = button_height/self.height()
        button_y = (1 - height_percentage * 2)

        # setting geometry to the push button
        push.setGeometry(button_x * self.width(), button_y * self.height(), button_width, button_height)

        scroll_area = QScrollArea(self)

        # determine scroll dimensions

        scroll_area.setGeometry(0, 0, self.width(), button_y * self.height())
        # scroll_area.setBackgroundRole(QPalette.Light)
        self.scroll_area = scroll_area
        mod_bar = ModLabel(self.scroll_area)
        mod_bar.set_dimensions(self.scroll_area.width(), 20)
        self.scroll_area.addScrollBarWidget(mod_bar, Qt.AlignCenter)

        # adding action method to the push button
        # push.clicked.connect(lambda: do_something())

        # method called by the push button when pressed
        # def do_something():

    def mod_ror(self):
        if not os.path.exists(self.temp_download_path):
            os.makedirs(self.temp_download_path)
        self.install_bepinex()
        self.install_better_ui()
        shutil.rmtree(self.temp_download_path)

    def install_bepinex(self):
        # make http request
        bepin_url = "https://thunderstore.io/package/download/bbepis/BepInExPack/5.4.2103/"
        request = requests.get(bepin_url, stream=True)
        bepinex_tmp_path = self.temp_download_path + "BepInEx/"

        #make the temp download path
        if not os.path.exists(bepinex_tmp_path):
            os.makedirs(bepinex_tmp_path)

        #write the zip file
        with open(bepinex_tmp_path + "_zip", "wb") as f:
            for chunk in request.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        # unzip the file
        with ZipFile(bepinex_tmp_path + "_zip", 'r') as zObject:
            zObject.extractall(path=bepinex_tmp_path + "_unzipped")

        # delete pre-existing files
        allfiles = os.listdir(bepinex_tmp_path + "_unzipped/" + "BepInExPack/")
        for f in allfiles:
            filepath = self.steam_common_path + f
            if os.path.isfile(filepath):
                os.remove(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)

        # copy the files
        self.copy_files_to_folder(bepinex_tmp_path + "_unzipped/" + "BepInExPack/", self.steam_common_path)

    def install_better_ui(self):
        # make http request
        better_ui_url = "https://thunderstore.io/package/download/XoXFaby/BetterUI/2.7.6/"
        request = requests.get(better_ui_url, stream=True)
        better_ui_tmp_path = self.temp_download_path + "BetterUI/"

        #make the temp download path
        if not os.path.exists(better_ui_tmp_path):
            os.makedirs(better_ui_tmp_path)

        #write the zip file
        with open(better_ui_tmp_path + "_zip", "wb") as f:
            for chunk in request.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        source = better_ui_tmp_path + "_unzipped/" + "plugins/BetterUI/"
        destination = self.steam_common_path + "BepInEx/plugins/"


        # unzip the file
        with ZipFile(better_ui_tmp_path + "_zip", 'r') as zObject:
            zObject.extractall(path=better_ui_tmp_path + "_unzipped")

        # delete pre-existing files
        allfiles = os.listdir(source)
        for f in allfiles:
            filepath = destination + f
            if os.path.exists(filepath):
                if os.path.isfile(filepath):
                    os.remove(filepath)
                elif os.path.isdir(filepath):
                    shutil.rmtree(filepath)

        # copy the files
        self.copy_files_to_folder(source, destination)



    def copy_files_to_folder(self, src_dir, dst_dir) -> None:
        source = src_dir
        destination = dst_dir

        # gather all files
        allfiles = os.listdir(source)

        # iterate on all files to move them to destination folder
        for f in allfiles:
            src_path = os.path.join(source, f)
            dst_path = os.path.join(destination, f)
            os.rename(src_path, dst_path)