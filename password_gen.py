#استدعاء المكاتب 
import string
import random

#صناعة متغيرات تحتوي على قائمة من الحروف و الاأرقام و الرموز 
Letters = (string.ascii_letters)
dijits = (string.digits)
code = (string.punctuation)

#تحديد عدد كل نوع تريده بالباسورد الخاص يك 
while True:
    total_num = int (input("Please enter the total password:- "))
    Letters_num = int (input("Enter the number of characters in the password:- "))
    dijits_num = int (input("Enter the number of dijits in the password:- "))
    code_num = int (input("Enter the number of code in the password:- "))

    x = Letters_num + dijits_num + code_num

    #التحقق لو مجموع اعداد الرموز تساوي العدد الكلي لخانات الباسورد
    if x == total_num :
        password = random.choices (Letters , k= Letters_num) + random.choices (dijits , k= dijits_num) + random.choices (code , k= code_num)
        random.shuffle(password)
        print ("".join(password))
        break
    
    else:
        input("The sum of the entered numbers does not equal the total number. Please press Enter to redo.")
        continue
#Karim_Kridi
#Eng_syria
