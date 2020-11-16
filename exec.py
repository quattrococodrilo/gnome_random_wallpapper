#!/home/quattroc/Documentos/python/gnome_random_wallpapper/env/bin/python

from Settings import FOLDER_IMAGES_PATH
from wallpapper.wallpapper import Wallpapper


def Executor():
    """Executes Wallpapper Class
    """

    Wallpapper(FOLDER_IMAGES_PATH)


if __name__ == "__main__":
    Executor()
