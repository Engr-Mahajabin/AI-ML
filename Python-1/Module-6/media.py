import streamlit as st

# Image:
image = st.file_uploader("Enter your image",type=['jpg','jpeg','png'])
print(type(image))
if image:
    st.image(image)


if image:
    col = st.columns(len(image))
    for i, per_image in enumerate(image):
        with col[i]:
            st.image(per_image)


# Audio_file:
audio_file = st.file_uploader("Enter your audio",type=['mp3','ogg','flac'])
print(type(audio_file))
if audio_file:
    st.stdio(audio_file)


# Video_file:
video_file = st.file_uploader("Enter your video",type=['mp4','mkv'])
button = st.button("Click to upload")
if button:
    if video_file:
        st.video(video_file)
        st.success("Your file is uploaded successfully")
    else:
        st.error("You must upload a file")
        
