from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float 
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
        
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.calculate_bmi)
    print("Patient data updated sucesfully..!")
    
patient_info = {'name': 'yash', 'email':'yashsb@icici.com','linkedin_url': 'http://linkedin.com', 'age': '21', 'weight': 68.9, 'height': 1.72, 'married': True, 'allergies':['pollen', 'dust'], 'contact_details': {'email':'yashsb@gmail.com', 'phone':
    '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)