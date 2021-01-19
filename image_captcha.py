from captcha.image import ImageCaptcha
import matplotlib.pyplot as p
import random


value = []
for upper in range(65, 90):
    result = chr(upper)
    value.append(result)
    for lower in range(97, 122):
        result = chr(lower)
        value.append(result)

        for digit in range(48, 57):
            result = chr(digit)
            value.append(result)


def captcha_generator(captcha_size):
    empty = []
    char = value
    for i in range(captcha_size):
        char2 = random.choice(char)
        empty.append(char2)
    empty_variable = ''

    for j in empty:
        empty_variable += str(j)

    return empty_variable


def image_captcha(text):
    captcha = ImageCaptcha()
    image = captcha.generate_image(captcha_text)
    captcha.create_noise_curve(image, image.getcolors())
    captcha.create_noise_dots(image, image.getcolors())
    image_file = "./langscape" + '' + captcha_text + ".png"
    captcha.write(captcha_text, image_file)

    print(image_file + " has been created.")

    p.imshow(image)
    p.show()


#if __name__ == '__main__':
captcha_text = captcha_generator(captcha_size=6)

image_captcha(captcha_text)
