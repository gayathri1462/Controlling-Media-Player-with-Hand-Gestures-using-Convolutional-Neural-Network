import streamlit as st
import operator
import sys, os

def main():
    html_temp = """
    <div style="background-color:#f63366 ;padding:10px;margin-bottom:10px;">
    <h1 style="color:white;text-align:center;">Hand Gesture Recognition Web App</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.sidebar.title("Pages")
    # Add a selectbox to the sidebar:
    pages=['About Web App','Project Demo', 'Download App']
    add_pages = st.sidebar.selectbox('', pages)

    st.sidebar.title("Made By:")
    html_temp6 = """
<ul style="font-weight:bold;">
<li>Gayathri Devi Nagalapuram </li>
<li>Varshashree D </li>
<li>Donal Jovian N </li>
<li>Dheeraj D </li>
</ul>
    """
    st.sidebar.markdown(html_temp6, unsafe_allow_html=True)

    if add_pages=='About Web App':
        html_temp2 = """
    <body style="background-color:white;padding:10px;">
    <h3 style="color:#f63366 ;text-align:center;">About Web App</h3>
    The Main aim of this application is to use the most natural form i.e., Hand gestures to interact with the
computer system. These gestures are implemented in such a way that they are easy to perform, fast,
efficient and ensuring an immediate response.
The application uses your device's camera to give you touch-free and remote-free control over your media player application
(without any special hardware).It increases productivity and makes life easier and comfortable by
letting you control your device from a distance.
    </body>
<div style="background-color:black;padding:10px;margin-bottom:10px;">
<h4 style="color:white;">Prepared using:</h4>
<ul style="color:white;">
<li>Opencv </li>
<li>Keras </li>
<li>Streamlit </li>
</ul>
</div>
"""
        st.markdown(html_temp2, unsafe_allow_html=True)

    elif add_pages =='Project Demo':
        html_temp3 = """
    <body style="background-color:white;padding:5px;">
    <h3 style="color:#f63366 ;text-align:center;">Demo of using Hand gestures to control Media player</h3>
    """
        st.markdown(html_temp3, unsafe_allow_html=True)
        st.video("demo.mp4")
    elif add_pages =='Download App':
                html_temp4 = """
            <body style="background-color:white;padding:5px;">
            <h3 style="color:#f63366 ;">Download Application</h3>
            <a style="background-color: black;
            color:white ;
            margin-top:20px;
            padding: 14px 25px;
            text-align: center;
            text-decoration: none;
            display: inline-block; " href="https://github.com/gayathri1462/Hand-Gesture-Recognition-Streamlit" target="_blank">Download Files</a>
            """
                st.markdown(html_temp4, unsafe_allow_html=True)
                st.subheader("Run App using the following command:")
                st.write("streamlit run localapp.py")

if __name__ == '__main__':
    main()
