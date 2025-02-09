import streamlit as st

# Make Item at center
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.header("TPN APP")
with col3:
    st.write("")


# Space
st.header("")

# HERO section
col1, col2 = st.columns(2)
with col1:
    st.image("baby - circle.png")
with col2:
    st.write("")
    st.write("")
    st.subheader("A Baby Receiving Parenteral Nutrition")
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged")

# Space
st.header("")

#Date
col1, col2, col3 = st.columns(3)  
with col1:
    date = st.date_input("Date")
with col2:
    doctor_name = st.text_input("Doctor Name", max_chars = 50)
with col3:
    unit = st.text_input("Unit")


#Basic patient Info
st.subheader("Basic patient Info")
col1, col2 = st.columns(2)  
with col1:
    patient_name = st.text_input("Patient Name", max_chars = 50)
with col2:
    ID = st.text_input("ID")

col3, col4, col5 = st.columns(3)
with col3:
    age = st.number_input("Age", min_value = 1, max_value = 24)  
with col4:
    age_unit = st.selectbox("Age Unit", ("Choose...", "Hours", "Days", "Weeks", "Months", "Years"))
with col5:
    weight = st.number_input("Weight(kg)", min_value = 0.5, format="%0.1f")

#Fluids
st.subheader("Fluids")
col1, col2, col3, col4 = st.columns(4)
with col1:
    fluids = st.text_input("Fluids (e.g. FM - Drugs)", max_chars = 30)
with col2:
    fluids_amount = st.number_input("Fluids Amount(ml)", format="%0.0f")
with col3:
    drugs = st.number_input("Drugs(ml)", format="%0.0f")
with col4:
    tpn_amount = st.number_input("TPN Amount(ml)", value= fluids_amount - drugs,disabled= True, format="%0.0f")

#Intravenous Line TYPE
st.subheader("Intravenous Line")
line = st.selectbox("Central/Peripheral line ", ("Choose...","Central Line", "Peripheral line"))

#Items
st.subheader("Items")
col1, col2, col3, col4 = st.columns(4)
with col1:
    protein = st.number_input("Protein(gm)", min_value= 0.1, max_value= 4.0)
with col2:
    lipid = st.number_input("Lipid(gm)", min_value= 0.1, max_value= 3.0)
with col3:
    na = st.number_input("Na(meq)", min_value= 1, max_value= 5)
with col4:
    k = st.number_input("K(meq/L)")

col1, col2 = st.columns(2)
with col1:
    mg = st.number_input("Mg")
with col2:
    po4 = st.number_input("Po4", value= 1)

col1, col2, col3 = st.columns(3)
with col1:
    GIR = st.number_input("GIR")
with col2:
    glucose_amount = st.number_input("Total Glucose Amount(ml)")
with col3:
    glucose_conc = st.text_input("Glucose conc (%)")

# Space
st.header("")

#Print
print_content = st.markdown('''

''')

if st.button("Print PDF", type= "primary"):
    st.write("Date: ", date)

    #Basic patient Info
    st.subheader("Basic patient Info")
    col1, col2 = st.columns(2)  
    with col1:
        st.write("Name: ", patient_name)
    with col2:
        st.write("ID: ",  ID)
    col3, col4 = st.columns(2)    
    with col3:
        st.write("Age: ",  age, "", age_unit)
    with col4:    
        st.write("Weight: ",  weight, "Kg")

    #FLUIDS
    st.subheader("Fluids & Line")
    col1, col2 = st.columns(2)  
    with col1:
        st.write("Fluids: ", fluids)
    with col2:
        st.write("Fluids Amount: ", fluids_amount, " ml",)

    col3, col4 = st.columns(2)     
    with col3:
        st.write("Drugs: ", drugs, " ml")
    with col4:
        st.write("TPN amount: ", tpn_amount, " ml")

    #Intravenous Item
    st.write("Line: ", line)

    #FLUIDS
    st.subheader("Items")
    st.write("Protein: ", protein * weight * 10, "gm")
    st.write("Lipid: ", lipid * weight * 5, " gm",)
    st.write("Na: ", na * weight * 1000 / 514, " 3% saline")
    st.write("K: ", (tpn_amount * (k/2) / 1000), " Potassium")
    st.write("Mg: ", mg * weight * 1.25, "gm")
    if (po4 == 1):
        st.write("Po4: ", po4 * weight, " gm",)
    st.write("GIR: ", GIR)
    st.write("Glucose Amount", glucose_amount, " ml => ", glucose_conc)

    #Rate of fluids
    st.subheader("Rate")
    st.write("Rate over 24 hours: ", tpn_amount/24, "ml/hr")

    #Doctor & the Unit
    st.subheader("Doctor & Unit")
    st.write("Doctor: ", doctor_name)
    st.write("Unit: ", unit)



