import streamlit as st
import streamlit.components.v1 as components
import markdown
import os
from pathlib import Path

# Set page config for a modern look
st.set_page_config(
    page_title="Agency Growth System",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern, clean look
st.markdown("""
<style>
    /* Main container */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #1a1a1a;
    }
    
    /* Headers */
    h1 {
        color: #1a1a1a;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    h2 {
        color: #2c3e50;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        margin-top: 2rem !important;
    }
    
    h3 {
        color: #34495e;
        font-size: 1.3rem !important;
        font-weight: 500 !important;
    }
    
    /* Cards */
    .stCard {
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 1.5rem;
        margin: 1rem 0;
        background-color: white;
        transition: transform 0.2s ease-in-out;
    }
    
    .stCard:hover {
        transform: translateY(-5px);
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        padding: 0.5rem 1rem;
        background-color: #2962ff;
        color: white;
        border: none;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        background-color: #1e4bd8;
        transform: translateY(-2px);
    }
    
    /* Progress bars */
    .stProgress>div>div>div {
        background-color: #2962ff;
    }
    
    /* Metrics */
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    /* Custom card classes */
    .module-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.2s ease-in-out;
    }
    
    .module-card:hover {
        transform: translateY(-5px);
    }
    
    .progress-card {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    /* Custom text styles */
    .text-muted {
        color: #64748b;
        font-size: 0.9rem;
    }
    
    .text-primary {
        color: #2962ff;
        font-weight: 500;
    }
    
    /* Navigation pills */
    .nav-pills {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .nav-pill {
        padding: 0.5rem 1rem;
        background-color: #f1f5f9;
        border-radius: 20px;
        color: #64748b;
        text-decoration: none;
        transition: all 0.2s ease-in-out;
    }
    
    .nav-pill:hover, .nav-pill.active {
        background-color: #2962ff;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Function to read markdown content
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to create a module card
def create_module_card(title, description, progress, action_items):
    with st.container():
        st.markdown(f"""
        <div class="module-card">
            <h3>{title}</h3>
            <p>{description}</p>
            <div class="progress-card">
                <div class="text-muted">Progress</div>
                <div class="stProgress">
                    <div style="width: {progress}%; height: 6px; background-color: #2962ff; border-radius: 3px;"></div>
                </div>
                <div class="text-primary">{progress}% Complete</div>
            </div>
            <div style="margin-top: 1rem;">
                <div class="text-muted">Action Items:</div>
                {''.join(f'<div style="margin-top: 0.5rem;">• {item}</div>' for item in action_items)}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Agency Growth")
    
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
    st.title("Your Growth Dashboard")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="stMetric">
            <div class="text-muted">Active Clients</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #1a1a1a;">12</div>
            <div style="color: #22c55e; font-size: 0.8rem;">+2 this month</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stMetric">
            <div class="text-muted">Monthly Revenue</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #1a1a1a;">$24,500</div>
            <div style="color: #22c55e; font-size: 0.8rem;">+15% from last month</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stMetric">
            <div class="text-muted">Leads in Pipeline</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #1a1a1a;">28</div>
            <div style="color: #22c55e; font-size: 0.8rem;">+5 this week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stMetric">
            <div class="text-muted">Client Satisfaction</div>
            <div style="font-size: 1.5rem; font-weight: 600; color: #1a1a1a;">94%</div>
            <div style="color: #22c55e; font-size: 0.8rem;">+2% this month</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown("""
    <h2 style="margin-top: 2rem;">Recent Activity</h2>
    <div class="module-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <div class="text-primary">New Client Onboarded</div>
                <div class="text-muted">Tech Solutions Inc.</div>
            </div>
            <div class="text-muted">2 hours ago</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <div class="text-primary">Proposal Sent</div>
                <div class="text-muted">Digital Marketing Package</div>
            </div>
            <div class="text-muted">5 hours ago</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div class="text-primary">Strategy Call Completed</div>
                <div class="text-muted">Growth Planning Session</div>
            </div>
            <div class="text-muted">Yesterday</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Module Progress
    st.markdown("<h2 style='margin-top: 2rem;'>Module Progress</h2>", unsafe_allow_html=True)
    
    create_module_card(
        "Client Acquisition",
        "Learn how to consistently attract and close high-ticket clients",
        85,
        ["Complete lead magnet", "Set up automation", "Review analytics"]
    )
    
    create_module_card(
        "Service Delivery",
        "Deliver exceptional results that turn clients into advocates",
        60,
        ["Update SOP documentation", "Train team on new process", "Schedule client reviews"]
    )
    
    create_module_card(
        "Team Management",
        "Build and manage a high-performing team",
        40,
        ["Create hiring plan", "Develop training materials", "Set up performance metrics"]
    )

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
        content = read_markdown_file(module_path)
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
        content = read_markdown_file(module_path)
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
        content = read_markdown_file(module_path)
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
