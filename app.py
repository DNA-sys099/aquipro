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
</style>
""", unsafe_allow_html=True)

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Signup/Login Page
if not st.session_state.logged_in:
    st.markdown("""
    <div class="auth-container">
        <div class="auth-header">
            <div class="auth-title">Welcome to AquiPro</div>
            <div class="auth-subtitle">Sign in to access your dashboard</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Sign In")
        
        if submitted:
            if len(password) >= 8:
                st.session_state.logged_in = True
                st.success("Signed in successfully!")
                st.experimental_rerun()
            else:
                st.error("Password must be at least 8 characters")
    
    st.markdown("""
    <div style="text-align: center; margin-top: 1.5rem;">
        <p style="color: #6b7280; font-size: 0.875rem;">Don't have an account? <a href="#" style="color: #3b82f6; font-weight: 500;">Create one</a></p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Sidebar navigation
    with st.sidebar:
        st.title("AquiPro")
        
        # User profile section
        st.markdown("""
        <div style="padding: 1rem; background-color: #2d2d2d; border-radius: 10px; margin: 1rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <div style="width: 40px; height: 40px; background-color: #2962ff; border-radius: 20px; margin-right: 0.5rem;"></div>
                <div>
                    <div style="color: white; font-weight: 500;">Your Name</div>
                    <div style="color: #64748b; font-size: 0.8rem;">Agency Owner</div>
                </div>
            </div>
            <div style="background-color: #3d3d3d; height: 4px; border-radius: 2px; margin: 0.5rem 0;">
                <div style="width: 65%; height: 100%; background-color: #2962ff; border-radius: 2px;"></div>
            </div>
            <div style="color: #64748b; font-size: 0.8rem;">65% Profile Complete</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu
        selected_section = st.radio(
            "",
            ["Dashboard", "Acquisition", "Delivery", "Growth", "Resources"],
            key="nav"
        )

    # Main content area
    if selected_section == "Dashboard":
        st.markdown("""
        <div class="dashboard-container">
            <h1 style="margin-bottom: 2rem; color: #1e293b;">Your Growth Dashboard</h1>
            
            <div class="metrics-grid">
                <div class="metric-card">
                    <div class="metric-title">Active Clients</div>
                    <div class="metric-value">12</div>
                    <div class="metric-change positive">+2 this month</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Monthly Revenue</div>
                    <div class="metric-value">$24,500</div>
                    <div class="metric-change positive">+15% from last month</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Leads in Pipeline</div>
                    <div class="metric-value">28</div>
                    <div class="metric-change positive">+5 this week</div>
                </div>
                
                <div class="metric-card">
                    <div class="metric-title">Client Satisfaction</div>
                    <div class="metric-value">94%</div>
                    <div class="metric-change positive">+2% this month</div>
                </div>
            </div>
            
            <div class="activity-card">
                <div class="activity-header">
                    <div class="activity-title">Recent Activity</div>
                </div>
                
                <div class="activity-item">
                    <div class="activity-content">
                        <div class="activity-action">New Client Onboarded</div>
                        <div class="activity-detail">Tech Solutions Inc.</div>
                    </div>
                    <div class="activity-time">2 hours ago</div>
                </div>
                
                <div class="activity-item">
                    <div class="activity-content">
                        <div class="activity-action">Proposal Sent</div>
                        <div class="activity-detail">Digital Marketing Package</div>
                    </div>
                    <div class="activity-time">5 hours ago</div>
                </div>
                
                <div class="activity-item">
                    <div class="activity-content">
                        <div class="activity-action">Strategy Call Completed</div>
                        <div class="activity-detail">Growth Planning Session</div>
                    </div>
                    <div class="activity-time">Yesterday</div>
                </div>
            </div>
            
            <h2 style="margin: 2rem 0; color: #1e293b;">Module Progress</h2>
            
            <div class="progress-section">
                <div class="progress-card">
                    <div class="progress-header">
                        <div class="progress-title">Client Acquisition</div>
                        <div class="progress-description">Learn how to consistently attract and close high-ticket clients</div>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-bar-fill" style="width: 85%;"></div>
                    </div>
                    <div class="progress-stats">
                        <div class="progress-percentage">85%</div>
                        <div class="progress-label">Complete</div>
                    </div>
                    <div class="action-items">
                        <div class="action-item">Complete lead magnet</div>
                        <div class="action-item">Set up automation</div>
                        <div class="action-item">Review analytics</div>
                    </div>
                </div>
                
                <div class="progress-card">
                    <div class="progress-header">
                        <div class="progress-title">Service Delivery</div>
                        <div class="progress-description">Deliver exceptional results that turn clients into advocates</div>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-bar-fill" style="width: 60%;"></div>
                    </div>
                    <div class="progress-stats">
                        <div class="progress-percentage">60%</div>
                        <div class="progress-label">Complete</div>
                    </div>
                    <div class="action-items">
                        <div class="action-item">Update SOP documentation</div>
                        <div class="action-item">Train team on new process</div>
                        <div class="action-item">Schedule client reviews</div>
                    </div>
                </div>
                
                <div class="progress-card">
                    <div class="progress-header">
                        <div class="progress-title">Team Management</div>
                        <div class="progress-description">Build and manage a high-performing team</div>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-bar-fill" style="width: 40%;"></div>
                    </div>
                    <div class="progress-stats">
                        <div class="progress-percentage">40%</div>
                        <div class="progress-label">Complete</div>
                    </div>
                    <div class="action-items">
                        <div class="action-item">Create hiring plan</div>
                        <div class="action-item">Develop training materials</div>
                        <div class="action-item">Set up performance metrics</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

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
