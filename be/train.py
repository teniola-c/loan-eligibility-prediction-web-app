import streamlit as st
from PIL import Image
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()


def run():
    img1 = Image.open("img.jfif")
    img1 = img1.resize((400,350))
    st.image(img1, use_column_width = False) 
    st.title("Big mart sales prediction web app")
    
    ##   Item weight
    ai = st.number_input("Item weight", value =0)
    
    ##item fat cintent
    itc =("Low Fat", "Regular")
    genk = list(range(len(itc)))
    ge = st.selectbox("Item fat content", genk, format_func= lambda x: itc[x] )
    
    ##item type
    geni =("Fruits and Vegetables", "Snack Foods","Household","Frozen Foods","Dairy","Canned","Baking Goods","Health and Hygiene","Soft Drinks","Meat","Breads","Hard Drinks","Others","Starchy Foods","Breakfast","Seafood")
    gens = list(range(len(geni)))
    it = st.selectbox("Gender", gens, format_func= lambda x: geni[x] )
    
    ##   Item mrp
    im = st.number_input("Item mrp", value =0)
    
    ##outlet size
    gen =("High", "Medium", "Small")
    goe = list(range(len(gen)))
    os = st.selectbox("Outlet size", goe, format_func= lambda x: gen[x] )
    
    ##outlet type
    out =("Tier 1", "Tier 2", "Tier 3")
    genko = list(range(len(out)))
    ot = st.selectbox("Outlet type", genko, format_func= lambda x: out[x] )
    
    if st.button("predict"):
        features = [[ai,ge,it,im,os,ot]]
        print(features)
        prediction = model.predict(features)
        for i in prediction:
          st.success(f"Your predicted sales is  {np.round(i)}")
    
    
    
    
run()

