import os

def calcular_costo_envio(peso, distancia):
    costo_base = 5000
    adicional_peso = peso * 500
    recargo_distancia = 0
    if distancia > 100:
        recargo_distancia = (distancia - 100) * 100
    costo_total = costo_base + adicional_peso + recargo_distancia
    return costo_base, adicional_peso, recargo_distancia, costo_total

def mostrar_desglose(nombre_cliente, peso, distancia, costo_base, adicional_peso, recargo_distancia, costo_total):
    print("\nDesglose del costo de envío:")
    print(f"Cliente: {nombre_cliente}")
    print(f"Peso del paquete: {peso} kg")
    print(f"Distancia de envío: {distancia} km")
    print(f"Costo base: ${costo_base} CLP")
    print(f"Adicional por peso: ${adicional_peso} CLP")
    if recargo_distancia > 0:
        print(f"Recargo por distancia: ${recargo_distancia} CLP")
    print(f"Costo total de envío: ${costo_total} CLP")

def generar_archivo_envio(nombre_cliente, peso, distancia, costo_total):
    nombre_archivo = f"envio_{nombre_cliente}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Cliente: {nombre_cliente}\n")
        archivo.write(f"Peso del paquete: {peso} kg\n")
        archivo.write(f"Distancia de envío: {distancia} km\n")
        archivo.write(f"Costo total de envío: ${costo_total} CLP\n")
    print(f"\nArchivo '{nombre_archivo}' generado con éxito.")

def main():
    while True:
        try:
            nombre_cliente = input("Ingrese el nombre del cliente (máximo 30 caracteres): ").strip()
            if not nombre_cliente or len(nombre_cliente) > 30:
                raise ValueError("El nombre del cliente no puede estar vacío y debe tener un máximo de 30 caracteres.")
            
            peso = float(input("Ingrese el peso del paquete en kilogramos: "))
            if peso <= 0:
                raise ValueError("El peso debe ser un valor numérico positivo.")
            
            distancia = float(input("Ingrese la distancia de envío en kilómetros: "))
            if distancia <= 0:
                raise ValueError("La distancia debe ser un valor numérico positivo.")
            
            costo_base, adicional_peso, recargo_distancia, costo_total = calcular_costo_envio(peso, distancia)
            mostrar_desglose(nombre_cliente, peso, distancia, costo_base, adicional_peso, recargo_distancia, costo_total)
            generar_archivo_envio(nombre_cliente, peso, distancia, costo_total)
            
            otra_consulta = input("¿Desea calcular otro envío? (s/n): ").lower()
            if otra_consulta != 's':
                break
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    main()