import streamlit as st
import streamlit.components.v1 as components
import markdown
import os
from pathlib import Path

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
        background-color: #f3f4f6;
    }
    
    /* Sidebar Styles */
    .css-1d391kg {
        background-color: #111827;
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
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
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
    .enter-button {
        background: white;
        color: #1e40af;
        padding: 1rem 2.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 1.125rem;
        border: 2px solid #e2e8f0;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    .enter-button:hover {
        background: #1e40af;
        color: white;
        border-color: #1e40af;
        transform: translateY(-2px);
    }
    /* Hide Streamlit Components */
    .stDeployButton, footer, header {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session states
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'show_home' not in st.session_state:
    st.session_state.show_home = True

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
        <a href="#" class="enter-button" onclick="document.querySelector('.enter-app-button').click()">Enter Platform</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden button for JavaScript click
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
    # Sidebar navigation
    with st.sidebar:
        st.title("AquiPro")
        selected_section = st.selectbox("Choose Your Module", ["Dashboard", "Acquisition", "Delivery", "Growth", "Resources"])
    
    # Main content area
    st.markdown("""
        <style>
            .metric-card {
                background: white;
                padding: 1.75rem;
                border-radius: 16px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
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
            .activity-item {
                padding: 1rem;
                border-bottom: 1px solid #e5e7eb;
            }
            .activity-item:last-child {
                border-bottom: none;
            }
            .progress-bar {
                height: 8px;
                background: linear-gradient(90deg, #3b82f6, #2563eb);
                border-radius: 4px;
            }
            .section-title {
                font-size: 1.5rem;
                font-weight: 700;
                color: #111827;
                letter-spacing: -0.025em;
                margin: 2.5rem 0 1.5rem;
            }
        </style>
    """, unsafe_allow_html=True)

    if selected_section == "Dashboard":
        # Metrics Grid
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">Active Clients</div>
                    <div class="metric-value">24</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">Monthly Revenue</div>
                    <div class="metric-value">$48.5k</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">Leads in Pipeline</div>
                    <div class="metric-value">12</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">Client Satisfaction</div>
                    <div class="metric-value">98%</div>
                </div>
            """, unsafe_allow_html=True)

        # Recent Activity
        st.markdown('<h2 class="section-title">Recent Activity</h2>', unsafe_allow_html=True)
        activity_data = [
            "New client onboarding: Tech Solutions Inc.",
            "Campaign performance report generated",
            "Team meeting scheduled for tomorrow",
            "New lead added to pipeline"
        ]
        
        for activity in activity_data:
            st.markdown(f"""
                <div class="activity-item">
                    <div style="color: #374151;">{activity}</div>
                </div>
            """, unsafe_allow_html=True)

        # Module Progress
        st.markdown('<h2 class="section-title">Module Progress</h2>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 500;">Client Acquisition</span>
                        <span style="color: #6b7280;">75%</span>
                    </div>
                    <div style="background: #e5e7eb; border-radius: 4px;">
                        <div class="progress-bar" style="width: 75%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 500;">Team Management</span>
                        <span style="color: #6b7280;">60%</span>
                    </div>
                    <div style="background: #e5e7eb; border-radius: 4px;">
                        <div class="progress-bar" style="width: 60%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 500;">Revenue Growth</span>
                        <span style="color: #6b7280;">85%</span>
                    </div>
                    <div style="background: #e5e7eb; border-radius: 4px;">
                        <div class="progress-bar" style="width: 85%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div style="margin-bottom: 1rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 500;">Client Retention</span>
                        <span style="color: #6b7280;">90%</span>
                    </div>
                    <div style="background: #e5e7eb; border-radius: 4px;">
                        <div class="progress-bar" style="width: 90%;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    elif selected_section == "Clients":
        st.title("Clients Module")
        st.write("Manage your client relationships here.")
        
    elif selected_section == "Tasks":
        st.title("Tasks Module")
        st.write("Track and manage your tasks here.")
        
    elif selected_section == "Analytics":
        st.title("Analytics Module")
        st.write("View detailed analytics and reports here.")
        
    elif selected_section == "Acquisition":
        st.title("Client Acquisition")
        
        # Module navigation
        st.markdown("""
        <div class="nav-pills">
            <a href="#" class="nav-pill active">Lead Generation</a>
            <a href="#" class="nav-pill">Sales System</a>
            <a href="#" class="nav-pill">Follow-up</a>
            <a href="#" class="nav-pill">Proposals</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Load and display module content
        module_path = Path("course-structure/modules/2-acquisition/lead-generation.md")
        if module_path.exists():
            content = markdown.markdown(module_path.read_text())
            st.markdown(content)

    elif selected_section == "Delivery":
        st.title("Service Delivery")
        
        # Module navigation
        st.markdown("""
        <div class="nav-pills">
            <a href="#" class="nav-pill active">Onboarding</a>
            <a href="#" class="nav-pill">Project Management</a>
            <a href="#" class="nav-pill">Quality Assurance</a>
            <a href="#" class="nav-pill">Client Success</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Load and display module content
        module_path = Path("course-structure/modules/3-delivery/onboarding-system.md")
        if module_path.exists():
            content = markdown.markdown(module_path.read_text())
            st.markdown(content)

    elif selected_section == "Growth":
        st.title("Agency Growth")
        
        # Module navigation
        st.markdown("""
        <div class="nav-pills">
            <a href="#" class="nav-pill active">Team Building</a>
            <a href="#" class="nav-pill">Financial Management</a>
            <a href="#" class="nav-pill">Systems & Processes</a>
            <a href="#" class="nav-pill">Scaling Strategy</a>
        </div>
        """, unsafe_allow_html=True)
        
        # Load and display module content
        module_path = Path("course-structure/modules/3-delivery/team-management.md")
        if module_path.exists():
            content = markdown.markdown(module_path.read_text())
            st.markdown(content)

    else:  # Resources
        st.title("Resources")
        
        # Resource cards
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Templates Library</h3>
                <p>Access our complete library of proven templates, scripts, and frameworks.</p>
                <button class="stButton">View Templates</button>
            </div>
            
            <div class="module-card">
                <h3>Training Videos</h3>
                <p>Step-by-step video tutorials for implementing every system.</p>
                <button class="stButton">Watch Videos</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Community Forum</h3>
                <p>Connect with other agency owners, share insights, and get support.</p>
                <button class="stButton">Join Community</button>
            </div>
            
            <div class="module-card">
                <h3>Expert Directory</h3>
                <p>Find and connect with vetted experts in various agency specialties.</p>
                <button class="stButton">Browse Experts</button>
            </div>
            """, unsafe_allow_html=True)
