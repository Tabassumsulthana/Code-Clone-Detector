import streamlit as st
import backend

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Code Clone Detector",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------
# CUSTOM CSS DESIGN
# --------------------------------

st.markdown("""
<style>

/* REMOVE TOP WHITE HEADER STRIP */

header[data-testid="stHeader"],
[data-testid="stDecoration"],
[data-testid="stToolbar"],
hr {
    display: none !important;
    height: 0px !important;
    visibility: hidden !important;
}

/* REMOVE TOP EMPTY SPACE */

.stAppViewContainer {
    padding-top: 0px !important;
    margin-top: 0px !important;
}

.stAppViewBlockContainer,
div[data-testid="stMainBlockContainer"],
.block-container,
section.main {
    padding-top: 0px !important;
    margin-top: 0px !important;
}

/* GLOBAL BACKGROUND */

html, body, .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background: linear-gradient(
        135deg,
        #DEF5F8 0%,
        #FADCEE 100%
    ) !important;
    background-attachment: fixed !important;
}

/* REMOVE DEFAULT CONTAINER BACKGROUNDS */

[data-testid="stMain"],
[data-testid="stAppViewContainer"],
[data-testid="stMainBlockContainer"] {
    background: transparent !important;
}

/* CENTERED HEADER CARD */

.centered-header-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
    padding: 15px 20px 25px !important;
    margin: 0 auto 20px !important;
    background: rgba(255,255,255,0.45);
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.6);
    box-shadow: 0 4px 30px rgba(0,0,0,0.03);
}

/* MAIN APPLICATION HEADING */

.main-heading {
    color: #585B7A !important;
    font-size: 60px !important;
    font-weight: 800 !important;
    margin: 0px 0px 14px 0px !important;
    letter-spacing: -1px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.06);
}

/* SUB HEADING */

.sub-heading-sentence {
    color: #C070C5 !important;
    font-size: 24px !important;
    font-weight: 700 !important;
    margin: 0px !important;
}

/* COLUMN SPACING */

.column-wrapper {
    margin-top: 30px !important;
    margin-bottom: 25px !important;
}

/* UPLOADER HEADINGS */

.column-title-sentence {
    color: #1FB3B7 !important;
    font-size: 26px !important;
    font-weight: 800 !important;
    margin-bottom: 18px !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.03);
}

/* RESULTS HEADING */

.results-section-heading {
    color: #C070C5 !important;
    font-size: 36px !important;
    font-weight: 800 !important;
    margin-top: 45px !important;
    margin-bottom: 20px !important;
}

/* SCAN BUTTON */

div.stButton > button:first-child {
    background: linear-gradient(
        135deg,
        #FFAB73 0%,
        #FF884D 100%
    ) !important;

    color: #FFFFFF !important;
    border: none !important;
    font-size: 22px !important;
    font-weight: 800 !important;
    padding: 18px 45px !important;
    border-radius: 14px !important;
    width: 100% !important;
    box-shadow: 0 8px 20px rgba(255,136,77,0.35);
    transition: all 0.25s ease-in-out !important;
    cursor: pointer;
    margin-top: 40px !important;
}

/* BUTTON HOVER EFFECT */

div.stButton > button:first-child:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(255,136,77,0.5) !important;
}

/* UPLOADER BOX DESIGN */

div[data-testid="stFileUploader"] section {
    background-color: #FFFFFF !important;
    border: 3px dashed #1FB3B7 !important;
    border-radius: 14px !important;
    padding: 20px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
}

/* UPLOADER HOVER EFFECT */

div[data-testid="stFileUploader"] section:hover {
    border-color: #C070C5 !important;
}

/* FILE UPLOADER TEXT */

div[data-testid="stFileUploader"] {
    color: #585B7A !important;
}

/* CODE TITLE TAG */

.code-title-tag {
    background-color: rgba(31,179,183,0.15);
    color: #585B7A;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 700;
    display: inline-block;
    margin-bottom: 12px;
    border: 2px solid rgba(31,179,183,0.4);
}

/* RESULT CONTAINERS */

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.75);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.8);
}

/* RESPONSIVE HEADING */

@media screen and (max-width: 768px) {
    .main-heading {
        font-size: 36px !important;
    }

    .sub-heading-sentence {
        font-size: 17px !important;
    }

    .column-title-sentence {
        font-size: 20px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# VISUAL UI HEADER
# --------------------------------


st.markdown(
    '<div class="centered-header-block">'
    '<h1 class="main-heading">🔵 Code Clone Detector</h1>'
    '<p class="sub-heading-sentence">'
    'Upload two source files below to execute '
    'dynamic structural analysis algorithms.'
    '</p>'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------
# UPLOADER SECTIONS LAYOUT
# --------------------------------

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown(
        '<p class="column-title-sentence">Primary Script File</p>',
        unsafe_allow_html=True
    )

    uploaded_file1 = st.file_uploader(
        "Upload primary source target",
        type=["py"],
        key="ui_file1",
        label_visibility="collapsed"
    )


with col2:

    st.markdown(
        '<p class="column-title-sentence">Secondary Script File</p>',
        unsafe_allow_html=True
    )

    uploaded_file2 = st.file_uploader(
        "Upload reference evaluation asset",
        type=["py"],
        key="ui_file2",
        label_visibility="collapsed"
    )


# --------------------------------
# SCAN TRIGGER BUTTON
# --------------------------------

run_trigger = st.button(
    "🚀 Execute Structural Similarity Scan Check",
    type="primary",
    use_container_width=True
)


# --------------------------------
# RUNTIME BACKEND HANDSHAKE
# --------------------------------

if run_trigger:

    if uploaded_file1 is not None and uploaded_file2 is not None:

        try:

            # READ UPLOADED FILES

            raw_code_data1 = uploaded_file1.getvalue().decode("utf-8")
            raw_code_data2 = uploaded_file2.getvalue().decode("utf-8")

            # CALCULATE SIMILARITY

            calculated_score = backend.calculate_similarity(
                raw_code_data1,
                raw_code_data2
            )

            # --------------------------------
            # RENDER RESULTS LAYOUT
            # --------------------------------

            st.markdown(
                '<h2 class="results-section-heading">'
                '📊 Evaluation Report</h2>',
                unsafe_allow_html=True
            )

            # DISPLAY SIMILARITY SCORE

            st.metric(
                label="Structural Similarity Score",
                value=f"{calculated_score:.2f}%"
            )

            # --------------------------------
            # RESULT CLASSIFICATION
            # --------------------------------

            if calculated_score >= 70.0:

                st.error(
                    f"⚠️ Structural Congruence Warning: "
                    f"Match Matrix registered at "
                    f"{calculated_score:.2f}%"
                )

                st.warning(
                    "Assessment Warning: High probability "
                    "of logical duplication/plagiarism identified."
                )

            else:

                st.success(
                    f"✅ Structural Originality Verified: "
                    f"Match Matrix registered at "
                    f"{calculated_score:.2f}%"
                )

                st.info(
                    "Assessment Clearance: Source script items "
                    "demonstrate relatively low structural similarity."
                )

            # --------------------------------
            # CODE INSPECTOR PREVIEW PANEL
            # --------------------------------

            st.markdown(
                '<h2 class="results-section-heading">'
                '🔬 Granular Workspace Inspection</h2>',
                unsafe_allow_html=True
            )

            view_col1, view_col2 = st.columns(2)

            with view_col1:

                st.markdown(
                    f'<span class="code-title-tag">'
                    f'Target Reference A: {uploaded_file1.name}'
                    f'</span>',
                    unsafe_allow_html=True
                )

                st.code(
                    raw_code_data1,
                    language="python"
                )

            with view_col2:

                st.markdown(
                    f'<span class="code-title-tag">'
                    f'Target Reference B: {uploaded_file2.name}'
                    f'</span>',
                    unsafe_allow_html=True
                )

                st.code(
                    raw_code_data2,
                    language="python"
                )

        except UnicodeDecodeError:

            st.error(
                "Unable to read the uploaded files. "
                "Please upload valid UTF-8 Python files."
            )

        except Exception as e:

            st.error(
                f"An unexpected error occurred: {e}"
            )

    else:

        st.error(
            "⚠️ Operation Aborted: Please upload both "
            "Python files before starting scan execution."
        )
