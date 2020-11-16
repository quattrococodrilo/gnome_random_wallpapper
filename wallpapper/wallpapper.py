""" Wallpapper class. """

import random
from os import listdir, path, system


class Wallpapper:
    """ This class sets a random image as wallpapper
    from a local folder. """

    def __init__(self, images_path):
        self.images_path = images_path
        images = self.get_images()
        image = self.random_image(images)
        self.code = self.set_wallpapper(image)

    def get_images(self):
        """Get images from a path specified in
        images_path attribute.

        Returns:
            list: List of name images.
        """

        images = listdir(self.images_path)
        if not images:
            assert (not images), f"There are not images in {self.images_path}"
        return images

    def random_image(self, images):
        """ Return a random image. """
        if len(images) == 1:
            return images[0]
        elif len(images) > 1:
            random.shuffle(images)
            group = random.sample(
                images,
               len(images) // 2
            )
            image = random.choice(images)
            return image
        return None

    def set_wallpapper(self, image):
        command = system(
            'gsettings set org.gnome.desktop.background picture-uri file://{}'.format(
                path.join(self.images_path, image)
            )
        )
        return command
