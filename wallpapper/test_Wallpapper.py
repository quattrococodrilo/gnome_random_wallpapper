""" Testing module. """

import unittest

from wallpapper import Wallpapper


class Test_Wallpapper(unittest.TestCase):

    def setUp(self):
        FOLDER_IMAGES_PATH = '/home/quattroc/Documentos/imagenes/backgrounds2'
        self.W = Wallpapper(images_path=FOLDER_IMAGES_PATH)

    def test_get_images(self):
        images = self.W.get_images()
        self.assertEquals(type(images), list)

    def test_get_random_image(self):
        images = self.W.get_images()
        image = self.W.random_image(images)
        self.assertEqual(type(image), str)

    def test_set_wallpaper(self):
        self.assertEqual(self.W.code, 0)


if __name__ == "__main__":
    unittest.main()
