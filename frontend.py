import streamlit as st
import backend  # Hooks seamlessly into your backend engine

# --- PAGE SETUP ---
st.set_page_config(page_title="Code Clone Detector", layout="wide")

# --- CUSTOM CSS FOR PERFECT CENTERING AND SPACING ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global Canvas Reset */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #FAFAFB !important;
    }
    
    .stApp {
        background-color: #FAFAFB;
    }
    
    /* 🎯 Perfect Center Container for Heading */
    .centered-header-block {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding: 50px 0px 40px 0px; /* Expands top space */
    }
    
    .main-heading {
        color: #388CC9; /* Vibrant Theme Teal/Blue */
        font-size: 56px !important; /* Prominent font sizing */
        font-weight: 800 !important;
        margin: 0px 0px 18px 0px !important; /* 18px separation gap below heading */
        letter-spacing: -1px;
    }
    
    .sub-heading-sentence {
        color: #E7B7CB; /* Muted Soft Rose */
        font-size: 22px !important;
        font-weight: 500 !important;
        margin: 0px !important;
    }
    
    /* ↕️ Generous Spacing for Input Blocks */
    .column-wrapper {
        margin-top: 30px !important; /* Adds clear distance below sub-heading */
        margin-bottom: 25px !important;
    }
    
    .column-title-sentence {
        color: #47CACC; /* Bright Soft Teal Accent */
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 16px !important; /* Space between text line and file input container */
    }
    
    .results-section-heading {
        color: #CD85D4; /* Pastel Purple */
        font-size: 34px !important;
        font-weight: 700 !important;
        margin-top: 45px !important; /* Large distance break above results section */
        margin-bottom: 20px !important;
    }
    
    /* 🚀 Action Button Alignment and Spacing */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FFB380 0%, #FFA266 100%) !important; /* Peach Gradient */
        color: #FFFFFF !important;
        border: none !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 16px 40px !important;
        border-radius: 12px !important;
        width: 100% !important;
        box-shadow: 0 6px 20px rgba(255, 179, 128, 0.35) !important;
        transition: all 0.25s ease-in-out !important;
        cursor: pointer;
        margin-top: 40px !important; /* Generous breathing room above the execution button */
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 179, 128, 0.5) !important;
    }
    
    .code-title-tag {
        background-color: rgba(71, 202, 204, 0.08);
        color: #388CC9;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 15px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
        border: 1px solid rgba(71, 202, 204, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- VISUAL UI HEADER (Centered perfectly via CSS flex) ---
st.markdown('<div class="centered-header-block">', unsafe_allow_html=True)
st.markdown('<h1 class="main-heading">🛡️ Code Clone Detector</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-heading-sentence">Upload two source files below to execute dynamic structural analysis algorithms.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- UPLOADER SECTIONS LAYOUT (Wrapped inside layout container constraints) ---
st.markdown('<div class="column-wrapper">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="column-title-sentence">📁 Primary Script File</p>', unsafe_allow_html=True)
    uploaded_file1 = st.file_uploader("Upload primary source target", type=["py"], key="ui_file_1", label_visibility="collapsed")

with col2:
    st.markdown('<p class="column-title-sentence">📁 Secondary Script File</p>', unsafe_allow_html=True)
    uploaded_file2 = st.file_uploader("Upload secondary source target", type=["py"], key="ui_file_2", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Scan execution button
run_trigger = st.button("🚀 Execute Structural Similarity Scan Check", type="primary")

# --- RUNTIME BACKEND RUNTIME PROCESS ---
if run_trigger:
    if uploaded_file1 is not None and uploaded_file2 is not None:
        
        # Read byte lines from uploaded objects
        raw_code_data1 = uploaded_file1.read().decode("utf-8")
        raw_code_data2 = uploaded_file2.read().decode("utf-8")
        
        # Ingest inputs into backend computation framework
        calculated_score = backend.calculate_similarity(raw_code_data1, raw_code_data2)
        
        # RENDER RESULTS LAYOUT
        st.markdown('<h2 class="results-section-heading">📊 Evaluation Report</h2>', unsafe_allow_html=True)
        
        if calculated_score >= 70.0:
            st.error(f"⚠️ Structural Congruence Warning: Match Matrix registered at {calculated_score}%")
            st.warning("Assessment Warning: High probability of logical duplication/plagiarism identified.")
        else:
            st.success(f"✅ Structural Originality Verified: Match Matrix registered at {calculated_score}%")
            st.info("Assessment Clearance: Source script items demonstrate safe separate logic variants.")
            
        # CODE INSPECTOR PREVIEW PANEL
        st.markdown('<h2 class="results-section-heading" style="color: #47CACC;">🔍 Granular Workspace Inspection</h2>', unsafe_allow_html=True)
        view_col1, view_col2 = st.columns(2)
        
        with view_col1:
            st.markdown(f'<span class="code-title-tag">Target Reference A: {uploaded_file1.name}</span>', unsafe_allow_html=True)
            st.code(raw_code_data1, language="python")
            
        with view_col2:
            st.markdown(f'<span class="code-title-tag">Target Reference B: {uploaded_file2.name}</span>', unsafe_allow_html=True)
            st.code(raw_code_data2, language="python")
        
    else:
        st.error("Operation Aborted: Please ensure both file components contain loaded source items prior to starting scan execution.")