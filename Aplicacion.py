import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Dibuja en este tablero")

with st.sidebar:
  st.subheader("Propiedades del tablero")

  st.subheader("Dimensiones del tablero")
  canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
  canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)



  drawing_mode = st.selectbox(
    "Herramientas de Dibujo:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
  )


  stroke_width = st.slider("Selecciona el ancho de la linea", 1, 30, 15)

  stroke_color = st.color_picker("Selecciona el color de la línea", "#FFFFFF")

  bg_color = st.color_picker("Color de fondo del tablero", "#000000")


canvas_result = st-canvas(
  fill_color = "rgba(255, 165, 0, 0.3)",
  stroke_width = stroke_width,
  stroke_color = stroke_color, 
  backround_color = bg_color,
  height = canvas_height,
  width = canvas_width,
  drawing_mode = drawing_mode,
  key = f"canvas_{canvas_width}_{canvas_height}")
