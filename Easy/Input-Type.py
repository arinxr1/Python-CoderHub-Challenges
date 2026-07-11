from typing import List

def input_type(value: str) -> str:
    try:
        int(value)
        return "integer"
    except:
        try:
            float(value)
            return "double"
        except:
            return "string"



print(input_type("Hello World"))