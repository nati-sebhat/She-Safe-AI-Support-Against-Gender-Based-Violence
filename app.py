# app.py – She Safe GBV Chatbot
import streamlit as st
import os
from assistant import get_response, get_safety_tips, get_coping_strategies
from questionnaire import QUESTIONNAIRE

# --- Page Settings ---
st.set_page_config(
    page_title="She Safe – GBV Support",
    page_icon="🦋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for dark mode styling ---
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        background-color: #0e1117;
        color: #fafafa;
    }
    
    .panic-button {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 999;
    }
    
    .emergency-section {
        background-color: #2d1b1b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
        margin: 20px 0;
        color: #fafafa;
    }
    
    .support-message {
        background-color: #1b2d1b;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4caf50;
        margin: 15px 0;
        color: #fafafa;
    }
    
    .warning-text {
        color: #ff6b6b;
        font-weight: bold;
    }
    
    .help-text {
        color: #b0b0b0;
        font-style: italic;
        font-size: 14px;
    }
    
    /* Force dark theme elements */
    .stButton > button {
        background-color: #e07a5f;
        color: white;
        border: none;
        border-radius: 8px;
    }
    
    .stTextInput > div > div > input {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #404040;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #404040;
    }
    
    .stSelectbox > div > div > select {
        background-color: #262730;
        color: #fafafa;
        border: 1px solid #404040;
    }
    
    .stRadio > div {
        background-color: transparent;
        color: #fafafa;
    }
    
    /* Chat message styling for dark mode */
    .stChatMessage {
        background-color: #262730;
        color: #fafafa !important;
    }
    
    /* AI assistant message styling - white text */
    .stChatMessage[data-testid="chatAvatarIcon-assistant"] {
        background-color: #262730;
        color: #ffffff !important;
    }
    
    .stChatMessage[data-testid="chatAvatarIcon-assistant"] .stMarkdown {
        color: #ffffff !important;
    }
    
    .stChatMessage[data-testid="chatAvatarIcon-assistant"] p {
        color: #ffffff !important;
    }
    
    /* User message styling */
    .stChatMessage[data-testid="chatAvatarIcon-user"] {
        background-color: #1a1a1a;
        color: #ffffff !important;
    }
    
    .stChatMessage[data-testid="chatAvatarIcon-user"] .stMarkdown {
        color: #ffffff !important;
    }
    
    .stChatMessage[data-testid="chatAvatarIcon-user"] p {
        color: #ffffff !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #262730;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #262730;
        color: #fafafa;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #262730;
        color: #fafafa;
    }
    
    /* Header/Toolbar styling - wine red background */
    .stApp > header {
        background-color: #722F37 !important;
    }
    
    header[data-testid="stHeader"] {
        background-color: #722F37 !important;
        height: 3rem;
    }
    
    .stApp > header, .stApp header {
        background-color: #722F37 !important;
    }
    
    /* Three dots menu styling */
    button[data-testid="baseButton-headerNoPadding"] {
        color: #fafafa !important;
    }
    
    /* Top toolbar background */
    .stToolbar {
        background-color: #722F37 !important;
    }
    
    /* Fix all text visibility issues */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #fafafa !important;
    }
    
    /* Form labels and text */
    .stFormSubmitButton, label, .stRadio label, .stCheckbox label, .stSelectbox label, .stTextInput label, .stTextArea label {
        color: #fafafa !important;
    }
    
    /* Tab content text */
    .stTabs [data-baseweb="tab-panel"] {
        color: #fafafa !important;
    }
    
    /* Expander content */
    .streamlit-expanderContent {
        background-color: #262730;
        color: #fafafa !important;
    }
    
    /* Success/error/warning messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        color: #fafafa !important;
    }
    
    /* General text elements */
    div, span, p, li, ul, ol {
        color: #fafafa !important;
    }
    
    /* Strong text elements */
    strong, b, em, i {
        color: #ffffff !important;
    }
    
    /* Ensure all chat input text is visible */
    .stChatInput textarea {
        background-color: #262730 !important;
        color: #fafafa !important;
        border: 1px solid #404040 !important;
    }
    
    /* Spinner text */
    .stSpinner {
        color: #fafafa !important;
    }
    
    /* Code blocks */
    code, pre {
        background-color: #1a1a1a !important;
        color: #fafafa !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Panic Button (Always Visible) ---
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🚨 Quick Exit", help="Leave immediately", type="primary"):
        st.markdown("""
            <script>
            window.open('https://www.google.com', '_self');
            </script>
        """, unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("assets/logo.png", width=100)
    except:
        st.markdown("🦋")
with col2:
    st.title("She Safe – AI Support Against GBV")
    st.markdown("**A confidential, safe, and supportive space for survivors and allies.**")

# Welcome message with supportive image
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="support-message">
    💝 <strong>You are not alone.</strong> This is a safe space where you can find support, resources, and guidance. 
    Your privacy and safety are our top priorities.
    </div>
    """, unsafe_allow_html=True)
with col2:
    try:
        st.image("assets/4.png", width=200, caption="")
    except:
        pass

# --- Emergency Support Section ---
st.markdown("""
<div class="emergency-section">
<h3>🚨 Emergency Support</h3>
<p class="warning-text">If you are in immediate danger, please contact local authorities immediately:</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **🇪🇹 Ethiopia**
    - **Police:** 991
    - **Ambulance:** 907
    - **Women & Children Hotline:** 978
    """)

with col2:
    st.markdown("""
    **🇨🇲 Cameroon**
    - **Police:** 117
    - **Ambulance:** 112
    - **Gender Violence Hotline:** 1521
    """)

st.markdown("</div>", unsafe_allow_html=True)

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat with She Safe", "📋 Assessment", "🛡️ Safety Resources", "💪 Mental Health"])

# --- Chat Tab ---
with tab1:
    st.subheader("Talk to She Safe")
    st.markdown("Share your concerns, ask questions, or just talk. She Safe is here to listen and provide guidance.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("She Safe is thinking..."):
                response = get_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- Assessment Tab ---
with tab2:
    st.subheader("Confidential Assessment")
    st.markdown("""
    <p class="help-text">This assessment helps She Safe understand your situation better to provide more targeted support. 
    All responses are confidential and not stored permanently.</p>
    """, unsafe_allow_html=True)
    
    # Initialize session state for questionnaire
    if "questionnaire_responses" not in st.session_state:
        st.session_state.questionnaire_responses = {}
    
    with st.form("gbv_assessment"):
        for section, questions in QUESTIONNAIRE.items():
            st.markdown(f"**{section}**")
            for i, question in enumerate(questions):
                key = f"{section}_{i}"
                if "Yes / No" in question:
                    response = st.radio(question, ["Select an option", "Yes", "No"], key=key)
                elif "Type of GBV:" in question:
                    response = st.selectbox(
                        question, 
                        ["Select type", "Physical", "Emotional", "Sexual", "Digital", "Economic", "Other"],
                        key=key
                    )
                elif "perpetrator" in question:
                    response = st.selectbox(
                        question,
                        ["Select option", "Partner", "Family", "Stranger", "Authority", "Other"],
                        key=key
                    )
                elif "Where does it occur" in question:
                    response = st.selectbox(
                        question,
                        ["Select location", "Home", "Work", "School", "Online", "Public"],
                        key=key
                    )
                else:
                    response = st.text_area(question, key=key, height=60)
                
                st.session_state.questionnaire_responses[key] = response
            st.markdown("---")
        
        submitted = st.form_submit_button("Submit Assessment")
        
        if submitted:
            # Process the assessment (in a real app, you might want to analyze this)
            st.success("Assessment completed. She Safe will use this information to provide better support.")
            
            # Generate personalized response based on assessment
            assessment_summary = "Based on your assessment: "
            critical_responses = []
            
            for key, response in st.session_state.questionnaire_responses.items():
                if response == "Yes" and ("immediate danger" in key or "not feel safe" in key):
                    critical_responses.append("immediate safety concerns")
            
            if critical_responses:
                st.error("⚠️ **Immediate Safety Concern Detected**")
                st.markdown("""
                Based on your responses, you may be in immediate danger. Please consider:
                - Contacting emergency services immediately
                - Reaching out to a trusted friend or family member
                - Having an emergency exit plan ready
                """)

# --- Safety Resources Tab ---
with tab3:
    st.subheader("Safety Resources & Tips")
    
    # Add "Break the Silence" imagery
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("assets/5.png", width=300, caption="")
        except:
            pass
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🛡️ Get Safety Tips"):
            st.markdown(get_safety_tips())
    
    with col2:
        if st.button("📚 Educational Resources"):
            st.markdown("""
            **Understanding GBV:**
            
            📖 **Types of Gender-Based Violence:**
            - **Physical:** Hitting, slapping, pushing, or any physical harm
            - **Emotional/Psychological:** Threats, humiliation, controlling behavior
            - **Sexual:** Any non-consensual sexual activity or coercion
            - **Digital:** Online harassment, sharing intimate images without consent
            - **Economic:** Controlling access to money, employment, or resources
            
            🏛️ **Your Rights:**
            - Right to safety and security
            - Right to make your own decisions
            - Right to seek help and support
            - Right to confidentiality when seeking help
            - Right to be believed and not judged
            
            ⚖️ **Legal Options:**
            - Protection orders/restraining orders
            - Criminal prosecution
            - Civil lawsuits
            - Family court proceedings
            """)
    
    st.markdown("---")
    
    st.subheader("Digital Safety Checklist")
    st.markdown("""
    **Protecting Your Digital Privacy:**
    
    ✅ **Device Security:**
    - [ ] Use strong, unique passwords
    - [ ] Enable two-factor authentication
    - [ ] Keep software updated
    - [ ] Use privacy mode/incognito browsing
    - [ ] Clear browsing history regularly
    
    ✅ **Social Media Safety:**
    - [ ] Review privacy settings
    - [ ] Limit who can see your posts
    - [ ] Be cautious about location sharing
    - [ ] Block and report abusive accounts
    - [ ] Consider limiting personal information shared
    
    ✅ **Communication Safety:**
    - [ ] Use secure messaging apps
    - [ ] Consider using a different device for help-seeking
    - [ ] Be aware of apps that may track your location
    - [ ] Know how to quickly delete conversations
    """)

# --- Mental Health Tab ---
with tab4:
    st.subheader("Mental Health & Wellbeing")
    
    # Add supportive imagery
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image("assets/3.png", width=300, caption="")
        except:
            pass
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🧘 Get Coping Strategies"):
            st.markdown(get_coping_strategies())
    
    with col2:
        if st.button("💝 Positive Affirmations"):
            # Show diverse women image for representation
            try:
                st.image("assets/2.png", width=300, caption="")
            except:
                pass
            st.markdown("""
            **Daily Affirmations for Survivors:**
            
            🌟 "I am worthy of love and respect."
            🌟 "My feelings are valid and important."
            🌟 "I have the strength to overcome challenges."
            🌟 "I deserve to feel safe and secure."
            🌟 "I am not defined by what happened to me."
            🌟 "Seeking help is a sign of courage, not weakness."
            🌟 "I trust my instincts and intuition."
            🌟 "I am taking steps toward a brighter future."
            🌟 "I am surrounded by people who care about me."
            🌟 "Every day, I am becoming stronger and more resilient."
            """)
    
    st.markdown("---")
    
    with st.expander("🌱 Breathing Exercise"):
        st.markdown("""
        **4-7-8 Breathing Technique for Anxiety Relief:**
        
        1. Sit or lie down in a comfortable position
        2. Place one hand on your chest, one on your belly
        3. Breathe in through your nose for 4 counts
        4. Hold your breath for 7 counts
        5. Exhale through your mouth for 8 counts
        6. Repeat 3-4 times
        
        *This technique can help calm anxiety and reduce stress.*
        """)
    
    with st.expander("🤝 Building Support Networks"):
        st.markdown("""
        **How to Build a Support Network:**
        
        👥 **Identify Safe People:**
        - Friends who listen without judgment
        - Family members you trust
        - Colleagues who are supportive
        - Healthcare providers
        - Counselors or therapists
        - Support group members
        
        📞 **Professional Support:**
        - Local GBV support organizations
        - Mental health hotlines
        - Counseling services
        - Legal aid organizations
        - Healthcare providers specializing in trauma
        
        💡 **Tips for Reaching Out:**
        - Start with one trusted person
        - Be clear about what kind of support you need
        - It's okay to set boundaries
        - Remember that asking for help is brave
        """)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 14px;">
<p>🦋 <strong>She Safe</strong> - Breaking the silence, building safety</p>
<p><em>Remember: You are not alone. You are believed. You are supported.</em></p>
<p>⚠️ If you're in immediate danger, please contact emergency services in your area.</p>
</div>
""", unsafe_allow_html=True)

# Add JavaScript for panic button functionality
st.markdown("""
<script>
function quickExit() {
    window.location.replace('https://www.google.com');
}

// Add keyboard shortcut for quick exit (Ctrl+Shift+X)
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.shiftKey && e.key === 'X') {
        quickExit();
    }
});
</script>
""", unsafe_allow_html=True)
