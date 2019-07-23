import ebooklib
from ebooklib import epub
from PIL import Image


james = '/Users/Wenz/Documents/Journal/Choose Yourself! - James Altucher.epub'

book = epub.read_epub(james)

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print(image)

