from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

@model_validator(mode='after') #we are using whole pydantic model to ham class define nahi kar rahe, just the mode and also default one 
#now we will create a method
def validate_emergency_contact(cls, model): #ab iss method ko apne aap 2 values milengi, class and whole model
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency number')
    return model



def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.weight)
    print(patient.allergies) #ab maine agar allergies nahi insert kari hogi to None show karega
    print('updated')

patient_info = {'name':'jay', 'email': 'abc@hdfc.com',  'age':'65', 'weight':60.0, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': {'phone': '89745920267'}} 

patient1 = Patient(**patient_info)# isi step me vlaidation perform hota hai aur type coersion bhi 

updated_patient_data(patient1)
