import datetime
import os
os.makedirs("data",exist_ok=True)

def whether_valid():
    whether_valid=0
    while whether_valid<1:
        mood=input("input your mood today: ").lower()
        if mood in ["happy","relaxed","apathetic","sad","angry"]:
            whether_valid+=1
        else:
            whether_valid=whether_valid
    return mood

def mood_to_num(user_mood):
    num_mood=0
    if user_mood=="happy":
        num_mood=2
    elif user_mood=="relaxed":
        num_mood=1
    elif user_mood=="apathetic":
        num_mood=0
    elif user_mood=="sad":
        num_mood=-1
    elif user_mood=="angry":
        num_mood=-2
    return str(num_mood)

def add_mood_in_diary(num_mood,input_date):
    mood_diary=os.path.join("data","mood_diary.txt")
    with open(mood_diary,"a") as file:
        file.write(input_date+","+num_mood+"\n")
    
def read_mood_diary():
    mood_diary=os.path.join("data","mood_diary.txt")
    if os.path.exists(mood_diary):
        with open(mood_diary,"r") as file:
            return file.readlines()
    else:
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
    if once_per_day(str_date):
        print("Sorry, you have already entered your mood today.")
        return
    users_mood=whether_valid()
    num_mood=mood_to_num(users_mood)
    add_mood_in_diary(num_mood,str_date)
    all_records=read_mood_diary()
    if len(all_records)<7:
        return
    recent_records=all_records[-7:]
    moods_list=[]
    for lines in recent_records:
        lines_split=lines.split(",")
        str_mood=lines_split[1]
        int_mood=int(str_mood)
        moods_list.append(int_mood)
    whether_happy=moods_list.count(2)
    whether_relaxed=moods_list.count(1)
    whether_apathetic=moods_list.count(0)
    whether_sad=moods_list.count(-1)
    whether_angry=moods_list.count(-2)
    average_mood=round((whether_angry*(-2)+whether_apathetic*0+whether_happy*2+whether_relaxed*1+whether_sad*(-1))/7)
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







    

