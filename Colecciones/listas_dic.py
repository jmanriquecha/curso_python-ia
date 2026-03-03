print("### Lista de personas ###")

personas = [
    {
        "nombre": "Jorge",
        "apellido": "Manrique",
        "edad": 20
    },
    {
        "nombre": "Yaneth",
        "apellido": "Gonzalez",
        "edad": 15
    }
]

#for i, persona in enumerate(personas):
for persona in personas:
    print(f"""
Nombre: {persona.get('nombre', 'no existe')}
Apellido: {persona.get('apellido', 'El apellido no existe')}
Edad: {persona.get('edad', 'La edad no existe')}""")

