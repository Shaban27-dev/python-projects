#          DAY-8
# Unit Converter (kg ↔ pounds, cm ↔ inches).
def kg_to_pounds(n1):
    return n1 * 2.2

def pounds_to_kg(n1):
    return n1 * 0.45

def cm_to_inches(n1):
    return n1 * 0.39

def inches_to_cm(n1):
    return n1 * 2.54

operations = {
    "kg_to_pounds": kg_to_pounds,
    "pounds_to_kg": pounds_to_kg,
    "cm_to_inches": cm_to_inches,
    "inches_to_cm": inches_to_cm,
}

def converter():
    print("Available conversions:")
    for symbols in operations:
        print(symbols)

    choice = input("Type the conversion you want(exactly as shown): ").lower()

    if choice not in operations:
        print("You typed an invalid conversion.")
        return
    
    value = float(input("Enter the value you want to convert: "))
    result = operations[choice](n1=value)
    print(f"Result: {result}")
    
converter()