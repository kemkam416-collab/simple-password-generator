#67مشروع رقم
#النداء على المكتبات لتفعيل الخيار العشوائي
import random

#قائم فيها كلمات عشوائية
all_words = ["karim" , "nour" , "Iraq" , "syria" , "mohamed" , "Lebanon" , "Egypt" ]

#قايمة تحتوي على مجموعة اشكال بصيغة الاسكي
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#قايمة تحتوي علي خيار لكلمة عشوائية من قائمة all_words
word_chois = random.choice(all_words)

#قائمة تحتوي على شرطات تحتية بعدد احرف word_chois و يخزن بها ادخال المستخدم ي حال كان صحيحا
words = ["_"] * int(len(word_chois[::1]))
print(*words)

num = 7
#هنا يوجد لوب يختبر هل عدد المحاولات انتهى او هل الكلمة المختارة اكتملت
while (num != 0) and ("".join(words) != word_chois):

    #مدخل يقول للمستخدم خمن حرف
    userin = input("pleas enter letter :- ").lower()

    #هنا يوجد لوب يختبر هل الحرف المدخل من المستخدم موجود في اي موقع من القايمة
    for index in range(len(words)):

        #شرط يقول لو المدخل  كان صحيح يضيفه الى قايمة words 
        if userin == word_chois[index]:

            #شرط يقول لو المدخل فعلا تم ادخاله سابقا اطبع له 
            if userin in words:
                print("This option actually exists")
            words[index] = userin

    #شرط يقول لو المدخل مش موجود في قايمة words نقص محاولة  و اطبع الاسكي معدم        
    if userin not in words:
        num -= 1
        print(HANGMANPICS[6-num])
    print(*words)
    print("The number of your attempts = " , num)

#Karim kridi
#Eng syria
