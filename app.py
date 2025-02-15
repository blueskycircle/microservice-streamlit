import streamlit as st
from mylib.bot import scrape


# Define the Streamlit app
def main():
    st.title("Microservice App")

    st.header("Scrape Wikipedia Page")
    wiki_name = st.text_input("Enter Wikipedia page name:")
    if st.button("Scrape"):
        if wiki_name:
            result = scrape(name=wiki_name)
            st.json({"wikipage": result})
        else:
            st.error("Please enter a Wikipedia page name.")

    st.header("Add Two Numbers")
    num1 = st.number_input("Enter first number:", value=0)
    num2 = st.number_input("Enter second number:", value=0)
    if st.button("Add"):
        total = num1 + num2
        st.success(f"The total is: {total}")


if __name__ == "__main__":
    main()
