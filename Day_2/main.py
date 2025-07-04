import requests
import json
list_a = []

def append_task(task):
    list_a.append(task)
append_task("Today is big")
append_task("Tomorrow is bigger")

def remove_task(index):
    list_a.remove(list_a[index])
remove_task(0)

def update_task(index,task):
    for i in range(len(list_a)):
        if index == i:
            list_a[i] = task
            break
    else:
        print("Error")
update_task(0,"today is good")

class Parent:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def walk(self):
        return f"{self.fname} is going for a walk"
    def __str__(self):
        return f"FirstName:{self.fname},LastName:{self.lname},Age:{self.age}"

class Child(Parent):
    def __init__(self,fname,lname,age,toys):
        super().__init__(fname,lname,age)
        self.toys = toys
    def play(self):
        return f"{self.fname} is playing hide and seek"
    def __str__(self):
        return f"FirstName:{self.fname} Has toys:{self.toys}"
child = Child("Dave","Manson",10,True)
print(child.walk())
print(child.play())
print(child)

class Bike:
    def __init__(self,model,wheels,speed):
        self.wheels = wheels
        self.speed = speed
        self.model = model
    def speedUp(self,speed):
        if speed < 10:
            self.speed += speed
            print("Maximum speed reached ",self.speed)
    def __str__(self):
        return f"Model:{self.model}"
    
class ElectricBike(Bike):
    def __init__(self,model,wheels,speed,electrical):
        super().__init__(model,wheels,speed)
        self.electrical = electrical
    def speedUp(self, speed):
        if speed < 25:
            self.speed += speed
            print("Maximum speed reached ",self.speed)
    def __str__(self):
        return f"Model:{self.model} Electrical:{self.electrical}"

mark1 = ElectricBike("Kutsot",4,25,True)
mark1.speedUp(24)
print(mark1)


response = requests.get("http://numbersapi.com/random/trivia?json")
data = response.json()
print("Number Fact:", data["text"])

