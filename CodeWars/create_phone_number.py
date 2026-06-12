### Crear Numero de telefono ###

def create_phone_number(n):
    primeros = n[0:3]
    segundos = n[3:6]
    terceros = n[6:10]
    
    str_primeros = ''.join(str(x) for x in primeros)
    str_segundos = ''.join(str(x) for x in segundos)
    str_terceros = ''.join(str(x) for x in terceros)
    
    return f"({str_primeros}) {str_segundos}-{str_terceros}"