from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in between 50 character.', examples=['Yash', 'etc..'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float = Field(gt=0)
    married: Annotated[bool, Field(default=None, description="Is the patient married or not.")]
    allergies: List[str]
    contact_details: Dict[str, str]
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted sucesfully..!")
    
patient_info = {'name': 'yash', 'email':'yashsb@gmail.com','linkedin_url': 'http://linkedin.com', 'age': 21, 'weight': 68.9, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details': {'email':'yashsb@gmail.com', 'phone':
    '1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
