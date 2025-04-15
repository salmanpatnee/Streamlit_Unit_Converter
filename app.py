import streamlit as st

# Define conversion factors
conversion_factors = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "foot": 0.3048,
        "inch": 0.0254,
    },
    "Weight": {
        "kilogram": 1,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}


st.title("🔄 Unit Converter")
category = st.selectbox("Choose Category", list(conversion_factors.keys()))
from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
to_unit = st.selectbox("To", list(conversion_factors[category].keys()))
value = st.number_input("Enter value", min_value=0.0, format="%.4f")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
