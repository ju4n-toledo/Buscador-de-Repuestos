# 🔍 Buscador de Repuestos

Esta es una aplicación web desarrollada con [Streamlit](https://streamlit.io) para buscar repuestos, ver su información y mostrar su imagen desde Google Drive.

## 📁 Estructura del Proyecto

- `buscador_repuestos_app_actualizada.py` → archivo principal de la app
- `BUSCADOR_REPUESTOS_CONVERTIDO.xlsx` → archivo Excel con los datos del inventario
- `requirements.txt` → dependencias necesarias

## 🚀 Cómo desplegar en Streamlit Cloud

1. Crea un repositorio en GitHub y sube los tres archivos mencionados arriba.
2. Ve a [Streamlit Cloud](https://streamlit.io/cloud) y haz clic en “Deploy”.
3. Conecta tu cuenta de GitHub.
4. Selecciona el repositorio y el archivo `buscador_repuestos_app_actualizada.py`.
5. Haz clic en “Deploy”.

## ✅ Requisitos

Tu archivo Excel debe tener al menos estas columnas:

- `REFERENCIA` → código del repuesto
- `DESCRIPCION` → nombre o descripción
- `UBICACION` → dónde está guardado
- `CANTIDAD` → cantidad en stock
- `IMAGEN CONVERTIDA` → enlace directo a la imagen en Google Drive (formato: `https://drive.google.com/uc?id=ID`)

## 📷 Cómo obtener el enlace correcto de Google Drive

1. Sube la imagen a tu Drive.
2. Haz clic en “Compartir” y selecciona “Cualquiera con el enlace”.
3. Copia el enlace. Ejemplo original:
