import streamlit as st
import os
import markdown

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
    </style>
""", unsafe_allow_html=True)

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error loading content: {str(e)}"

def main():
    # Sidebar
    with st.sidebar:
        st.title("⚡ AquiPro")
        st.markdown("---")
        
        # Main sections with emojis
        sections = {
            "🎯 Foundation & Positioning": "course-structure/modules/1-foundation/pricing-strategy-guide.md",
            "🔥 Client Acquisition": "course-structure/modules/2-acquisition/client-acquisition-guide.md",
            "⚡ Service Delivery": "course-structure/modules/3-delivery/service-delivery-guide.md",
            "🤝 Client Retention": "course-structure/modules/4-retention/retention-guide.md",
            "👥 Team Building": "course-structure/modules/5-team/team-building-guide.md"
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
        file_path = os.path.join(os.getcwd(), sections[selected_section])
        
        # Header with gradient
        st.markdown(f"""
            <div style='background: linear-gradient(90deg, #FF4B4B 0%, #FF8C8C 100%); 
                        padding: 2rem; 
                        border-radius: 10px; 
                        margin-bottom: 2rem;'>
                <h1 style='color: white; margin: 0; padding: 0;'>{clean_section}</h1>
            </div>
        """, unsafe_allow_html=True)
        
        if os.path.exists(file_path):
            content = read_markdown_file(file_path)
            st.markdown(content)
        else:
            st.warning(f"Content for {clean_section} is coming soon!")
            
            # Show placeholder content
            st.markdown("""
                ### Module Overview
                This module is currently under development. It will include:
                
                * Comprehensive strategies and frameworks
                * Step-by-step implementation guides
                * Templates and resources
                * Action plans and checklists
                
                Check back soon for updates!
            """)

if __name__ == "__main__":
    main()
