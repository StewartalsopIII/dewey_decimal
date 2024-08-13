import streamlit as st
import random
from updated_dewey_data import dewey_system

def get_random_subdivision():
    main_class = random.choice(list(dewey_system.keys()))
    subdivision = random.choice(dewey_system[main_class])
    return main_class, subdivision

def main():
    st.title("Dewey Decimal System Subdivision Randomizer")

    st.write("Click the button below to get a random Dewey Decimal System subdivision to learn:")

    if st.button("Get Random Subdivision"):
        main_class, subdivision = get_random_subdivision()
        
        # Extract the main class number and description
        main_class_number = main_class.split()[0]
        main_class_description = ' '.join(main_class.split()[1:])

        st.subheader(f"Main Class: {main_class_number} - {main_class_description}")
        st.write(f"Subdivision: {subdivision}")

        # Optional: Display more information about the main class
        st.write("---")
        st.write("All subdivisions in this main class:")
        for sub in dewey_system[main_class]:
            st.write(f"- {sub}")

    # Sidebar with information about the Dewey Decimal System
    st.sidebar.title("About the Dewey Decimal System")
    st.sidebar.write("""
    The Dewey Decimal System is a proprietary library classification system first published in the United States by Melvil Dewey in 1876. It has been revised and expanded through 23 major editions, the latest issued in 2011, and has become the most widely used library classification system in the world.
    """)

if __name__ == "__main__":
    main()