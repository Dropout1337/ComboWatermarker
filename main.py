import os
import keyboard

banner = '''\u001b[34m____ ____ _  _ ___  ____    _ _ _ ____ ___ ____ ____ _  _ ____ ____ _  _ 
|    |  | |\/| |__] |  |    | | | |__|  |  |___ |__/ |\/| |__| |__/ |_/  
|___ |__| |  | |__] |__|    |_|_| |  |  |  |___ |  \ |  | |  | |  \ | \_ \u001b[37m'''

class Watermark():
    def All(type, author, checker):
        try:
            with open('Combos.txt', "r") as Combo_File: 
                for line in Combo_File:
                    line = line.replace('\n', '')
                    Account_Combo = line.split(':')
                    email = Account_Combo[0]
                    password = Account_Combo[1]
                    with open('New_Combo.txt', "a+") as f:
                        f.write(f'{email}:{password} | Type: {checker} | Checked By: {author} | Checker: {checker}\n')
                print('\n[\u001b[34mWATERMARK\u001b[37m] Success')
                input()
                os._exit(0)    
        except IndexError:
            print('\n[\u001b[34mWATERMARK\u001b[37m] Invalid Combo Syntax, Example dropout@gmail.com:FuckingNoLife123')   
            input()
            os._exit(0)      

    def Type(type):
        try:
            with open('Combos.txt', "r") as Combo_File: 
                for line in Combo_File:
                    line = line.replace('\n', '')
                    Account_Combo = line.split(':')
                    email = Account_Combo[0]
                    password = Account_Combo[1]
                    with open('New_Combo.txt', "a+") as f:
                        f.write(f'{email}:{password} | Type: {type}\n')
                print('\n[\u001b[34mWATERMARK\u001b[37m] Success')
                input()
                os._exit(0)     
        except IndexError:
            print('\n[\u001b[34mWATERMARK\u001b[37m] Invalid Combo Syntax, Example dropout@gmail.com:FuckingNoLife123')   
            input()
            os._exit(0)      

    def Author(author):
        try:
            with open('Combos.txt', "r") as Combo_File: 
                for line in Combo_File:
                    line = line.replace('\n', '')
                    Account_Combo = line.split(':')
                    email = Account_Combo[0]
                    password = Account_Combo[1]
                    with open('New_Combo.txt', "a+") as f:
                        f.write(f'{email}:{password} | Checked By: {author}\n')
                print('\n[\u001b[34mWATERMARK\u001b[37m] Success')
                input()
                os._exit(0)   
        except IndexError:
            print('\n[\u001b[34mWATERMARK\u001b[37m] Invalid Combo Syntax, Example dropout@gmail.com:FuckingNoLife123')   
            input()
            os._exit(0)        

    def Checker(checker):
        try:
            with open('Combos.txt', "r") as Combo_File: 
                for line in Combo_File:
                    line = line.replace('\n', '')
                    Account_Combo = line.split(':')
                    email = Account_Combo[0]
                    password = Account_Combo[1]
                    with open('New_Combo.txt', "a+") as f:
                        f.write(f'{email}:{password} | Checker: {checker}\n')
                print('\n[\u001b[34mWATERMARK\u001b[37m] Success')
                input()
                os._exit(0)   
        except IndexError:
            print('\n[\u001b[34mWATERMARK\u001b[37m] Invalid Combo Syntax, Example dropout@gmail.com:FuckingNoLife123')      
            input()
            os._exit(0)     

if __name__ == "__main__":
    os.system('cls & title [Combo Watermarker] By Dropout')
    print(
        f'{banner}\n',
        '\n[\u001b[34m1\u001b[37m] All',
        '\n[\u001b[34m2\u001b[37m] Combo Type',
        '\n[\u001b[34m3\u001b[37m] Author',
        '\n[\u001b[34m4\u001b[37m] Checker'
        )
    while True:
        try:
            if keyboard.is_pressed('1'):
                keyboard.write('\b')
                cmd_type = input('\n\u001b[34m>\u001b[37m Combo Type: ')
                author = input('\u001b[34m>\u001b[37m Author: ')
                checker = input('\u001b[34m>\u001b[37m Checker: ')
                Watermark.All(cmd_type, author, checker)
                break
            elif keyboard.is_pressed('2'):
                keyboard.write('\b')
                cmd_type = input('\n\u001b[34m>\u001b[37m Combo Type: ')
                Watermark.Type(cmd_type)
                break
            elif keyboard.is_pressed('3'):
                keyboard.write('\b')
                author = input('\n\u001b[34m>\u001b[37m Author: ')
                Watermark.Author(author)
                break
            elif keyboard.is_pressed('4'):
                keyboard.write('\b')
                checker = input('\n\u001b[34m>\u001b[37m Checker: ')
                Watermark.Checker(checker)
                break
        except:
            continue    