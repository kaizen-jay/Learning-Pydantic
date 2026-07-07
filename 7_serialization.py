from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str = 'Male' #default value dedi hamne ise male ki
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict= {'city': 'panna', 'state':'MP', 'pin':'488001'}

address1 = Address(**address_dict)

patient_dict = {'name':'Jay', 'age':20, 'address': address1} #bts isme male wali field automatically aa jayegi 

patient1 = Patient(**patient_dict)

#Now what we do is using the builtin pydantic methods like model_dump()

temp = patient1.model_dump() #existing pydantic model object ko python dictionary me convert kar dega
#we can also mention ki kon konse fields hame export karne hai jaise 
temp1 = patient1.model_dump(include=['name']) #similarl in exclude
temp2 = patient1.model_dump(exclude=['name', 'gender'])#also:
temp3 = patient1.model_dump(exclude={'address':['state']})
temp4 = patient1.model_dump(exclude_unset=True) #matlab ki object banate time jo values set nahi ki gayi hai to jab ham export karenge model ko to usme gender nahi dikhayi dega
print(temp)
print(temp1)
print(temp2)
print(temp3)
print(type(temp))

#agar hame json chahiye to ham use karte hai model_dump_json()


