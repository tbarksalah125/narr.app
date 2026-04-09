import streamlit as st
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OpenAI API Key is missing!")
    st.stop()

client = OpenAI(api_key=api_key)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful educational assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


def generate_story(text: str) -> str:
    prompt = f"""
    معايا الفقرة دي من درس تعليمي:
    \"\"\"{text}\"\"\"

    حوّل الفقرة دي لقصة تعليمية قصيرة بالعربية الفصحى البسيطة،
    موجهة لطالب في المرحلة الإعدادية.

    المطلوب:
    - الحفاظ على صحة المعلومات
    - أسلوب مشوق وفيه قصة
    - في النهاية ملخص بسيط من سطرين
    """
    return call_llm(prompt)


def generate_questions(text: str) -> str:
    prompt = f"""
    معايا الفقرة دي:
    \"\"\"{text}\"\"\"

    طلع 3 إلى 5 أسئلة بسيطة باللغة العربية
    لقياس فهم الطالب للنص.
    """
    return call_llm(prompt)


st.set_page_config(page_title="Narrify – Smart Story Learning", page_icon="📖")

st.title("Narrify – Smart Story Learning")
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

if generate_story_btn:
    if not lesson_text.strip():
        st.warning("⚠️ Please enter some lesson text before generating a story.")
    else:
        with st.spinner("Generating story..."):
            try:
                story = generate_story(lesson_text)
                st.subheader("القصة المبسطة")
                st.write(story)
            except Exception as e:
                st.error(f"❌ Failed to generate story: {e}")

if generate_questions_btn:
    if not lesson_text.strip():
        st.warning("⚠️ Please enter some lesson text before generating questions.")
    else:
        with st.spinner("Generating questions..."):
            try:
                questions = generate_questions(lesson_text)
                st.subheader("الأسئلة")
                st.write(questions)
            except Exception as e:
                st.error(f"❌ Failed to generate questions: {e}")
