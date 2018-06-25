import numpy as np

# Class for seeing the image (converting the seen image into the usable form of a numpy array of 1's and 0's)
# Further developments will involve adding support for color, as right now only black and white works


class Retina(object):
    """binary 2D boolean array
    :param length: number of binary cells along each side of the square retina
    """
    def __init__(self, length):
        self.vision_cells = np.zeros((length, length), dtype=bool)

    def see_binary_image(self, image, print_image_to_console=False):
        """stores the seen part of the world
        :param image: a binary square section of the world
        :return: 2D int array where '1' is black and '0' is white
        """
        image_width = image.size[0]
        image_height = image.size[1]
        pixels = image.load()
        image_row = ''
        for c in range(image_height):
            for r in range(image_width):
                if pixels[r, c] == 1:
                    self.vision_cells[r][c] = True
                    image_row += '1'
                else:
                    self.vision_cells[r][c] = False
                    image_row += '0'
            image_row += '\n'

        if (print_image_to_console):
            print(image_row)

        return pixels