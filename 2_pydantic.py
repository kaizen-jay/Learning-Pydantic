from pydantic import BaseModel #ye class hame almost hamesha import karni padti hai
from typing import List, Dict
#Step 1 : create a pydantic model where we have defined our schema
class Patient(BaseModel):
    name:str
    age:int #with these two we are performing type validation
    weight:float
    married:bool
    allergies:List[str]
    contact_details: Dict[str, str] #means contact details me ek dictionary import karenge
    #jisme jo key hai vo bhi string hai and jo vlaue hai vo bhi string hai

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print('inserted')

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print('updated')

#Step 2 : now we will make an object for our class. usse pehle we will create a dictionary
patient_info = {'name':'Jay', 'age':20, 'weight':60.0, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': {'email':'abc@gmail.com', 'phone': '89745920267'}}
 
    #dictionary ki help se mai apne object ko intantiate karunga
patient1 = Patient(**patient_info)

#Step 3: ab hame simply iss patient1 object ko apne function ke paas oopar bjejenge 
#hamne oopar jaake function me object ko pass kar diya hai 
#now we will run the program 
updated_patient_data(patient1)

'''Ab aap kitne bhi function bana lo we can use only one object
like the patient1 in every function and it made the code more
easy and effecient without typing it individually many times. 
This is what pydantic helps in'''


#Iss code me hamne type validation hi dekha hai bas
#Data validation on the upcoming course

