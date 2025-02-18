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
        st.markdown("""
        <h1 style='color: white; margin-bottom: 2rem;'>AquiPro</h1>
        """, unsafe_allow_html=True)
        selected_section = st.selectbox("Choose Your Module", list(sections.keys()))

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
            st.metric("Active Workflows", "12", "+2")
        
        with stat_col2:
            st.metric("Tasks Automated", "127", "+15")
            
        with stat_col3:
            st.metric("Time Saved (hrs/week)", "45", "+5")
            
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
        
        # Sub-module tabs
        tab1, tab2, tab3, tab4 = st.tabs(["**Lead Generation**", "**Sales System**", "**Follow-up**", "**Proposals**"])
        
        with tab1:  # Lead Generation
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
                their goals. That single lead magnet brought in over 200 qualified leads in just two months.

                The second type is what I call the 'Quick Win' guide. This isn't your typical PDF - it's a super specific, 
                step-by-step process that solves ONE problem. For example, we created a "5-Minute LinkedIn Optimization 
                Checklist" that shows exactly how to improve your LinkedIn profile for B2B lead generation.

                Here's why it worked so well - it promises (and delivers) value in just 5 minutes. Business owners love 
                that. They can implement it right away and see results almost immediately.

                In the next section, I'm going to show you exactly how to create and position these lead magnets for 
                maximum impact. Trust me, this is where most agencies get it completely wrong, and I'm going to show 
                you how to do it right.
                """)

                if st.button("Next Page →"):
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

                That's when I developed what I call the "Triple Threat" promotion strategy. Here's exactly how it works:

                First, we use LinkedIn. But not just regular posts - we do it strategically. Here's my exact process:
                1. Post valuable content for 2 weeks straight
                2. Build engagement with your target audience
                3. Then, on week 3, introduce your lead magnet
                4. Important: Don't just drop a link - tell a story about why you created it

                I'll give you a real example. We posted daily LinkedIn tips for two weeks. Each post got good engagement. 
                Then, when we introduced our LinkedIn optimization checklist, it was an instant hit. People already knew 
                we knew our stuff.

                The second part of the Triple Threat is paid ads. But here's the trick - we don't promote the lead 
                magnet directly. Instead, we promote a valuable post that naturally leads to the lead magnet. This 
                works so much better than direct promotion.

                For example, we'll boost a post about "The 3 Biggest LinkedIn Mistakes CEOs Make" and then naturally 
                mention our checklist as the solution. The conversion rate on this approach is insane - we're talking 
                25-30% versus the usual 2-3% from direct promotion.

                The third part is email outreach. But not cold email - we call it "warm prospecting." Here's exactly 
                how it works:
                1. Find someone who engaged with your content
                2. Send them a personalized message
                3. Offer the lead magnet as additional value
                4. Don't ask for anything in return

                In the next section, I'll show you exactly how to convert these leads into paying clients. This is 
                where the real magic happens.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page"):
                        st.session_state.lead_gen_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →"):
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
                • Send a case study related to their industry
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
                    if st.button("← Previous Page"):
                        st.session_state.lead_gen_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over"):
                        st.session_state.lead_gen_page = 1
                        st.rerun()

        with tab2:  # Sales System
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

                Then one day, I had this call with a potential client, and instead of pitching, I just shut up and listened. 
                I asked questions about their business, and suddenly, the whole conversation changed. They opened up about 
                their problems, their goals, their fears. And that's when it hit me - this is what a discovery call should be.

                So let me break down exactly how I structure these calls now. First, when someone gets on a call with you, 
                you need to establish authority immediately. Here's what I say: "Thanks for taking the time today. I've 
                looked at your website and noticed a few things we could improve, but first I'd love to hear more about 
                your business."

                See what I did there? I've already shown them I did my homework, and I'm giving them a chance to talk about 
                themselves. People love talking about their business, and this is where you'll get your most valuable information.

                Now, during the first 15 minutes, you want to ask these specific questions:
                "What made you start looking for marketing help now?"
                "What have you tried so far?"
                "What would success look like 12 months from now?"

                Let me tell you why these questions are so powerful. The first question gets at their pain points and 
                motivation. The second question tells you what hasn't worked - this is gold for your proposal. And the 
                third question? That's where you get their vision, their goals, their dreams for their business.

                But here's what most people get wrong - they rush through these questions. Don't do that. When they answer, 
                stay quiet for a moment. Let them think. Let them add more details. The silence might feel uncomfortable, 
                but trust me, this is where the magic happens.

                I remember one call where I asked about their previous marketing efforts, and after their initial answer, 
                I just stayed quiet. That silence led them to open up about a bad experience with another agency - 
                information that was crucial for me to position our services correctly.

                In the next section, I'll show you exactly how to qualify these leads so you're only working with clients 
                who can afford your services and are ready to start. Trust me, this next part is crucial - it's where you 
                separate the tire-kickers from serious clients.
                """)

                if st.button("Next Page →"):
                    st.session_state.sales_page = 2
                    st.rerun()

            # Page 2: Qualification Process
            elif st.session_state.sales_page == 2:
                st.title("Qualifying Your Leads")
                
                st.write("""
                Alright, welcome back. Now that you know how to run the discovery call, let me share something really 
                important. This is actually the biggest mistake I see agency owners make - they get excited about any 
                potential client and don't properly qualify them.

                I learned this the hard way, and let me tell you that story. Early in my agency, I took on a client who 
                couldn't really afford our services. They were paying $2,000 a month, which was way below our usual rate, 
                but I was desperate for clients. Well, guess what happened? They turned out to be the most demanding 
                client we ever had.

                Every day, there were new requests. Every week, they wanted to know why they weren't ranking #1 on Google 
                yet. They drained our resources, constantly complained about price, and eventually, we had to part ways. 
                That experience cost us not just money, but team morale and time we could have spent on better-fit clients.

                So here's what you need to ask - and I want you to ask these questions in this exact order, because the 
                order matters. I'll explain why in a minute.

                First: "What's your current monthly marketing spend?"
                Don't be shy about this. If they can't afford your services, you need to know right away. When they tell 
                you a number, don't react. Just note it down. If it's too low, you can end the call early and save 
                everyone's time.

                Second: "Who else is involved in making marketing decisions?"
                This is crucial because if you're not talking to the decision-maker, you're wasting your time. I once 
                spent two weeks going back and forth with someone, creating proposals, having follow-up calls, only to 
                find out they needed approval from a CEO who had a completely different vision.

                Third: "Have you worked with agencies before?"
                Their answer will tell you so much about their expectations and past experiences. Listen carefully here. 
                If they've worked with multiple agencies in the past year, that's a red flag. It usually means they have 
                unrealistic expectations or they're difficult to work with.

                Fourth: "What's your timeline for making a decision?"
                This separates the serious prospects from the tire-kickers. If they can't give you a specific timeline, 
                they're probably not ready to buy. I usually say something like, "Most of our clients make a decision 
                within two weeks of our call. Does that timeline work for you?"

                Now, why this order? Because each question builds on the last. If they don't have the budget, there's no 
                point asking about decision-making. If they're not the decision-maker, why discuss timeline? See what I 
                mean?

                In the next section, I'll show you exactly how to handle their responses and close the deal. This is where 
                it gets really good, because I'm going to share the exact words I use to handle objections and close 
                high-ticket deals.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page"):
                        st.session_state.sales_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →"):
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

                That's it for this training. In the next video, I'll show you exactly how to handle the follow-up process 
                and what to do after the call to maximize your chances of closing the deal. Make sure to subscribe and 
                hit that notification bell so you don't miss it.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page"):
                        st.session_state.sales_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over"):
                        st.session_state.sales_page = 1
                        st.rerun()

        with tab3:
            st.markdown("""
            <div class="lesson-box">
                <div class="lesson-title">Follow-up Email Sequences</div>
                <div class="lesson-content">
                    A well-crafted email sequence can significantly improve your chances of closing a deal.
                </div>
                
                <div class="key-point">
                    <strong>Key Components:</strong><br>
                    • Introduction Email (sent immediately)<br>
                    • Value Email (sent 2 days after intro)<br>
                    • Problem Agitation Solution Email (sent 4 days after intro)<br>
                    • Case Study Email (sent 6 days after intro)<br>
                    • Final Follow-up Email (sent 8 days after intro)
                </div>
            </div>
            """, unsafe_allow_html=True)

        with tab4:
            st.markdown("""
            <div class="lesson-box">
                <div class="lesson-title">Proposal Templates</div>
                <div class="lesson-content">
                    A well-structured proposal can make all the difference in winning a client.
                </div>
                
                <div class="key-point">
                    <strong>Key Components:</strong><br>
                    • Executive Summary<br>
                    • Company Overview<br>
                    • Problem Statement<br>
                    • Solution Overview<br>
                    • Implementation Plan<br>
                    • Pricing and Packages
                </div>
            </div>
            """, unsafe_allow_html=True)

    elif selected_section == "Delivery":
        st.title("Service Delivery")
        
        st.markdown("""
        <div class="nav-pills">
            <a href="#" class="nav-pill active">Onboarding</a>
            <a href="#" class="nav-pill">Project Management</a>
            <a href="#" class="nav-pill">Quality Assurance</a>
            <a href="#" class="nav-pill">Client Success</a>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Client Onboarding</h3>
                <p>Create an exceptional first impression with a smooth onboarding process.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Welcome sequence</li>
                    <li>Kickoff meeting template</li>
                    <li>Asset collection</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Project Management</h3>
                <p>Keep projects on track and clients happy.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Timeline management</li>
                    <li>Task delegation</li>
                    <li>Progress tracking</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Quality Assurance</h3>
                <p>Maintain high standards across all deliverables.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Review process</li>
                    <li>Quality checklist</li>
                    <li>Client approval workflow</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Client Success</h3>
                <p>Turn clients into long-term partners.</p>
                <ul style="color: #4b5563; margin-left: 1.5rem;">
                    <li>Regular check-ins</li>
                    <li>Performance reporting</li>
                    <li>Upsell opportunities</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
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
