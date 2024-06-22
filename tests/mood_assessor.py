import datetime
import os
os.makedirs("data",exist_ok=True)

def whether_valid():
    whether_valid=0
    while whether_valid<1:
        mood=input("What's your mood today: ").lower()
        if mood in ["happy","relaxed","apathetic","sad","angry"]:
            whether_valid+=1
        else:
            whether_valid=whether_valid
    return str(mood)

def add_mood_in_diary(user_mood,input_date):
    mood_diary=os.path.join("data","mood_diary.txt")
    if user_mood=="happy":
        with open(mood_diary,"a") as file:
            file.write(str(input_date)+"2\n")
    elif user_mood=="relaxed":
        with open(mood_diary,"a") as file:
            file.write(str(input_date)+"1\n")
    elif user_mood=="apathetic":
        with open(mood_diary,"a") as file:
            file.write(str(input_date)+"0\n")
    elif user_mood=="sad":
        with open(mood_diary,"a") as file:
            file.write(str(input_date)+"-1\n")
    elif user_mood=="angry":
        with open(mood_diary,"a") as file:
            file.write(str(input_date)+"-2\n")
    
def read_mood_diary():
    mood_diary=os.path.join("data","mood_diary.txt")
    if os.path.exists(mood_diary):
        with open(mood_diary,"r") as file:
            return file.readlines()
    return []
    
def once_per_day(current_date):
    context=read_mood_diary()
    for records in context:
        if records.startswith(current_date):
            return True
        else:
            return False
        
def assess_mood():
    str_date=str(datetime.date.today())
    for i in range(7):
        if once_per_day(str_date):
            print("Sorry, you have already entered your mood today.")
            return
        users_mood=whether_valid()
        add_mood_in_diary(users_mood,str_date)
        all_records=read_mood_diary()
        mood_ckeck=all_records[-7:]
        if len(all_records)<7:
            return
        whether_happy=0
        whether_relaxed=0
        whether_apathetic=0
        whether_sad=0
        whether_angry=0
        for lines in mood_ckeck:
            line_split=lines.split()
            mood_type=int(line_split[1])
            if mood_type==2:
                whether_happy+=1
            elif mood_type==1:
                whether_relaxed+=1
            elif mood_type==0:
                whether_apathetic+=1
            elif mood_type==-1:
                whether_sad+=1
            elif mood_type==-2:
                whether_angry+=1
        average_mood=round((whether_angry+whether_apathetic+whether_happy+whether_relaxed+whether_sad)/7)
        if whether_happy>=5:
            print("Your diagnosis: manic!")
        elif whether_sad>=4:
            print("Your diagnosis: depressive!")
        elif whether_apathetic>=6:
            print("Your diagnosis: schizoid!")
        else:
            if average_mood==2:
                print("Your diagnosis: happy!")
            elif average_mood==1:
                print("Your diagnosis: relaxed!")
            elif average_mood==0:
                print("Your diagnosis: apathetic!")
            elif average_mood==-1:
                print("Your diagnosis: sad!")
            elif average_mood==-2:
                print("Your diagnosis: angry!")







    

