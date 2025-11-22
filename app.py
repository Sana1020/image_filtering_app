import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

#### FILTER FUNCTIONS ________________
def black_and_white(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    return img_gray

def Brightness(img, level):
    img_gray = cv2.convertScaleAbs(img, beta=level)
    return img_gray

def Style(img,sigma_s,sigma_r):
    blur_img = cv2.GaussianBlur(img,(5,5),0)
    stylized_img = cv2.stylization(blur_img, sigma_s=sigma_s, sigma_r=sigma_r)
    return stylized_img

def Vintage(img,level):
    hight , width = img.shape[:2]
    x_kerenl = cv2.getGaussianKernel(width,width/level) #1d kernel
    y_kerenl = cv2.getGaussianKernel(hight,hight/level) #1d kernel
    
    kernel = x_kerenl.T *y_kerenl #2d kernel
    mask = kernel/kernel.max() #normalize

    Vintage_img = np.copy(img)
    for i in range(3): # loop on each channel (R,G,B)
        Vintage_img[:,:,i] = Vintage_img[:,:,i]*mask
    return Vintage_img

def HDR(img,level,sigma_s,sigma_r):
    Brightness_img = cv2.convertScaleAbs(img, beta=level)
    hdr_img = cv2.detailEnhance(Brightness_img, sigma_s=sigma_s, sigma_r=sigma_r)
    return hdr_img

### APP________________________
st.title("Image Filtering App with OpenCV")
uploaded_file = st.file_uploader('Upload Image',type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = np.array(img)
    
    og_img , output_img = st.columns(2)
    
    with og_img:
        st.header("Original Image")
        st.image(img)
        
    st.header('List of Filters')
    filter_option = st.selectbox('Select Filter', 
                                 ('None', 'Black and White', 'Brightness', 'Style', 'Vintage','HDR'))
    
   
    color = 'BGR'
    output_flag = 1
    
    
    if filter_option == 'None':
        output_flag = 1
        output = img
        
    elif filter_option == 'Black and White':
        output = black_and_white(img)
        color = 'GRAY'
    
    
    elif filter_option == 'Brightness':
        level = st.slider('Select Brightness Level', -50, 50, 10, step=5)
        output = Brightness(img, level)
    
    
    elif filter_option == 'Style':
        sigma_s = st.slider('Select Sigma S', 0, 200, 60, step=10)
        sigma_r = st.slider('Select Sigma R', 0.0, 1.0, 0.45, step=0.05)
        output = Style(img, sigma_s, sigma_r)
    
    
    elif filter_option == 'Vintage':
        level = st.slider('Select Vintage Level', 0, 5, 3, step=1)
        output = Vintage(img, level)
    
    
    elif filter_option == 'HDR':
        level = st.slider('Select Brightness Level', -50, 50, 10, step=5)
        sigma_s = st.slider('Select Sigma S', 0, 200, 60, step=10)
        sigma_r = st.slider('Select Sigma R', 0.0, 1.0, 0.45, step=0.05)
        output = HDR(img, level, sigma_s, sigma_r)
    
    with output_img:
        st.header("Filtered Image")
        if color == 'GRAY':
            st.image(output, channels='GRAY')
        else:
            st.image(output,channels='RGB')