import streamlit as st
st.title('Startup Dashboard') 

st.header('I am learning streamlit')
st.subheader('Archi Jaiswal')

st.write ('This is  a normal text')
st.markdown("""
            ### My favorite movies
            - Race 3
            - Humshakals
            - Housefull 4""")

st.code("""
def foo(input):
        return foo**2
x = foo(2) 
           """)

st.latex('x^2 + y^2 + 2 = 0' )