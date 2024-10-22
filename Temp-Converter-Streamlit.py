import streamlit as st

# Title
st.title("Temperature Converter")

# Choose temperature to convert from
st.write("Select the temperature scale to convert from:")
choice_to_convert_from = st.selectbox("Choose an option:", ["Celsius", "Fahrenheit", "Kelvin"])

# User input for the temperature
temperature = st.number_input("Enter the temperature:", step=1.0)

if st.button("Convert"):
    if choice_to_convert_from == "Celsius":
        fahrenheit = round(temperature * 9 / 5 + 32, 2)
        kelvin = round(temperature + 273.15, 2)
        st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
        st.write(f"The temperature in Kelvin is: {kelvin}")

    elif choice_to_convert_from == "Fahrenheit":
        celsius = round((temperature - 32) * 5 / 9, 2)
        kelvin = round(celsius + 273.15, 2)
        st.write(f"The temperature in Celsius is: {celsius}")
        st.write(f"The temperature in Kelvin is: {kelvin}")

    elif choice_to_convert_from == "Kelvin":
        celsius = round(temperature - 273.15, 2)
        fahrenheit = round((temperature - 273.15) * 9 / 5 + 32, 2)
        st.write(f"The temperature in Celsius is: {celsius}")
        st.write(f"The temperature in Fahrenheit is: {fahrenheit}")


