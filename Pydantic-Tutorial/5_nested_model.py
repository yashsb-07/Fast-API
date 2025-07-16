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

print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)
 
    