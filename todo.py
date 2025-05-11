import json as js
import os


if os.path.exists("todo.json"):
    print("hello")
else:
    with open("todo.json" , 'w') as mio:
        pass

data = dict()
data['works'] = []

def add():
    new_todo = dict()
    new_todo['title'] = input("enter ur job")
    new_todo['stats'] = True if input("enter true for done and anything for not") == "true" else False
    data['works'].append(new_todo)
    

def change_stats():
    existance = False
    name = input("what job u whant to change stats?\n")
    for i in range(0,len(data['works'])):
        if name == data['works'][i]['title']:
            existance =True
            data['works'][i]['stats'] = True
    if existance:
        print("well done!")
    else:
        print("title not available")

def delete():
    existance = False
    name = input("enter job you want to delete:\n")
    for i in range(0,len(data['works'])):
        if name == data['works'][i]['title']:
            existance = True
            del(data['works'][i])
            break
    if existance:
        print("well done!")
    else:
        print("title not available")

def show_all():
    
    for i in data['works']:
        print(i)
with open("todo.json" , 'r') as myfile:
    data = js.load(myfile)
    print(data)
while True:
    try:
        action = int(input("enter:\n1: to add todo\n2: change stats of a todo\n3: delete a todo\n4: show all todos\n5: quit\n"))
    except:
        print("wrong input!")
        continue
    match action:
        case 1:
            add()
        case 2:
            change_stats()
        case 3:
            delete()
        case 4:
            show_all()
        case 5:
            with open("todo.json" , 'w') as myfile:
                js.dump(data , myfile)

            exit()