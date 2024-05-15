from PIL import Image

# Open the PNG file
image = Image.open("meteor_challenge_01.png")

# Get the pixel data
pixel_data = list(image.getdata())

width = image.width
water_level = set()


star_color = (255, 255, 255, 255)
star = 0
meteor_color = (255, 0, 0, 255)
meteor = 0
water_color = (0, 0, 255, 255)
meteors_in_water = 0
ground_color = (0, 0, 0, 255)

# Iterate over each pixel
for i, pixel in enumerate(reversed(pixel_data)):
    if pixel == star_color:
        star += 1
    elif pixel == meteor_color:
        meteor += 1
        w = i % width
        if w in water_level:
            meteors_in_water += 1
    elif pixel == water_color:
        w = i % width
        water_level.add(w)

print(star)
print(meteor)
print(meteors_in_water)

print(width)
        
# Remember to close the file when you're done
image.close()
