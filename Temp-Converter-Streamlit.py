import streamlit as st

# Title
st.title("Temperature Converter")

# Choose temperature to convert from
st.write("Press 1 if you want to Convert from Celsius")
st.write("Press 2 if you want to Convert from Fahrenheit")
st.write("Press 3 if you want to Convert from Kelvin")

# User input for conversion choice
choice_to_convert_from = st.number_input("Enter your choice:", step=1, key='choice_from')

if choice_to_convert_from == 1:
    temperature = st.number_input("Enter the temperature in Celsius:", step=1.0, key='temp_celsius')
    if st.button("Convert"):
        fahrenheit = round(temperature * 9 / 5 + 32, 2)
        kelvin = round(temperature + 273.15, 2)

        st.write("Press 1 if you want to Convert to Fahrenheit")
        st.write("Press 2 if you want to Convert to Kelvin")
        st.write("Press 3 if you want to Convert to Both")

        choice_to_convert_to = st.number_input("Enter your choice:", step=1, key='choice_to_celsius')

        if choice_to_convert_to == 1:
            st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
        elif choice_to_convert_to == 2:
            st.write(f"The temperature in Kelvin is: {kelvin}")
        elif choice_to_convert_to == 3:
            st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
            st.write(f"The temperature in Kelvin is: {kelvin}")

elif choice_to_convert_from == 2:
    temperature = st.number_input("Enter the temperature in Fahrenheit:", step=1.0, key='temp_fahrenheit')
    if st.button("Convert"):
        celsius = round((temperature - 32) * 5 / 9, 2)
        kelvin = round(celsius + 273.15, 2)

        st.write("Press 1 if you want to Convert to Celsius")
        st.write("Press 2 if you want to Convert to Kelvin")
        st.write("Press 3 if you want to Convert to Both")

        choice_to_convert_to = st.number_input("Enter your choice:", step=1, key='choice_to_fahrenheit')

        if choice_to_convert_to == 1:
            st.write(f"The temperature in Celsius is: {celsius}")
        elif choice_to_convert_to == 2:
            st.write(f"The temperature in Kelvin is: {kelvin}")
        elif choice_to_convert_to == 3:
            st.write(f"The temperature in Celsius is: {celsius}")
            st.write(f"The temperature in Kelvin is: {kelvin}")

elif choice_to_convert_from == 3:
    temperature = st.number_input("Enter the temperature in Kelvin:", step=1.0, key='temp_kelvin')
    if st.button("Convert"):
        celsius = round(temperature - 273.15, 2)
        fahrenheit = round((temperature - 273.15) * 9 / 5 + 32, 2)

        st.write("Press 1 if you want to Convert to Celsius")
        st.write("Press 2 if you want to Convert to Fahrenheit")
        st.write("Press 3 if you want to Convert to Both")

        choice_to_convert_to = st.number_input("Enter your choice:", step=1, key='choice_to_kelvin')

        if choice_to_convert_to == 1:
            st.write(f"The temperature in Celsius is: {celsius}")
        elif choice_to_convert_to == 2:
            st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
        elif choice_to_convert_to == 3:
            st.write(f"The temperature in Celsius is: {celsius}")
            st.write(f"The temperature in Fahrenheit is: {fahrenheit}")

else:
    st.write("You entered an invalid input.")
