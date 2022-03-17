import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open("loan_model.pkl", "rb"))

def run():
    img1 = Image.open("bankpic.jfif")
    img1 = img1.resize((400,350))
    st.image(img1, use_column_width = False) 
    st.title("Loan Eligibility prediction web app")
    
    ## Acc Number
    ac = st.text_input("Account Number")

    ##Full Name
    fn = st.text_input("Fill Name")

    ##Gender
    gen =("Female", "Male")
    genk = list(range(len(gen)))
    ge = st.selectbox("Gender", genk, format_func= lambda x: gen[x] )    
    
    
    ##Married
    me =("No", "Yes")
    menk = list(range(len(me)))
    gem = st.selectbox("Married", menk, format_func= lambda x: me[x] ) 
    
    
    ##NO of Dependents
    med =("No", "One","Two","More than two")
    mens = list(range(len(med)))
    ges = st.selectbox("No Of Dependents", mens, format_func= lambda x: med[x] )
    
    ##Education
    educ =("Graduate", "No Graduate")
    eco = list(range(len(educ)))
    gece = st.selectbox("Education", eco, format_func= lambda x: educ[x] )
    
    ##AEmPoyment status
    sef =("Job", "Business")
    sa = list(range(len(sef)))
    geca = st.selectbox("Employment Status", sa, format_func= lambda x: sef[x] )
    
    ##   Applicant income
    ai = st.number_input("Applicant income($)", value =0)
    
    ##  coApplicant income
    cai = st.number_input("Co Applicant income($)", value =0)
    
    ##   Loan Amount
    la = st.number_input("Loan Amount", value =0)
    
    ##Property Area
    pa =("Rural", "Semi Urban", "urban")
    p = list(range(len(pa)))
    gecp = st.selectbox("Property area", p, format_func= lambda x: pa[x] )
    
    ##Credit history
    ch =("Between 300 to 500", "Above 500")
    re = list(range(len(educ)))
    chh = st.selectbox("Credit History", re, format_func= lambda x: ch[x] )
    

    ##Loan Amount Term
    LT =("2 Month", "6 Month","8 Month","1 Year", "16 Month ")
    menl = list(range(len(LT)))
    dur = st.selectbox("Loan Amount Term", menl, format_func= lambda x: LT[x] )
    
    if st.button("submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 100
        if dur ==2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        
        features = [[ge,gem,ges,gece,geca,ai,cai,la,gecp,chh,dur]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans =  int("".join(lc))
        if ans == 0:
            st.error(
                "Hello:" + fn + "||"
                "Account number : "+ac +"||"
                "According to our calculations,you will not get the loan from bank"
                
                )
        else:
            st.success(
                "Hello:" + fn + "||"
                "Account number : "+ac +"||"
                "Congratulations!! You will get the loan from the bank"
            )
     
run()   