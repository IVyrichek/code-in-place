from simpleimage import SimpleImage
INSTA_SIZE = 270
SHIFT = 35

def main():
    check_background = False
    insta_image = SimpleImage.blank(INSTA_SIZE, INSTA_SIZE)

# Show the greeting picture to user
    print('')
    print("Oregon loves you! Let's share your moments and create a custom postcard!")
    theme = int(input("Now select background - 1 for lavender, 2 for painted hills: "))

# Check the background selection is valid
    while not check_background:
        if theme == 1:
            postcard = SimpleImage('pictures/lavender.jpg')
            print("Great choice, same vibe!")
            check_background = True
        elif theme == 2:
            postcard = SimpleImage('pictures/hills.jpg')
            print("Great choice, same vibe!")
            check_background = True
        else:
            print("Oops, smth went wrong, please choose 1 or 2") 

# Upload insta photos from user and minimize the size to the constant INSTA_SIZE
    print('')
    file1 = get_file('first','pictures/me.jpg')
    photo1 = SimpleImage(file1)
    photo1.make_as_big_as(insta_image)
    print('')
    file2 = get_file('second','pictures/boys.jpg')
    photo2 = SimpleImage(file2)
    photo2.make_as_big_as(insta_image)
    print('')
    file3 = get_file('third','pictures/we.jpg')
    photo3 = SimpleImage(file3)
    photo3.make_as_big_as(insta_image)

# Putting photos on the postcard
    put_insta_image(postcard, photo1, 1)
    put_insta_image(postcard, photo2, 2)
    put_insta_image(postcard, photo3, 3)
    postcard.show()

# Insert one photo on the postcard function, n - number of photo 
def put_insta_image(result, photo, n):
    for x in range(INSTA_SIZE):
        for y in range(INSTA_SIZE):
            pixel = photo.get_pixel(x, y)
            result.set_pixel(x + SHIFT, y + SHIFT*n + INSTA_SIZE*(n - 1), pixel)
    return(result)

def get_file(n, default):
    # Read image file path from user
    filename = input('Enter '+n+' insta image file (or press enter for default): ')
    if filename == '':
        filename = default
    return filename


if __name__ == '__main__':
    main()
