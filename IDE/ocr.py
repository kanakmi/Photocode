
# if tesseract is not in environment variables
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

def ocr_core(filename):
    from PIL import Image
    import pytesseract
    """
    This function will handle the core OCR processing of images.
    """
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    text = pytesseract.image_to_string(Image.open(filename))
    return text