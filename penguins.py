import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own Scatterplot about penguins!')

selected_species = st.selectbox('What species would you like to visualize?', 
                                ['Adelie', 'Gentoo', 'Chinstrap'])

selected_x_var = st.selectbox('What do you want the X variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

selected_y_var = st.selectbox('What do you want the Y variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

#import the data 
penguins_df = pd.read_csv('penguins.csv')
penguins_df = penguins_df[penguins_df['species'] == selected_species]
st.write(penguins_df.head())



#plotting
sns.set_style('darkgrid')

# Define the marker shapes for each category in the 'species' column
markers = {"Adelie": "X", "Gentoo":"s", "Chinstrap": "o"}

# Create a scatter plot with the specified x, y, hue, markers, and style parameters
fig, ax = plt.subplots()
ax = sns.scatterplot(x=penguins_df[selected_x_var], y=penguins_df[selected_y_var], hue = penguins_df['species'], markers = markers, style = penguins_df['species'])
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title(f'Scatterplot of {selected_species} Penguins')
st.pyplot(fig)


