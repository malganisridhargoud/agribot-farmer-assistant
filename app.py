import streamlit as st
import time # For simulating loading

# Assume these are in ai_engine.py and chatbot.py
from ai_engine import get_crop_suggestion, get_fertilizer_advice, get_pest_control, get_market_price, get_govt_schemes
from chatbot import chat_response

# --- Page Configuration ---
st.set_page_config(
    page_title="Agribot - AI Assistant for Farmers",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for a Modern Look ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-right: 4rem;
        padding-left: 4rem;
        padding-bottom: 2rem;
        background-color: #f0f2f6; /* Light gray background for content */
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }

    /* Sidebar styling */
    .stSidebar {
        background-color: #004d40; /* Dark green */
        color: white;
        padding-top: 2rem;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    .stSidebar .stRadio > label {
        color: white;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .stSidebar .stRadio div[role="radiogroup"] {
        background-color: #006050; /* Slightly lighter green for radio group */
        border-radius: 8px;
        padding: 10px;
    }
    .stSidebar .stRadio div[role="radiogroup"] label > div {
        color: white !important; /* Ensure radio button text is white */
        padding: 8px 12px;
        border-radius: 6px;
        transition: background-color 0.2s;
    }
    .stSidebar .stRadio div[role="radiogroup"] label:hover > div {
        background-color: #00796b; /* Hover for radio buttons */
    }
    .stSidebar .stRadio div[role="radiogroup"] label > div[aria-checked="true"] {
        background-color: #388e3c; /* Selected radio button color (green) */
        font-weight: 700;
    }

    /* Header styling */
    h1, h2, h3, h4, h5, h6 {
        color: #004d40; /* Dark green for headings */
        font-weight: 600;
    }

    /* Button styling */
    .stButton > button {
        background-color: #388e3c; /* Green button */
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
        transition: background-color 0.2s, transform 0.1s;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #2e7d32; /* Darker green on hover */
        transform: translateY(-2px);
    }

    /* Info and Success messages */
    .stAlert {
        border-radius: 8px;
        padding: 1rem;
        margin-top: 1rem;
        font-weight: 500;
    }
    .stAlert.info {
        background-color: #e3f2fd; /* Light blue */
        color: #1565c0; /* Dark blue */
        border-left: 5px solid #1565c0;
    }
    .stAlert.success {
        background-color: #e8f5e9; /* Light green */
        color: #2e7d32; /* Dark green */
        border-left: 5px solid #2e7d32;
    }

    /* Input fields */
    .stTextInput > div > div > input, .stSelectbox > div > div > div, .stNumberInput > div > label + div > div > input {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 0.5rem 1rem;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    .stTextInput > div > div > input:focus, .stSelectbox > div > div > div:focus-within, .stNumberInput > div > label + div > div > input:focus {
        border-color: #388e3c;
        box-shadow: 0 0 0 0.2rem rgba(56, 142, 60, 0.25);
        outline: none;
    }

    /* Custom divider */
    .st-emotion-cache-nahz7x { /* Targeting the Streamlit divider line */
        background-color: #e0e0e0;
        height: 1px;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: flex-start; gap: 20px; padding-bottom: 20px;">
        <img src="https://storage.googleapis.com/a1aa/image/157904af-a8a9-47f2-00ad-9dd4fdbc14f5.jpg" width="80" style="border-radius: 50%;">
        <div>
            <h1 style="margin: 0; color: #004d40;">Agribot <span style="font-size: 0.7em; color: #388e3c;">🌱</span></h1>
            <p style="margin: 0; font-size: 1.1em; color: #555;">Your AI-Powered Farming Assistant for Indian Farmers</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---") # Custom styled divider

# --- Sidebar Navigation ---
with st.sidebar:
    st.image("https://storage.googleapis.com/a1aa/image/157904af-a8a9-47f2-00ad-9dd4fdbc14f5.jpg", width=120)
    st.markdown("<h2 style='color:white;'>Navigation</h2>", unsafe_allow_html=True)
    menu = {
        "Chatbot Assistant": "🤖",
        "Crop Suggestion": "🌾",
        "Fertilizer Advice": "🌿",
        "Pest Control": "🐛",
        "Market Prices": "📈",
        "Govt Schemes": "🏛"
    }
    # Create radio buttons with icons
    choice = st.radio(
        "Go to",
        options=list(menu.keys()),
        format_func=lambda x: f"{menu[x]} {x}"
    )

# --- Main Content Area ---
st.markdown("<br>", unsafe_allow_html=True) # Add some space

if choice == "Chatbot Assistant":
    st.header("🤖 Chatbot - Ask your queries")
    st.markdown("---")
    st.write("Ask me anything related to agriculture! I'm here to help.")

    user_input = st.text_input("Your question:", placeholder="e.g., How to improve soil fertility?")

    if user_input:
        with st.spinner("Agribot is thinking..."):
            time.sleep(1) # Simulate AI processing time
            response = chat_response(user_input)
        st.success(response)
        st.info("💡 Tip: Try asking about specific crops, diseases, or market trends!")

elif choice == "Crop Suggestion":
    st.header("🌾 Smart Crop Suggestion")
    st.markdown("---")
    st.write("Get personalized crop recommendations based on your soil type, climate, and season.")

    col1, col2, col3 = st.columns(3)
    with col1:
        soil = st.selectbox("Soil Type", ["Select", "Loamy", "Sandy", "Clay", "Silty", "Peaty", "Chalky"], help="Choose the predominant soil type of your farm.")
    with col2:
        climate = st.selectbox("Climate", ["Select", "Tropical", "Dry", "Temperate", "Continental", "Polar"], help="Select the climate zone of your region.")
    with col3:
        season = st.selectbox("Season", ["Select", "Kharif (Monsoon)", "Rabi (Winter)", "Zaid (Summer)"], help="Which growing season are you planning for?")

    if st.button("Get Suggestions", type="primary"):
        if soil == "Select" or climate == "Select" or season == "Select":
            st.warning("Please select all fields to get a crop suggestion.")
        else:
            with st.spinner("Analyzing conditions..."):
                time.sleep(1.5) # Simulate processing
                suggestion = get_crop_suggestion(soil, climate, season)
            st.success(f"*Recommended Crops:* {suggestion}")
            st.info("For best results, consider a detailed soil test.")

elif choice == "Fertilizer Advice":
    st.header("🌿 Fertilizer Usage Advice")
    st.markdown("---")
    st.write("Receive tailored fertilizer recommendations for your crops based on soil pH.")

    crop = st.text_input("Crop Name", placeholder="e.g., Wheat, Tomato")
    ph = st.number_input("Soil pH", min_value=3.0, max_value=10.0, step=0.1, value=6.5, help="Enter your soil's pH value (e.g., 6.5).")

    if st.button("Get Fertilizer Advice", type="primary"):
        if not crop or not ph:
            st.warning("Please enter both Crop Name and Soil pH.")
        else:
            with st.spinner("Calculating fertilizer needs..."):
                time.sleep(1.5)
                advice = get_fertilizer_advice(crop, ph)
            st.success(f"*Fertilizer Recommendation:* {advice}")
            st.info("Always follow local agricultural guidelines and test your soil regularly.")

elif choice == "Pest Control":
    st.header("🐛 Pest Control Measures")
    st.markdown("---")
    st.write("Find effective pest control strategies for common agricultural pests.")

    pest = st.text_input("Pest Name", placeholder="e.g., Aphids, Fall Armyworm")
    crop_affected = st.text_input("Affected Crop", placeholder="e.g., Cotton, Maize")

    if st.button("Get Pest Control Advice", type="primary"):
        if not pest or not crop_affected:
            st.warning("Please enter both Pest Name and Affected Crop.")
        else:
            with st.spinner(f"Searching for {pest} control on {crop_affected}..."):
                time.sleep(1.5)
                control_advice = get_pest_control(pest, crop_affected)
            st.success(f"*Pest Control Advice:* {control_advice}")
            st.info("Consider integrated pest management (IPM) for sustainable solutions.")

elif choice == "Market Prices":
    st.header("📈 Market Price Estimation")
    st.markdown("---")
    st.write("Get estimated market prices for your crops in specific locations.")

    crop_price = st.text_input("Crop Name", placeholder="e.g., Paddy, Onion")
    location_price = st.text_input("Your Location (City/District)", placeholder="e.g., Hyderabad, Nashik")

    if st.button("Get Market Prices", type="primary"):
        if not crop_price or not location_price:
            st.warning("Please enter both Crop Name and Location.")
        else:
            with st.spinner(f"Fetching market prices for {crop_price} in {location_price}..."):
                time.sleep(2) # Longer simulate for market data fetch
                price_info = get_market_price(crop_price, location_price)
            st.success(f"*Estimated Market Price:* {price_info}")
            st.info("Market prices can fluctuate. This is an estimation.")

elif choice == "Govt Schemes":
    st.header("🏛 Government Schemes & Subsidies")
    st.markdown("---")
    st.write("Discover relevant government schemes and subsidies for farmers in your state.")

    state_scheme = st.selectbox(
        "Your State",
        ["Select", "Andhra Pradesh", "Bihar", "Karnataka", "Maharashtra", "Punjab", "Tamil Nadu", "Uttar Pradesh", "West Bengal", "Gujarat", "Rajasthan", "Madhya Pradesh", "Kerala", "Haryana", "Odisha", "Assam"],
        help="Select your state to view applicable schemes."
    )

    if st.button("Get Schemes", type="primary"):
        if state_scheme == "Select":
            st.warning("Please select your State.")
        else:
            with st.spinner(f"Loading schemes for {state_scheme}..."):
                time.sleep(1.5)
                schemes_info = get_govt_schemes(state_scheme)
            st.success(f"*Available Schemes:* {schemes_info}")
            st.info("For detailed information and application, please visit official government websites.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; color: #777; font-size: 0.9em;">
        Agribot - Empowering Farmers with AI. <br>
        Developed with ❤ for the agricultural community of India.
    </p>
    """,
    unsafe_allow_html=True
)