#!/usr/bin/env python3

import os
import cv2
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ImageMerger(ABC):
    @abstractmethod
    def merge(self, image1, image2):
        pass

class VerticalMerger(ImageMerger):
    def merge(self, image1, image2):
        return vconcat_resize([image1, image2])

class HorizontalMerger(ImageMerger):
    def merge(self, image1, image2):
        return hconcat_resize([image1, image2])

def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(img.shape[1] for img in img_list)
    im_list_resize = [cv2.resize(img, (w_min, int(img.shape[0] * w_min / img.shape[1])), interpolation=interpolation) for img in img_list]
    return cv2.vconcat(im_list_resize)

def hconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)
    im_list_resize = [cv2.resize(img, (int(img.shape[1] * h_min / img.shape[0]), h_min), interpolation=interpolation) for img in img_list]
    return cv2.hconcat(im_list_resize)

class ImageLoader:
    def load(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"[ERROR] {path} does not exist.")
        if os.path.isdir(path):
            raise IsADirectoryError(f"[ERROR] {path} is a directory.")
        return cv2.imread(path)

class ImageProcessor:
    def __init__(self, merger: ImageMerger):
        self.merger = merger

    def process(self, img1, img2, output_path):
        concatenated_image = self.merger.merge(img1, img2)
        cv2.imwrite(output_path, concatenated_image)
        print(f"Image saved at {output_path}")

def main():
    img_loader = ImageLoader()

    imgpath1 = input("Enter 1st image path: ")
    imgpath2 = input("Enter 2nd image path: ")

    try:
        img1 = img_loader.load(imgpath1)
        img2 = img_loader.load(imgpath2)

        merge_method = input("Merge [V]erically or [H]orizontally? ").strip().lower()
        
        if merge_method == "h":
            merger = HorizontalMerger()
            output_path = "horizontal_concatenated.jpg"
        elif merge_method == "v":
            merger = VerticalMerger()
            output_path = "vertical_concatenated.jpg"
        else:
            print("Invalid Option!")
            return

        processor = ImageProcessor(merger)
        processor.process(img1, img2, output_path)

    except (FileNotFoundError, IsADirectoryError) as e:
        print(e)

if __name__ == "__main__":
    main()
