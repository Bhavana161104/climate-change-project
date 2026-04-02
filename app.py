import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Title
st.title("🌍 Climate Change Analysis & Prediction")

# Load data
df = pd.read_csv("GlobalLandTemperaturesByCity.csv")

# Data cleaning
df = df.dropna()
df['dt'] = pd.to_datetime(df['dt'])
df['year'] = df['dt'].dt.year

# Sidebar
st.sidebar.header("Filter Data")

# Select country
country = st.sidebar.selectbox("Select Country", df['Country'].unique())

filtered_data = df[df['Country'] == country]

# Show data
st.subheader(f"Temperature Data for {country}")
st.write(filtered_data.head())

# Plot trend
st.subheader("📈 Temperature Trend")

temp_data = filtered_data.groupby('year')['AverageTemperature'].mean()

fig, ax = plt.subplots()
ax.plot(temp_data.index, temp_data.values)
ax.set_xlabel("Year")
ax.set_ylabel("Temperature")
st.pyplot(fig)

# Model
model_df = temp_data.reset_index()

X = model_df[['year']]
y = model_df['AverageTemperature']

model = LinearRegression()
model.fit(X, y)

# Prediction
st.subheader("🔮 Future Prediction")

future_year = st.number_input("Enter Year", min_value=2025, max_value=2100)

prediction = model.predict([[future_year]])

st.write(f"Predicted Temperature for {future_year}: {prediction[0]:.2f}")