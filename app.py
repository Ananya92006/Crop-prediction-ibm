import streamlit as st
import pandas as pd
import pickle

# 🔧 Fix for AttributeError: _RemainderColsList
import sklearn.compose._column_transformer
class _RemainderColsList(list):
    pass
sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList

# ✅ Add Background Image via CSS
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://unsplash.com/photos/brown-field-near-tree-during-daytime-sYffw0LNr7s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: rgba(0,0,0,0);
    }

    .css-18e3th9 {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Load pipeline
with open("pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

# 📊 Prediction logic
def predict_crop_yield(pipeline, area, item, year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp):
    input_data = pd.DataFrame({
        'Area': [area],
        'Item': [item],
        'Year': [year],
        'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
        'pesticides_tonnes': [pesticides_tonnes],
        'avg_temp': [avg_temp]
    })
    prediction = pipeline.predict(input_data)
    return prediction[0]

# 🖥️ Main App
def main():
    st.markdown("<h1 style='text-align: center;'>🌾 Crop Yield Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size:18px;'>Predict crop yield based on environmental and agricultural factors.</p>", unsafe_allow_html=True)
    st.markdown("---")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            area = st.text_input('🌍 Area', 'Albania')
            year = st.number_input('📅 Year', min_value=1900, max_value=2100, value=2025)
            pesticides_tonnes = st.number_input('🧪 Pesticides (tonnes)', value=130.0)
        with col2:
            item = st.text_input('🌾 Crop Item', 'Maize')
            average_rain_fall_mm_per_year = st.number_input('🌧️ Avg. Rainfall (mm/year)', value=1500.0)
            avg_temp = st.number_input('🌡️ Avg. Temperature (°C)', value=17.5)

    st.markdown("")

    if st.button('🔍 Predict Crop Yield'):
        predicted_yield = predict_crop_yield(
            pipeline,
            area,
            item,
            year,
            average_rain_fall_mm_per_year,
            pesticides_tonnes,
            avg_temp
        )
        st.success(f"✅ Predicted Crop Yield: **{predicted_yield:.2f} hg/ha**")

    st.markdown("---")
    st.markdown("<p style='text-align:center;'>© 2025 Crop Predictor | Powered by Streamlit</p>", unsafe_allow_html=True)

# ▶️ Run
if __name__ == "__main__":
    main()




# import streamlit as st
# import pandas as pd
# import pickle

# # 🔧 Fix for AttributeError: _RemainderColsList
# import sklearn.compose._column_transformer
# class _RemainderColsList(list):
#     pass
# sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList

# # 🚀 Load model pipeline
# with open("pipeline.pkl", "rb") as f:
#     pipeline = pickle.load(f)

# # 📊 Prediction function
# def predict_crop_yield(pipeline, area, item, year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp):
#     input_data = pd.DataFrame({
#         'Area': [area],
#         'Item': [item],
#         'Year': [year],
#         'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
#         'pesticides_tonnes': [pesticides_tonnes],
#         'avg_temp': [avg_temp]
#     })
#     prediction = pipeline.predict(input_data)
#     return prediction[0]

# # 🖥️ Streamlit app
# def main():
#     st.title("🌾 Crop Yield Prediction App")
#     st.write("Predict crop yield based on environmental and agricultural factors.")

#     # Input fields
#     area = st.text_input('Area', 'Albania')
#     item = st.text_input('Crop Item', 'Maize')
#     year = st.number_input('Year', min_value=1900, max_value=2100, value=2025)
#     average_rain_fall_mm_per_year = st.number_input('Average Rainfall (mm/year)', value=1500.0)
#     pesticides_tonnes = st.number_input('Pesticides (tonnes)', value=130.0)
#     avg_temp = st.number_input('Average Temperature (°C)', value=17.5)

#     if st.button('Predict Crop Yield'):
#         predicted_yield = predict_crop_yield(
#             pipeline,
#             area,
#             item,
#             year,
#             average_rain_fall_mm_per_year,
#             pesticides_tonnes,
#             avg_temp
#         )
#         st.success(f"🌾 Predicted Crop Yield: **{predicted_yield:.2f} hg/ha**")

# if __name__ == "__main__":
#     main()
# import streamlit as st
# import pandas as pd
# import pickle

# st.set_page_config(page_title="Crop Yield Predictor", layout="centered")

# # 🫧 Inject bubble background CSS
# st.markdown("""
# <style>
# .bubble-bg {
#   position: fixed;
#   top: 0;
#   left: 0;
#   height: 100vh;
#   width: 100vw;
#   overflow: hidden;
#   z-index: -1;
# }
# .bubble {
#   position: absolute;
#   bottom: -100px;
#   width: 40px;
#   height: 40px;
#   background: rgba(0, 255, 127, 0.25);
#   border-radius: 50%;
#   animation: rise 20s infinite ease-in;
# }
# .bubble:nth-child(2) { left: 20%; width: 60px; height: 60px; animation-duration: 22s; }
# .bubble:nth-child(3) { left: 40%; animation-duration: 25s; }
# .bubble:nth-child(4) { left: 60%; width: 50px; height: 50px; animation-duration: 18s; }
# .bubble:nth-child(5) { left: 80%; animation-duration: 28s; }

# @keyframes rise {
#   0%   { bottom: -100px; transform: translateX(0) scale(1); }
#   50%  { transform: translateX(20px) scale(1.2); }
#   100% { bottom: 110%; transform: translateX(-20px) scale(1); }
# }
# </style>

# <div class="bubble-bg">
#   <div class="bubble"></div>
#   <div class="bubble"></div>
#   <div class="bubble"></div>
#   <div class="bubble"></div>
#   <div class="bubble"></div>
# </div>
# """, unsafe_allow_html=True)

# # 💡 Custom style for the heading container
# st.markdown("""
# <style>
# .main-container {
#     background-color: rgba(255, 255, 255, 0.9);
#     padding: 20px;
#     border-radius: 16px;
#     box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
#     text-align: center;
#     margin-bottom: 20px;
# }
# h1 {
#     color: #2E8B57;
#     font-family: 'Arial', sans-serif;
# }
# </style>

# <div class="main-container">
#     <h1>🌾 Crop Yield Predictor</h1>
#     <p>Predict crop yield based on environmental and agricultural data.</p>
# </div>
# """, unsafe_allow_html=True)

# # 🎯 Load trained model
# with open("pipeline.pkl", "rb") as f:
#     pipeline = pickle.load(f)

# # 🧾 User Inputs
# area = st.selectbox("📍 Area", ["India", "Albania", "Brazil", "Canada", "China"])
# item = st.selectbox("🌿 Crop Item", ["Wheat", "Rice", "Maize", "Barley"])
# year = st.number_input("📅 Year", min_value=2000, max_value=2030, value=2025)
# rainfall = st.number_input("🌧️ Average Rainfall (mm/year)", value=1500.0)
# pesticides = st.number_input("🧪 Pesticides (tonnes)", value=130.0)
# avg_temp = st.number_input("🌡️ Avg Temperature (°C)", value=25.0)

# # 🔮 Prediction
# if st.button("Predict Yield"):
#     input_df = pd.DataFrame({
#         'Area': [area],
#         'Item': [item],
#         'Year': [year],
#         'average_rain_fall_mm_per_year': [rainfall],
#         'pesticides_tonnes': [pesticides],
#         'avg_temp': [avg_temp]
#     })

#     prediction = pipeline.predict(input_df)[0]
#     st.success(f"🌾 Predicted Crop Yield: **{prediction:.2f} hg/ha**")
