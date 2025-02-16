import streamlit as st
import os
import markdown
import json

# Custom CSS
st.set_page_config(
    page_title="AquiPro | Agency Growth System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 2rem;
    }
    .stMarkdown h1 {
        color: #FF4B4B;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 2rem;
    }
    .stMarkdown h2 {
        color: #1E1E1E;
        font-size: 2rem;
        font-weight: 700;
        margin-top: 2rem;
    }
    .stMarkdown h3 {
        color: #2E2E2E;
        font-size: 1.5rem;
        font-weight: 600;
    }
    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    .stMarkdown ul {
        font-size: 1.1rem;
        line-height: 1.8;
    }
    .stSidebar {
        background-color: #1E1E1E;
        padding: 2rem 1rem;
    }
    .stSidebar .stMarkdown h1 {
        color: white;
        font-size: 1.5rem;
        font-weight: 700;
    }
    .stSelectbox label {
        font-size: 1.2rem;
        font-weight: 600;
        color: white;
    }
    .stSelectbox div[data-baseweb="select"] {
        margin-top: 0.5rem;
    }
    .step-button {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.25rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
    }
    .step-button:hover {
        background-color: #FF4B4B;
        color: white;
    }
    .step-button.active {
        background-color: #FF4B4B;
        color: white;
    }
    .module-content {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

def read_markdown_file(file_path, section=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if section:
                # Split content by sections and find the requested section
                sections = content.split('## ')
                for s in sections:
                    if s.startswith(section):
                        return '## ' + s
            return content
    except Exception as e:
        return f"Error loading content: {str(e)}"

def main():
    # Sidebar
    with st.sidebar:
        st.title("⚡ AquiPro")
        st.markdown("---")
        
        # Main sections with emojis
        sections = {
            "🎯 Foundation & Positioning": {
                "path": "course-structure/modules/1-foundation",
                "modules": {
                    "Market Research": [
                        "Before You Begin",
                        "Initial Market Analysis",
                        "Deep Market Research",
                        "Competitor Analysis",
                        "Market Selection",
                        "Market Entry Planning"
                    ],
                    "Positioning Strategy": [
                        "Unique Value Proposition",
                        "Brand Voice",
                        "Market Positioning",
                        "Implementation"
                    ]
                }
            },
            "🔥 Client Acquisition": {
                "path": "course-structure/modules/2-acquisition",
                "modules": {
                    "Market Research": [
                        "Before You Begin",
                        "Initial Market Analysis",
                        "Deep Market Research",
                        "Competitor Analysis",
                        "Market Selection",
                        "Market Entry Planning"
                    ],
                    "Offer Creation": [
                        "Value Stack",
                        "Pricing Strategy",
                        "Delivery Framework",
                        "Sales Process"
                    ],
                    "Lead Generation": [
                        "Content Strategy",
                        "Paid Acquisition",
                        "Organic Growth",
                        "Lead Nurturing"
                    ]
                }
            },
            "⚡ Service Delivery": {
                "path": "course-structure/modules/3-delivery",
                "modules": [
                    "Client Onboarding",
                    "Project Management",
                    "Communication",
                    "Quality Assurance",
                    "Process Optimization"
                ]
            },
            "🤝 Client Retention": {
                "path": "course-structure/modules/4-retention",
                "modules": [
                    "Value Maximization",
                    "Relationship Building",
                    "Success System",
                    "Loyalty Program",
                    "Implementation"
                ]
            },
            "👥 Team Building": {
                "path": "course-structure/modules/5-team",
                "modules": [
                    "Team Structure",
                    "Hiring System",
                    "Training Program",
                    "Culture Building",
                    "Systems & Processes"
                ]
            }
        }
        
        selected_section = st.selectbox("Choose Your Module", list(sections.keys()))
        
        st.markdown("---")
        st.markdown("""
            <div style='color: #666; font-size: 0.9rem;'>
            Powered by proven strategies from:<br>
            • Alex Hormozi<br>
            • Sam Ovens<br>
            • Dan Henry
            </div>
        """, unsafe_allow_html=True)
    
    # Main content
    if selected_section:
        # Remove emoji for file path
        clean_section = selected_section[2:]
        section_data = sections[selected_section]
        
        # Header with gradient
        st.markdown(f"""
            <div style='background: linear-gradient(90deg, #FF4B4B 0%, #FF8C8C 100%); 
                        padding: 2rem; 
                        border-radius: 10px; 
                        margin-bottom: 2rem;'>
                <h1 style='color: white; margin: 0; padding: 0;'>{clean_section}</h1>
            </div>
        """, unsafe_allow_html=True)
        
        # Create columns for module navigation
        col1, col2 = st.columns([1, 3])
        
        # Module navigation in left column
        with col1:
            st.markdown("### Module Navigation")
            selected_module = None
            for module in section_data["modules"]:
                if st.button(f"📘 {module}", key=module, use_container_width=True):
                    selected_module = module
                    st.session_state.selected_step = None
        
        # Module content in right column
        with col2:
            if selected_module:
                # Show step navigation buttons
                st.markdown("### Steps")
                if isinstance(section_data["modules"][selected_module], dict):
                    steps = section_data["modules"][selected_module]
                    cols = st.columns(3)
                    selected_step = None
                    
                    for i, step in enumerate(steps):
                        col_index = i % 3
                        with cols[col_index]:
                            if st.button(f"Step {i+1}: {step}", key=f"step_{i}", use_container_width=True):
                                selected_step = step
                                st.session_state.selected_step = step
                    
                    st.markdown("---")
                    
                    # Show selected step content or full module
                    if hasattr(st.session_state, 'selected_step') and st.session_state.selected_step:
                        step = st.session_state.selected_step
                        module_path = f"{section_data['path']}/{selected_module.lower().replace(' ', '-')}.md"
                        if os.path.exists(module_path):
                            content = read_markdown_file(module_path, step)
                            st.markdown(content)
                    else:
                        module_path = f"{section_data['path']}/{selected_module.lower().replace(' ', '-')}.md"
                        if os.path.exists(module_path):
                            content = read_markdown_file(module_path)
                            st.markdown(content)
                        else:
                            st.warning(f"Content for {selected_module} is coming soon!")
                            st.markdown("""
                                ### Module Overview
                                This module is currently under development. It will include:
                                
                                * Step-by-step implementation guide
                                * Automation processes
                                * Templates and resources
                                * Action plans and checklists
                                
                                Check back soon for updates!
                            """)
                else:
                    module_path = f"{section_data['path']}/{selected_module.lower().replace(' ', '-')}.md"
                    if os.path.exists(module_path):
                        content = read_markdown_file(module_path)
                        st.markdown(content)
                    else:
                        st.warning(f"Content for {selected_module} is coming soon!")
                        st.markdown("""
                            ### Module Overview
                            This module is currently under development. It will include:
                            
                            * Step-by-step implementation guide
                            * Automation processes
                            * Templates and resources
                            * Action plans and checklists
                            
                            Check back soon for updates!
                        """)
            else:
                st.info("👈 Select a module from the navigation menu to view its content")

if __name__ == "__main__":
    main()
