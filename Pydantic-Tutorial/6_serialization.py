from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str
    
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'pune', 'state': 'maharashtra', 'pin': '411046'}

address1 = Address(**address_dict)

patient_dict = {'name': 'yash', 'gender': 'male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=['name'])
# temp = patient1.model_dump_json()

print(temp)
print(type(temp))
    