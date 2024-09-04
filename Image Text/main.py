from image_processor_factory import ImageProcessorFactory

def main():
    processor = ImageProcessorFactory.create_image_processor()
    image_path = Config.get_image_path()
    extracted_text = processor.process_image(image_path)
    print(extracted_text[:-1])

if __name__ == "__main__":
    main()
