from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have emergency contact number.')
        return model
        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("Patient data updated sucesfully..!")
    
patient_info = {'name': 'yash', 'email':'yashsb@icici.com','linkedin_url': 'http://linkedin.com', 'age': '65', 'weight': 68.9, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details': {'email':'yashsb@gmail.com', 'phone':
    '1234567890', 'emergency': '783787768'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)