import streamlit as st
import pickle

# Judul
st.title("Klasifikasi Pada Data Fruit")

# Memilih jenis data
jenis_algoritma = st.radio("Pilih Jenis Algoritma", ["Support Vector Machine (SVM)", "Perceptron", "Random Forest"])

if jenis_algoritma == "Support Vector Machine (SVM)":
    # Meembuka model Algoritma SVM
    with open('svm.pkl', 'rb') as file:
        model = pickle.load(file)

    # Input untuk variabel
    with st.expander("Masukkan Data Fruit"):
        fitur1 = st.number_input("Diameter")
        fitur2 = st.number_input("Weight")
        fitur3 = st.number_input("Red")
        fitur4 = st.number_input("Green")
        fitur5 = st.number_input("Blue")

    # Prediksi
    if st.button("Prediksi"):
        prediction = model.predict([[fitur1, fitur2, fitur3, fitur4, fitur5]])
        predicted_label = model.label[prediction[0]]
        st.success(f"Predicted Class: {predicted_label}")

elif jenis_algoritma == "Perceptron":
    # Membuka model Algoritma Perceptron
    with open('perceptron.pkl', 'rb') as file:
        model = pickle.load(file)

    # Input untuk variabel
    with st.expander("Masukkan Data Fruit"):
        fitur1 = st.number_input("Diameter")
        fitur2 = st.number_input("Weight")
        fitur3 = st.number_input("Red")
        fitur4 = st.number_input("Green")
        fitur5 = st.number_input("Blue")

    # Prediksi
    if st.button("Prediksi"):
        prediction = model.predict([[fitur1, fitur2, fitur3, fitur4, fitur5]])
        predicted_label = model.label[prediction[0]]
        st.success(f"Predicted Class: {predicted_label}")

elif jenis_algoritma == "Random Forest":
    # Membuka model Algoritma Random  Forest
    with open('randomforest.pkl', 'rb') as file:
        model = pickle.load(file)

    # Input untuk variabel
    with st.expander("Masukkan Data Fruit"):
        fitur1 = st.number_input("Diameter")
        fitur2 = st.number_input("Weight")
        fitur3 = st.number_input("Red")
        fitur4 = st.number_input("Green")
        fitur5 = st.number_input("Blue")

    # Prediksi
    if st.button("Prediksi"):
        prediction = model.predict([[fitur1, fitur2, fitur3, fitur4, fitur5]])
        predicted_label = model.label[prediction[0]]
        st.success(f"Predicted Class: {predicted_label}")
