# Practice Day-6.5:

import streamlit as st

st.title("Simple Calculator")

st.divider()

# Inputes:
num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")

# Operation:
op = st.selectbox("Choose operation",( "+", "-", "*", "/"))

ans = None

# Buttons:
if st.button("Calculate"):
    if op == "+":
        ans = num1+num2
    elif op == "-":
        ans = num1-num2
    elif op == "*":
        ans = num1*num2
    elif op == "/":
        # ans = num1/num2
        if num2 != 0:
            ans = num1 / num2
        else:
            st.error("Cannot divide by zero")

# Show result:
if ans is not None:
    st.success(f"Result: {ans}")
