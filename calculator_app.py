import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Calculator Application")

num1 = st.number_input("Enter first number", value=0.0, format="%f")
num2 = st.number_input("Enter second number", value=0.0, format="%f")
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

result = None
print('yes')
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero.")
    if result is not None:
        st.success(f"Result: {result}")
