#

print("*** Sistema de prestamo de libros ***")

DISTANCIA_KM = 3

tiene_credencial = input("Tienes credencial? (Si/No): ")
distancia_km_vivienda = int(input("Distancia de su vivienda en KM?: "))
vive_cerca = distancia_km_vivienda <= DISTANCIA_KM

se_puede_prestar_libro = tiene_credencial.lower() == "si" or vive_cerca == True

print(f"Se puede prestar el libro al usuario? {se_puede_prestar_libro}")