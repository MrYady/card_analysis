import json
import os

class TarjetaCredito:
    def __init__(self, numero, titular, expiracion, cvv, limite):
        self.numero = numero
        self.titular = titular
        self.expiracion = expiracion
        self.cvv = cvv
        self.limite = limite

    def __str__(self):
        # Ocultamos parte del número por seguridad en consola
        num_oculto = f"**** **** **** {self.numero[-4:]}"
        return f"Tarjeta: {num_oculto} | Titular: {self.titular} | Límite: {self.limite}"

class AnalizadorTarjetas:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.tarjetas = []

    def cargar_datos(self):
        if not os.path.exists(self.ruta_archivo):
            print(f"Error: No se encontró el archivo {self.ruta_archivo}")
            return False
        
        try:
            with open(self.ruta_archivo, 'r') as file:
                datos = json.load(file)
                self.tarjetas = [TarjetaCredito(**item) for item in datos]
                print(f"✅ Se han cargado {len(self.tarjetas)} tarjetas con éxito.")
                return True
        except Exception as e:
            print(f"Error al procesar el JSON: {e}")
            return False

    def realizar_auditoria(self):
            print("\n" + "="*50)
            print("SISTEMA DE AUDITORÍA DE TARJETAS - DATA.JSON")
            print("="*50)
            
            validas = 0
            invalidas = 0

            for t in self.tarjetas:
                print(t)
                if t.es_valida_luhn():
                    validas += 1
                else:
                    invalidas += 1
            
            print("-" * 50)
            print(f"RESUMEN FINAL:")
            print(f"✔️  Correctas: {validas}")
            print(f"❌  Erróneas:  {invalidas}")
            print("="*50)

class TarjetaCredito:
    def __init__(self, numero, titular, expiracion, cvv, limite):
        self.numero = str(numero).replace(" ", "").replace("-", "") # Limpieza básica
        self.titular = titular
        self.expiracion = expiracion
        self.cvv = cvv
        self.limite = limite

    def es_valida_luhn(self):
        """Implementación del Algoritmo de Luhn."""
        suma = 0
        num_digitos = len(self.numero)
        paridad = num_digitos % 2

        for i in range(num_digitos):
            digito = int(self.numero[i])
            
            # Multiplicar cada segundo dígito
            if i % 2 == paridad:
                digito *= 2
                if digito > 9:
                    digito -= 9
            
            suma += digito

        return (suma % 10) == 0

    def obtener_emisor(self):
        """Identifica el emisor basado en los primeros dígitos."""
        if self.numero.startswith('4'):
            return "VISA"
        elif self.numero.startswith(('51', '52', '53', '54', '55')):
            return "MASTERCARD"
        elif self.numero.startswith(('34', '37')):
            return "AMEX"
        return "DESCONOCIDO"

    def __str__(self):
        valida = "VÁLIDA" if self.es_valida_luhn() else "INVÁLIDA"
        num_oculto = f"**** **** **** {self.numero[-4:]}"
        return f"[{valida}] {self.obtener_emisor()} | {num_oculto} | Titular: {self.titular}"

# --- Ejecución Principal ---
if __name__ == "__main__":
    analizador = AnalizadorTarjetas("Data.json")
    
    if analizador.cargar_datos():
        analizador.realizar_auditoria()