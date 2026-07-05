from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.allergies) #ab maine agar allergies nahi insert kari hogi to None show karega
    print('updated')