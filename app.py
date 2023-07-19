import streamlit as st
import joblib
import pandas as pd


clf = joblib.load('nb.pkl')

def classify(num):
    if num == 0:
        return 'Leftist Ideology'
    elif num == 1:
        return 'Neutral Ideology'
    else:
        return 'Rightist Ideology'

def main():
    st.title("BTECH PROJECT -II")
    st.text("")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction of Political Biasness     </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities = ['Naive bayes']
    option = st.sidebar.selectbox('Which model would you like to use?', activities)
    st.text("")
    
    title = st.text_input('Write the statement',)

    a_ser = pd.Series(title)
    
    st.subheader(option)

    if st.button('Classify'):
        
        if option == 'Naive bayes':
            st.success(classify(clf.predict(a_ser)))
      
if __name__ == '__main__':
    main()