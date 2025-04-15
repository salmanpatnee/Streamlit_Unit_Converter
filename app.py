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

def convert_units(category, from_unit, to_unit, value):
    if category == "Temperature":
        return convert_temperature(from_unit, to_unit, value)
    else:
        base_value = value * conversion_factors[category][from_unit]
        return base_value / conversion_factors[category][to_unit]

def convert_temperature(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    else:
        return value

# Streamlit UI
def render_converter():
    st.title("🔄 Streamlit Unit Converter")

    with st.form("converter_form"):
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            category = st.selectbox("Category", list(conversion_factors.keys()))

        with col2:
            from_unit = st.selectbox("From", list(conversion_factors[category].keys()))

        with col3:
            to_unit = st.selectbox("To", list(conversion_factors[category].keys()))

        value = st.number_input("Value", min_value=0.0, format="%.4f")

        submitted = st.form_submit_button("Convert")

        if submitted:
            result = convert_units(category, from_unit, to_unit, value)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    render_converter()
