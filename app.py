import streamlit as st
import streamlit.components.v1 as components
import markdown
import os
from pathlib import Path
import pandas as pd

# Set page config for a modern look
st.set_page_config(
    page_title="AquiPro - Agency Growth System",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        max-width: 100%;
        background-color: #f8fafc;
    }
    
    /* Sidebar Styles */
    .css-1d391kg {
        background-color: #1e293b;
    }
    .css-1d391kg .stTitle {
        color: white;
    }
    
    /* Dashboard Container */
    .dashboard-container {
        padding: 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Metrics Grid */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.75rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .metric-title {
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
    }
    .metric-value {
        font-size: 2.25rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
        font-family: 'Inter', sans-serif;
    }
    .metric-change {
        display: flex;
        align-items: center;
        gap: 0.375rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .metric-change.positive {
        color: #059669;
    }
    
    /* Activity Card */
    .activity-card {
        background: white;
        padding: 1.75rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 2rem;
    }
    .activity-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
    }
    .activity-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #111827;
        letter-spacing: -0.025em;
    }
    .activity-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.25rem 0;
        border-bottom: 1px solid #e5e7eb;
    }
    .activity-item:last-child {
        border-bottom: none;
    }
    .activity-content {
        display: flex;
        flex-direction: column;
        gap: 0.375rem;
    }
    .activity-action {
        font-weight: 600;
        color: #111827;
        font-size: 0.9375rem;
    }
    .activity-detail {
        color: #6b7280;
        font-size: 0.875rem;
    }
    .activity-time {
        color: #9ca3af;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Progress Section */
    .progress-section {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
    }
    .progress-card {
        background: white;
        padding: 1.75rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
    }
    .progress-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .progress-header {
        margin-bottom: 1.5rem;
    }
    .progress-title {
        font-size: 1.125rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    .progress-description {
        color: #6b7280;
        font-size: 0.875rem;
        line-height: 1.5;
    }
    .progress-bar {
        height: 8px;
        background: #e5e7eb;
        border-radius: 4px;
        margin: 1.25rem 0;
        overflow: hidden;
    }
    .progress-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #2563eb, #3b82f6);
        border-radius: 4px;
        transition: width 0.5s ease;
    }
    .progress-stats {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 0.75rem;
    }
    .progress-percentage {
        font-weight: 700;
        color: #111827;
        font-size: 1.125rem;
    }
    .progress-label {
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .action-items {
        margin-top: 1.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid #e5e7eb;
    }
    .action-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.625rem 0;
        color: #4b5563;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .action-item:before {
        content: "";
        width: 6px;
        height: 6px;
        background: #3b82f6;
        border-radius: 50%;
    }
    
    /* Headers */
    h1 {
        color: #111827;
        font-size: 1.875rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
        margin-bottom: 2rem !important;
    }
    h2 {
        color: #111827;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em !important;
        margin: 2.5rem 0 1.5rem !important;
    }
    
    /* Auth Container */
    .auth-container {
        max-width: 400px;
        margin: 4rem auto;
        padding: 2.5rem;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .auth-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .auth-title {
        font-size: 1.875rem;
        font-weight: 700;
        color: #111827;
        letter-spacing: -0.025em;
        margin-bottom: 0.75rem;
    }
    .auth-subtitle {
        color: #6b7280;
        font-size: 1rem;
    }
    .auth-form {
        display: flex;
        flex-direction: column;
        gap: 1.25rem;
    }
    /* Override Streamlit's default form styling */
    .stTextInput > div > div {
        padding: 0.75rem !important;
        background: #f9fafb !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 8px !important;
    }
    .stTextInput > div > div > input {
        color: #111827 !important;
    }
    .stTextInput > label {
        color: #374151 !important;
        font-weight: 500 !important;
    }
    .stTextInput > div > div:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
    }
    .stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
        color: white !important;
        padding: 0.75rem !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        letter-spacing: 0.025em !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #1d4ed8, #2563eb) !important;
        transform: translateY(-1px) !important;
    }
    /* Hide Streamlit branding */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    /* Style form container */
    .stForm {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    .stForm > div {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    
    /* Homepage Styles */
    .homepage {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background: white;
    }
    .logo-container {
        text-align: center;
        margin-bottom: 1rem;
    }
    .logo-text {
        font-family: 'Inter', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.05em;
    }
    .logo-line {
        width: 60px;
        height: 4px;
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        margin: 1.5rem auto;
        border-radius: 2px;
    }
    .author {
        font-size: 1.25rem;
        color: #64748b;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    .enter-app-btn {
        background: white;
        color: #1e40af;
        padding: 1rem 2.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.125rem;
        border: 2px solid #e2e8f0;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
    }
    .enter-app-btn:hover {
        background: #1e40af;
        color: white;
        border-color: #1e40af;
        transform: translateY(-2px);
    }
    
    /* Dashboard Styles */
    .metric-card {
        background: white;
        padding: 1.75rem;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 1rem;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .metric-value {
        font-family: 'Inter', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #111827;
        margin: 0.5rem 0;
    }
    .metric-label {
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }
    
    /* Module Content */
    .module-content {
        padding: 2rem;
        background: white;
        border-radius: 16px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
    }
    .module-title {
        color: #111827;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .module-description {
        color: #4b5563;
        font-size: 1rem;
        line-height: 1.5;
    }
    
    /* Sidebar */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #1e293b;
    }
    .css-1d391kg a, .css-1lcbmhc a {
        color: white !important;
    }
    
    /* Hide Streamlit Components */
    .stDeployButton, footer, header {
        display: none !important;
    }
    
    /* General Styles */
    .stApp {
        background-color: #f8fafc !important;
        color: #111827 !important;
    }
    
    /* Sidebar Styles */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #1e293b !important;
    }
    .css-1d391kg a, .css-1lcbmhc a {
        color: white !important;
    }
    .stSelectbox label {
        color: white !important;
    }
    .stSelectbox div[data-baseweb="select"] div {
        background-color: #2d3748 !important;
        color: white !important;
    }
    
    /* Module Styles */
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .module-card h3 {
        color: #111827;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .module-card p {
        color: #4b5563;
        margin-bottom: 1rem;
    }
    .nav-pills {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
        overflow-x: auto;
        padding-bottom: 0.5rem;
    }
    .nav-pill {
        background: white;
        color: #4b5563;
        padding: 0.75rem 1.5rem;
        border-radius: 9999px;
        font-weight: 500;
        white-space: nowrap;
        transition: all 0.2s;
        border: 1px solid #e5e7eb;
    }
    .nav-pill.active {
        background: #2563eb;
        color: white;
        border-color: #2563eb;
    }
    .nav-pill:hover {
        background: #f3f4f6;
    }
    .nav-pill.active:hover {
        background: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# Add styles for better contrast
st.markdown("""
<style>
.main-title {
    color: #1a202c !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    margin-bottom: 2rem !important;
    padding: 1rem !important;
    background-color: white !important;
    border-radius: 8px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
}
.lesson-box {
    background-color: white;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
.lesson-title {
    color: #1a202c;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
}
.lesson-content {
    color: #4a5568;
    font-size: 1.1rem;
    line-height: 1.6;
}
.key-point {
    background-color: #EDF2F7;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    color: #2D3748;
}
.navigation {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Add custom styles
st.markdown("""
<style>
/* Fix tab text contrast */
.stTabs [data-baseweb="tab-list"] {
    gap: 2rem;
    background-color: white;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}

.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 1rem;
    font-weight: 600;
    color: #4a5568 !important;
}

.stTabs [data-baseweb="tab-list"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
    color: #2563eb !important;
}

/* General text contrast fixes */
p, li {
    color: #1a202c !important;
}

h1, h2, h3 {
    color: #1a202c !important;
}

/* Sidebar Styles */
.css-1d391kg, .css-1lcbmhc {
    background-color: #1e293b !important;
}

/* Sidebar Text Colors */
.css-1d391kg .stSelectbox label {
    color: white !important;
}
.css-1d391kg .stSelectbox div[data-baseweb="select"] div {
    color: white !important;
}

/* Sidebar Dropdown Styles */
.stSelectbox [data-testid="stMarkdownContainer"] p {
    color: white !important;
}
.css-81oif8 {
    color: white !important;
}
.css-1d391kg .stSelectbox {
    color: white !important;
}

/* Selected Option */
.css-1d391kg .stSelectbox [aria-selected="true"] {
    background-color: #2d3748 !important;
    color: white !important;
}

/* Dropdown Options */
.css-1d391kg .stSelectbox [role="listbox"] {
    background-color: #1e293b !important;
}
.css-1d391kg .stSelectbox [role="option"] {
    color: white !important;
}
.css-1d391kg .stSelectbox [role="option"]:hover {
    background-color: #2d3748 !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session states and sections dictionary
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Define sections with better contrast
sections = {
    "Dashboard": {
        "icon": "📊",
        "description": "Overview and metrics"
    },
    "Acquisition": {
        "icon": "🎯",
        "description": "Build your client pipeline"
    },
    "Delivery": {
        "icon": "🚀",
        "description": "Streamline your operations"
    },
    "Growth": {
        "icon": "📈",
        "description": "Scale your business"
    },
    "Resources": {
        "icon": "📚",
        "description": "Access tools and templates"
    }
}

# Add styles for better contrast
st.markdown("""
<style>
/* Main Navigation Styles */
.css-1544g2n {
    padding: 1rem;
    background-color: white;
    border-radius: 8px;
    margin-bottom: 1rem;
}

/* Sidebar Title */
.sidebar-title {
    color: white !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    margin-bottom: 2rem !important;
    text-align: center !important;
    padding: 1rem !important;
    background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%) !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
}

/* Section Selection */
.css-1v0mbdj {
    margin-top: 1rem;
}
.css-1v0mbdj > label {
    color: white !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    margin-bottom: 0.5rem !important;
}
.css-1v0mbdj select {
    background-color: #2d3748 !important;
    color: white !important;
    border: 1px solid #4a5568 !important;
    border-radius: 6px !important;
    padding: 0.5rem !important;
}
.css-1v0mbdj select option {
    background-color: #2d3748 !important;
    color: white !important;
    padding: 0.5rem !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session states and sections dictionary
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'show_home' not in st.session_state:
    st.session_state.show_home = True

# Define sections
sections = {
    "Dashboard": "View your agency's performance",
    "Acquisition": "Client acquisition strategies",
    "Delivery": "Service delivery management",
    "Growth": "Agency growth tactics",
    "Resources": "Tools and resources"
}

def switch_to_auth():
    st.session_state.show_home = False
    st.rerun()

def switch_to_signup():
    st.session_state.show_signup = True
    st.rerun()

def switch_to_login():
    st.session_state.show_signup = False
    st.rerun()

# Homepage
if st.session_state.show_home:
    st.markdown("""
    <div class="homepage">
        <div class="logo-container">
            <div class="logo-text">AquiPro</div>
            <div class="logo-line"></div>
            <div class="author">By Dhruv Atluri</div>
        </div>
        <button class="enter-app-btn" onclick="document.querySelector('#enter-app-button').click()">Enter Platform</button>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Enter App", key="enter-app-button", help=None):
        switch_to_auth()

elif not st.session_state.logged_in:
    if not st.session_state.show_signup:
        # Login Form
        st.markdown("""
        <div class="auth-container">
            <div class="auth-header">
                <div class="auth-title">Welcome to AquiPro</div>
                <div class="auth-subtitle">Sign in to access your dashboard</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign In")
            
            if submitted:
                if len(password) >= 8:
                    st.session_state.logged_in = True
                    st.success("Signed in successfully!")
                    st.rerun()
                else:
                    st.error("Password must be at least 8 characters")
        
        st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Don't have an account? <a href="#" onclick="document.querySelector('.create-account-button').click()" style="color: #3b82f6; font-weight: 500;">Create one</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button for JavaScript click
        if st.button("Create Account", key="create-account-button", help=None):
            switch_to_signup()
            st.rerun()
    
    else:
        # Signup Form
        st.markdown("""
        <div class="auth-container">
            <div class="auth-header">
                <div class="auth-title">Create Account</div>
                <div class="auth-subtitle">Join AquiPro to grow your agency</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("signup_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Create Account")
            
            if submitted:
                if len(password) >= 8:
                    if password == confirm_password:
                        st.session_state.logged_in = True
                        st.success("Account created successfully!")
                        st.rerun()
                    else:
                        st.error("Passwords don't match")
                else:
                    st.error("Password must be at least 8 characters")
        
        st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem;">
            <p style="color: #6b7280; font-size: 0.875rem;">Already have an account? <a href="#" onclick="document.querySelector('.sign-in-button').click()" style="color: #3b82f6; font-weight: 500;">Sign in</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Hidden button for JavaScript click
        if st.button("Sign In", key="sign-in-button", help=None):
            switch_to_login()
            st.rerun()

else:
    # Initialize session state for metrics if not exists
    if 'metrics' not in st.session_state:
        st.session_state.metrics = {
            'revenue': [],
            'clients': [],
            'projects': [],
            'team_size': []
        }

    # Initialize session state for sub-module selection
    if 'sub_module' not in st.session_state:
        st.session_state.sub_module = 'Lead Generation'

    # Initialize session state for conversation step
    if 'conversation_step' not in st.session_state:
        st.session_state.conversation_step = 1

    # Initialize session state for user responses
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = {}

    # Initialize step state if not exists
    if 'step' not in st.session_state:
        st.session_state.step = 1

    # Sidebar
    with st.sidebar:
        st.markdown('<h1 class="sidebar-title">AquiPro</h1>', unsafe_allow_html=True)
        
        # Create the selectbox with icons and descriptions
        options = list(sections.keys())  # Simplified to just use the keys for now
        selected_section = st.selectbox("Choose Your Module", options)

    if selected_section == "Dashboard":
        st.title("Agency Automation Hub")
        
        # Automation Categories
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Client Communication</h3>
                <p>Automated email sequences and follow-ups</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Welcome sequences</li>
                    <li>Progress updates</li>
                    <li>Meeting reminders</li>
                </ul>
                <div style="margin-top: 1rem;">
                    <p style="color: #2563eb; font-weight: 500;">Status: Active</p>
                </div>
            </div>
            
            <div class="module-card">
                <h3>Project Management</h3>
                <p>Task automation and workflow management</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Task assignments</li>
                    <li>Deadline tracking</li>
                    <li>Progress reporting</li>
                </ul>
                <div style="margin-top: 1rem;">
                    <p style="color: #2563eb; font-weight: 500;">Status: Active</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Social Media</h3>
                <p>Content scheduling and posting automation</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Post scheduling</li>
                    <li>Analytics tracking</li>
                    <li>Engagement monitoring</li>
                </ul>
                <div style="margin-top: 1rem;">
                    <p style="color: #2563eb; font-weight: 500;">Status: Active</p>
                </div>
            </div>
            
            <div class="module-card">
                <h3>Reporting</h3>
                <p>Automated report generation and delivery</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Performance reports</li>
                    <li>Client dashboards</li>
                    <li>ROI tracking</li>
                </ul>
                <div style="margin-top: 1rem;">
                    <p style="color: #2563eb; font-weight: 500;">Status: Active</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Active Automations Overview
        st.subheader("Active Automations")
        
        # Create three columns for automation stats
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        
        with stat_col1:
            st.metric("Active Workflows", "12", "")
        
        with stat_col2:
            st.metric("Tasks Automated", "127", "")
            
        with stat_col3:
            st.metric("Time Saved (hrs/week)", "45", "")
            
        # Recent Automation Activity
        st.subheader("Recent Activity")
        
        activity_data = [
            {
                "time": "2 hours ago",
                "event": "Welcome sequence triggered for new client: Tech Solutions Inc.",
                "type": "Client Communication"
            },
            {
                "time": "4 hours ago",
                "event": "Monthly performance reports generated and sent to all clients",
                "type": "Reporting"
            },
            {
                "time": "Yesterday",
                "event": "Social media content scheduled for next week",
                "type": "Social Media"
            },
            {
                "time": "2 days ago",
                "event": "Project milestone notifications sent to team",
                "type": "Project Management"
            }
        ]
        
        for activity in activity_data:
            st.markdown(f"""
            <div style="padding: 1rem; background: white; border-radius: 0.5rem; margin-bottom: 0.5rem; border: 1px solid #e5e7eb;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="color: #4b5563; font-size: 0.875rem;">{activity['time']}</span>
                    <span style="color: #2563eb; font-size: 0.875rem;">{activity['type']}</span>
                </div>
                <div style="color: #111827;">{activity['event']}</div>
            </div>
            """, unsafe_allow_html=True)

    elif selected_section == "Acquisition":
        st.markdown('<h1 class="main-title">Client Acquisition</h1>', unsafe_allow_html=True)
        
        # Sub-module tabs with better contrast and unique names
        tabs = st.tabs([
            "**Lead Magnet Creation**",
            "**Sales Framework**", 
            "**Follow-up System**", 
            "**Proposal Writing**"
        ])

        with tabs[0]:  # Lead Generation
            if 'lead_gen_page' not in st.session_state:
                st.session_state.lead_gen_page = 1

            # Page 1: Lead Magnet Strategy
            if st.session_state.lead_gen_page == 1:
                st.title("Creating Irresistible Lead Magnets")
                
                st.write("""
                Hey everyone! Welcome back to another video. Today we're going to talk about something that's absolutely 
                crucial for your agency - lead magnets. I'm going to show you exactly how I create lead magnets that 
                convert at 47% or higher. Yes, you heard that right - 47%.

                But first, let me tell you a quick story. When I first started my agency, I made the biggest mistake 
                possible with lead magnets. I created this massive 50-page ebook about digital marketing. Spent weeks 
                on it. Guess what happened? Nobody downloaded it. Not a single person.

                That's when I realized something crucial - busy business owners don't want another ebook to read. They 
                want something they can use RIGHT NOW to solve a specific problem.

                So let me show you what actually works. There are three types of lead magnets that I've found convert 
                incredibly well for agencies:

                First, we have templates. These are absolute gold. I'm talking about things like:
                • Social media content calendars
                • Email campaign templates
                • Marketing budget spreadsheets
                • ROI calculators

                The key is that these need to be something they can use immediately. For example, we created a simple 
                Google Ads budget calculator. It helps businesses figure out exactly how much they need to spend to hit 
                their goals.

                The second type is what I call the 'Quick Win' guide. This isn't your typical PDF - it's a super specific, 
                step-by-step process that solves ONE problem. For example, we created a "5-Minute LinkedIn Optimization 
                Checklist" that shows exactly how to improve your LinkedIn profile for B2B lead generation.

                Here's why it worked so well - it promises (and delivers) value in just 5 minutes. Business owners love 
                that. They can implement it right away and see results almost immediately.

                In the next section, I'm going to show you exactly how to create and position these lead magnets for 
                maximum impact. Trust me, this is where most agencies get it completely wrong, and I'm going to show 
                you how to do it right.
                """)

                if st.button("Next Page →", key="lead_gen_next_1"):
                    st.session_state.lead_gen_page = 2
                    st.rerun()

            # Page 2: Lead Generation Strategy
            elif st.session_state.lead_gen_page == 2:
                st.title("Promoting Your Lead Magnet")
                
                st.write("""
                Welcome back! Now that you know how to create a killer lead magnet, let's talk about getting it in front 
                of the right people. This is where I see so many agencies mess up - they create something great but 
                nobody ever sees it.

                Let me tell you about a massive failure I had when I first started. I created this amazing lead magnet - 
                a social media audit template. It was genuinely good stuff. But I just put it on our website and expected 
                people to find it. Guess what happened? Nothing. Absolutely nothing.

                Then I realized something crucial - it's not about the number of downloads, it's about what happens AFTER 
                the download. Here's the exact follow-up sequence we developed that now converts 20% of our leads into 
                sales calls:

                Immediately after download:
                • Send the lead magnet (obviously)
                • Include a 2-minute video explaining how to get the most value from it
                • Add one quick win they can implement right now

                24 hours later:
                • Send an industry insight
                • Ask if they've had a chance to implement the quick win
                • Offer help if they're stuck

                3 days later:
                • Share another valuable tip (something not in the lead magnet)
                • Ask about their biggest challenge in [topic area]
                • This email gets the most responses - people love sharing their challenges

                5 days later:
                • Send a "common mistakes" email
                • Show how your service helps avoid these mistakes
                • Include a calendar link for those who want to learn more

                Here's what most people get wrong - they try to sell too soon. We don't pitch our services until day 5, 
                and even then, it's soft. We're just offering more help.

                The key is to keep providing value after the lead magnet. Think about it - if someone downloads a LinkedIn 
                checklist, they're probably trying to improve their LinkedIn presence. So every follow-up should help 
                them with that goal.

                That's it for this video! In the next one, I'll show you how to scale this entire process using 
                automation. Make sure to hit subscribe and the notification bell so you don't miss it. And hey, if 
                you've gotten value from this, give it a thumbs up - it really helps the channel.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="lead_gen_prev_2"):
                        st.session_state.lead_gen_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="lead_gen_next_2"):
                        st.session_state.lead_gen_page = 3
                        st.rerun()

            # Page 3: Converting Leads
            elif st.session_state.lead_gen_page == 3:
                st.title("Converting Leads Into Clients")
                
                st.write("""
                Alright, this is the final and most important part. You've got your lead magnet, you're promoting it 
                well, and now you're getting downloads. But how do you turn these leads into paying clients?

                Let me share a story that completely changed how I think about lead conversion. We had this lead magnet 
                that was getting tons of downloads - like 50-60 per week. But we weren't converting any of them into 
                clients. I was getting frustrated, thinking maybe lead magnets don't work.

                Then I realized something crucial - it's not about the number of downloads, it's about what happens AFTER 
                the download. Here's the exact follow-up sequence we developed that now converts 20% of our leads into 
                sales calls:

                Immediately after download:
                • Send the lead magnet (obviously)
                • Include a 2-minute video explaining how to get the most value from it
                • Add one quick win they can implement right now

                24 hours later:
                • Send an industry insight
                • Ask if they've had a chance to implement the quick win
                • Offer help if they're stuck

                3 days later:
                • Share another valuable tip (something not in the lead magnet)
                • Ask about their biggest challenge in [topic area]
                • This email gets the most responses - people love sharing their challenges

                5 days later:
                • Send a "common mistakes" email
                • Show how your service helps avoid these mistakes
                • Include a calendar link for those who want to learn more

                Here's what most people get wrong - they try to sell too soon. We don't pitch our services until day 5, 
                and even then, it's soft. We're just offering more help.

                The key is to keep providing value after the lead magnet. Think about it - if someone downloads a LinkedIn 
                checklist, they're probably trying to improve their LinkedIn presence. So every follow-up should help 
                them with that goal.

                That's it for this video! In the next one, I'll show you how to scale this entire process using 
                automation. Make sure to hit subscribe and the notification bell so you don't miss it. And hey, if 
                you've gotten value from this, give it a thumbs up - it really helps the channel.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="lead_gen_prev_3"):
                        st.session_state.lead_gen_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="lead_gen_start_over"):
                        st.session_state.lead_gen_page = 1
                        st.rerun()

        with tabs[1]:  # Sales System
            if 'sales_page' not in st.session_state:
                st.session_state.sales_page = 1

            # Page 1: Discovery Call Framework
            if st.session_state.sales_page == 1:
                st.title("The Perfect Discovery Call")
                
                st.write("""
                Hey everyone, welcome back to another video. Today I'm going to break down exactly how I run my discovery 
                calls that have been converting at over 80%. This is the exact same process I've used to close over 
                $500,000 in client deals in the past year alone.

                Now, before I dive in, let me tell you a quick story. When I first started my agency, I was terrible at 
                sales calls. I mean really bad. I would get on these calls and just start pitching right away. I'd talk 
                about our services, our process, how great we were... and guess what? I barely closed any deals.

                Then I had this breakthrough moment. I was looking at our CRM data and noticed something interesting. 
                The clients who ended up signing with us had an average of 7-8 touchpoints before they signed. But 
                we were giving up after 2-3 emails.

                So I developed what I call the "Value Ladder Follow-up System." Here's exactly how it works:

                Day 1: Send a value-packed resource
                • Something they can use immediately
                • No pitch, just pure value
                • Ask for feedback

                Day 3: Share relevant results
                • Make it relevant to their industry
                • Focus on the process, not just results
                • Include specific numbers and timelines

                Day 5: Send an industry insight
                • Share a trend or opportunity they might have missed
                • Position yourself as an expert
                • Make it actionable

                The key is that each touchpoint adds value. We're not just "checking in" - we're giving them a reason 
                to respond. And in the next section, I'll show you exactly how to create each of these touchpoints 
                and what to say in each one.
                """)

                if st.button("Next Page →", key="sales_next_1"):
                    st.session_state.sales_page = 2
                    st.rerun()

            # Page 2: Qualification Process
            elif st.session_state.sales_page == 2:
                st.title("Qualifying Your Leads")
                
                st.write("""
                Alright, welcome back. Now I'm going to share the exact email templates we use in our follow-up sequence. These 
                aren't just any templates - these have been tested and refined over hundreds of leads.

                Let me tell you a quick story about these templates. We had a client who was using generic follow-up 
                emails and getting a 2% response rate. We implemented these templates, and their response rate shot up 
                to 23%. That's more than a 10x improvement!

                Here's the first email template - the Value Resource Email:

                Subject: [Their Industry] Strategy Guide: Implementing What We Discussed
                
                Hey [Name],

                Following up on our conversation about [specific challenge they mentioned].

                I put together a quick guide that shows you how to [solve specific problem] - even if you don't end 
                up working with us. You can find it attached.

                Key points covered:
                • [Specific point 1]
                • [Specific point 2]
                • [Specific point 3]

                Let me know if you have any questions!

                Here's the Industry Insight Email (Day 3):

                Subject: Spotted This [Industry] Trend - Thought of You

                Hey [Name],

                Just came across some interesting data about [their industry]:
                [Share specific insight or trend]

                This could mean [specific opportunity] for [their company name].

                Here's a quick tip you can implement right now: [actionable tip]

                Want to discuss how to take advantage of this?
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="sales_prev_2"):
                        st.session_state.sales_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="sales_next_2"):
                        st.session_state.sales_page = 3
                        st.rerun()

            # Page 3: Closing Process
            elif st.session_state.sales_page == 3:
                st.title("Closing The Deal")
                
                st.write("""
                Welcome to the final part of this training. This is where it all comes together. I'm going to show you 
                exactly how I close deals, and more importantly, how to handle those common objections that always come up.

                But first, let me tell you about the biggest deal I almost lost. This was a $15,000 per month client, 
                and I nearly blew it because I handled the close wrong. I got nervous about the price, started rambling 
                about features and benefits, and almost talked them out of it. Luckily, I caught myself, shut up, and 
                used the framework I'm about to share with you.

                Here's my exact closing script. When you're ready to present your solution, say this:
                "Based on what you've shared, there are three main challenges we need to address..."
                Then list their challenges using their exact words - this is crucial. I literally write down their exact 
                phrases during the discovery part of the call.

                Then say: "Here's how we'll solve each of these..."
                Present your solution, but keep it high level. Don't get too technical. I made this mistake early on, 
                getting into the weeds about SEO algorithms and social media strategies. You'll lose them. Keep it focused 
                on outcomes.

                Finally: "The investment for this solution is $X per month..."
                Then - and this is crucial - be completely silent. Don't say another word. Let them respond first. This 
                silence might feel uncomfortable, but it's powerful. I count to ten in my head if I need to.

                Now, here's what they're going to say, and exactly how you should respond:

                When they say "I need to think about it":
                You say: "What specific aspects would you like to think about?"
                This helps you address their real concerns immediately. Often, "I need to think about it" really means 
                "I have an objection I'm not comfortable sharing."

                When they say "It's too expensive":
                You say: "Let me show you the ROI calculation based on your current numbers..."
                Always focus on value, never apologize for your prices. I learned this the hard way - the moment you 
                apologize for your price or try to justify it, you've lost.

                When they say "We want to try it internally first":
                You say: "Let me show you a comparison of in-house versus agency costs..."
                Then break down the real costs of hiring and training an internal team. Include salary, benefits, 
                software costs, training time - everything. This usually opens their eyes.

                Remember, your job isn't to convince them. It's to help them make a clear decision about whether this is 
                right for their business. Sometimes that decision will be no, and that's okay. Better to know now than 
                after you've started working together.

                I used to think sales was about persuasion and closing techniques. But really, it's about asking the right 
                questions, listening carefully, and then showing people how you can help them get what they want. Do this 
                right, and the closing takes care of itself.

                That's it for this training. In the next video, I'll show you how to handle the follow-up process 
                and what to do after the call to maximize your chances of closing the deal. Make sure to subscribe and 
                hit that notification bell so you don't miss it. And if this was helpful, give it a thumbs up!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="sales_prev_3"):
                        st.session_state.sales_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="sales_start_over"):
                        st.session_state.sales_page = 1
                        st.rerun()

        with tabs[2]:  # Follow-up System
            if 'followup_page' not in st.session_state:
                st.session_state.followup_page = 1

            # Page 1: Follow-up Strategy
            if st.session_state.followup_page == 1:
                st.title("The Perfect Follow-up System")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to dive into something that's making my agency an extra 
                $25,000 per month - our follow-up system. And the crazy thing? It's almost entirely automated.

                But first, let me tell you about the massive mistake I made when I first started. I used to think 
                follow-up meant just sending a "checking in" email every few days. You know the ones - "Hey, just 
                checking in to see if you've made a decision." Guess how well that worked? Exactly. Zero responses.

                Then I had this breakthrough moment. I was looking at our CRM data and noticed something interesting. 
                The clients who ended up signing with us had an average of 7-8 touchpoints before they signed. But 
                we were giving up after 2-3 emails.

                So I developed what I call the "Value Ladder Follow-up System." Here's how it works:

                Day 1: Send a value-packed resource
                • Something they can use immediately
                • No pitch, just pure value
                • Ask for feedback

                Day 3: Share relevant results
                • Make it relevant to their industry
                • Focus on the process, not just results
                • Include specific numbers and timelines

                Day 5: Send an industry insight
                • Share a trend or opportunity they might have missed
                • Position yourself as an expert
                • Make it actionable

                The key is that each touchpoint adds value. We're not just "checking in" - we're giving them a reason 
                to respond. And in the next section, I'll show you exactly how to create each of these touchpoints 
                and what to say in each one.
                """)

                if st.button("Next Page →", key="followup_next_1"):
                    st.session_state.followup_page = 2
                    st.rerun()

            # Page 2: Email Templates
            elif st.session_state.followup_page == 2:
                st.title("Email Templates That Convert")
                
                st.write("""
                Welcome back! Now I'm going to share the exact email templates we use in our follow-up sequence. These 
                aren't just any templates - these have been tested and refined over hundreds of leads.

                Let me tell you a quick story about these templates. We had a client who was using generic follow-up 
                emails and getting a 2% response rate. We implemented these templates, and their response rate shot up 
                to 23%. That's more than a 10x improvement!

                Here's the first email template - the Value Resource Email:

                Subject: [Their Industry] Strategy Guide: Implementing What We Discussed
                
                Hey [Name],

                Following up on our conversation about [specific challenge they mentioned].

                I put together a quick guide that shows you how to [solve specific problem] - even if you don't end 
                up working with us. You can find it attached.

                Key points covered:
                • [Specific point 1]
                • [Specific point 2]
                • [Specific point 3]

                Let me know if you have any questions!

                Here's the Industry Insight Email (Day 3):

                Subject: Spotted This [Industry] Trend - Thought of You

                Hey [Name],

                Just came across some interesting data about [their industry]:
                [Share specific insight or trend]

                This could mean [specific opportunity] for [their company name].

                Here's a quick tip you can implement right now: [actionable tip]

                Want to discuss how to take advantage of this?

                In the next section, I'll show you how to customize these templates and when to use each one.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="followup_prev_2"):
                        st.session_state.followup_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="followup_next_2"):
                        st.session_state.followup_page = 3
                        st.rerun()

            # Page 3: Automation and Scaling
            elif st.session_state.followup_page == 3:
                st.title("Automating Your Follow-up System")
                
                st.write("""
                Alright, this is where the magic happens. I'm going to show you how to automate this entire follow-up 
                system so it runs on autopilot. This is how we manage to follow up with hundreds of leads without 
                missing a single one.

                Let me share a story that changed everything for us. We were doing okay with our follow-up system, 
                but we were spending hours each day manually sending emails. Then one of our team members got sick 
                for a week, and our follow-ups completely fell apart. That's when I realized we needed to automate.

                Here's the exact system we built:

                1. CRM Integration
                • Set up tags for different lead sources
                • Create custom fields for tracking responses
                • Build automated sequences based on lead source

                2. Email Automation Rules
                • If they open but don't reply → Send follow-up #1 after 3 days
                • If they click but don't book → Send case study
                • If no engagement → Switch to different angle

                3. Engagement Tracking
                • Track email opens and clicks
                • Monitor website visits
                • Record content downloads

                4. Response Management
                • Auto-categorize responses
                • Priority flagging for hot leads
                • Automated meeting scheduling

                The key to making this work is what I call "intelligent automation." It's not just about sending 
                automated emails - it's about sending the RIGHT email at the RIGHT time based on their behavior.

                For example, if someone downloads your pricing guide but doesn't book a call, they automatically get 
                a different sequence than someone who downloaded a basic whitepaper. The system recognizes their level 
                of interest and responds accordingly.

                Here's what happened when we implemented this system:
                • Follow-up consistency went from 60% to 100%
                • Response rates increased by 47%
                • Sales team saved 15 hours per week
                • Lead-to-meeting conversion went up 28%

                That's it for this video! In the next one, I'll show you how to set up your proposal system to close 
                these leads at a higher rate. Don't forget to hit subscribe and the notification bell to catch that 
                one. And if this was helpful, smash that like button!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="followup_prev_3"):
                        st.session_state.followup_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="followup_start_over"):
                        st.session_state.followup_page = 1
                        st.rerun()

        with tabs[3]:  # Proposal Writing
            if 'proposal_page' not in st.session_state:
                st.session_state.proposal_page = 1

            # Page 1: Proposal Structure
            if st.session_state.proposal_page == 1:
                st.title("Writing High-Converting Proposals")
                
                st.write("""
                Hey everyone! Welcome back. Today I'm going to show you exactly how I write proposals that convert at 
                85%. Yes, you heard that right - 85%. And I'm not talking about small projects either. These are 
                five and six-figure deals.

                But first, let me tell you about the worst proposal I ever wrote. It was for a $120,000 website project. 
                I spent three days writing this monster - 25 pages of technical details, process breakdowns, and 
                fancy graphics. I was so proud of it. The client's response? "This is way too complicated." We lost 
                the deal.

                That's when I realized something crucial - clients don't want to read a novel. They want to know three 
                things:
                1. Do you understand their problem?
                2. Can you solve it?
                3. How much will it cost?

                So I developed what I call the "3-Block Proposal Framework." Here's exactly how it works:

                Block 1: The Problem Statement
                • Start with THEIR words (from the discovery call)
                • List 3-4 specific challenges they mentioned
                • Show the cost of not solving these problems

                For example, instead of saying "Your website needs optimization," I write:
                "During our call, you mentioned that your website is only converting at 1%, costing you approximately 
                $50,000 in lost revenue each month."

                Block 2: The Solution Overview
                • High-level solution (no technical jargon)
                • Expected outcomes
                • Timeline for results

                Block 3: The Investment
                • Clear pricing structure
                • Payment terms
                • Start date and next steps

                Here's what happened when I switched to this framework:
                • Proposal length went from 25 pages to 5
                • Time to write went from 3 days to 2 hours
                • Close rate went from 30% to 85%

                In the next section, I'll show you exactly how to write each block and what language to use to maximize 
                your chances of closing the deal.
                """)

                if st.button("Next Page →", key="proposal_next_1"):
                    st.session_state.proposal_page = 2
                    st.rerun()

            # Page 2: Writing Each Section
            elif st.session_state.proposal_page == 2:
                st.title("The Perfect Proposal Language")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly what to write in each section of your proposal. I'm 
                talking specific phrases that trigger emotional responses and drive decisions.

                Let me share a quick story. We had this client who was reviewing three different agency proposals. All 
                had similar pricing and services. But they chose us because, in their words, "Your proposal felt like 
                you were reading our minds." I'm going to show you how to create that same effect.

                Let's break down each section:

                1. The Opening Statement
                Bad: "Thank you for the opportunity to submit this proposal."
                Good: "Based on our discussion about [specific challenge], here's how we'll help [company name] achieve 
                [specific goal] within [timeframe]."

                2. The Problem Statement
                Bad: "Your website needs improvement."
                Good: "Your current website conversion rate of 1.2% is significantly below the industry standard of 3%, 
                resulting in approximately 450 lost leads per month."

                3. The Solution Section
                Bad: "We'll implement SEO best practices."
                Good: "We'll increase your organic traffic by:
                • Optimizing your top 20 product pages (identified in our audit)
                • Creating 12 industry-specific blog posts
                • Building 15 high-authority backlinks
                Expected result: 

                4. The Social Proof Section
                Bad: "We've helped many companies."
                Good: "We recently helped [similar company] increase their conversion rate from 1.2% to 3.8% in 60 days, 
                resulting in 127 additional leads per month."

                5. The Investment Section
                Bad: "Our fee is $5,000 per month."
                Good: "Investment: $5,000 per month
                Expected ROI: 
                Time to break even: 

                In the next section, I'll show you how to present this proposal in a way that makes it almost impossible 
                to say no.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="proposal_prev_2"):
                        st.session_state.proposal_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="proposal_next_2"):
                        st.session_state.proposal_page = 3
                        st.rerun()

            # Page 3: Presenting and Following Up
            elif st.session_state.proposal_page == 3:
                st.title("Presenting Your Proposal")
                
                st.write("""
                Alright, this is where most people mess up. They send the proposal via email and wait. Big mistake. 
                Let me show you the exact process that's helped us close 85% of our proposals.

                First, a story. We once had this huge proposal - $250,000 project. I was tempted to just email it 
                because I was nervous about the size. But I stuck to our process. We ended up closing that deal, and 
                the client later told me it was our presentation approach that won them over.

                Here's the exact process:

                Step 1: The Setup
                • Never send the proposal before presenting it
                • Schedule a 30-minute video call
                • Send a calendar invite with clear agenda
                • Have your screen share ready to go

                Step 2: The Presentation Script
                "Thanks for joining today. I'm going to walk you through our proposed solution for [specific challenge]. 
                I've kept this brief and focused on the outcomes you mentioned were most important to you."

                Then walk through each section:
                • Reflect their challenges (show you listened)
                • Present the solution (focus on outcomes)
                • Share relevant insights
                • Explain the investment (focus on ROI)

                Step 3: The Close
                • "Based on what I've shared, do you have any questions?"
                • Address questions immediately
                • "Would you like to move forward?"

                If they say "We need to think about it":
                • "Of course. What specific aspects would you like to think about?"
                • Address concerns right there
                • Suggest a follow-up date

                Step 4: After the Call
                • Send the proposal immediately
                • Include a summary of discussed points
                • Add a clear call to action
                • Set a follow-up task for 24 hours

                The key to making this work is confidence. You're not begging for their business - you're showing them 
                how you'll solve their problems.

                That's it for this video series! You now have everything you need to create and close winning proposals. 
                If you found this helpful, don't forget to like and subscribe. And drop a comment below if you have any 
                questions!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="proposal_prev_3"):
                        st.session_state.proposal_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="proposal_start_over"):
                        st.session_state.proposal_page = 1
                        st.rerun()

    elif selected_section == "Delivery":
        st.title("Service Delivery")
        
        # Sub-module tabs with better contrast and unique names
        delivery_tabs = st.tabs([
            "**Client Onboarding**",
            "**Project Management**", 
            "**Quality Control**", 
            "**Client Success**"
        ])
        
        with delivery_tabs[0]:  # Client Onboarding
            if 'onboarding_page' not in st.session_state:
                st.session_state.onboarding_page = 1

            # Page 1: Onboarding Framework
            if st.session_state.onboarding_page == 1:
                st.title("The Perfect Client Onboarding")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's absolutely crucial for your 
                agency - client onboarding. I'm going to show you the exact system we use that's resulted in a 95% 
                client retention rate.

                But first, let me tell you about a complete disaster I had with a client. We signed this big client - 
                $15,000 per month. I was so excited about landing them that I rushed straight into the work. No proper 
                onboarding, no clear expectations, no defined processes. Three months later, they fired us. That was a 
                $180,000 lesson in the importance of proper onboarding.

                Here's what I learned and what we do now. I call it the "5-Star Onboarding System":

                Step 1: Welcome Package (Day 1)
                • Send welcome video from agency owner
                • Share onboarding timeline
                • Include all necessary forms
                • Set up client portal access

                Step 2: Kickoff Call (Day 3)
                • Review project scope in detail
                • Set clear expectations
                • Define communication channels
                • Establish reporting schedule

                Step 3: Strategy Session (Day 5)
                • Deep dive into their business
                • Set measurable goals
                • Create 90-day roadmap
                • Assign team members
                """)

                if st.button("Next Page →", key="onboarding_next_1"):
                    st.session_state.onboarding_page = 2
                    st.rerun()

            # Page 2: Welcome Package and Kickoff
            elif st.session_state.onboarding_page == 2:
                st.title("Welcome Package & Kickoff Call")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly what goes into our welcome package and how to run a 
                kickoff call that sets you up for success.

                Let me tell you about an interesting experiment we did. We tested two different welcome packages with 
                100 clients each. The first was just a standard email with forms. The second was our new enhanced 
                package. The enhanced package group had 40% fewer support requests in the first month and reported 
                90% higher satisfaction.

                Here's exactly what goes into our welcome package:

                1. Welcome Video Script:
                "Hi [Client Name], this is [Your Name] from [Agency]. I'm so excited to have you on board! In this 
                video, I'll walk you through what happens next and introduce you to your team..."

                2. Required Forms (with explanations):
                • Client Questionnaire: "This helps us understand your brand voice..."
                • Access Form: "We'll use this to set up your analytics..."
                • Brand Guidelines: "This ensures all work matches your brand..."

                3. Kickoff Call Agenda:
                • Introductions (5 minutes)
                • Project Overview (10 minutes)
                • Goal Setting (15 minutes)
                • Timeline Review (10 minutes)
                • Q&A (20 minutes)

                4. The Success Roadmap:
                • Week 1: Setup and Strategy
                • Week 2: Initial Deliverables
                • Week 3: Review and Adjust
                • Week 4: Scale and Optimize

                In the next section, I'll show you how to handle the crucial first 30 days to ensure long-term client 
                success.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="onboarding_prev_2"):
                        st.session_state.onboarding_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="onboarding_next_2"):
                        st.session_state.onboarding_page = 3
                        st.rerun()

            # Page 3: First 30 Days
            elif st.session_state.onboarding_page == 3:
                st.title("The First 30 Days")
                
                st.write("""
                Alright, this is where the magic happens. The first 30 days will make or break your client 
                relationship. I'm going to show you exactly how to structure this crucial period.

                Quick story - we once had a client who was ready to cancel after 30 days. We managed to turn them 
                around using this exact system, and they ended up being our biggest advocate, referring us three other 
                clients.

                Here's our exact 30-day plan:

                Week 1: Foundation
                • Day 1: Send welcome package
                • Day 2: Collect all accesses
                • Day 3: Kickoff call
                • Day 5: Strategy session
                • Day 7: First progress update

                Week 2: Initial Wins
                • Implement quick wins
                • Show initial results
                • Get early feedback
                • Adjust approach if needed

                Week 3: Deep Implementation
                • Roll out full strategy
                • Team check-in
                • Client feedback session
                • Progress report

                Week 4: Review and Scale
                • Results presentation
                • Strategy refinement
                • Success celebration
                • Plan next 60 days

                Key Success Metrics to Track:
                • Response time to client requests
                • Task completion rate
                • Client engagement level
                • Early wins delivered

                That's it for this video! In the next one, I'll show you how to set up your project management system 
                for maximum efficiency. Don't forget to hit subscribe and the notification bell to catch that one. 
                And if this was helpful, give it a thumbs up!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="onboarding_prev_3"):
                        st.session_state.onboarding_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="onboarding_start_over"):
                        st.session_state.onboarding_page = 1
                        st.rerun()

    elif selected_section == "Growth":
        st.title("Agency Growth")
        
        st.markdown("""
        <div class="nav-pills">
            <a href="#" class="nav-pill active">Team Building</a>
            <a href="#" class="nav-pill">Financial Management</a>
            <a href="#" class="nav-pill">Systems & Processes</a>
            <a href="#" class="nav-pill">Scaling Strategy</a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Team Building</h3>
                <p>Build and manage a high-performing team.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Hiring process</li>
                    <li>Training system</li>
                    <li>Performance management</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Financial Management</h3>
                <p>Optimize your agency's financial performance.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Profit optimization</li>
                    <li>Cash flow management</li>
                    <li>Financial forecasting</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Systems & Processes</h3>
                <p>Create scalable systems for growth.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>SOP development</li>
                    <li>Automation setup</li>
                    <li>Tool stack optimization</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Scaling Strategy</h3>
                <p>Scale your agency systematically.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Growth roadmap</li>
                    <li>Service expansion</li>
                    <li>Market positioning</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
    elif selected_section == "Resources":
        st.title("Resources")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Templates Library</h3>
                <p>Access our complete library of proven templates, scripts, and frameworks.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Proposal templates</li>
                    <li>Email scripts</li>
                    <li>SOPs and checklists</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Training Videos</h3>
                <p>Step-by-step video tutorials for implementing every system.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Implementation guides</li>
                    <li>Best practices</li>
                    <li>Case studies</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Community Forum</h3>
                <p>Connect with other agency owners, share insights, and get support.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Discussion boards</li>
                    <li>Expert Q&A</li>
                    <li>Resource sharing</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Expert Directory</h3>
                <p>Find and connect with vetted experts in various agency specialties.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Specialist profiles</li>
                    <li>Booking system</li>
                    <li>Reviews and ratings</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
