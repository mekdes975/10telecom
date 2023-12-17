import streamlit as st
import sys
import os

def main():
    st.sidebar.title('Telecom Analysis')
    selected_option = st.sidebar.radio("Select Option", ('Home','EDA', 'User Engagement', 'Other Section'))

    if selected_option == 'EDA':
        display_eda_section()
    elif selected_option == 'User Engagement':
        display_user_engagement_section()
    elif selected_option == 'Other Section':
        display_other_section()
    elif selected_option == 'Home':
        display_Home_section()
def display_Home_section():
    st.title('welcome to telecome user analytics page')
    '''
    some introduction about the project 
    '''
def display_eda_section():
    st.title('Exploratory Data Analysis (EDA)')
    # Your EDA code goes here
    st.write('Placeholder for EDA content')

def display_user_engagement_section():
    st.title('User Engagement Analysis')
    # Your User Engagement analysis code goes here
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

    if parent_directory not in sys.path:
        sys.path.insert(0, parent_directory)














        
    
    from notebooks import user_engagement

    user_engagement
    st.write('Placeholder for User Engagement content')

def display_other_section():
    st.title('Other Section')
    # Your code for other sections goes here
    st.write('Placeholder for other section content')

if __name__ == "__main__":

    
    main()
