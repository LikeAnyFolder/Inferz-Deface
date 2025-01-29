# InferzDeface

InferzDeface es una herramienta para la carga de archivos en múltiples sitios web de manera automatizada. Sigue esta guía para instalar y usar la herramienta correctamente.

## 📌 Requisitos Previos
Antes de usar InferzDeface, asegúrate de tener instalado lo siguiente en tu sistema:

- **Python 3.8 o superior**
- **Bibliotecas necesarias:** `requests`, `colorama`
  
Para instalarlas, ejecuta el siguiente comando en la terminal:
```bash
pip install requests colorama
```

## 📂 Estructura del Proyecto
El proyecto InferzDeface requiere los siguientes archivos en la misma carpeta donde se encuentra el script:

```
📁 InferzDeface
│── InferzDeface.py   # Script principal
│── targets.txt       # Lista de URLs objetivo (una por línea)
│── deface.html       # Archivo HTML a subir
│── uploader.log      # Registro de actividad generado automáticamente
```

## ⚙️ Configuración Inicial

### 1️⃣ Preparar `targets.txt`
Abre el archivo `targets.txt` y añade las URLs de los sitios web objetivo, una por línea. Ejemplo:
```
http://example.com
http://test.com
```

### 2️⃣ Preparar `deface.html`
Crea un archivo HTML llamado `deface.html` en la misma carpeta que `InferzDeface.py`. Este archivo será el que se suba a los sitios web. Ejemplo:
```html
<html>
  <body>
    <h1>Hacked by InferzSquad</h1>
  </body>
</html>
```

## 🚀 Ejecución del Script
1. Abre una terminal o consola en la carpeta donde se encuentra `InferzDeface.py`.
2. Ejecuta el siguiente comando:
   ```bash
   python InferzDeface.py
   ```
3. Sigue las instrucciones del menú interactivo:
   - **Opción 1**: Cargar automáticamente los objetivos desde `targets.txt`.
   - **Opción 2**: Ejecutar la subida del archivo `deface.html` a los objetivos.
   - **Opción 3**: Salir del programa.

## 📊 Resultados y Registro
- **Mensajes en verde** ✅ indican éxito.
- **Mensajes en rojo** ❌ indican errores.
- Todos los resultados se almacenan en el archivo `uploader.log`.

## 📝 Notas Adicionales
- **Asegúrate de que `targets.txt` y `deface.html` estén en la misma carpeta** que `InferzDeface.py`.
- El script está diseñado para ser **fácil de usar** y no requiere configuración adicional.

---
**⚠️ Advertencia:** Este script debe ser utilizado con fines educativos y de prueba en entornos autorizados. El uso indebido puede tener consecuencias legales.
