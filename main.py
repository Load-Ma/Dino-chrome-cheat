from PIL import ImageGrab, ImageDraw, Image
import sys
from time import sleep
import pyautogui


def cheat():
    sleep(1)
    x = 0
    # size 300/640
    # color gris clair 172;172;172

    # rgb = ImageGrab.grab().load()[200, 640]
    # photo = ImageGrab.grab()
    # draw = ImageDraw.Draw(photo)
    # draw.line((100, photo.size[1]/2+100, 200, photo.size[1]/2+100), fill=128)
    # photo.save(sys.stdout, "PNG")
    # photo.show()
    # print("\n")
    # print(photo.size[1]/2+100)

    while True:
        sleep(0.1)
        pyautogui.keyDown('down')
        rgb = ImageGrab.grab().load()[400, 650]
        if (rgb[0] == 172 and rgb[1] == 172 and rgb[2] == 172) or (rgb[0] == 0 and rgb[1] == 0 and rgb[2] == 0) or (rgb[0] == 0 and rgb[1] == 8 and rgb[2] == 8):
            pyautogui.keyUp('down')
            pyautogui.keyDown('space')
            sleep(0.1)
            pyautogui.keyUp('space')

        x += 1


if __name__ == '__main__':
    cheat()