import cv2
import numpy as np
import streamlit as st
import pyautogui
import time
from keras.models import model_from_json
import operator
import os
import sys

json_file = open("gesture-model.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("gesture-model.h5")
print("Loaded model from disk")
# Category dictionary
categories = {0: 'palm', 1: 'fist', 2: 'thumbs-up', 3: 'thumbs-down', 4: 'index-right', 5: 'index-left', 6:'no-gesture'}

def main():
    html_temp = """
    <div style="background-color:#f63366 ;padding:10px;margin-bottom:10px;">
    <h1 style="color:white;text-align:center;">Hand Gesture Recognition Web App</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.sidebar.title("Pages")
    # Add a selectbox to the sidebar:
    pages=['About Web App','Project Demo','Gesture Control Page']
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
<li>PyAutoGui </li>
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
        st.video("D:\\Minor Project\\media\\demo.mp4")


    elif add_pages =='Gesture Control Page':
        html_temp5 = """
    <body style="background-color:white;padding:5px;">
    <h3 style="color:#f63366 ;text-align:center;">Control Media player using Hand Gestures </h3>
        <ul> Gestures and their Function
        <li>✋ or 🤚 : Palm : Play / Pause</li>
        <li>✊ : fist : Mute</li>
        <li>👍: Thumbs Up : Volume up</li>
        <li>👎: Thumbs Down: Volume Down </li>
        <li>👉: Index Right: Forward </li>
        <li>👈: Index Left: Rewind </li>
        <li>No Hand : No gesture: No action  </li>
        </ul>
    """
        st.markdown(html_temp5, unsafe_allow_html=True)
        run = st.button('Start Web Camera')
        FRAME_WINDOW1 = st.image([])
        FRAME_WINDOW2 = st.image([])
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
        #st.write("Test image")
        while run:
            _, frame = camera.read()
            # Simulating mirror image
            frame = cv2.flip(frame, 1)
            # Got this from collect-data.py
            # Coordinates of the ROI
            x1 = int(0.5*frame.shape[1])
            y1 = 10
            x2 = frame.shape[1]-10
            y2 = int(0.5*frame.shape[1])
            # Drawing the ROI
            # The increment/decrement by 1 is to compensate for the bounding box
            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0),3)
            # Extracting the ROI
            roi = frame[y1:y2, x1:x2]

            # Resizing the ROI so it can be fed to the model for prediction
            roi = cv2.resize(roi, (120, 120))
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            _, test_image = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            FRAME_WINDOW1.image(test_image)
            result = loaded_model.predict(test_image.reshape(1, 120, 120, 1))
            prediction = {'palm': result[0][0],
                              'fist': result[0][1],
                              'thumbs-up': result[0][2],
                              'thumbs-down': result[0][3],
                              'index-right': result[0][4],
                              'index-left': result[0][5],
                              'no-gesture':result[0][6]}
                # Sorting based on top prediction
            prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
            if(prediction[0][0] == 'palm'):
                final_label = 'palm'
                action = "PLAY/PAUSE"
                pyautogui.press('playpause', presses=1)
                time.sleep(0.5)
            elif (prediction[0][0] == 'fist'):
                final_label = 'fist'
                action = "MUTE"
                pyautogui.press('volumemute', presses=1)
                time.sleep(0.5)
            elif (prediction[0][0] == 'thumbs-up'):
                final_label = "thumbs-up"
                action = "VOLUME UP"
                pyautogui.press('volumeup', presses=1)
            elif (prediction[0][0] == "thumbs-down"):
                final_label = "thumbs-down"
                action = "VOLUME DOWN"
                pyautogui.press('volumedown', presses=1)
            elif (prediction[0][0] == "index-right"):
                final_label = "index-right"
                action = "FORWARD"
                pyautogui.press('nexttrack', presses=1)
            elif (prediction[0][0] == "index-left"):
                final_label = "index-left"
                action = "REWIND"
                pyautogui.press('prevtrack', presses=1)
            elif (prediction[0][0] == "no-gesture"):
                final_label = "no-gesture"
                action = "NO-ACTION"
            text1= "Gesture: {}".format(final_label)
            text2= "Action:{}".format(action)
                # Displaying the predictions
            cv2.putText(frame, text1 , (10, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
            cv2.putText(frame, text2 , (10, 220), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 1)
            FRAME_WINDOW2.image(frame)
        camera.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
