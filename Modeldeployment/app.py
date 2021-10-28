import streamlit as st
import pickle
import numpy as np
#import the model
pipe=pickle.load(open('pipe.pkl','rb'))
data=pickle.load(open('data.pkl','rb'))

st.title('Restaurant rating predictor')
#online order
order=st.selectbox('online order',data['online_order'].unique())
#book table
book=st.selectbox('book table',data['book_table'].unique())
#votes
vote=st.number_input('number of votes')

#location
location=st.selectbox('location',data['location'].unique())

#rest type
rest_type=st.selectbox('rest_type',data['rest_type'].unique())
#cost two
cost_two=st.number_input('cost for two')

#service type
service_type=st.selectbox('service_type',data['service_type'].unique())


if st.button('predict rating'):
    #query
    query=np.array([order,book,vote,location,rest_type,cost_two,service_type])
    query=query.reshape(1,7)
    st.title(np.around((pipe.predict(query)[0]),2))
