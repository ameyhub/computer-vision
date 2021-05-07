
from PIL import Image

from resizeimage import resizeimage


with open('C:/Users/ameyd/Finger Counter using Hand Tracking/fingure_image/6.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [200, 200])
        cover.save(
            'C:/Users/ameyd/Finger Counter using Hand Tracking/6.jpg', image.format)
