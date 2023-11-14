import random

def randomNumber():
    Number = random.randint(1, 100)
    
    while True:
        try:
            userInput = int(input("ทายตัวเลขที่มีค่าอยู่ที่ 1-100: "))
            if userInput == Number:
                print("ยินดีด้วยคุณทายถูก!")
                break
            elif userInput < Number:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
            else:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

randomNumber()