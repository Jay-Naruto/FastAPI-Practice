import json
from fastapi.exceptions import HTTPException
from src.parser.validate import validate_data
structure = {
        "appointment_id": "",
        "appointment_datetime": "",
        "patient": {
            "id": "",
            "first_name": "",
            "last_name": "",
            "dob": "",
            "gender": ""
        },
        "provider": {
            "id": "",
            "name": ""
        },
        "location": "",
        "reason": ""
    }

def hl7_parse():
    try:
        with open('src/parser/input.hl7','r') as file:
            hl7_message = file.read()
        sections = hl7_message.split('\n')
        for section in sections:
            section = section.strip()
            field = section.split('|')

            if field[0] == 'SCH':
                if len(field) > 1:
                    structure['appointment_id'] = field[1].split('^')[0]
                if len(field) > 3:
                    structure['appointment_datetime'] = field[3]
                if len(field) > 5:
                    structure['location'] = field[5]
                
            elif field[0] == "PID":
                if len(field) > 3:
                    structure['patient']['id'] = field[3].split('^')[0]
                if len(field) >  5:
                    full_name = field[5].split('^')
                    if len(full_name) > 0:
                        structure['patient']['last_name'] = full_name[0]
                    if len(full_name) > 1:
                        structure['patient']['first_name'] = full_name[1]
                if len(field) > 7:
                    structure['patient']['dob'] = field[7]
                if len(field) > 8:
                    structure['patient']['gender'] = field[8]
            
            elif field[0] == 'PV1':
                if len(field) > 3:
                    provider = field[3].split('^')
                    structure['provider']['id'] = provider[0]

                    if len(provider) > 2:
                        structure['provider']['name'] = f"{provider[2]} {provider[1]}"
                    else:
                        structure['provider']['name'] = provider[1]
        validate_data(structure)
        return structure
        
    except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

