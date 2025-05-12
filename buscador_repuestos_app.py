import streamlit as st
import pandas as pd

st.set_page_config(page_title="Buscador de Repuestos", layout="wide")

st.title("🔍 Buscador de Repuestos")
st.markdown("Busca un repuesto por nombre, referencia o ubicación.")

@st.cache_data
def cargar_datos():
    return pd.read_excel("BUSCADOR_REPUESTOS_CONVERTIDO.xlsx", sheet_name="INVENTARIO")

df = cargar_datos()

# Preparar columnas para búsqueda
df["DESCRIPCION"] = df["DESCRIPCION"].astype(str)
df["REFERENCIA"] = df["REFERENCIA"].astype(str)
df["UBICACION"] = df["UBICACION"].astype(str)

# Cuadro de búsqueda
busqueda = st.text_input("🔎 Escribe parte del nombre, referencia o ubicación:").strip().lower()

if busqueda:
    resultados = df[
        df["DESCRIPCION"].str.lower().str.contains(busqueda) |
        df["REFERENCIA"].str.lower().str.contains(busqueda) |
        df["UBICACION"].str.lower().str.contains(busqueda)
    ]
    st.write(f"🔧 {len(resultados)} repuestos encontrados:")
    for _, row in resultados.iterrows():
        st.markdown("---")
        st.subheader(f"🔩 {row['DESCRIPCION']}")
        st.write(f"**Referencia:** {row['REFERENCIA']}")
        st.write(f"**Ubicación:** {row['UBICACION']}")
        st.write(f"**Casa Comercial:** {row['CASA COMERCIAL']}")
        st.write(f"**Cantidad Disponible:** {row['CANTIDAD']}")
        if "traduccion" in row:
            st.write(f"**traduccion:** {row['traduccion']}")
        if "analizador" in row:
            st.write(f"**analizador:** {row['analizador']}")

        # Mostrar imagen si está disponible
        if pd.notna(row.get("IMAGEN CONVERTIDA", None)):
            st.image(row["IMAGEN CONVERTIDA"], width=300)
else:
    st.info("Escribe un término para iniciar la búsqueda.")

