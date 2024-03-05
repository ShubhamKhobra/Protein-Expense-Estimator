import streamlit as st

st.title('Protein Expense Estimator')
st.write('Select protein quantity from below sources')
col1, col2 = st.columns(2)

# Protein Quantity
soy = col1.slider('Soy Chunk (in g)', 0, 200)
whey = col1.slider('Whey Protein (in g)', 0, 200)
casein = col1.slider('Casein Protein (in g)', 0, 200)
plant_protein = col1.slider('Plant Based Vegan Protein (in g)', 0, 200)
paneer = col2.slider('Paneer (in g)', 0, 200)
milk = col2.slider('Milk (in g)', 0, 200)
egg = col1.slider('Egg (in g)', 0, 198, step=6)
chicken = col2.slider('Chicken (in g)', 0, 200)
mutton = col2.slider('Mutton (in g)', 0, 200)
fish = col2.slider('Fish (in g)', 0, 200)

# Source quantity for given protein quantity
soy_qt = soy * 1.92
whey_qt = whey * 1.28
casein_qt = casein * 1.28
plant_protein_qt = plant_protein * 1.43
egg_qt = egg * (1/6) # Egg quantity in numbers
chicken_qt = chicken * (100/24)
mutton_qt = mutton * (100/25)
fish_qt = fish * (100/20)
paneer_qt = paneer * (100/18)
milk_qt = milk * (100/3) # Milk quantity in ml

# Price in Rupees per 1000g
soy_price = 200
whey_price = 2000
casein_price = 3000
plant_protein_price = 2400
egg_price = 10 # Egg price for single egg
chicken_price = 550
mutton_price = 1800
fish_price = 1000
paneer_price = 470
milk_price = 80

daily_exp = (soy_qt * (soy_price/1000)) + (whey_qt * (whey_price/1000)) + (casein_qt * (casein_price/1000)) + (plant_protein_qt * (plant_protein_price/1000)) +  (egg_qt * (egg_price)) + (chicken_qt * (chicken_price/1000)) + (mutton_qt * (mutton_price/1000)) + (fish_qt * (fish_price/1000)) + (paneer_qt * (paneer_price/1000)) + (milk_qt * (milk_price/1000))

daily_con = soy + whey + casein + plant_protein + egg + chicken + mutton + fish + paneer + milk
st.write('Daily protein consumption is: ', daily_con, 'g')
st.write('Daily protein expense is: ₹', round(daily_exp, 2))
st.write('Monthly protein expense is: ₹', round(daily_exp*30, 2))