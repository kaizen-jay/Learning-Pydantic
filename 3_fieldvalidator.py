from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @field_validator('email') #yaha pe ham batayenge ki field validator kis field ke oopar apply ho
    @classmethod #we have to define this too
    def email_validator(cls, value): #we have to check if the 'value' has 'icici.com or hdfc.com' in it 
        #pehle ham list bana lenge
        valid_domains=['hdfc.com', 'icici.com']
        #ab ham apne email se '@' ke baad wala part extract karenge eg. abc@gmail.com
        domain_name = value.split('@')[-1] #-1 means hame last wali value chahiye in that email after split

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    



def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.allergies) #ab maine agar allergies nahi insert kari hogi to None show karega
    print('updated')

patient_info = {'name':'Jay', 'email': 'abc@hdfc .com',  'age':20, 'weight':60.0, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': {'phone': '89745920267'}} 

patient1 = Patient(**patient_info)

updated_patient_data(patient1)