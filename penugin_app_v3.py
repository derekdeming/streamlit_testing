import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


st.title("Palmer's Penguins version 3.0")
st.markdown('Use this Streamlit app to make your own Scatterplot about penguins!')
st.subheader('If needed, upload file below:')

#import the data 
penguin_file = st.file_uploader('Select your local csv datafile (default provided approx 200 MB)')

if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')
    

st.subheader('')

#Show raw data on the app 
st.write(penguins_df.head())

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

st.subheader('')

st.subheader('Filter Selection within All Species: Variable_X, Variable_Y')

#DROP DOWN SELECTORS FOR THE USER 
selected_x_var1 = st.selectbox('What do you want the X variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='x_var1')

selected_y_var1 = st.selectbox('What do you want the Y variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='y_var1')

#plotting
sns.set_style('darkgrid')

# Define the marker shapes for each category in the 'species' column
markers = {"Adelie": "X", "Gentoo":"s", "Chinstrap": "o"}

# Create a scatter plot with the specified x, y, hue, markers, and style parameters
fig1, ax1 = plt.subplots()
ax1 = sns.scatterplot(x=penguins_df[selected_x_var1], y=penguins_df[selected_y_var1], hue = penguins_df['species'], markers = markers, style = penguins_df['species'])
plt.xlabel(selected_x_var1)
plt.ylabel(selected_y_var1)
plt.title(f'Scatterplot of All Penguin Species')
st.pyplot(fig1)

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
st.subheader('')
st.subheader('')

st.subheader('Filter Selection: Species, Variable_X, and Variable_Y')

#DROP DOWN SELECTORS FOR THE USER 
selected_species2 = st.selectbox('What species would you like to visualize?', 
                                 ['Adelie', 'Gentoo', 'Chinstrap'],
                                 key='species2')

selected_x_var2 = st.selectbox('What do you want the X variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='x_var2')

selected_y_var2 = st.selectbox('What do you want the Y variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'],
                              key='y_var2')


penguins_df = penguins_df[penguins_df['species'] == selected_species2]

fig2, ax2 = plt.subplots()
ax2 = sns.scatterplot(x=penguins_df[selected_x_var2], y=penguins_df[selected_y_var2], hue = penguins_df['species'], markers = markers, style = penguins_df['species'])
plt.xlabel(selected_x_var2)
plt.ylabel(selected_y_var2)
plt.title(f'Scatterplot of {selected_species2} Penguins Species')
st.pyplot(fig2)


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

st.subheader('')
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

selected_gender = st.selectbox('What gender do you want to filter for?', 
                              ['All', 'Male', 'Female'],
                              key='z_var3')

if selected_gender == 'male': 
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass 

#PLOTTING
sns.set_style('darkgrid')

# Define the marker shapes for each category in the 'species' column
markers = {"Adelie": "X", "Gentoo":"s", "Chinstrap": "o"}

# Create a scatter plot with the specified x, y, hue, markers, and style parameters
fig3, ax3 = plt.subplots()
ax2 = sns.scatterplot(x=penguins_df[selected_x_var2], y=penguins_df[selected_y_var2], hue = penguins_df['species'], markers = markers, style = penguins_df['species'])
plt.xlabel(selected_x_var3)
plt.ylabel(selected_y_var3)
plt.title(f'Scatterplot of {selected_gender} Penguin Species')
st.pyplot(fig3)


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
