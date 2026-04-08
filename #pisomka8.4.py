#pisomka8.4.py
#obrazok 200x na 300z, nech sa v nom pixeli sachovnicovo striedaju v dvoch farbach
from PIL import Image
pic = Image.new("RGB",(200,300),"blue")
pixels = pic.load()
for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        if (x%2==0 and y%2==1)or(x%2==1 and y%2==0):
            pixels[x,y] = (255,255,255)
pic.show()
