import streamlit as st

def create_component(key):
    st.slider('Chapter 2', 0, 4, key=f"slider-{key}")

    # with col_add:
    #    st.button("➕", help="See more", on_click=create_component, key=f"button-{component_id}", use_container_width=True) 
    
    st.slider("Chapter 2 Step", 0, 5, key=f"slider-step-{key}")

if __name__ == '__main__':
    
    # Pages
    st.markdown("# Chapters")
    st.sidebar.markdown("# Chapters")
    

    slider1 = st.slider('Chapter 1', 0, 3)

    for i in range(4):
        create_component(i)       








