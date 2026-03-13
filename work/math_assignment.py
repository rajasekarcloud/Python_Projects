# Maths assignment application buid using AWS Kiro with Streamlit and Python
import streamlit as st
import random
import sqlite3
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Math Practice for Kids", page_icon="🧮", layout="centered")

# Database setup
def init_db():
    """Initialize the database"""
    conn = sqlite3.connect('math_scores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  student_name TEXT,
                  difficulty TEXT,
                  operation TEXT,
                  problem TEXT,
                  correct INTEGER,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

def save_score(student_name, difficulty, operation, problem, correct):
    """Save a score to the database"""
    conn = sqlite3.connect('math_scores.db')
    c = conn.cursor()
    c.execute('''INSERT INTO scores (student_name, difficulty, operation, problem, correct, timestamp)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (student_name, difficulty, operation, problem, correct, datetime.now()))
    conn.commit()
    conn.close()

def get_scores(student_name=None):
    """Retrieve scores from the database"""
    conn = sqlite3.connect('math_scores.db')
    if student_name:
        df = pd.read_sql_query(
            "SELECT * FROM scores WHERE student_name = ? ORDER BY timestamp DESC",
            conn, params=(student_name,))
    else:
        df = pd.read_sql_query("SELECT * FROM scores ORDER BY timestamp DESC", conn)
    conn.close()
    return df

def get_student_stats(student_name):
    """Get statistics for a student"""
    conn = sqlite3.connect('math_scores.db')
    c = conn.cursor()
    c.execute('''SELECT COUNT(*) as total, SUM(correct) as correct
                 FROM scores WHERE student_name = ?''', (student_name,))
    result = c.fetchone()
    conn.close()
    return result if result else (0, 0)

# Initialize database
init_db()

# Initialize session state
defaults = {
    'score': 0,
    'total': 0,
    'current_problem': None,
    'show_result': False,
    'student_name': "",
    'assignment_active': False,   # True while a 15-problem session is running
    'problem_number': 0,          # 1-15 counter
    'answered': False,            # whether current problem has been answered
    'assignment_results': [],     # list of {problem, correct} for summary
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

TOTAL_PROBLEMS = 15

def generate_problem(difficulty, operation):
    """Generate a math problem based on difficulty and operation"""
    # Generate 10 numbers based on difficulty
    if difficulty == "Easy (1-10)":
        numbers = [random.randint(1, 10) for _ in range(5)]
    elif difficulty == "Medium (1-50)":
        numbers = [random.randint(1, 50) for _ in range(5)]
    else:  # Hard
        numbers = [random.randint(1, 100) for _ in range(5)]
    
    if operation == "Addition ➕":
        answer = sum(numbers)
        problem = " + ".join(map(str, numbers))
    elif operation == "Subtraction ➖":
        # Start with largest number and subtract the rest
        numbers.sort(reverse=True)
        answer = numbers[0]
        for num in numbers[1:]:
            answer -= num
        problem = " - ".join(map(str, numbers))
    elif operation == "Multiplication ✖️":
        # Use smaller numbers for multiplication to keep answer reasonable
        if difficulty == "Easy (1-10)":
            numbers = [random.randint(1, 3) for _ in range(5)]
        elif difficulty == "Medium (1-50)":
            numbers = [random.randint(1, 5) for _ in range(5)]
        else:
            numbers = [random.randint(1, 7) for _ in range(5)]
        answer = 1
        for num in numbers:
            answer *= num
        problem = " × ".join(map(str, numbers))
    else:  # Division
        # For division, create a chain that results in a whole number
        # Start with a large number and divide by smaller ones
        if difficulty == "Easy (1-10)":
            divisors = [random.randint(2, 5) for _ in range(5)]
        elif difficulty == "Medium (1-50)":
            divisors = [random.randint(2, 7) for _ in range(5)]
        else:
            divisors = [random.randint(2, 10) for _ in range(5)]
        
        # Calculate starting number to ensure whole number result
        product = 1
        for d in divisors:
            product *= d
        answer = random.randint(1, 10)
        start_num = product * answer
        
        numbers = [start_num] + divisors
        problem = " ÷ ".join(map(str, numbers))
    
    return problem, answer

def start_assignment(difficulty, operation):
    """Kick off a fresh 15-problem assignment"""
    selected_op = operation
    if operation == "Mixed 🎲":
        selected_op = random.choice(["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])
    problem, answer = generate_problem(difficulty, selected_op)
    st.session_state.assignment_active = True
    st.session_state.problem_number = 1
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.answered = False
    st.session_state.show_result = False
    st.session_state.assignment_results = []
    st.session_state.current_problem = {
        "problem": problem, "answer": answer,
        "difficulty": difficulty, "operation": selected_op
    }

def load_next_problem(difficulty, operation):
    """Load the next problem in the assignment"""
    selected_op = operation
    if operation == "Mixed 🎲":
        selected_op = random.choice(["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])
    problem, answer = generate_problem(difficulty, selected_op)
    st.session_state.problem_number += 1
    st.session_state.answered = False
    st.session_state.show_result = False
    st.session_state.current_problem = {
        "problem": problem, "answer": answer,
        "difficulty": difficulty, "operation": selected_op
    }

# Title and header
st.title("🧮 Math Practice for Kids")

# Student name input
student_name = st.text_input("👤 Enter your name:", value=st.session_state.student_name, key="name_input")
if student_name:
    st.session_state.student_name = student_name

st.markdown("---")

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    difficulty = st.selectbox(
        "Difficulty Level",
        ["Easy (1-10)", "Medium (1-50)", "Hard (1-100)"]
    )
    operation = st.selectbox(
        "Operation Type",
        ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗", "Mixed 🎲"]
    )
    
    st.markdown("---")
    st.header("📊 Current Session")
    if st.session_state.total > 0:
        percentage = (st.session_state.score / st.session_state.total) * 100
        st.metric("Correct", f"{st.session_state.score}/{st.session_state.total}")
        st.progress(percentage / 100)
        st.write(f"**{percentage:.1f}%** accuracy")
    else:
        st.info("Start solving problems!")
    
    if st.button("🔄 Reset Session"):
        st.session_state.score = 0
        st.session_state.total = 0
        st.session_state.assignment_active = False
        st.session_state.problem_number = 0
        st.session_state.current_problem = None
        st.session_state.assignment_results = []
        st.rerun()
    
    # Overall stats from database
    if st.session_state.student_name:
        st.markdown("---")
        st.header("🏆 Overall Stats")
        total_db, correct_db = get_student_stats(st.session_state.student_name)
        if total_db > 0:
            overall_percentage = (correct_db / total_db) * 100
            st.metric("Total Problems", total_db)
            st.metric("Total Correct", correct_db)
            st.write(f"**{overall_percentage:.1f}%** overall accuracy")

# Main content
if not st.session_state.student_name:
    st.warning("👆 Please enter your name above to start practicing!")
else:
    # ── Assignment not started yet ──────────────────────────────────────────
    if not st.session_state.assignment_active:
        st.info("Press 'Start Assignment' to begin 15 problems in a row.")
        if st.button("🚀 Start Assignment", type="primary", use_container_width=True):
            start_assignment(difficulty, operation)
            st.rerun()

    # ── Assignment complete ─────────────────────────────────────────────────
    elif st.session_state.problem_number > TOTAL_PROBLEMS:
        pct = (st.session_state.score / TOTAL_PROBLEMS) * 100
        st.success(f"🎉 Assignment complete! You scored **{st.session_state.score}/{TOTAL_PROBLEMS}** ({pct:.0f}%)")
        
        # Summary table
        results_df = pd.DataFrame(st.session_state.assignment_results)
        results_df['Result'] = results_df['correct'].apply(lambda x: '✅' if x else '❌')
        results_df = results_df.rename(columns={'problem': 'Problem', 'expected': 'Answer'})
        st.dataframe(results_df[['Problem', 'Answer', 'Result']], use_container_width=True, hide_index=True)

        if st.button("🔄 Start New Assignment", type="primary", use_container_width=True):
            st.session_state.assignment_active = False
            st.session_state.problem_number = 0
            st.rerun()

    # ── Active assignment ───────────────────────────────────────────────────
    else:
        prob = st.session_state.current_problem

        # Progress bar
        progress = (st.session_state.problem_number - 1) / TOTAL_PROBLEMS
        st.progress(progress, text=f"Problem {st.session_state.problem_number} of {TOTAL_PROBLEMS}")

        st.markdown("### Solve this problem:")
        st.markdown(f"## {prob['problem']} = ?")

        user_answer = st.number_input("Your answer:", value=0, step=1, key=f"ans_{st.session_state.problem_number}", format="%d")

        if not st.session_state.answered:
            if st.button("✅ Check Answer", type="primary", use_container_width=True):
                is_correct = user_answer == prob['answer']
                st.session_state.total += 1
                if is_correct:
                    st.session_state.score += 1
                st.session_state.answered = True
                st.session_state.show_result = "correct" if is_correct else "incorrect"

                # Save to DB
                save_score(
                    st.session_state.student_name,
                    prob['difficulty'], prob['operation'],
                    prob['problem'], 1 if is_correct else 0
                )
                # Record for end-of-assignment summary
                st.session_state.assignment_results.append({
                    "problem": prob['problem'],
                    "expected": prob['answer'],
                    "correct": is_correct
                })
                st.rerun()

        # Show feedback + Next button after answering
        if st.session_state.answered:
            if st.session_state.show_result == "correct":
                st.success("🎉 Correct!")
                st.balloons()
            else:
                st.error(f"❌ The answer was {prob['answer']}")

            # Score so far
            st.caption(f"Score so far: {st.session_state.score}/{st.session_state.total}")

            next_label = "➡️ Next Problem" if st.session_state.problem_number < TOTAL_PROBLEMS else "🏁 See Results"
            if st.button(next_label, type="primary", use_container_width=True):
                if st.session_state.problem_number < TOTAL_PROBLEMS:
                    load_next_problem(difficulty, operation)
                else:
                    st.session_state.problem_number += 1  # push past 15 to trigger summary
                st.rerun()

# Footer
st.markdown("---")

# Show performance graphs
if st.session_state.student_name:
    df = get_scores(st.session_state.student_name)
    
    if not df.empty:
        st.header("📈 Your Performance")
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["📊 Progress Over Time", "🎯 By Operation", "📋 Recent History"])
        
        with tab1:
            # Performance over time
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['date'] = df['timestamp'].dt.date
            daily_stats = df.groupby('date').agg({
                'correct': ['sum', 'count']
            }).reset_index()
            daily_stats.columns = ['date', 'correct', 'total']
            daily_stats['accuracy'] = (daily_stats['correct'] / daily_stats['total'] * 100).round(1)
            
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(
                x=daily_stats['date'],
                y=daily_stats['accuracy'],
                mode='lines+markers',
                name='Accuracy %',
                line=dict(color='#1f77b4', width=3),
                marker=dict(size=8)
            ))
            fig1.update_layout(
                title='Daily Accuracy Trend',
                xaxis_title='Date',
                yaxis_title='Accuracy (%)',
                yaxis_range=[0, 100],
                hovermode='x unified'
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            # Problems solved per day
            fig2 = px.bar(daily_stats, x='date', y='total',
                         title='Problems Solved Per Day',
                         labels={'total': 'Number of Problems', 'date': 'Date'},
                         color='total',
                         color_continuous_scale='Blues')
            st.plotly_chart(fig2, use_container_width=True)
        
        with tab2:
            # Performance by operation
            op_stats = df.groupby('operation').agg({
                'correct': ['sum', 'count']
            }).reset_index()
            op_stats.columns = ['operation', 'correct', 'total']
            op_stats['accuracy'] = (op_stats['correct'] / op_stats['total'] * 100).round(1)
            
            fig3 = px.bar(op_stats, x='operation', y='accuracy',
                         title='Accuracy by Operation Type',
                         labels={'accuracy': 'Accuracy (%)', 'operation': 'Operation'},
                         color='accuracy',
                         color_continuous_scale='Greens',
                         text='accuracy')
            fig3.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig3.update_layout(yaxis_range=[0, 110])
            st.plotly_chart(fig3, use_container_width=True)
            
            # Performance by difficulty
            diff_stats = df.groupby('difficulty').agg({
                'correct': ['sum', 'count']
            }).reset_index()
            diff_stats.columns = ['difficulty', 'correct', 'total']
            diff_stats['accuracy'] = (diff_stats['correct'] / diff_stats['total'] * 100).round(1)
            
            fig4 = px.bar(diff_stats, x='difficulty', y='accuracy',
                         title='Accuracy by Difficulty Level',
                         labels={'accuracy': 'Accuracy (%)', 'difficulty': 'Difficulty'},
                         color='accuracy',
                         color_continuous_scale='Oranges',
                         text='accuracy')
            fig4.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig4.update_layout(yaxis_range=[0, 110])
            st.plotly_chart(fig4, use_container_width=True)
        
        with tab3:
            # Recent history table
            st.subheader("Recent Problems")
            recent_df = df.head(20)[['timestamp', 'difficulty', 'operation', 'problem', 'correct']].copy()
            recent_df['result'] = recent_df['correct'].apply(lambda x: '✅ Correct' if x == 1 else '❌ Incorrect')
            recent_df['timestamp'] = pd.to_datetime(recent_df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')
            recent_df = recent_df.drop('correct', axis=1)
            recent_df.columns = ['Time', 'Difficulty', 'Operation', 'Problem', 'Result']
            st.dataframe(recent_df, use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown("*Keep practicing to improve your math skills! 🌟*")
