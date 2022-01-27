# Controlling Media Player with Hand Gestures using Convolutional Neural Network

## Kindly go through our Research Paper published by IEEE on this project for more information and cite it in your projects
## https://ieeexplore.ieee.org/document/9641567

## Contact Me on Linkedin: https://www.linkedin.com/in/gayathri1462/

### A Web Application to control media player using Hand gestures (Using Streamlit)

The primary aim is to use the most natural form, i.e., hand gestures to interact with the computer system. The goal of this project is to create a web application that uses your device's camera to give you touch-free and remote-free control over any media player application (with no special hardware). It would implement these gestures such that they are easy to perform, fast, efficient, and ensure an immediate response. It increases your productivity and makes your life easier and comfortable by letting you control your device from a distance.

The proposed system can control the media player from a distance using hand gestures. 
1. OpenCV is used to collect raw images and convert them to black and white images for dataset creation. 
2. Two Dimensional Convolutional Neural Network is built for feature extraction and classification.
3. The PyAutoGUI library is used to integrate the Keyboard keys to hand gestures 
4. A user interface is created using the Streamlit web framework 
5. A webpage is deployed which contains source files and demo using streamlit.io sharing.


![alt text](https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/cam%20page.png?raw=true)

#### Web App link: 

https://share.streamlit.io/gayathri1462/hand-gesture-recognition-streamlit/main/webapp.py

#### System Design Flow: 
<img src="https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/design.png?raw=true.type" width="500" height="400">

#### Data collection and preprocessing using OpenCV: 

<img src="https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/data-collection.png?raw=true.type" width="500" height="400">

**Gestures obtained after Data collection and preprocessing**:
Palm, fist, thumbs up, thumbs down, index pointing right, index pointing left and no gesture (Left to right)

![alt text](https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/gestures.png?raw=true)

#### Architecture of trained CNN model: 
<img src="https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/CNNlayers.png?raw=true.type" width="300" height="300">

#### Results: 
<img src="https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/results.png?raw=true.type" width="400" height="400">

#### Performance Evalutaion:
<img src="https://github.com/gayathri1462/Controlling-Media-Player-with-Hand-Gestures-using-Convolutional-Neural-Network/blob/main/images/Confusion%20matrix.png?raw=true.type" width="400" height="400">


