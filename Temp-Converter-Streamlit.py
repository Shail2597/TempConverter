import streamlit as st

# Title
st.title("Temperature Converter")

# Choose temperature to convert from
st.write("Press 1 if you want to Convert from Celsius")
st.write("Press 2 if you want to Convert from Fahrenheit")
st.write("Press 3 if you want to Convert from Kelvin")

# User input for conversion choice
choice_to_convert_from = st.number_input("Enter your choice:", step=1, key='choice_from')

if choice_to_convert_from in [1, 2, 3]:
    temperature = st.number_input("Enter the temperature:", step=1.0, key='temp_input')
    
    if st.button("Convert"):
        if choice_to_convert_from == 1:  # Celsius
            fahrenheit = round(temperature * 9 / 5 + 32, 2)
            kelvin = round(temperature + 273.15, 2)
        elif choice_to_convert_from == 2:  # Fahrenheit
            celsius = round((temperature - 32) * 5 / 9, 2)
            kelvin = round(celsius + 273.15, 2)
        elif choice_to_convert_from == 3:  # Kelvin
            celsius = round(temperature - 273.15, 2)
            fahrenheit = round((temperature - 273.15) * 9 / 5 + 32, 2)

        # Choice for conversion output
        choice_to_convert_to = st.number_input("Press 1 for Celsius, 2 for Fahrenheit, 3 for Kelvin, 4 for All:", step=1, key='choice_to_convert_to')

        # Display results based on user choice
        if choice_to_convert_from == 1:  # From Celsius
            if choice_to_convert_to == 1:
                st.write(f"The temperature in Celsius is: {temperature}")
            elif choice_to_convert_to == 2:
                st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
            elif choice_to_convert_to == 3:
                st.write(f"The temperature in Kelvin is: {kelvin}")
            elif choice_to_convert_to == 4:
                st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
                st.write(f"The temperature in Kelvin is: {kelvin}")

        elif choice_to_convert_from == 2:  # From Fahrenheit
            if choice_to_convert_to == 1:
                st.write(f"The temperature in Celsius is: {celsius}")
            elif choice_to_convert_to == 2:
                st.write(f"The temperature in Fahrenheit is: {temperature}")
            elif choice_to_convert_to == 3:
                st.write(f"The temperature in Kelvin is: {kelvin}")
            elif choice_to_convert_to == 4:
                st.write(f"The temperature in Celsius is: {celsius}")
                st.write(f"The temperature in Kelvin is: {kelvin}")

        elif choice_to_convert_from == 3:  # From Kelvin
            if choice_to_convert_to == 1:
                st.write(f"The temperature in Celsius is: {celsius}")
            elif choice_to_convert_to == 2:
                st.write(f"The temperature in Fahrenheit is: {fahrenheit}")
            elif choice_to_convert_to == 3:
                st.write(f"The temperature in Kelvin is: {temperature}")
            elif choice_to_convert_to == 4:
                st.write(f"The temperature in Celsius is: {celsius}")
                st.write(f"The temperature in Fahrenheit is: {fahrenheit}")

else:
    st.write("You entered an invalid input.")

