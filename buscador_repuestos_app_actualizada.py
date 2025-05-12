import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Configuración de la página
st.set_page_config(page_title="Buscador de Repuestos", layout="wide")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("data/BUSCADOR REPUESTOS.xlsx", sheet_name="INVENTARIO")
    # Limpiar nombres de columnas (eliminar espacios y mayúsculas)
    df.columns = [col.strip().upper() for col in df.columns]
    return df

df = load_data()

# Título y búsqueda
st.title("🔍 Buscador de Repuestos - Inventario")
search_term = st.text_input("Buscar por Referencia, Descripción o Ubicación:")

# Filtrado de datos
if search_term:
    filtered_df = df[
        df.apply(
            lambda row: any(
                str(search_term).lower() in str(row[col]).lower() 
                for col in ["REFERENCIA", "DESCRIPCION", "UBICACION"]
            ),
            axis=1
        )
    ]
else:
    filtered_df = df

# Mostrar resultados
if not filtered_df.empty:
    st.write(f"**Resultados encontrados:** {len(filtered_df)}")
    for _, row in filtered_df.iterrows():
        st.divider()
        col1, col2 = st.columns([1, 3])

        # Columna 1: Imagen (si existe)
        with col1:
            if pd.notna(row["IMAGEN"]) and str(row["IMAGEN"]).startswith("http"):
                try:
                    response = requests.get(row["IMAGEN"])
                    img = Image.open(BytesIO(response.content))
                    st.image(img, width=200, caption=row["REFERENCIA"])
                except:
                    st.warning("Error al cargar la imagen")
            else:
                st.warning("Imagen no disponible")

        # Columna 2: Datos del repuesto
        with col2:
            st.subheader(f"{row['REFERENCIA']} - {row['DESCRIPCION']}")
            st.write(f"**Casa Comercial:** {row['CASA COMERCIAL']}")
            st.write(f"**Ubicación:** {row['UBICACION']}")
            st.write(f"**Cantidad:** {row['CANTIDAD']}")
            if pd.notna(row["TRADUCCION"]):
                st.write(f"**Traducción:** {row['TRADUCCION']}")

else:
    st.error("No se encontraron repuestos. Intenta con otro término.")
