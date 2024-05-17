from PIL import Image

# Open the PNG file
image = Image.open("meteor_challenge_01.png")

# Get the pixel data
pixel_data = list(image.getdata())

# Get the width of the image
width = image.width

# Set to store indices of columns with water
water_level = set()

# Define colors
star_color = (255, 255, 255, 255)
meteor_color = (255, 0, 0, 255)
water_color = (0, 0, 255, 255)

# Initialize counters
star = 0
meteor = 0
meteors_in_water = 0

# Binary matrix to store the phrase
phrase_bin = [[0] * width for _ in range(2)]

# Iterate over each pixel in reverse order 
# Reversing to pass through water first, so we don't need to traverse the array twice    
for i, pixel in enumerate(reversed(pixel_data)):  
    w = i % width  # Calculate the current column
    if pixel == star_color:
        star += 1
        phrase_bin[0][w] = 1  # Mark position in binary matrix for star
    elif pixel == meteor_color:
        meteor += 1
        if w in water_level:
            meteors_in_water += 1  # Increment count of meteors in water
        phrase_bin[1][w] = 1  # Mark position in binary matrix for meteor
    elif pixel == water_color:
        water_level.add(w)  # Add column to set of columns with water

# Print counts of stars, meteors, and meteors in water
print("Number of Stars: " + str(star))
print("Number of Meteors: " + str(meteor))
print("Meteors falling on the Water: " + str(meteors_in_water))

# Initialize the phrase
phrase = ""

# Convert the binary matrix to ASCII characters
for l in phrase_bin:
    l.reverse()  # Reverse the list to maintain the correct order of the phrase
    for i in range(0, len(l), 8):
        binary_group = l[i:i+8]  # Take 8 bits at a time

        pb = ""
        for g in binary_group:
            pb += str(g)  # Concatenate bits to form a binary string
        
        char_int = int(pb, 2)  # Convert binary string to integer
        
        ascii_character = chr(char_int)  # Convert integer to ASCII character
        phrase += ascii_character  # Append character to the phrase
    
print("(optional) Hidden Phrase: " + phrase)

# Remember to close the file when you're done
image.close()
