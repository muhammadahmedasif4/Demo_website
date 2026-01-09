import streamlit as st

st.title('Corvit Grading system...')

marks = st.number_input('Enter Obtain Marks:',min_value = 1)

total = st.number_input('Enter Total marks:',min_value = 1)

p = round(marks/total * 100, 2)

r = st.button('Calculate Results')

if r:
    st.subheader(f'Your Percentage: :blue[{p} %]')

    if p >= 80:
        st.success('Excellent')
    elif p >= 60 and p < 80:
        st.info('Pass')
    else:
        st.error('Fail')