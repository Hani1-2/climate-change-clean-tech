import streamlit as st
import numpy as np
import pickle

model_1 = pickle.load(open('model_2.pkl', 'rb'))
def main():
    st.title('Climate Change Prediction:')
    st.subheader('Enter relevant data to predict the temperature change:')

    d = {'Afghanistan':0,
    'Australia':1,
    'Austria':2,
    'Burundi':3,
    'Benin':4,
    'Burkina Faso':5,
    'Bangladesh':6,
    'Belize':7,
    'Brazil':8,
    'Central African Republic':9,}
    c1 = st.selectbox('Select your Country ',('Afghanistan',
    'Australia',
    'Austria',
    'Burundi',
    'Benin',
    'Burkina Faso',
    'Bangladesh',
    'Belize',
    'Brazil',
    'Central African Republic'))
    if c1 in d:
        c1 = d[c1]
    else:
        c1 = 0.0

    ## for column 2
    c2 = st.text_input('Enter the year of the data (1961 and onwards')
    if c2 == '':
        c2 = 0.0

    ## for column 3
    c3 = st.text_input('Enter the Carbon Dioxide Emission')
    if c3 == '':
        c3 = 0.0
    
    ## for column 4
    c4 = st.text_input('Enter the GDP per capita')
    if c4 == '':
        c4 = 0.0

    # prediction
    if st.button('Predict'):
        make_prediction = model_1.predict((np.array([c1,c2,c3,c4]).reshape(1,-1)))
        print(make_prediction)
        output = round((make_prediction[0]),2)
        print(output)
        st.success('The change in temperature will be: {}'.format(output))


if __name__ == '__main__':
    main()