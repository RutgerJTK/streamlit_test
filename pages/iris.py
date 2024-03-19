import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

@st.cache_data
def load_data():
    iris_data = pd.read_csv("data/Iris.csv")
    return iris_data

def iris_classifier():
    st.title("Iris Dataset Classification")

    iris_data = load_data()

    # Display the first few rows of the dataset
    st.subheader("Iris Dataset:")
    st.write(iris_data.head())

    # Plot Sepal Length vs. Sepal Width
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])

    st.subheader("Scatter Plot: Sepal Length vs. Sepal Width")
    sns.scatterplot(data=iris_data, x="SepalLengthCm", y="SepalWidthCm", hue="Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    st.pyplot(fig)

    # Plot Petal Length vs. Petal Width
    fig2, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    st.subheader("Scatter Plot: Petal Length vs. Petal Width")
    sns.scatterplot(data=iris_data, x="PetalLengthCm", y="PetalWidthCm", hue="Species")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    st.pyplot(fig2)

    # User input for sepal and petal measurements
    st.sidebar.subheader("Input Iris Measurements:")
    sepal_length = st.sidebar.slider("Sepal Length (cm)", float(iris_data["SepalLengthCm"].min()), float(iris_data["SepalLengthCm"].max()))
    sepal_width = st.sidebar.slider("Sepal Width (cm)", float(iris_data["SepalWidthCm"].min()), float(iris_data["SepalWidthCm"].max()))
    petal_length = st.sidebar.slider("Petal Length (cm)", float(iris_data["PetalLengthCm"].min()), float(iris_data["PetalLengthCm"].max()))
    petal_width = st.sidebar.slider("Petal Width (cm)", float(iris_data["PetalWidthCm"].min()), float(iris_data["PetalWidthCm"].max()))

    # Predict the species based on user input
    input_features = [[sepal_length, sepal_width, petal_length, petal_width]]
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(iris_data.drop(['Species', 'Id'], axis=1), iris_data['Species'])
    prediction = classifier.predict(input_features)

    st.sidebar.subheader("Predicted Species:")
    st.sidebar.write(prediction[0])

if __name__ == "__main__":
    iris_classifier()
