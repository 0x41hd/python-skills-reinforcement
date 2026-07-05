import streamlit as st
from src.password_generators import PinGenerator, PasswordGenerateor, MemorablePasswordGenerator, RandomPasswordGenerator


st.image("https://wavebrowser.co/cms-content/autofill_password_manager_9ad6764850.jpg", width=600)
st.title(":closed_lock_with_key: Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == 'Pin Code':
    length = st.slider("Select the length of the pin code", 4, 32)
    generator = PinGenerator(length=length)
elif option == 'Random Password':
    length = length = st.slider("Select the length of the password", 8, 64)
    include_number = st.toggle("Include Number")
    include_symbol = st.toggle("Include Symbols")
    generator = RandomPasswordGenerator(
        length=length, include_number=include_number, include_symbols=include_symbol)
elif option == 'Memorable Password':
    num_of_word = st.slider("Select number of words", 2, 10)
    separator = st.text_input("Separator", value="-")
    capitalization = st.toggle("capitalization")
    generator = MemorablePasswordGenerator(
        num_of_words=num_of_word, separator=separator, caplitalize=capitalization)

password = generator.generate()
st.write(fr"Your password is: ``` {password} ``` ")
