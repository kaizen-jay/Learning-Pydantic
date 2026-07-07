from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

#Ab patient model ka pydantic object banane se pehle hame Address ka pydantic object banana padega

address_dict= {'city': 'panna', 'state':'MP', 'pin':'488001'} #ab iss raw dictionary se Address pydantic model ka object banayenge

address1 = Address(**address_dict)#ye Address class ka object hai jaha pe ham unpack karenge address_dict ko 

#Ab ham patient ke liye dictionary banayenge

patient_dict = {'name':'Jay', 'gender': 'male', 'age':20, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)

#Ab agar ham chaahe to iss address class se kuch bhi nikal sakte hai jaise 

print(patient1.name)
print(patient1.address.city) #aap patient1 ke address me jaake city bhi nikal sakte ho
print(patient1.address.pin) #similarly

'''Ab ye Address wali class patient ke alawa kahi aur bhi use ho sakti hai '''

#Better organization of related data (eg: vitals, address, insurance)

#Reusability: use Vitals in multiple models (eg. patient, MedicalRecord)

#Readability: easy for developers and api consumers to understand

#Validation: Nested models are validated automatically, no extra work needed 


