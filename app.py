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
.module-card {
    background-color: white !important;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
}
.module-card h3 {
    color: #1a202c !important;
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    font-weight: 600;
}
.module-card p {
    color: #4a5568 !important;
    margin-bottom: 1rem;
}
.module-card ul {
    color: #4a5568 !important;
    margin-left: 1.5rem;
}
.step-container {
    background-color: white;
    padding: 2rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}
.step-header {
    color: #1a202c;
    font-size: 1.5rem;
    margin-bottom: 1rem;
    font-weight: 600;
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
        st.title("Client Acquisition")
        
        # Sub-module tabs
        tab1, tab2, tab3, tab4 = st.tabs(["Lead Generation", "Sales System", "Follow-up", "Proposals"])
        
        with tab1:
            if st.session_state.step == 1:
                st.markdown("""
                <div class="step-container">
                    <div class="step-header">Step 1: Define Your Target Client</div>
                </div>
                """, unsafe_allow_html=True)
                
                industry = st.selectbox("What industry does your ideal client work in?",
                    ["Technology", "E-commerce", "Healthcare", "Real Estate", "Other"])
                company_size = st.selectbox("What's their company size?",
                    ["1-10 employees", "11-50 employees", "51-200 employees", "201+ employees"])
                budget = st.selectbox("What's their typical monthly marketing budget?",
                    ["$1,000 - $5,000", "$5,001 - $10,000", "$10,001 - $25,000", "$25,000+"])
                
                if st.button("Next Step →"):
                    st.session_state.step = 2
                    st.rerun()
            
            elif st.session_state.step == 2:
                st.markdown("""
                <div class="step-container">
                    <div class="step-header">Step 2: Create Your Lead Magnet</div>
                </div>
                """, unsafe_allow_html=True)
                
                lead_magnet = st.selectbox("What type of lead magnet will you create?",
                    ["Free Consultation", "Industry Report", "Video Training", "Template/Tool"])
                delivery = st.selectbox("How will you deliver it?",
                    ["Email", "Download Page", "Member Portal", "Video Platform"])
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous"):
                        st.session_state.step = 1
                        st.rerun()
                with col2:
                    if st.button("Next →"):
                        st.session_state.step = 3
                        st.rerun()
            
            elif st.session_state.step == 3:
                st.markdown("""
                <div class="step-container">
                    <div class="step-header">Step 3: Implementation Plan</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="module-card">
                    <h3>Action Steps</h3>
                    <ol style="color: #4a5568; margin-left: 1.5rem;">
                        <li>Create your lead magnet content</li>
                        <li>Set up delivery system</li>
                        <li>Create landing page</li>
                        <li>Set up tracking</li>
                    </ol>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("← Back to Step 2"):
                    st.session_state.step = 2
                    st.rerun()
                if st.button("Start Over"):
                    st.session_state.step = 1
                    st.rerun()

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
