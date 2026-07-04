from pydantic import BaseModel, EmailStr, AnyUrl, Field #ye class hame almost hamesha import karni padti hai
from typing import List, Dict, Optional


#Step 1 : create a pydantic model where we have defined our schema
class Patient(BaseModel):
    name:str

    email:EmailStr #ab ham koi bhi email denge to vo validate hoga against this custom datatype
    #now the code will run but agar maine email me se '@' hata diya to ye ek validation error raise karega.

    linkedin_url:AnyUrl

    age:int = Field(gt=0, lt=120) #with these two we are performing type validation #hamne field ki help se range definr kar di.

    weight:float = Field(gt=0) #so that koi negative values nahi de paaye #gt means greater than 

    married:Optional[bool] = False #matlab hai ki married ko by default false rakhna hai.

    allergies:Optional[List[str]] = None #means allergies khudme list hoga but uske andar ka har item string hoga
    #Mai inn above inputs ko optional bhi bana sakta hu by importing the optional library

    contact_details: Dict[str, str] #same goes for this 'Dict' #means contact details me ek dictionary import karenge jisme har key string honi chahiye aur har value bhi string honi chahiye.
    #jisme jo key hai vo bhi string hai and jo vlaue hai vo bhi string hai
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.allergies)
    print('inserted')

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.allergies) #ab maine agar allergies nahi insert kari hogi to None show karega
    print('updated')

#Step 2 : now we will make an object for our class. usse pehle we will create a dictionary
patient_info = {'name':'Jay', 'email': 'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1625', 'age':20, 'weight':60.0, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': {'phone': '89745920267'}} #isme hame saari details as per the data type defined deni hai warna code work nahi karega
 
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

