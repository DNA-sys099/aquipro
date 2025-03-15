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
        padding: 1rem !important;
        background-color: white !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
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

# Add custom CSS for the download button
st.markdown("""
<style>
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    margin: 16px 0;
}
div.stButton > button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# Remove metrics initialization
if 'metrics' in st.session_state:
    del st.session_state['metrics']

# Remove case study references
st.markdown("""
<style>
/* Remove metrics styling */
.metrics-grid, .metric-card, .metric-title, .metric-value, .metric-change {
    display: none !important;
}

/* Remove case study styling */
.case-study, .case-study-card {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize session states and sections dictionary
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Define sections with better contrast
sections = {
    "Dashboard": "View your agency's overview",
    "Acquisition": "Client acquisition strategies",
    "Delivery": "Service delivery management",
    "Growth": "Agency growth tactics",
    "Resources": "Tools and resources"
}

# Update sections to remove metrics references
sections = {
    "Dashboard": "View your agency's overview",
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
        
        st.markdown('<div class="content-text">', unsafe_allow_html=True)
        st.write("""
        Hey everyone! Welcome back to another video. Today we're going to dive into the heart of agency automation.
        I'm going to show you exactly how we automate our entire agency to run like a well-oiled machine.

        Let me tell you a quick story. When I first started, I was doing everything manually. It was a mess.
        I was working 80-hour weeks and still falling behind. Then I discovered these automation categories
        that changed everything.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Automation Categories
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="module-card">
                <h3>Lead Generation</h3>
                <p>Automate your lead generation process with proven systems.</p>
                <ul>
                    <li>Lead magnet automation</li>
                    <li>Email sequences</li>
                    <li>Social media automation</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Client Onboarding</h3>
                <p>Streamline your client onboarding with automated workflows.</p>
                <ul>
                    <li>Welcome sequence</li>
                    <li>Document collection</li>
                    <li>Project setup</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="module-card">
                <h3>Project Management</h3>
                <p>Automate your project management tasks and workflows.</p>
                <ul>
                    <li>Task automation</li>
                    <li>Progress tracking</li>
                    <li>Client updates</li>
                </ul>
            </div>
            
            <div class="module-card">
                <h3>Client Success</h3>
                <p>Keep clients happy with automated check-ins and updates.</p>
                <ul>
                    <li>Check-in automation</li>
                    <li>Feedback collection</li>
                    <li>Success tracking</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="content-text">', unsafe_allow_html=True)
        st.write("""
        That's it for this overview! In the next videos, we'll dive deep into each of these categories.
        Make sure to hit subscribe and the notification bell so you don't miss any of them!
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    elif selected_section == "Growth":
        st.title("Agency Growth")
        st.write("""
        Hey everyone! Today we're going to talk about growing your agency in a sustainable way.
        I'll show you the exact frameworks and systems we use to scale effectively.
        """)

        growth_tabs = st.tabs([
            "Team Building",
            "Systems & Processes",
            "Financial Growth",
            "Strategic Planning"
        ])

        with growth_tabs[0]:
            st.write("""
            Building a strong team is crucial for agency growth. Let's focus on the key areas:
            
            • Clear role definitions
            • Growth opportunities
            • Regular feedback
            • Team recognition
            
            Remember: your team is your most valuable asset. Invest in them, and they'll invest in your vision.
            """)

        with growth_tabs[1]:
            st.write("""
            Good systems are the foundation of a scalable agency. Here's what to focus on:
            
            • Client communication
            • Project workflows
            • Quality checks
            • Team coordination
            
            The key is to start small and gradually build up your systems.
            """)

        with growth_tabs[2]:
            st.write("""
            Smart financial management is essential. Focus on these areas:
            
            • Cash flow management
            • Pricing strategy
            • Expense tracking
            • Growth planning
            
            Remember: good financial management is the foundation of a sustainable agency.
            """)

        with growth_tabs[3]:
            st.write("""
            Strategic planning helps you grow intentionally. Key elements include:
            
            • Vision setting
            • Goal planning
            • Action steps
            • Progress reviews
            
            Take time to plan your growth - don't just let it happen randomly.
            """)

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
            st.title("Lead Generation Mastery")
            
            st.write("""
            ## Lead Generation Deep Dive

            ### 1. Content Marketing Strategy
            The foundation of successful lead generation is a solid content marketing strategy. Here's how to build one:

            #### Content Types
            • **Blog Posts**: In-depth articles that showcase your expertise
            • **Video Content**: Tutorials and behind-the-scenes content
            • **Podcasts**: Industry interviews and expert insights
            • **Social Media**: Platform-specific content that engages

            #### Content Creation Process
            1. Research Phase
               • Identify target audience pain points
               • Analyze competitor content gaps
               • Research trending topics
               • Define content goals

            2. Creation Phase
               • Develop content briefs
               • Write compelling headlines
               • Create valuable content
               • Optimize for SEO

            ### 2. Lead Magnet Creation
            Your lead magnets should solve specific problems. Here are the most effective types:

            #### Educational Resources
            • Industry reports
            • White papers
            • Strategy guides
            • Tutorial series

            #### Tools and Templates
            • ROI calculators
            • Project planners
            • Process templates
            • Checklist systems

            ### 3. Distribution Strategy
            Getting your content in front of the right audience is crucial:

            #### Channels
            • **Social Media**: LinkedIn, Twitter, Instagram
            • **Email Marketing**: Segmented lists, automation
            • **Paid Advertising**: Platform-specific campaigns
            • **Partnerships**: Co-marketing opportunities
            """)

            # Add PDF download button
            with open("pdfs/lead_generation_guide.md", "r") as f:
                st.markdown('<div class="stDownloadButton">', unsafe_allow_html=True)
                btn = st.download_button(
                    label="📥 Download Complete Lead Generation Guide (PDF)",
                    data=f.read(),
                    file_name="agency_lead_generation_guide.pdf",
                    mime="application/pdf"
                )
                st.markdown('</div>', unsafe_allow_html=True)

            st.write("""
            ### Implementation Steps
            1. **Week 1**: Set up your content marketing foundation
               • Choose your primary content types
               • Create your content calendar
               • Set up tracking systems

            2. **Week 2**: Create your first lead magnets
               • Choose your lead magnet type
               • Develop the content
               • Set up delivery system

            3. **Week 3**: Launch your distribution strategy
               • Set up social media accounts
               • Create email sequences
               • Plan paid campaigns
            """)

        with tabs[1]:  # Sales System
            st.title("Agency Sales Mastery")
            
            st.write("""
            ## Module Overview
            Master the art of selling agency services with our proven system. This comprehensive module 
            breaks down every aspect of the sales process, from initial contact to closing high-ticket deals.

            ### What You'll Learn:
            • Building a repeatable sales framework
            • Conducting effective discovery calls
            • Creating winning proposals
            • Closing deals with confidence
            • Following up and nurturing leads

            ### Module Structure:
            1. Sales Foundation
            2. Discovery Process
            3. Proposal Creation
            4. Closing Strategy
            5. Follow-up System

            ### Implementation Timeline:
            This module is structured for implementation over 3-4 weeks. Each component builds on the previous, 
            creating a comprehensive sales system for your agency.
            """)

            # Add PDF download button
            with open("pdfs/sales_system_guide.md", "r") as f:
                btn = st.download_button(
                    label="📥 Download Complete Sales System Guide (PDF)",
                    data=f.read(),
                    file_name="agency_sales_system_guide.pdf",
                    mime="application/pdf"
                )

            st.write("""
            ### Getting Started:
            Begin with the Sales Foundation section. This will establish the core framework for your entire 
            sales process. Complete each section's action items before moving to the next.

            ### Expert Tips:
            • Focus on value, not features
            • Listen more than you talk
            • Always follow up systematically
            • Document everything for consistency

            Ready to transform your agency's sales process? Let's begin!
            """)

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

                Let me tell you about an interesting experiment we did. We tested two different welcome packages with 
                100 clients each. The first was just a standard email with forms. The second was our new enhanced 
                package. The enhanced package group had 40% fewer support requests in the first month and reported 
                90% higher satisfaction.

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

                Let me share a story that changed everything for us. We were spending hours manually sending emails. 
                Then we realized we could automate a lot of these emails. Game changer!

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
                Good: "Based on what you've shared, there are three main challenges we need to address..."
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
                hit that notification bell to catch that one. And if this was helpful, give it a thumbs up!
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

                The key is to keep providing value after the proposal. Think about it - if someone downloads a LinkedIn 
                checklist, they're probably trying to improve their LinkedIn presence. So every follow-up should help 
                them with that goal.

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

                That's when I realized something crucial - clients don't want to read a novel. They want to know three 
                things:
                1. Do you understand their problem?
                2. Can you solve it?
                3. How much will it cost?

                So I developed what I call the "5-Star Onboarding System":

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
                And hey, if you've gotten value from this, give it a thumbs up - it really helps the channel.
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

        with delivery_tabs[1]:  # Project Management
            if 'project_page' not in st.session_state:
                st.session_state.project_page = 1

            # Page 1: Project Setup
            if st.session_state.project_page == 1:
                st.title("Setting Up Your Project Management System")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that completely transformed my 
                agency - our project management system. I'm going to show you exactly how we set up and run projects 
                so nothing falls through the cracks.

                But first, let me tell you about a nightmare situation I had. We were managing everything through 
                email and spreadsheets. One day, we missed a crucial deadline because an email got buried in someone's 
                inbox. The client was furious, and we almost lost them.

                That's when I developed what I call the "Clear Vision Project System." Here's exactly how it works:

                Phase 1: Project Setup
                • Create project hub
                • Set up communication channels
                • Define project milestones
                • Assign team roles

                Phase 2: Task Organization
                • Break down deliverables
                • Set dependencies
                • Create task templates
                • Schedule check-ins

                Phase 3: Workflow Automation
                • Automate status updates
                • Set up reminders
                • Create report templates
                • Configure notifications

                The key is to make everything visible and accessible. No more digging through emails or wondering 
                what's happening with a task. In the next section, I'll show you exactly how to set up each part 
                of this system.
                """)

                if st.button("Next Page →", key="project_next_1"):
                    st.session_state.project_page = 2
                    st.rerun()

            # Page 2: Daily Operations
            elif st.session_state.project_page == 2:
                st.title("Running Your Daily Operations")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to run your daily operations using this system. 
                This is where most agencies struggle - they have a system, but they don't know how to use it effectively.

                Let me tell you about a game-changing moment. We were struggling with our morning meetings - they were 
                taking too long and people weren't prepared. Then we implemented this daily routine, and everything 
                changed.

                Here's the exact daily schedule we use:

                9:00 AM - Morning Huddle
                • Review priority tasks
                • Address blockers
                • Align on daily goals
                • Quick team updates

                11:00 AM - Focus Time
                • No meetings allowed
                • Deep work sessions
                • Task completion
                • Document progress

                2:00 PM - Client Updates
                • Send progress reports
                • Schedule check-ins
                • Address questions
                • Update timelines

                4:00 PM - Team Sync
                • Share accomplishments
                • Plan for tomorrow
                • Discuss challenges
                • Celebrate wins

                In the next section, I'll show you how to scale this system as your agency grows.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="project_prev_2"):
                        st.session_state.project_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="project_next_2"):
                        st.session_state.project_page = 3
                        st.rerun()

            # Page 3: Scaling Operations
            elif st.session_state.project_page == 3:
                st.title("Scaling Your Project Management")
                
                st.write("""
                Alright, this is where it gets exciting. I'm going to show you how to scale your project management 
                system as your agency grows. This is crucial because what works for 5 clients won't work for 50.

                Let me share a story. We hit a point where we had so many projects that our system started breaking 
                down. Tasks were slipping, team members were overwhelmed, and I was working weekends just to keep up. 
                That's when we developed this scaling framework.

                Here's exactly how we scale:

                Level 1: Team Structure
                • Create project pods
                • Assign pod leaders
                • Define escalation paths
                • Set communication protocols

                Level 2: Process Documentation
                • Create process wikis
                • Build template library
                • Standard operating procedures
                • Training materials

                Level 3: Automation Tools
                • Task assignment flows
                • Status update triggers
                • Report generation
                • Client communication

                Level 4: Quality Control
                • Review checkpoints
                • Feedback loops
                • Performance metrics
                • Improvement systems

                That's it for this video! In the next one, I'll show you how to implement quality control systems 
                that keep your deliverables consistent. Don't forget to hit subscribe and the notification bell to 
                catch that one!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="project_prev_3"):
                        st.session_state.project_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="project_start_over"):
                        st.session_state.project_page = 1
                        st.rerun()

        with delivery_tabs[2]:  # Quality Control
            if 'quality_page' not in st.session_state:
                st.session_state.quality_page = 1

            # Page 1: Quality Framework
            if st.session_state.quality_page == 1:
                st.title("Building Your Quality Control System")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's absolutely crucial for your 
                agency - quality control. I'm going to show you exactly how we maintain consistent quality 
                across all our deliverables.

                Let me tell you about a wake-up call I had. Early in my agency, we sent out a social media calendar 
                to a client without our usual review process. There were typos everywhere, some posts had the wrong 
                dates, and worst of all, one post was for their competitor's product! Talk about embarrassing.

                That's when I realized something crucial - clients don't want to read a novel. They want to know three 
                things:
                1. Do you understand their problem?
                2. Can you solve it?
                3. How much will it cost?

                So I developed what I call the "Triple Check System." Here's exactly how it works:

                Level 1: Creator Check
                • Self-review checklist
                • Brand guidelines review
                • Technical requirements
                • Content accuracy

                Level 2: Peer Review
                • Fresh eyes review
                • Technical validation
                • Brand consistency
                • User experience

                Level 3: Final Approval
                • Project manager review
                • Client requirements check
                • Strategic alignment
                • Final polish

                In the next section, I'll show you exactly what goes into each level of this system.
                """)

                if st.button("Next Page →", key="quality_next_1"):
                    st.session_state.quality_page = 2
                    st.rerun()

            # Page 2: Review Process
            elif st.session_state.quality_page == 2:
                st.title("The Perfect Review Process")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to run each level of the review process. This 
                is where most agencies fail - they either make it too complicated or too simple.

                Here's a story that changed everything. We used to have this massive 50-point checklist for 
                every deliverable. Sounds thorough, right? Wrong. People would just check boxes without really 
                looking. So we completely redesigned our process.

                Here's our exact review framework:

                Creator Check Process:
                • Complete the work
                • Step away for 10 minutes
                • Review with fresh eyes
                • Run through basic checklist

                Basic Checklist:
                • Spelling and grammar
                • Links and buttons work
                • Images and media load
                • Formatting is consistent

                Peer Review Process:
                • Assign to fresh eyes
                • Provide context
                • Set review deadline
                • Gather feedback

                Final Approval Process:
                • Strategic alignment check
                • Client requirement review
                • Final polish
                • Delivery prep

                In the next section, I'll show you how to automate parts of this process to make it even more 
                efficient.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="quality_prev_2"):
                        st.session_state.quality_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="quality_next_2"):
                        st.session_state.quality_page = 3
                        st.rerun()

            # Page 3: Quality Automation
            elif st.session_state.quality_page == 3:
                st.title("Automating Your Quality Control")
                
                st.write("""
                Alright, this is where it gets really interesting. I'm going to show you how to automate your 
                quality control process so it runs smoothly.

                Let me share a story that changed everything for us. We were spending hours manually checking deliverables 
                against our brand guidelines. Then we realized we could automate a lot of these checks. Game changer!

                Here's exactly how we automate quality control:

                Automated Checks:
                • Spelling and grammar
                • Brand term usage
                • Link validation
                • Image optimization

                Workflow Automation:
                • Review assignments
                • Deadline reminders
                • Status updates
                • Team coordination

                Template System:
                • Review checklists
                • Feedback forms
                • Client presentations
                • Delivery documents

                Communication Automation:
                • Review notifications
                • Feedback collection
                • Status updates
                • Client communications

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

                That's it for this video! In the next one, I'll show you how to set up your client success systems 
                to ensure happy, long-term clients. Make sure to hit subscribe and the notification bell so you 
                don't miss it!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="quality_prev_3"):
                        st.session_state.quality_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="quality_start_over"):
                        st.session_state.quality_page = 1
                        st.rerun()

        with delivery_tabs[3]:  # Client Success
            if 'success_page' not in st.session_state:
                st.session_state.success_page = 1

            # Page 1: Success Framework
            if st.session_state.success_page == 1:
                st.title("Building Your Client Success System")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's absolutely crucial for your 
                agency - client success. I'm going to show you exactly how we keep our clients happy and 
                engaged long-term.

                Let me tell you about a painful lesson I learned. We used to think that good work was enough to 
                keep clients happy. Then we lost three clients in one month - all of them said they just didn't 
                feel valued. That's when I realized we needed a real client success system.

                Here's what I developed - the "Client Joy System." Here's exactly how it works:

                Phase 1: Regular Check-ins
                • Weekly progress calls
                • Monthly strategy sessions
                • Quarterly reviews
                • Annual planning

                Phase 2: Proactive Communication
                • Industry updates
                • New opportunity alerts
                • Strategy suggestions
                • Educational content

                Phase 3: Value Demonstration
                • Progress tracking
                • Strategy alignment
                • Goal monitoring
                • Innovation planning

                In the next section, I'll show you exactly how to run each type of client meeting for maximum impact.
                """)

                if st.button("Next Page →", key="success_next_1"):
                    st.session_state.success_page = 2
                    st.rerun()

            # Page 2: Client Meetings
            elif st.session_state.success_page == 2:
                st.title("Running Effective Client Meetings")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to run each type of client meeting. This is 
                where most agencies mess up - they wing it and waste everyone's time.

                Here's a story that changed everything for us. We had this client who was always frustrated after 
                our calls. Turns out, we were talking about what WE thought was important, not what THEY cared 
                about. Once we fixed that, everything changed.

                Here's our exact meeting framework:

                Weekly Progress Calls:
                • Review this week's work
                • Address any concerns
                • Plan next week's tasks
                • Collect feedback

                Monthly Strategy Sessions:
                • Review monthly goals
                • Discuss market changes
                • Adjust strategies
                • Plan next month

                Quarterly Reviews:
                • Goal progress review
                • Strategy assessment
                • Market analysis
                • Future planning

                Annual Planning:
                • Year in review
                • Goal setting
                • Strategy development
                • Innovation planning

                In the next section, I'll show you how to automate parts of this process while keeping it personal.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="success_prev_2"):
                        st.session_state.success_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="success_next_2"):
                        st.session_state.success_page = 3
                        st.rerun()

            # Page 3: Success Automation
            elif st.session_state.success_page == 3:
                st.title("Automating Client Success")
                
                st.write("""
                Alright, this is where it all comes together. I'm going to show you how to automate your client 
                success system while keeping that personal touch that clients love.

                Let me share something interesting. We used to spend hours preparing for client meetings, sending 
                follow-ups, and tracking action items. Then we automated the routine stuff, which gave us more time 
                for strategic thinking and personal interaction.

                Here's exactly how we automate client success:

                Meeting Automation:
                • Calendar scheduling
                • Agenda creation
                • Reminder system
                • Follow-up emails

                Communication Automation:
                • Update notifications
                • Educational content
                • Industry news
                • Milestone alerts

                Documentation Automation:
                • Meeting notes
                • Action items
                • Progress tracking
                • Strategy documents

                Relationship Building:
                • Birthday reminders
                • Company milestones
                • Success celebrations
                • Thank you notes

                That's it for this video series! You now have everything you need to build an amazing client 
                success system. If you found this helpful, don't forget to like and subscribe. And drop a comment 
                below if you have any questions!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="success_prev_3"):
                        st.session_state.success_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="success_start_over"):
                        st.session_state.success_page = 1
                        st.rerun()

    elif selected_section == "Resources":
        st.title("Tools & Resources")
        
        # Sub-module tabs with better contrast
        resource_tabs = st.tabs([
            "**Essential Tools**",
            "**Templates**", 
            "**Checklists**", 
            "**Training**"
        ])
        
        with resource_tabs[0]:  # Essential Tools
            if 'tools_page' not in st.session_state:
                st.session_state.tools_page = 1

            # Page 1: Project Management Tools
            if st.session_state.tools_page == 1:
                st.title("Project Management Tools")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about the essential tools every agency needs 
                for project management. I'm going to show you exactly what tools to use and how to set them up.

                Let me tell you about a common mistake. When I started, I tried using too many tools at once. 
                It was overwhelming and actually slowed us down. That's when I developed this simple framework.

                Here's what you need:

                Core Project Tools:
                • Task management
                • Time tracking
                • File storage
                • Team chat

                Client Communication:
                • Meeting scheduler
                • Video conferencing
                • Document sharing
                • Email management

                Team Collaboration:
                • Design tools
                • Development tools
                • Writing tools
                • Review systems

                In the next section, I'll show you exactly how to choose the right tools for your agency.
                """)

                if st.button("Next Page →", key="tools_next_1"):
                    st.session_state.tools_page = 2
                    st.rerun()

            # Page 2: Marketing & Sales Tools
            elif st.session_state.tools_page == 2:
                st.title("Marketing & Sales Tools")
                
                st.write("""
                Welcome back! Now I'm going to show you the essential tools for marketing and sales. These are 
                the tools that help you find and close new clients.

                Here's our essential toolkit:

                Marketing Tools:
                • Email platform
                • Social scheduler
                • Content planner
                • Analytics tools

                Sales Tools:
                • CRM system
                • Proposal software
                • Contract platform
                • Payment system

                Automation Tools:
                • Lead capture
                • Email sequences
                • Task automation
                • Data sync

                Integration Tools:
                • API connections
                • Workflow tools
                • Data transfer
                • Reporting system

                In the next section, I'll show you how to integrate all these tools together.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="tools_prev_2"):
                        st.session_state.tools_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="tools_next_2"):
                        st.session_state.tools_page = 3
                        st.rerun()

            # Page 3: Tool Integration
            elif st.session_state.tools_page == 3:
                st.title("Integrating Your Tools")
                
                st.write("""
                Alright, this is where it all comes together. I'm going to show you how to integrate all your 
                tools into one smooth system.

                Here's our integration framework:

                Data Flow:
                • Tool mapping
                • Connection points
                • Data routing
                • Sync schedule

                Automation Rules:
                • Trigger events
                • Action steps
                • Error handling
                • Backup systems

                User Access:
                • Permission levels
                • Team roles
                • Client access
                • Security rules

                Maintenance Plan:
                • Regular checks
                • Updates schedule
                • Backup system
                • Recovery plan

                That's it for this video! In the next one, I'll show you our essential templates. Make sure to 
                hit subscribe and the notification bell to catch that one. And if this was helpful, give it a thumbs up!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="tools_prev_3"):
                        st.session_state.tools_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="tools_start_over"):
                        st.session_state.tools_page = 1
                        st.rerun()

    elif selected_section == "Growth":
        st.title("Agency Growth")
        
        # Sub-module tabs with better contrast
        growth_tabs = st.tabs([
            "**Team Building**",
            "**Systems & Processes**", 
            "**Financial Growth**", 
            "**Strategic Planning**"
        ])
        
        with growth_tabs[0]:  # Team Building
            if 'team_page' not in st.session_state:
                st.session_state.team_page = 1

            # Page 1: Team Structure
            if st.session_state.team_page == 1:
                st.title("Building Your Dream Team")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's absolutely crucial for your 
                agency - building your team. I'm going to show you exactly how to hire, train, and structure your 
                team.

                Let me tell you about a massive mistake I made early on. I hired people based purely on their skills, 
                without considering culture fit. We had brilliant people who just couldn't work together. It was a 
                nightmare. That's when I developed what I call the "Dream Team Framework."

                Here's exactly how it works:

                Phase 1: Role Definition
                • Create clear job descriptions
                • Define expectations
                • Set team structure
                • Map career paths

                Phase 2: Hiring Process
                • Culture fit assessment
                • Skills evaluation
                • Team compatibility
                • Growth potential

                Phase 3: Onboarding System
                • Welcome process
                • Training program
                • Mentorship setup
                • Integration plan

                The key is to hire for attitude and train for skills. In the next section, I'll show you exactly 
                how to run your hiring process to find these perfect-fit team members.
                """)

                if st.button("Next Page →", key="team_next_1"):
                    st.session_state.team_page = 2
                    st.rerun()

            # Page 2: Hiring Process
            elif st.session_state.team_page == 2:
                st.title("The Perfect Hiring Process")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to run your hiring process. This is where most 
                agencies mess up - they rush the process and end up with the wrong people.

                Here's a story that changed everything for us. We once spent three months trying to fill a position 
                because we kept compromising on our standards. When we finally got strict about our process, we 
                found the perfect person in just two weeks.

                Here's our exact hiring framework:

                Step 1: Initial Screening
                • Review application
                • Culture questionnaire
                • Portfolio review
                • Quick video intro

                Step 2: Skills Assessment
                • Practical test project
                • Tool proficiency
                • Problem-solving task
                • Communication test

                Step 3: Team Integration
                • Team interview
                • Work style assessment
                • Scenario handling
                • Values alignment

                Step 4: Final Evaluation
                • Reference checks
                • Team feedback
                • Offer preparation
                • Onboarding plan

                In the next section, I'll show you how to train and develop your team for long-term success.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="team_prev_2"):
                        st.session_state.team_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="team_next_2"):
                        st.session_state.team_page = 3
                        st.rerun()

            # Page 3: Team Development
            elif st.session_state.team_page == 3:
                st.title("Growing Your Team")
                
                st.write("""
                Alright, this is where it gets really exciting. I'm going to show you how to develop your team 
                into a high-performing unit that can handle anything.

                Let me share something powerful. We used to lose good people because they couldn't see their future 
                with us. Then we created clear growth paths and development plans. Now our retention is amazing, 
                and our team is constantly leveling up.

                Here's exactly how we develop our team:

                Individual Development:
                • Skill assessment
                • Learning paths
                • Mentorship program
                • Growth tracking

                Team Development:
                • Cross-training
                • Knowledge sharing
                • Team workshops
                • Collaboration tools

                Leadership Development:
                • Management training
                • Decision making
                • Delegation skills
                • Team building

                Career Progression:
                • Role advancement
                • Specialization paths
                • Leadership tracks
                • Skill certification

                That's it for this video! In the next one, I'll show you how to build systems and processes that 
                help your team perform at their best. Don't forget to hit subscribe and the notification bell to 
                catch that one!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="team_prev_3"):
                        st.session_state.team_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="team_start_over"):
                        st.session_state.team_page = 1
                        st.rerun()

        with growth_tabs[1]:  # Systems & Processes
            if 'systems_page' not in st.session_state:
                st.session_state.systems_page = 1

            # Page 1: Systems Framework
            if st.session_state.systems_page == 1:
                st.title("Building Scalable Systems")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's crucial for 
                scaling your agency - systems and processes. I'm going to show you exactly how to build systems 
                that work.

                Let me tell you about a painful lesson. We were growing fast, but everything was in my head. When 
                I got sick for a week, the whole agency nearly ground to a halt. That's when I realized we needed 
                proper systems.

                Here's what I developed - the "Scalable Systems Framework":

                Level 1: Core Systems
                • Project management
                • Communication flows
                • Task tracking
                • Team coordination

                Level 2: Process Documentation
                • Standard procedures
                • Work instructions
                • Quality guidelines
                • Training materials

                Level 3: Automation Tools
                • Workflow automation
                • Task scheduling
                • Team updates
                • Project tracking

                In the next section, I'll show you exactly how to document and implement these systems.
                """)

                if st.button("Next Page →", key="systems_next_1"):
                    st.session_state.systems_page = 2
                    st.rerun()

            # Page 2: Implementation
            elif st.session_state.systems_page == 2:
                st.title("Implementing Your Systems")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to implement these systems in your agency. 
                This is where most people fail - they create great systems that nobody actually uses.

                Here's a story that changed everything. We spent months creating this perfect system, but nobody 
                was using it. Then we realized we needed to make it easier to use than not to use. That's when 
                everything changed.

                Here's our implementation framework:

                Phase 1: Documentation
                • Process mapping
                • Step-by-step guides
                • Video tutorials
                • Quick reference cards

                Phase 2: Team Training
                • System overview
                • Hands-on practice
                • Q&A sessions
                • Feedback collection

                Phase 3: Integration
                • Gradual rollout
                • Daily support
                • Team updates
                • Process updates

                Phase 4: Optimization
                • User feedback
                • System updates
                • Process changes
                • Team input

                In the next section, I'll show you how to automate parts of this process to make it even more 
                efficient.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="systems_prev_2"):
                        st.session_state.systems_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="systems_next_2"):
                        st.session_state.systems_page = 3
                        st.rerun()

            # Page 3: Automation
            elif st.session_state.systems_page == 3:
                st.title("Automating Your Systems")
                
                st.write("""
                Alright, this is where it gets really powerful. I'm going to show you how to automate your systems 
                so they run smoothly.

                Let me share a story that changed everything for us. We were spending hours manually checking 
                deliverables against our brand guidelines. Then we realized we could automate a lot of these checks. 
                Game changer!

                Here's exactly how we automate:

                Workflow Automation:
                • Task assignment
                • Daily updates
                • Status checks
                • Team coordination

                Communication Automation:
                • Update notifications
                • Team messages
                • Project updates
                • Team alerts

                Process Automation:
                • Data collection
                • File organization
                • System checks
                • Task tracking

                Integration Automation:
                • Tool connections
                • Data sync
                • System updates
                • Backup systems

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

                That's it for this video! In the next one, I'll show you how to manage your agency's finances. 
                Make sure to hit subscribe and the notification bell so you don't miss it!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="systems_prev_3"):
                        st.session_state.systems_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="systems_start_over"):
                        st.session_state.systems_page = 1
                        st.rerun()

        with growth_tabs[2]:  # Financial Growth
            if 'finance_page' not in st.session_state:
                st.session_state.finance_page = 1

            # Page 1: Financial Framework
            if st.session_state.finance_page == 1:
                st.title("Financial Management Fundamentals")
                
                st.write("""
                Hey everyone! Welcome to another video. Today we're going to talk about something
                that's absolutely crucial for your agency - financial management.

                When I first started my agency, I was terrible at managing finances. I was focused
                on getting clients and delivering work, but the financial side was a mess. Here's
                what I learned:
                """)
                
                st.markdown("""
                <div class="module-card">
                    <h3>Financial Management Framework</h3>
                    <ul>
                        <li>Cash flow management</li>
                        <li>Pricing strategy</li>
                        <li>Expense tracking</li>
                        <li>Financial planning</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("""
                In the next video, we'll dive deep into each of these components. Make sure to
                subscribe so you don't miss it!
                """)

                if st.button("Next Page →", key="finance_next_1"):
                    st.session_state.finance_page = 2
                    st.rerun()

            # Page 2: Pricing Strategy
            elif st.session_state.finance_page == 2:
                st.title("Pricing Your Services")
                
                st.write("""
                Welcome back! Now let's talk about one of the most important aspects of financial
                management - pricing your services correctly.

                Here's what we'll cover today:
                """)
                
                st.markdown("""
                <div class="module-card">
                    <h3>Pricing Strategy Components</h3>
                    <ul>
                        <li>Value-based pricing</li>
                        <li>Package creation</li>
                        <li>Upsell opportunities</li>
                        <li>Pricing psychology</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("""
                Remember: your pricing isn't just about covering costs. It's about positioning
                your agency in the market and attracting the right clients.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="finance_prev_2"):
                        st.session_state.finance_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="finance_next_2"):
                        st.session_state.finance_page = 3
                        st.rerun()

            # Page 3: Financial Planning
            elif st.session_state.finance_page == 3:
                st.title("Financial Planning for Growth")
                
                st.write("""
                Hey everyone! In this final video about financial management, we're going to talk
                about planning for growth.

                Here's what you need to focus on:
                """)
                
                st.markdown("""
                <div class="module-card">
                    <h3>Growth Planning Elements</h3>
                    <ul>
                        <li>Investment strategy</li>
                        <li>Resource allocation</li>
                        <li>Risk management</li>
                        <li>Growth targets</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("""
                Remember: sustainable growth comes from smart financial planning and disciplined
                execution. Don't rush the process.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="finance_prev_3"):
                        st.session_state.finance_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="finance_start_over"):
                        st.session_state.finance_page = 1
                        st.rerun()

        with growth_tabs[3]:  # Strategic Planning
            if 'strategy_page' not in st.session_state:
                st.session_state.strategy_page = 1

            # Page 1: Strategic Framework
            if st.session_state.strategy_page == 1:
                st.title("Strategic Planning Framework")
                
                st.write("""
                Hey everyone! Welcome back. Today we're going to talk about something that's absolutely crucial 
                for your agency's future - strategic planning. I'm going to show you exactly how to plan for 
                sustainable growth.

                Let me tell you about a big mistake I made. I used to just focus on getting more clients, 
                without any real strategy. We grew, but it was chaotic and stressful. That's when I developed 
                the "Strategic Growth Framework."

                Here's exactly how it works:

                Vision Setting:
                • Agency mission
                • Core values
                • Long-term goals
                • Market position

                Market Analysis:
                • Industry trends
                • Competitor research
                • Client needs
                • Opportunity gaps

                Growth Planning:
                • Service expansion
                • Market targeting
                • Team development
                • Resource allocation

                In the next section, I'll show you exactly how to implement this framework in your agency.
                """)

                if st.button("Next Page →", key="strategy_next_1"):
                    st.session_state.strategy_page = 2
                    st.rerun()

            # Page 2: Implementation
            elif st.session_state.strategy_page == 2:
                st.title("Implementing Your Strategy")
                
                st.write("""
                Welcome back! Now I'm going to show you exactly how to implement your strategic plan. This is 
                where most agencies fail - they make great plans but never execute them properly.

                Here's a story that changed everything. We had this beautiful strategic plan, but six months 
                later, nothing had changed. Then we developed this implementation system, and everything started 
                moving forward.

                Here's our implementation framework:

                90-Day Sprints:
                • Key objectives
                • Action items
                • Team assignments
                • Progress tracking

                Monthly Reviews:
                • Goal progress
                • Strategy alignment
                • Resource check
                • Plan adjustments

                Weekly Actions:
                • Task priorities
                • Team updates
                • Blocker removal
                • Quick wins

                Daily Management:
                • Morning planning
                • Progress checks
                • Team support
                • End-day review

                In the next section, I'll show you how to adjust and optimize your strategy over time.
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="strategy_prev_2"):
                        st.session_state.strategy_page = 1
                        st.rerun()
                with col2:
                    if st.button("Next Page →", key="strategy_next_2"):
                        st.session_state.strategy_page = 3
                        st.rerun()

            # Page 3: Strategy Optimization
            elif st.session_state.strategy_page == 3:
                st.title("Optimizing Your Strategy")
                
                st.write("""
                Alright, this is where it all comes together. I'm going to show you how to continuously 
                optimize your strategy for maximum impact.

                Let me share something powerful. We used to stick to our plans no matter what, even when 
                things weren't working. Then we learned to be more flexible and adaptive, and our growth 
                really took off.

                Here's exactly how we optimize:

                Performance Review:
                • Strategy assessment
                • Team feedback
                • Market response
                • Future planning

                Adaptation Process:
                • Market changes
                • Client needs
                • Team capacity
                • Resource planning

                Innovation Planning:
                • Service development
                • Process improvement
                • Team evolution
                • Technology adoption

                Future Preparation:
                • Trend analysis
                • Market research
                • Risk assessment
                • Growth planning

                That's it for this video series! You now have everything you need to create and implement a 
                powerful strategic plan for your agency. If you found this helpful, don't forget to like and 
                subscribe. And drop a comment below if you have any questions!
                """)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("← Previous Page", key="strategy_prev_3"):
                        st.session_state.strategy_page = 2
                        st.rerun()
                with col2:
                    if st.button("Start Over", key="strategy_start_over"):
                        st.session_state.strategy_page = 1
                        st.rerun()

# Remove results from Team Building section
st.write("""
Let me share something powerful. We used to lose good people because they couldn't see their future 
with us. Then we created clear growth paths and development plans. Now our team is stronger than ever.

Here's what we focus on:
• Clear role definitions
• Growth opportunities
• Regular feedback
• Team recognition

Remember: your team is your most valuable asset. Invest in them, and they'll invest in your vision.
""")

# Remove case study references from Team Building section
st.write("""
Let me share something powerful. We used to lose good people because they couldn't see their future 
with us. Then we created clear growth paths and development plans. Now our team is stronger than ever.

Here's what we focus on:
• Clear role definitions
• Growth opportunities
• Regular feedback
• Team recognition

Remember: your team is your most valuable asset. Invest in them, and they'll invest in your vision.
""")

# Remove case study references from Systems section
st.write("""
Let me share something that changed everything. We used to waste hours on repetitive tasks.
Then we created systems to automate them. Now our team can focus on what really matters.

Here's what we systemize:
• Client communication
• Project workflows
• Quality checks
• Team coordination

The key is to start small and gradually build up your systems.
""")

# Remove case study references from Financial section
st.write("""
When I started my agency, I made a lot of mistakes with finances. Now we have a clear system
that keeps everything organized and predictable.

Focus on these areas:
• Cash flow management
• Pricing strategy
• Expense tracking
• Growth planning

Remember: good financial management is the foundation of a sustainable agency.
""")

# Remove metrics from Systems section
st.write("""
Here's exactly how we automate:

Workflow Automation:
• Task assignment
• Daily updates
• Status checks
• Team coordination

Communication Automation:
• Update notifications
• Team messages
• Project updates
• Team alerts

Process Automation:
• Data collection
• File organization
• System checks
• Task tracking

Integration Automation:
• Tool connections
• Data sync
• System updates
• Backup systems
""")

# Remove performance metrics from Financial section
st.write("""
Here's our exact pricing framework:

Service Packages:
• Basic package
• Standard package
• Premium package
• Custom solutions

Package Components:
• Core services
• Add-on options
• Support levels
• Delivery timeline
""")

# Remove ROI and metrics from Strategy section
st.write("""
Here's exactly how we optimize:

Strategy Review:
• Plan assessment
• Team feedback
• Market analysis
• Future planning

Adaptation Process:
• Market changes
• Client needs
• Team capacity
• Resource planning
""")

# Remove success metrics from Quality Control
st.write("""
Here's exactly how we automate quality control:

Automated Checks:
• Content review
• Brand alignment
• Link validation
• Image optimization
""")

# Remove performance metrics from Client Success
st.write("""
Here's exactly how we automate client success:

Meeting Automation:
• Calendar scheduling
• Agenda creation
• Reminder system
• Follow-up emails

Communication Automation:
• Update notifications
• Educational content
• Industry news
• Project updates

Documentation Automation:
• Meeting notes
• Action items
• Progress tracking
• Strategy documents

Relationship Building:
• Regular check-ins
• Company updates
• Project milestones
• Thank you notes
""")

# Remove metrics from Systems & Processes section
st.write("""
Here's exactly how we automate:

Workflow Automation:
• Task assignment
• Daily updates
• Status checks
• Team coordination

Communication Automation:
• Update notifications
• Team messages
• Project updates
• Team alerts

Process Automation:
• Data collection
• File organization
• System checks
• Task tracking

Integration Automation:
• Tool connections
• Data sync
• System updates
• Backup systems
""")

# Remove metrics from Financial Growth section
st.write("""
Here's our pricing framework:

Service Packages:
• Basic package
• Standard package
• Premium package
• Custom solutions

Package Components:
• Core services
• Add-on options
• Support levels
• Delivery timeline

Value Pricing:
• Client needs
• Industry standards
• Market position
• Service scope

Pricing Structure:
• Package design
• Feature layout
• Option structure
• Service paths
""")

# Remove metrics from Strategic Planning section
st.write("""
Here's exactly how we optimize:

Strategy Review:
• Plan assessment
• Team feedback
• Market analysis
• Future planning

Adaptation Process:
• Market changes
• Client needs
• Team capacity
• Resource planning

Innovation Planning:
• Service development
• Process improvement
• Team evolution
• Technology adoption

Future Planning:
• Trend analysis
• Market research
• Risk planning
• Growth strategy
""")

# Remove metrics from Quality Control section
st.write("""
Here's how we maintain quality:

Content Review:
• Brand alignment
• Technical review
• Design check
• Final polish

Process Review:
• Team feedback
• Client input
• System updates
• Process changes

Documentation:
• Project guides
• Team resources
• Process docs
• Training materials
""")

# Remove performance metrics from Client Success
st.write("""
Here's exactly how we automate client success:

Meeting Automation:
• Calendar scheduling
• Agenda creation
• Reminder system
• Follow-up emails

Communication Automation:
• Update notifications
• Educational content
• Industry news
• Milestone alerts

Documentation Automation:
• Meeting notes
• Action items
• Progress tracking
• Strategy documents

Relationship Building:
• Birthday reminders
• Company milestones
• Success celebrations
• Thank you notes
""")

# Remove metrics from Client Success section
st.write("""
Here's exactly how we automate client success:

Meeting Automation:
• Calendar scheduling
• Agenda creation
• Reminder system
• Follow-up emails

Communication Automation:
• Update notifications
• Educational content
• Industry news
• Project updates

Documentation Automation:
• Meeting notes
• Action items
• Progress tracking
• Strategy documents

Relationship Building:
• Regular check-ins
• Company updates
• Project milestones
• Thank you notes
""")
