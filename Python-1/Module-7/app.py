import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

# Titles:
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzess")
st.divider()

# Sidebar:
with st.sidebar:
    st.header("Contents")

    # Images:
    images = st.file_uploader(
        "Upload the photos of your note",
        type = ['png','jpeg','jpg'],
        accept_multiple_files=True
    )

    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images) > 3:
            st.error("Upload to max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded images")

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    
    # Difficulties:
    selected_option = st.selectbox(
        "Enter your difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None    
    )

    # if selected_option:
    #     st.markdown(f"You selected {selected_option} as dificulty of your quiz")
    # else: 
    #     st.error("You must select a difficulty")
    # st.button("Click the button to initiate",type="primary")

    pressed = st.button("Click the button to initiate",type="primary")

if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select an option")
    if images and selected_option:
        # Note:
        with st.container(border=True):
            st.subheader("Your Note")
            # The portion below will be replaced by API call:
            # st.text("Note will be shown here")
            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        # Audio transcript:
        with st.container(border=True):
            st.subheader("Audio Transcription")
            # st.text("Audio transcription will be shown here")
            generated_notes = generated_notes.replace("#","")
            generated_notes = generated_notes.replace("*","")
            generated_notes = generated_notes.replace("-","")
            generated_notes = generated_notes.replace(".","")
            generated_notes = generated_notes.replace("","")

            with st.spinner("AI is transcripting audio for you"):
                audio_transcript = audio_transcription(generated_notes)
                st.audio("Audio transcript will be shown here")

        # Quiz:
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            # st.text("Your quiz will be here")
            with st.spinner("AI is generating quizzes for you"):
                quizzes = quiz_generator(pil_images,selected_option)
                st.markdown("quizzes")
