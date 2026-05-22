import streamlit as st
from filters import (
    apply_blur,
    apply_sharpness,
    apply_brightness,
    apply_contrast,
    apply_grayscale,
    apply_edge_detection
)

from utils import (
    load_image,
    image_to_bytes
)

# PAGE CONFIG
st.set_page_config(
    page_title="AI Image Editor",
    page_icon="🎨",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

/* MAIN BACKGROUND */
.main {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

/* REMOVE STREAMLIT HEADER */
header {
    visibility: hidden;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #1d4ed8;
    font-weight: 600;
    margin-bottom: 30px;
}

/* LIGHT SIDEBAR */
section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 2px solid #e2e8f0;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* SLIDER LABELS */
.stSlider label {
    color: black !important;
    font-weight: 600;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px dashed #38bdf8;
}

/* IMAGE CARDS */
.image-card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.3);
}

/* BUTTONS */
.stButton button {
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
}

.stDownloadButton button {
    background: linear-gradient(90deg,#22c55e,#16a34a);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
}

/* IMAGE TITLES */
h3 {
    color: white !important;
    text-align: center;
}

/* MAIN CONTAINER */
.block-container {
    padding-top: 2rem;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<div class='title'>🎨 AI Image Editor</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Modern Image Processing App using Streamlit & OpenCV</div>",
    unsafe_allow_html=True
)

# SIDEBAR
st.sidebar.title("⚙️ Image Controls")

blur_value = st.sidebar.slider(
    "Blur",
    1,
    51,
    1,
    step=2
)

sharpness = st.sidebar.slider(
    "Sharpness",
    0.0,
    3.0,
    1.0
)

brightness = st.sidebar.slider(
    "Brightness",
    -100,
    100,
    0
)

contrast = st.sidebar.slider(
    "Contrast",
    0.5,
    3.0,
    1.0
)

grayscale = st.sidebar.checkbox("Grayscale")

edge_detect = st.sidebar.checkbox("Edge Detection")

# RESET BUTTON
if st.sidebar.button("Reset Filters"):
    st.rerun()

# FILE UPLOADER
uploaded_file = st.file_uploader(
    "📤 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    # LOAD IMAGE
    image = load_image(uploaded_file)

    processed_image = image.copy()

    # APPLY FILTERS
    processed_image = apply_blur(
        processed_image,
        blur_value
    )

    processed_image = apply_sharpness(
        processed_image,
        sharpness
    )

    processed_image = apply_brightness(
        processed_image,
        brightness
    )

    processed_image = apply_contrast(
        processed_image,
        contrast
    )

    if grayscale:
        processed_image = apply_grayscale(
            processed_image
        )

    if edge_detect:
        processed_image = apply_edge_detection(
            processed_image
        )

    # IMAGE DISPLAY
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            "<div class='image-card'>",
            unsafe_allow_html=True
        )

        st.subheader("🖼️ Original Image")

        st.image(
            image,
            use_container_width=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            "<div class='image-card'>",
            unsafe_allow_html=True
        )

        st.subheader("✨ Processed Image")

        st.image(
            processed_image,
            use_container_width=True
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    # DOWNLOAD BUTTON
    image_bytes = image_to_bytes(processed_image)

    st.download_button(
        label="⬇️ Download Edited Image",
        data=image_bytes,
        file_name="edited_image.png",
        mime="image/png"
    )

# FOOTER
st.markdown(
    "<div class='footer'>Built with ❤️ using Streamlit & OpenCV</div>",
    unsafe_allow_html=True
)