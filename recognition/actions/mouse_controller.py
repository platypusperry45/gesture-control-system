import pyautogui


class MouseController:

    @staticmethod
    def left_click():

        pyautogui.click()

        print("Left Click")

    @staticmethod
    def right_click():

        pyautogui.rightClick()

        print("Right Click")

    @staticmethod
    def double_click():

        pyautogui.doubleClick()

        print("Double Click")

    @staticmethod
    def move(dx, dy):

        pyautogui.moveRel(dx, dy, duration=0.1)

    @staticmethod
    def scroll(amount):

        pyautogui.scroll(amount)