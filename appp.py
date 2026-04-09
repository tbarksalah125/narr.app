import streamlit as st

# =========================
# Offline LLM Function (بدون AI)
# =========================
def call_llm(prompt: str) -> str:
    return """
⚠️ AI غير متاح حالياً (Offline Mode)

📖 القصة:
كان هناك طالب مجتهد يقرأ دروسه ويحاول فهمها بطريقة بسيطة وممتعة، فحوّل المعلومات إلى قصة ليسهل عليه الحفظ.

📝 الملخص:
الدرس تم تبسيطه في شكل قصة تساعد على الفهم السريع.

❓ الأسئلة:
1- ما الفكرة الرئيسية في النص؟
2- كيف يمكن تلخيص الدرس؟
3- ماذا استفدت من القصة؟
"""

# =========================
# Generate Story
# =========================
def generate_story(text: str) -> str:
    return call_llm(text)

# =========================
# Generate Questions
# =========================
def generate_questions(text: str) -> str:
    return call_llm(text)

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Narrify – Smart Story Learning", page_icon="📖")

st.title("📖 Narrify – Smart Story Learning")
st.markdown("Transform lesson text into engaging stories and comprehension questions.")

st.markdown("---")

lesson_text = st.text_area(
    label="Lesson Text",
    placeholder="Paste your lesson text here...",
    height=200,
)

col1, col2 = st.columns(2)

with col1:
    generate_story_btn = st.button("📖 Generate Story", use_container_width=True)

with col2:
    generate_questions_btn = st.button("❓ Generate Questions", use_container_width=True)

st.markdown("---")

# =========================
# Story Button
# =========================
if generate_story_btn:
    if not lesson_text.strip():
        st.warning("⚠️ Please enter some lesson text first.")
    else:
        with st.spinner("Generating story..."):
            st.subheader("📖 القصة المبسطة")
            st.write(generate_story(lesson_text))

# =========================
# Questions Button
# =========================
if generate_questions_btn:
    if not lesson_text.strip():
        st.warning("⚠️ Please enter some lesson text first.")
    else:
        with st.spinner("Generating questions..."):
            st.subheader("❓ الأسئلة")
            st.write(generate_questions(lesson_text))
