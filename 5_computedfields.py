from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @computed_field() #decorator
    @property #decorator
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2) #round means rounding off upto two decimal places
        return bmi

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age) #yaha dono jagah pe hamne OOP lagaya hai
    print(patient.weight)
    print('BMI', patient.bmi)
    print(patient.allergies) #ab maine agar allergies nahi insert kari hogi to None show karega
    print('updated')

patient_info = {'name':'jay', 'email': 'abc@hdfc.com',  'age':'65', 'weight':60.0, 'height': 1.72, 'married':False, 'allergies':['pollen', 'dust'], 'contact_details': {'phone': '89745920267'}} 

patient1 = Patient(**patient_info)# isi step me vlaidation perform hota hai aur type coersion bhi 

updated_patient_data(patient1)
