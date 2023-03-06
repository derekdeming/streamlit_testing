import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt 


st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('An app test by Derek Deming')
st.write(('This app simulates a thousand coin flips using the chancew of heads input below,'
          ' and then samples with replacement from that population and plots the histogram of the '
          'means of the samples, in order to illustrate the Central Limit Theorem!')) 

percent_heads = st.number_input(label = 'Chance of Coins Landing on Heads', min_value = 0.0, max_value=1.0, value = .5)
# graph_title = st.text_input(label = 'Graph Title')
binom_dist = np.random.binomial(1, percent_heads, 1000)


list_of_means = []
for i in range (0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 50, replace=True).mean())

fig, ax = plt.subplots()
plt.hist(list_of_means, range=[0,1])
# plt.title(graph_title)
st.pyplot(fig)





