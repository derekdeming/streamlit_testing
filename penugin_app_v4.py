import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import time


st.title("Palmer's Penguins version 3.0")
st.markdown('Use this Streamlit app to make your own Scatterplot about penguins!')
st.subheader('If needed, upload file below:')

#import the data 
penguin_file = st.file_uploader('Select your local csv datafile (default provided approx 200 MB)')
@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
penguins_df = load_file(penguin_file)

st.subheader('')

st.subheader('Filter Selection within All Species and Specific Gender:'
             ' Variable_X, Variable_Y, and Gender')
    
    
#DROP DOWN SELECTORS FOR THE USER 
selected_x_var3 = st.selectbox('What do you want the X variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='x_var3')

selected_y_var3 = st.selectbox('What do you want the Y variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='y_var3')

selected_gender3 = st.selectbox('What gender do you want to filter for?', 
                              ['All', 'Male', 'Female'],
                              key='z_var3')

if selected_gender3 == 'male': 
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender3 == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass 

#PLOTTING
# Create a scatter plot with the specified x, y, hue, markers, and style parameters
fig3, ax3 = plt.subplots()
ax3 = sns.scatterplot(x=penguins_df[selected_x_var3], y=penguins_df[selected_y_var3], hue = penguins_df['species'])
plt.xlabel(selected_x_var3)
plt.ylabel(selected_y_var3)
plt.title(f'Scatterplot of {selected_gender3} Penguin Species')
st.pyplot(fig3)


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
