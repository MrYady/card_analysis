# 💳 Credit Card Analyzer (Python POO)

Sistema robusto desarrollado en Python bajo el paradigma de **Programación Orientada a Objetos (POO)** para la carga, validación y auditoría de tarjetas de crédito mediante el **Algoritmo de Luhn**.

Este proyecto simula la lógica de una pasarela de pagos web, procesando datos desde una fuente JSON y realizando verificaciones de seguridad y capacidad financiera.

## 🚀 Características Principales

* **Validación de Integridad:** Implementación del Algoritmo de Luhn (Módulo 10) para descartar números de tarjeta falsos o erróneos.
* **Identificación de Emisores:** Detección automática de redes de pago (VISA, MasterCard, AMEX) basada en los prefijos del PAN (Primary Account Number).
* **Gestión de Datos JSON:** Carga dinámica de información desde `Data.json`, facilitando la integración con bases de datos externas.
* **Simulación de Riesgo:** Filtro avanzado para validar si una cuenta posee el límite de crédito suficiente para una transacción específica.
* **Seguridad en Consola:** Máscara de datos sensibles para proteger la privacidad de los números de tarjeta durante el análisis.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Formato de Datos:** JSON (JavaScript Object Notation)
* **Arquitectura:** Programación Orientada a Objetos (Clases `TarjetaCredito` y `AnalizadorTarjetas`).

## 📂 Estructura del Proyecto

```text
.
├── Data.json           # Base de datos local con info de tarjetas
├── main.py             # Script principal con la lógica POO
└── README.md           # Documentación técnica
```

* **Seguridad:** Recuerda que este es un proyecto educativo. En un entorno real, los datos de tarjetas nunca deben guardarse en un JSON plano sin cifrado (como AES-256).
