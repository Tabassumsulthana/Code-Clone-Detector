import streamlit as st
import backend  # Connects directly to your backend calculation engine

# --- PAGE SETUP ---
st.set_page_config(page_title="Code Clone Detector", layout="wide")

# --- ABSOLUTE GLOBAL CSS OVERHAUL TO REMOVE ALL CONTAINER BACKGROUNDS & LINES ---
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* 🎯 REMOVES THE TOP WHITE LINE AND STRUCTURAL MARGINS */
    header[data-testid="stHeader"], [data-testid="stDecoration"], hr {
        display: none !important;
        height: 0px !important;
    }
    .stAppViewBlockContainer {
        padding-top: 0rem !important;
    }
    div[data-testid="stMainView"] > div:nth-child(1) {
        border-bottom: none !important;
        background: transparent !important;
    }
    
    /* 🛑 GLOBAL ACCENT RESET: Forces every layer to inherit your marble backdrop gradient */
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    html, body, .stApp, [data-testid="stMainView"], [data-testid="stAppViewContainer"], .main {
        background: linear-gradient(135deg, #DEF5F8 0%, #FADCEE 100%) !important;
        background-attachment: fixed !important;
    }
    
    /* Removes default inner block color fragments and lines */
    div.block-container, [data-testid="stVerticalBlock"], [data-testid="stMainView"] {
        background-color: transparent !important;
        background: transparent !important;
    }
    
    /* Centered Header Section Glassmorphism Layout Card */
    .centered-header-block {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding: 40px 20px;
        background: rgba(255, 255, 255, 0.45);
        border-radius: 16px;
        margin-top: 20px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03);
    }
    
    /* Main Heading: High-visibility solid Mineral Purple-Slate */
    .main-heading {
        color: #585B7A !important; 
        font-size: 60px !important;
        font-weight: 800 !important;
        margin: 0px 0px 14px 0px !important;
        letter-spacing: -1px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.06);
    }
    
    /* Sub-heading Sentence: Vivid Fuchsia Orchid */
    .sub-heading-sentence {
        color: #C070C5 !important; 
        font-size: 24px !important;
        font-weight: 700 !important;
        margin: 0px !important;
    }
    
    .column-wrapper {
        margin-top: 30px !important;
        margin-bottom: 25px !important;
    }
    
    /* Column Headings: High-contrast Vivid Cyan/Teal */
    .column-title-sentence {
        color: #1FB3B7 !important; 
        font-size: 26px !important;
        font-weight: 800 !important;
        margin-bottom: 18px !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.03);
    }
    
    .results-section-heading {
        color: #C070C5 !important;
        font-size: 36px !important;
        font-weight: 800 !important;
        margin-top: 45px !important;
        margin-bottom: 20px !important;
    }
    
    /* 🚀 Highly Saturated Interactive Button (Vivid Peach Gradient) */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FFAB73 0%, #FF884D 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        padding: 18px 45px !important;
        border-radius: 14px !important;
        width: 100% !important;
        box-shadow: 0 8px 20px rgba(255, 136, 77, 0.35) !important;
        transition: all 0.25s ease-in-out !important;
        cursor: pointer;
        margin-top: 40px !important;
    }
    
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 28px rgba(255, 136, 77, 0.5) !important;
    }
    
    .code-title-tag {
        background-color: rgba(31, 179, 183, 0.15);
        color: #585B7A;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 12px;
        border: 2px solid rgba(31, 179, 183, 0.4);
    }
    
    /* Solid high-contrast opaque white boxes for uploaders */
    div[data-testid="stFileUploader"] section {
        background-color: #FFFFFF !important;
        border: 3px dashed #1FB3B7 !important;
        border-radius: 14px !important;
        padding: 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    }
    
    div[data-testid="stFileUploader"] section:hover {
        border-color: #C070C5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- VISUAL UI HEADER ---
st.markdown('<div class="centered-header-block">', unsafe_allow_html=True)
st.markdown('<h1 class="main-heading">🛡️ Code Clone Detector</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-heading-sentence">Upload two source files below to execute dynamic structural analysis algorithms.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- UPLOADER SECTIONS LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="column-title-sentence">Primary Script File</p>', unsafe_allow_html=True)
    uploaded_file1 = st.file_uploader("Upload primary source target", type=["py"], key="ui_file1", label_visibility="collapsed")

with col2:
    st.markdown('<p class="column-title-sentence">Secondary Script File</p>', unsafe_allow_html=True)
    uploaded_file2 = st.file_uploader("Upload reference evaluation asset", type=["py"], key="ui_file2", label_visibility="collapsed")

# --- SCAN TRIGGER BUTTON ---
run_trigger = st.button("🚀 Execute Structural Similarity Scan Check", type="primary")

# --- RUNTIME BACKEND HANDSHAKE ---
if run_trigger:
    if uploaded_file1 is not None and uploaded_file2 is not None:
        raw_code_data1 = uploaded_file1.read().decode("utf-8")
        raw_code_data2 = uploaded_file2.read().decode("utf-8")
        
        calculated_score = backend.calculate_similarity(raw_code_data1, raw_code_data2)
        
        # --- RENDER RESULTS LAYOUT ---
        st.markdown('<h2 class="results-section-heading">📊 Evaluation Report</h2>', unsafe_allow_html=True)
        
        if calculated_score >= 70.0:
            st.error(f"⚠️ Structural Congruence Warning: Match Matrix registered at {calculated_score}%")
            st.warning("Assessment Warning: High probability of logical duplication/plagiarism identified.")
        else:
            st.success(f"✅ Structural Originality Verified: Match Matrix registered at {calculated_score}%")
            st.info("Assessment Clearance: Source script items demonstrate safe separate logic variants.")
            
        # --- CODE INSPECTOR PREVIEW PANEL ---
        st.markdown('<h2 class="results-section-heading" style="color: #585B7A;">🕵️ Granular Workspace Inspection</h2>', unsafe_allow_html=True)
        view_col1, view_col2 = st.columns(2)
        
        with view_col1:
            st.markdown(f'<span class="code-title-tag">Target Reference A: {uploaded_file1.name}</span>', unsafe_allow_html=True)
            st.code(raw_code_data1, language="python")
            
        with view_col2:
            st.markdown(f'<span class="code-title-tag">Target Reference B: {uploaded_file2.name}</span>', unsafe_allow_html=True)
            st.code(raw_code_data2, language="python")
    else:
        st.error("Operation Aborted: Please ensure both file components contain loaded source items prior to starting scan execution.")
