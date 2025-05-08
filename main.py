import streamlit as st


# Page Configuration
st.set_page_config(
    page_title="Resilience Journey",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium UI
st.markdown("""
    <style>
        :root {
            --primary: #2563eb;
            --primary-light: #3b82f6;
            --secondary: #1e40af;
            --accent: #f59e0b;
            --text: #1f2937;
            --light: #f8fafc;
            --card-bg: #ffffff;
        }
        
        body {
            background: linear-gradient(135deg, #f0f4f8 0%, #e5e9f0 100%);
            font-family: 'Inter', sans-serif;
        }
        
        .sidebar {
            background: linear-gradient(180deg, var(--card-bg) 0%, #f8fafc 100%);
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .header {
            color: var(--secondary);
            font-size: 3rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #2563eb, #1e40af);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .subheader {
            color: var(--text);
            font-size: 1.4rem;
            text-align: center;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        .stButton > button {
            background: linear-gradient(to right, var(--primary), var(--primary-light)) !important;
            color: var(--light) !important;
            border-radius: 12px;
            font-size: 1rem;
            padding: 0.75rem 1.5rem;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .content-section {
            padding: 2rem;
            background: var(--card-bg);
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 1.5rem;
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .pill {
            display: inline-block;
            padding: 0.35rem 0.8rem;
            border-radius: 50px;
            background-color: #e0e7ff;
            color: var(--primary);
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            font-size: 0.85rem;
        }
        
        .quote-card {
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border-left: 4px solid var(--accent);
            padding: 1.5rem;
            border-radius: 0 12px 12px 0;
            margin: 1.5rem 0;
            font-style: italic;
            color: var(--text);
        }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar ----
with st.sidebar:
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.header("🌱 Your Resilience Profile")
    
    name = st.text_input("Your Name", placeholder="Enter your name")
    resilience_level = st.select_slider(
        "Current Resilience Level",
        options=["🌱 Seedling", "🌿 Sprouting", "🌳 Growing", "🏔️ Strong", "🦾 Unbreakable"],
        value="🌳 Growing"
    )
    goal = st.text_area("Note to Future Self", placeholder="What encouragement do you need to hear?")
    
    uploaded_image = st.file_uploader("Upload an Inspiring Image", type=["jpg", "jpeg", "png"])
    
    if st.button("Begin My Journey", type="primary", use_container_width=True):
        st.success(f"Welcome, {name}! Your resilience story starts now. ✨")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Main Content ----
st.markdown('<p class="header">Resilience Journey</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Cultivate unshakable strength through life\'s challenges</p>', unsafe_allow_html=True)

# Resilience Definition
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("What is Resilience?")
        st.write("""
        Resilience is your psychological immune system - the capacity to recover quickly from difficulties 
        and adapt well in the face of adversity. It's not about avoiding struggle, but rather developing 
        the tools to navigate through it and emerge stronger.
        """)
        st.markdown("""
        <div class="quote-card">
            "Resilience is accepting your new reality, even if it's less good than the one you had before."
            <br>- Elizabeth Edwards
        </div>
        """, unsafe_allow_html=True)
   
# Resilience Benefits
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Why Resilience Matters")
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <span style='font-size: 2.5rem;'>💪</span>
            <h4>Emotional Strength</h4>
            <p>Better stress management and emotional regulation</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <span style='font-size: 2.5rem;'>🧠</span>
            <h4>Cognitive Flexibility</h4>
            <p>Improved problem-solving during challenges</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div style='text-align: center; padding: 1rem;'>
            <span style='font-size: 2.5rem;'>🌟</span>
            <h4>Post-Traumatic Growth</h4>
            <p>Potential to grow stronger after adversity</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='margin-top: 1.5rem;'>
        <span class="pill">+37% faster recovery</span>
        <span class="pill">42% less stress</span>
        <span class="pill">5x more adaptable</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Building Resilience
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Building Your Resilience Toolkit")
    
    tab1, tab2, tab3 = st.tabs(["🧘 Mindset", "🤝 Relationships", "⚡ Habits"])
    
    with tab1:
        st.markdown("""
        - Practice **cognitive reframing** of challenges
        - Develop **self-compassion** practices
        - Cultivate **realistic optimism**
        - Maintain **perspective** during difficulties
        """)
        
    with tab2:
        st.markdown("""
        - Build a **support network** you can rely on
        - Seek **mentors** who've overcome adversity
        - Practice **vulnerability** in safe relationships
        - Offer **support** to others in need
        """)
        
    with tab3:
        st.markdown("""
        - Establish **stress-reduction** routines
        - Prioritize **sleep and nutrition**
        - Engage in **regular physical activity**
        - Practice **mindfulness meditation**
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Interactive Exercise
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("📝 Your Resilience Action Plan")
    
    challenge = st.text_area("Describe a current challenge you're facing")
    
    col1, col2 = st.columns(2)
    with col1:
        strategy = st.selectbox(
            "Which resilience strategy will you try?",
            ["Cognitive Reframing", "Seeking Support", "Self-Care Practice", "Finding Meaning"]
        )
    with col2:
        timeline = st.select_slider(
            "Commitment timeline",
            options=["1 day", "1 week", "2 weeks", "1 month", "3 months+"]
        )
    
    if st.button("Commit to This Plan", type="primary"):
        st.success("Excellent choice! Remember: small consistent actions build unshakable resilience.")
        st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# Image Display
with st.container():
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Your Resilience Symbol")
    
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Your personal resilience inspiration", use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?fit=crop&w=1200&q=80", 
                caption="Like mountains, we grow through weathering the storms", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)