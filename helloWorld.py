import cowsay
import time 
import webbrowser
import pyautogui

name=(input('What is your name?\n>>> '))
name=name.upper()
output='Hello ' +name+ '! Can you pick a number between 1 and 6? ツ'
cowsay.cow(output)

pyautogui.position()
pyautogui.size()
chosen=-1   
while(chosen!=0):
   chosen=int(input('>>> #')) 
   match chosen:
    case 1:
        cowsay.cow("HELLO WORLD! #1 - Cowsay is ME! Pick another number!")
    case 2:
        cowsay.cow("Let's see project #2 --Chip vs Frog---")
        time.sleep(5) 
        webbrowser.open('https://scratch.mit.edu/projects/800708237/', new=2)
    case 3:
        cowsay.cow("#3 a calculator...  \_(ツ)_/¯ to calculate things... ")
        time.sleep(5) 
        webbrowser.open('calculator.html', new=2)
    case 4:
        cowsay.cow("#4 Group progect, LECCAirlines ✈️")
        time.sleep(5) 
        webbrowser.open('https://www.agency.mktech.co.mz/', new=2)
    case 5:
        cowsay.cow('#5 Lost and Found!')
       webbrowser.open('https://youtube.com/shorts/qjx5sKz1u1A?feature=share', new=2)
    case 6:
        cowsay.cow('6. Look mom! No Hands!')
        time.sleep(2)
        pyautogui.moveTo(519,1060, duration = 1)
        pyautogui.alert(text='I KNOW WHERE YOU LIVE', title='👻👻 (BEHIND YOU)', button='NO WAY!')
        webbrowser.open('https://typewritesomething.com/', new=2)
        pyautogui.click()
        time.sleep(5)
        pyautogui.typewrite(message=' LOOK BEHIND YOU, ', interval=0.5,) 
        pyautogui.typewrite(message=name.upper(), interval=1)
        pyautogui.typewrite(message='!', interval=2) 
        time.sleep(5)
        webbrowser.open('https://i.imgur.com/EcUAQ04.gif', new=2)
    case _:
        print("Thank you for coming to our stand <3")
