# 🛒 Proyecto Urban Grocers - Pruebas Automatizadas de API (Sprint 8)

Urban Grocers es una aplicación orientada al comercio electrónico (*e-grocery*) y servicio de entrega de comestibles a domicilio. La plataforma permite a los usuarios crear cuentas, consultar la disponibilidad de inventario en almacenes urbanos, gestionar carritos de compra y organizar sus productos mediante la creación de kits temáticos personalizados.

El sistema backend procesa flujos transaccionales y la logística de preparación de pedidos (*picking*), respondiendo de forma asincrónica a través de una arquitectura cliente-servidor basada en microservicios y respuestas HTTP.

---

## 🎯 Objetivo del Proyecto

El propósito fundamental de este proyecto es automatizar de forma íntegra las pruebas de la lista de comprobación (*checklist*) diseñada para el campo `name` en la solicitud de creación de un kit de productos. El objetivo es validar el correcto funcionamiento de la API, reducir los tiempos de regresión y asegurar resultados confiables bajo escenarios positivos y negativos basados en la documentación oficial antes de su lanzamiento.

---

## 🦹 Alcance de las pruebas

Las pruebas cubren la verificación exhaustiva de los servicios REST API del servidor, incluyendo:

📍 **Gestión del campo Name en Kits (`/api/v1/kits`)**
* Creación de kits con nombres válidos e inválidos (análisis de valores límite y particiones de equivalencia de strings).
* Validación de estructuras JSON en solicitudes `POST` y persistencia de los nombres en el backend.
* Verificación del comportamiento del servidor ante la omisión de campos obligatorios o tipos de datos incorrectos en el cuerpo de la petición.

💳 **Validación de Códigos de Respuesta HTTP**
* Verificación de la consistencia de respuestas esperadas para escenarios positivos (`201 Created`).
* Evaluación de control de excepciones y fronteras para escenarios negativos (`400 Bad Request`).

💬 **Integridad de Datos y Autenticación (`/api/v1/users`)**
* Flujo de registro automático de nuevos perfiles de usuario para la captura dinámica de tokens de autenticación en los encabezados (*headers*) de las llamadas.

---

## 🟣 Lógica de funcionamiento

* En el estado inicial, las peticiones que carecen de un token de autenticación válido (`Authorization`) son rechazadas automáticamente por el servidor con un código de error de acceso.
* La creación de un kit está restringida por la base de datos a un formato de nombre específico; strings vacíos o con longitudes que excedan los límites provocan fallas de validación controladas en el backend.
* El sistema procesa las solicitudes de forma síncrona: si los parámetros son válidos, inyecta el kit y actualiza el inventario local; si fallan, deniega el guardado y retorna la estructura de error correspondiente.
* Cualquier modificación en el payload de entrada actualiza en el acto el cuerpo de la respuesta en formato JSON devuelto por el servidor.

## 🪶 Contenido del Proyecto

Este proyecto contiene el desarrollo y la implementación de la suite de pruebas automatizadas encargada de ejecutar las aserciones lógicas para la creación de kits personales dentro de la plataforma de Urban Grocers. La estructura está desacoplada bajo buenas prácticas de ingeniería de software para aislar la conectividad de red de los datos de prueba estáticos.

### 📁 Estructura de Archivos
```plaintext
qa-project-Urban-Grocers-es/
│
├── .gitignore              # Evita que se carguen carpetas locales de caché y del sistema
├── README.md               # Documentación general y guía técnica del proyecto
├── configuration.py        # Define las variables de entorno y rutas base de la API
├── create_kit_test.py      # Suite con los 9 casos de prueba automatizados secuenciales
├── data.py                 # Almacena los diccionarios JSON, payloads y headers de prueba
└── sender_stand_request.py # Implementación de métodos HTTP (POST, GET, PUT) con la librería requests
```

## 🧩 Tecnologías y Herramientas

* **Lenguaje principal de programación:** `python`
* **Framework para pruebas automatizadas:** `pytest`
* **Librerías de comunicación de red:** `requests`
* **Estructuras de intercambio de datos:** `json`
* **Control de versiones y almacenamiento de código:** `git` / `github`

### 🏷️ Documentación Oficial de la API
* `API Docs:` https://cnt-1a53e386-65dc-4b4d-9eee-630030c7e29b.containerhub.tripleten-services.com/docs/

---

## 🪄 Enfoque de testing

Se utiliza un enfoque enfocado en pruebas funcionales de Backend y API de Caja Negra, interactuando directamente con el servidor a través de peticiones HTTP automatizadas sin capas de interfaz gráfica intermedia.

Incluye:
* **Pruebas Positivas:** Creación correcta de kits utilizando parámetros permitidos y validación de las respuestas esperadas del sistema.
* **Pruebas Negativas:** Inyección de datos inválidos, campos faltantes y validación de errores controlados por el servidor para asegurar una cobertura completa de excepciones.
* **Manejo Dinámico de Datos:** Uso de diccionarios centralizados independientes para manipular el cuerpo de las peticiones en tiempo de ejecución.

## ⚡ Aspectos destacados

* **Validación rigurosa de respuestas:** Comprobación dual que audita tanto el código de estado HTTP (`status_code`) como el contenido del objeto JSON devuelto.
* **Cero dependencias estáticas:** Uso de métodos que modifican los payloads dinámicamente en tiempo de ejecución, evitando la colisión de datos duplicados en el servidor.
* **Alta mantenibilidad:** Centralización completa de rutas y configuraciones de red, lo que permite migrar las pruebas de un entorno de desarrollo a otro modificando una sola línea.

## 🎯 Objetivo

Garantizar el correcto funcionamiento de la API, detectar posibles fallos lógicos en las restricciones del negocio y asegurar la estabilidad del sistema bajo diferentes condiciones de entrada antes del lanzamiento oficial de la aplicación.

---

## 🚀 Instrucciones de Execution

### Prerrequisitos
Antes de iniciar, asegúrate de contar con Python 3.x instalado en tu entorno local.

### Instalación de Dependencias
Prepara el entorno instalando las librerías necesarias con el siguiente comando en tu terminal:
```bash
pip install pytest requests
```

### Ejecución de la Suite
* **Ejecutar todas las pruebas automáticas:**
  ```bash
  pytest
  ```

---

## 📌 Conclusión

Este proyecto fortalece la calidad del producto mediante pruebas automatizadas robustas, asegurando que la funcionalidad de creación de kits personales opere correctamente, maneje los errores de forma controlada y cumpla de manera estricta con todos los estándares lógicos y de negocio esperados.


