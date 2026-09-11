import streamlit as st

st.set_page_config(page_title="؟؟؟", page_icon="💘")  # اینجا اسم برنامه رو بذار

# ---------- تنظیمات ظاهری ----------
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #ffe6f0, #fdeef7, #fff); }
    .stButton > button { border-radius: 20px; }
</style>
""", unsafe_allow_html=True)

# ---------- مدیریت مراحل ----------
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'name' not in st.session_state:
    st.session_state.name = ""

step = st.session_state.step

# ---------- صفحه ۰: خوش‌آمد ----------
if step == 0:
    st.title("✨ یک آزمون جالب ✨")
    st.write("چند دقیقه وقت داری تا یک چیز جالب درباره‌ی خودت کشف کنیم؟ 😉")
    name = st.text_input("اول بگو اسمت چیه؟")
    if st.button("شروع کنیم 🚀"):
        if name.strip() != "":
            st.session_state.name = name.strip()
            st.session_state.step = 1
        else:
            st.warning("اسم رو ننوشتی که! 😅")

# ---------- صفحه ۱ تا ۳: سوال‌ها ----------
QUESTIONS = [
    # اینجا سوال ۱ و ۲ خودت رو با گزینه‌هاش بنویس
    ("سوال اول؟", ["گزینه ۱", "گزینه ۲", "گزینه ۳"]),
    ("سوال دوم؟", ["گزینه ۱", "گزینه ۲", "گزینه ۳"]),
    ("قهوه ☕ یا چای 🍵؟", ["قهوه ☕", "چای 🍵", "هیچ‌کدام، من آبمیوه‌ای‌ام 🧃"]),
]

for i, (q, options) in enumerate(QUESTIONS, start=1):
    if step == i:
        st.title(f"سوال {i} از {len(QUESTIONS)}")
        st.subheader(f"خب {st.session_state.name} جان، {q}")
        answer = st.radio("انتخاب کن:", options, key=f"q{i}")
        if st.button("بعدی ➡️"):
            st.session_state.step = i + 1

# ---------- صفحه ۴: تحلیل ----------
elif step == 4:
    st.title("در حال تحلیل پاسخ‌ها... 🧠")
    bar = st.progress(0)
    for p in range(100):
        bar.progress(p + 1)
    st.success(f"🎉 {st.session_state.name} جان، نتیجه آماده شد!")
    st.header("٪۹۷ سازگاری با یک توسعه‌دهنده پیدا شد! 👨‍💻")
    st.write("این شخص یکی رو می‌شناسیم که برنامه بلده، بامزه‌ست و دنبال یه دوست خوبه...")
    if st.button("می‌خوام بشناسمش! 💫"):
        st.session_state.step = 5

# ---------- صفحه ۵: پایان ----------
elif step == 5:
    st.balloons()
    st.title("آشنایی با خوشاگین آشنا شدی! 🎉")
    # اینجا یک جمله خودمونی از طرف خودت بنویس
    st.markdown("اینجا جای یک جمله‌ی دوستانه و دعوت‌کننده از طرف توست...")
    # لینک روبیکای شما
    st.link_button("گپ با توسعه‌دهنده 👨‍💻", "https://rubika.ir/Amir_samadi83ie")
