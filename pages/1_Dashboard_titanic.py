import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

#absolute path this file
FILE_DIR=os.path.dirname(os.path.abspath(__file__))
#absolute path to this filles root directory
PARENT_DIR=os.path.join(FILE_DIR,os.pardir)

dir_of_intrest=os.path.join(PARENT_DIR,'resources')

IMAGE_PARTH=os.path.join(dir_of_intrest,'titanic.jpeg')

DATA_PATH=os.path.join(dir_of_intrest,'titanic.csv')

st.title('Dashboard- titanic Data')

img=image.imread(IMAGE_PARTH)

st.image(img)

df=pd.read_csv(DATA_PATH)

survived=st.selectbox('Select the species:',df['Survived'].unique())

col1,col2=st.columns(2)

fig_1=px.histogram(df[df['Survived']==survived],x='Age')
col1.plotly_chart(fig_1,user_container_width=True)

fig_2=px.box(df[df['Survived']==survived],y='Age')
col2.plotly_chart(fig_2,user_container_width=True)