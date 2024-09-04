#!/usr/bin/env python

import os
import cv2
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()

# Environment Variables
IMAGE_PATH = os.getenv('IMAGE_PATH', 'sample.jpg')

# Abstract Base Class
class ImageProcessor(ABC):
    @abstractmethod
    def process(self, img):
        pass

# Concrete Strategy for Inversion of Control / Dependency Injection
class Inverter(ImageProcessor):
    def process(self, img):
        return [[[255 - k for k in j] for j in i] for i in img]

class MirrorVertical(ImageProcessor):
    def process(self, img):
        return [img[-i - 1] for i in range(len(img))]

class Blur(ImageProcessor):
    def __init__(self, strength):
        self.strength = strength

    def process(self, img):
        temp1 = []
        for i in range(len(img)):
            temp2 = []
            for j in range(len(img[0])):
                temp3 = []
                for k in range(len(img[0][0])):
                    # Blur operation
                    a_pixels = 0
                    temp = 0
                    for x in range(-self.strength, self.strength + 1):
                        for y in range(-self.strength, self.strength + 1):
                            try:
                                temp += img[i + x][j + y][k]
                                a_pixels += 1
                            except IndexError:
                                continue
                    temp3.append(int(temp / a_pixels) if a_pixels > 0 else img[i][j][k])
                temp2.append(temp3)
            temp1.append(temp2)
        return temp1

class Lightness(ImageProcessor):
    def __init__(self, b):
        self.b = b

    def process(self, img):
        return [[[int((255 * (self.b / 100)) + (img[i][j][k] * (1 - (self.b / 100)))) 
                   for k in range(len(img[0][0]))] for j in range(len(img[0]))] for i in range(len(img))]

# Context for Strategy Pattern to apply chosen processes
class ImageContext:
    def __init__(self, processor: ImageProcessor):
        self.processor = processor

    def set_processor(self, processor: ImageProcessor):
        self.processor = processor

    def execute(self, img):
        return self.processor.process(img)

# Factory for different image operations
class ImageProcessorFactory:
    @staticmethod
    def create_processor(processor_type, *args):
        if processor_type == "invert":
            return Inverter()
        elif processor_type == "mirror_vertical":
            return MirrorVertical()
        elif processor_type == "blur":
            return Blur(*args)
        elif processor_type == "lightness":
            return Lightness(*args)
        else:
            raise ValueError("Unknown processor type")

# Image Display Function
def display_image(original, manipulated, title_1="Original", title_2="Manipulated"):
    plt.figure(figsize=(15, 25))
    plt.subplot(1, 2, 1)
    plt.title(title_2)
    plt.imshow(manipulated)
    plt.subplot(1, 2, 2)
    plt.title(title_1)
    plt.imshow(original)
    plt.show()

# Read and process the image
image = cv2.imread(IMAGE_PATH)
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).tolist()

# Example of using the factory and context
context = ImageContext(ImageProcessorFactory.create_processor("invert"))
inverted_img = context.execute(img)

context.set_processor(ImageProcessorFactory.create_processor("mirror_vertical"))
mirrored_img = context.execute(img)

context.set_processor(ImageProcessorFactory.create_processor("blur", 5))
blurred_img = context.execute(img)

# Display original and manipulated images
display_image(img, inverted_img, "Original", "Inverted")
display_image(img, mirrored_img, "Original", "Mirrored")
display_image(img, blurred_img, "Original", "Blurred")
