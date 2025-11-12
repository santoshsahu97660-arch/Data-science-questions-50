import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Data Science Practice", page_icon="📘", layout="wide")
st.title("📘 Data Science Practice")

st.markdown("### 💰 Entry Fee: ₹10 (Just for fun — no real payment needed)")
st.info("This app is for learning practice only. Enjoy the quiz!")

# 🧠 50 Questions (20 old + 30 new)
quiz_data = [
    {"question": "Which library is mainly used for data manipulation and analysis in Python?",
     "options": ["NumPy", "Matplotlib", "Pandas", "Seaborn"], "answer": "Pandas"},
    {"question": "Which of these is a supervised learning algorithm?",
     "options": ["K-Means", "Linear Regression", "DBSCAN", "PCA"], "answer": "Linear Regression"},
    {"question": "Which function is used to read CSV files in pandas?",
     "options": ["pd.read()", "pd.read_csv()", "pd.open_csv()", "pd.load_csv()"], "answer": "pd.read_csv()"},
    {"question": "Which of the following is used for data visualization?",
     "options": ["TensorFlow", "Scikit-learn", "Matplotlib", "Flask"], "answer": "Matplotlib"},
    {"question": "Which library is used for machine learning in Python?",
     "options": ["scikit-learn", "pygame", "flask", "pillow"], "answer": "scikit-learn"},
    {"question": "Which Python library is best for numerical computation?",
     "options": ["Seaborn", "NumPy", "Matplotlib", "Flask"], "answer": "NumPy"},
    {"question": "Which of the following is used to handle missing data in pandas?",
     "options": ["fillna()", "drop()", "replace()", "append()"], "answer": "fillna()"},
    {"question": "Which function returns the first 5 rows of a DataFrame?",
     "options": ["df.tail()", "df.start()", "df.head()", "df.top()"], "answer": "df.head()"},
    {"question": "Which library is used for creating plots and charts?",
     "options": ["Matplotlib", "Scikit-learn", "TensorFlow", "Flask"], "answer": "Matplotlib"},
    {"question": "Which command is used to install a Python package?",
     "options": ["python install", "pip install", "import install", "setup install"], "answer": "pip install"},
    {"question": "Which of the following is used for web development in Python?",
     "options": ["Django", "NumPy", "Matplotlib", "Seaborn"], "answer": "Django"},
    {"question": "What type of data does a pandas Series hold?",
     "options": ["1D data", "2D data", "3D data", "Text data"], "answer": "1D data"},
    {"question": "Which pandas function is used to merge DataFrames?",
     "options": ["pd.join()", "pd.merge()", "pd.concat()", "pd.combine()"], "answer": "pd.merge()"},
    {"question": "Which of the following is used for deep learning?",
     "options": ["Flask", "TensorFlow", "Matplotlib", "Seaborn"], "answer": "TensorFlow"},
    {"question": "Which function removes duplicate rows in pandas?",
     "options": ["dropna()", "drop_duplicates()", "remove()", "clear()"], "answer": "drop_duplicates()"},
    {"question": "What does CSV stand for?",
     "options": ["Common Separated Values", "Comma Separated Values", "Column Separated Values", "Character Separated Values"],
     "answer": "Comma Separated Values"},
    {"question": "Which of the following is used for data cleaning?",
     "options": ["Pandas", "Flask", "Django", "PyGame"], "answer": "Pandas"},
    {"question": "Which function gives the shape (rows, columns) of a DataFrame?",
     "options": ["df.size", "df.length", "df.shape", "df.type"], "answer": "df.shape"},
    {"question": "Which Python statement is used to handle exceptions?",
     "options": ["catch", "error", "try-except", "exception"], "answer": "try-except"},
    {"question": "Which library is used for array manipulation?",
     "options": ["NumPy", "Matplotlib", "Django", "Flask"], "answer": "NumPy"},

    # Additional 30 questions
    {"question": "Which of these is NOT a Python data type?",
     "options": ["List", "Tuple", "Dictionary", "Tree"], "answer": "Tree"},
    {"question": "What is the extension of a Python file?",
     "options": [".py", ".java", ".cpp", ".html"], "answer": ".py"},
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["function", "def", "lambda", "fun"], "answer": "def"},
    {"question": "Which method is used to add an element to a list?",
     "options": ["add()", "insert()", "append()", "push()"], "answer": "append()"},
    {"question": "Which Python function gives the length of a list?",
     "options": ["count()", "size()", "len()", "length()"], "answer": "len()"},
    {"question": "Which statement is used for looping in Python?",
     "options": ["loop", "for", "repeat", "iterate"], "answer": "for"},
    {"question": "Which of the following creates an empty set?",
     "options": ["{}", "[]", "set()", "empty()"], "answer": "set()"},
    {"question": "Which operator is used for floor division in Python?",
     "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "Which symbol is used for comments in Python?",
     "options": ["//", "#", "/* */", "<!-- -->"], "answer": "#"},
    {"question": "What does IDE stand for?",
     "options": ["Integrated Development Environment", "Internal Data Engine", "Input Device Extension", "Integrated Data Execution"], 
     "answer": "Integrated Development Environment"},
    {"question": "Which data structure uses key-value pairs?",
     "options": ["List", "Tuple", "Set", "Dictionary"], "answer": "Dictionary"},
    {"question": "Which Python keyword is used to create a class?",
     "options": ["class", "define", "object", "new"], "answer": "class"},
    {"question": "Which function converts a string to lowercase?",
     "options": ["lower()", "down()", "small()", "to_lower()"], "answer": "lower()"},
    {"question": "Which of the following is immutable?",
     "options": ["List", "Set", "Tuple", "Dictionary"], "answer": "Tuple"},
    {"question": "Which operator is used for exponentiation?",
     "options": ["*", "**", "^", "//"], "answer": "**"},
    {"question": "Which method removes the last item from a list?",
     "options": ["remove()", "pop()", "delete()", "clear()"], "answer": "pop()"},
    {"question": "Which function returns a range of numbers?",
     "options": ["range()", "numbers()", "series()", "list()"], "answer": "range()"},
    {"question": "What is the output type of range(5)?",
     "options": ["list", "range", "tuple", "set"], "answer": "range"},
    {"question": "Which keyword is used to exit from a loop?",
     "options": ["continue", "exit", "break", "stop"], "answer": "break"},
    {"question": "Which function converts string to integer?",
     "options": ["str()", "chr()", "int()", "ord()"], "answer": "int()"},
    {"question": "Which function checks the data type?",
     "options": ["type()", "data()", "typeof()", "dtype()"], "answer": "type()"},
    {"question": "What is the result of 2 ** 3?",
     "options": ["5", "6", "8", "9"], "answer": "8"},
    {"question": "Which module in Python supports regular expressions?",
     "options": ["re", "regex", "pyregex", "string"], "answer": "re"},
    {"question": "What is the output of bool(0)?",
     "options": ["True", "False", "0", "None"], "answer": "False"},
    {"question": "Which keyword is used to import a module?",
     "options": ["package", "include", "import", "require"], "answer": "import"},
    {"question": "What will 3 == '3' return?",
     "options": ["True", "False", "Error", "None"], "answer": "False"},
    {"question": "Which function is used to get user input?",
     "options": ["scan()", "read()", "input()", "get()"], "answer": "input()"},
    {"question": "Which statement is used to skip an iteration in loop?",
     "options": ["pass", "continue", "skip", "break"], "answer": "continue"},
    {"question": "Which keyword defines anonymous functions?",
     "options": ["def", "lambda", "func", "hidden"], "answer": "lambda"},
    {"question": "Which function finds the maximum value?",
     "options": ["max()", "high()", "greatest()", "big()"], "answer": "max()"},
]

TOTAL_Q = len(quiz_data)

# 🧾 Login
st.subheader("Login to Start Quiz")
name = st.text_input("Enter your Name")
mobile = st.text_input("Enter your Mobile Number")

if not name or not mobile:
    st.info("Please enter your name and mobile number to start the quiz.")
    st.stop()

st.success(f"Welcome {name}! There are {TOTAL_Q} questions. Good luck! 🎯")

# Initialize session
if "answers" not in st.session_state:
    st.session_state["answers"] = [None] * TOTAL_Q
if "submitted" not in st.session_state:
    st.session_state["submitted"] = [False] * TOTAL_Q
if "score" not in st.session_state:
    st.session_state["score"] = 0

# Quiz
for i, q in enumerate(quiz_data):
    st.write(f"### Q{i+1}. {q['question']}")
    choice = st.radio("Choose your answer:", q["options"], key=f"q{i}")
    st.session_state["answers"][i] = choice

    if not st.session_state["submitted"][i]:
        if st.button(f"Submit Answer {i+1}", key=f"btn_{i}"):
            st.session_state["submitted"][i] = True
            if choice == q["answer"]:
                st.success("🎉 Congratulations! Your answer is right!")
                st.session_state["score"] += 1
            else:
                st.error("❌ Better luck next time!")

st.markdown("---")

# Submit
if st.button("Finish and Submit Quiz"):
    score = st.session_state["score"]
    st.success(f"Your Final Score: {score}/{TOTAL_Q}")

    # Save attempt
    attempts_file = "attempts.csv"
    attempt = pd.DataFrame([{"timestamp": datetime.now().isoformat(), "name": name, "mobile": mobile, "score": score}])
    if os.path.exists(attempts_file):
        df_all = pd.read_csv(attempts_file)
        df_all = pd.concat([df_all, attempt], ignore_index=True)
    else:
        df_all = attempt
    df_all.to_csv(attempts_file, index=False)

    # Leaderboard for perfect scorers
    if score == TOTAL_Q:
        leaderboard_file = "leaderboard.csv"
        entry = pd.DataFrame([{"timestamp": datetime.now().isoformat(), "name": name, "mobile": mobile, "score": score}])
        if os.path.exists(leaderboard_file):
            lb = pd.read_csv(leaderboard_file)
            lb = pd.concat([lb, entry], ignore_index=True)
        else:
            lb = entry
        lb['timestamp'] = pd.to_datetime(lb['timestamp'])
        lb = lb.sort_values(by='timestamp', ascending=False).head(10)
        lb.to_csv(leaderboard_file, index=False)
        st.balloons()
        st.markdown("## 🏆 BIG CONGRATULATIONS! You scored 50/50!")
        st.markdown("🎁 **Prize:** You win a Data Science Masterclass Pass! 🧠")
    else:
        st.info("Thank you for participating! Only full scorers appear in Top 10 leaderboard.")

    # Leaderboard Display
    st.markdown("### 🏆 Top 10 Perfect Scorers")
    if os.path.exists("leaderboard.csv"):
        lb = pd.read_csv("leaderboard.csv")
        if not lb.empty:
            lb = lb.sort_values(by='timestamp', ascending=False).head(10).reset_index(drop=True)
            st.dataframe(lb)
        else:
            st.write("No perfect scorers yet.")
    else:
        st.write("No perfect scorers yet.")

    # All Attempts
    st.markdown("### 📋 All Attempts (Recent)")
    if os.path.exists("attempts.csv"):
        att = pd.read_csv("attempts.csv")
        att['timestamp'] = pd.to_datetime(att['timestamp'])
        att = att.sort_values(by='timestamp', ascending=False).reset_index(drop=True)
        st.dataframe(att.head(50))
    else:
        st.write("No attempts yet.")
