# Note: i might not need this script. use converter.py instead?

from PIL import Image

def image_to_bitmap_array(image_path):
    # Load image
    img = Image.open(image_path)
    # Convert to monochrome (1-bit pixels, black and white, stored with one pixel per byte)
    img = img.convert('1')  
    # Resize if necessary, e.g., img = img.resize((128, 160)), keeping aspect ratio or not as required
    width, height = img.size
    
    # Create bitmap array
    bitmap = []
    for y in range(height):
        for x in range(0, width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < width:
                    if img.getpixel((x + bit, y)):
                        byte |= (1 << (7 - bit))
            bitmap.append(byte)
    
    return bitmap

# Example usage -> basically put your image in the same directoryni 
bitmap = image_to_bitmap_array('file-modified.bmp')
print(bitmap)
