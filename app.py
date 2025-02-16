import streamlit as st
import os
import markdown

# Set page config
st.set_page_config(
    page_title="Agency Growth System",
    page_icon="🚀",
    layout="wide"
)

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error loading content: {str(e)}"

def main():
    st.title("Agency Growth System")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    
    # Main sections
    sections = [
        "Foundation & Positioning",
        "Client Acquisition",
        "Service Delivery",
        "Client Retention",
        "Team Building"
    ]
    
    selected_section = st.sidebar.selectbox("Choose a Module", sections)
    
    # Content paths
    content_map = {
        "Foundation & Positioning": "course-structure/modules/1-foundation/pricing-strategy-guide.md",
        "Client Acquisition": "course-structure/modules/2-acquisition/client-acquisition-guide.md",
        "Service Delivery": "course-structure/modules/3-delivery/service-delivery-guide.md",
        "Client Retention": "course-structure/modules/4-retention/retention-guide.md",
        "Team Building": "course-structure/modules/5-team/team-building-guide.md"
    }
    
    # Display content
    if selected_section in content_map:
        file_path = os.path.join(os.getcwd(), content_map[selected_section])
        if os.path.exists(file_path):
            content = read_markdown_file(file_path)
            st.markdown(content)
        else:
            st.warning(f"Content for {selected_section} is coming soon!")

if __name__ == "__main__":
    main()
