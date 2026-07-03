#we're recieving patient's data and inserting it in our database


# def insert_patient_data(name, age):

#     print(name)
#     print(age)
#     print('inserted into database')


    #koi junior programmer iss function ko use karega in order to insert data into the database
    #python me dynamic typing hoti hai static nahi like java or C++
    #matlab ki ham ek hi variable me alag alag type ki values store kar sakte hai
    #As a programmer hame aisa hone se rokna hai to what we can do is 
    #I can use "type hinting" i.e 
    #I will initalize what kind of datatype can be entered into the variables
    # for example insert_patient_data(name: str, age: int)
'''Now as a programmer what i will do is i will make it  a strict code like:'''

def insert_patient_data(name, age):

    if type(name) == str and type(age) == int:
        if age < 0:
              raise ValueError('Age cannot be negative')
        else:
         print(name)
         print(age)
         print('inserted into the database')
    else:
         raise TypeError('Incorrect datatype')
 
 #Lets make another function similar to the insert function wit everything similar
 #Ab hame sab cheeze same karni hai to hame baar baar aise functions likhne honge which is not sacalable

def update_patient_data(name, age):

    if type(name) == str and type(age) == int:
        if age < 0:
              raise ValueError('Age cannot be negative')
        else:
         print(name)
         print(age)
         print('updated')
    else:
         raise TypeError('Incorrect datatype')
insert_patient_data('Jay', -1)
