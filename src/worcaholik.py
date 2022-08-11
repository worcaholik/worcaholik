#! /usr/bin/env python3
import pyautogui, time, os, random, string
from datetime import datetime

VERSION = '1.0.0'

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    characters = list(string.ascii_letters + string.digits + "_!?@#$%&*()-+<>")


    start = datetime.now()

    clear()

    print(' _  _  _                        _           _  _ _ ')    
    print('(_)(_)(_)                      | |         | |(_) |    ')
    print(' _  _  _  ___   ____ ____ _____| |__   ___ | | _| |  _ ')
    print('| || || |/ _ \ / ___) ___|____ |  _ \ / _ \| || | |_/ )')
    print('| || || | |_| | |  ( (___/ ___ | | | | |_| | || |  _ ( ')
    print(' \_____/ \___/|_|   \____)_____|_| |_|\___/ \_)_|_| \_)')

    print(f'                                            (Ver:{VERSION})\n')
    print("Start =", start.strftime("%H:%M:%S"))
    print('\n\n')

    try:
        while True:
            sleep = (random.randint(1,59))
            next_char = characters[random.randint(0, len(characters)-1)]

            print ("\033[A                             \033[A")
            print ("\033[A                             \033[A")
            print(f" Next char will be '{next_char}' in {sleep} second." if sleep < 2 else f" Next char will be '{next_char}' in {sleep} seconds.")
            print(' Running... (press CTRL + C to EXIT)')
            time.sleep(sleep)        
            pyautogui.press(next_char)

    except KeyboardInterrupt as err:
        end = datetime.now()
        final = end - start
        
        final_in_s = final.total_seconds()
        hours = divmod(final_in_s, 3600)[0]
        minutes = divmod(final_in_s, 60)[0]
        print('')
        print ("\033[A                             \033[A")
        seconds = final.total_seconds()
        print(f'\nEnd = {end.strftime("%H:%M:%S")}')
        print(f' AFK: {round(minutes):02d}m\n')

if __name__ == "__main__":
    main()