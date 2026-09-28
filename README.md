# 🎓 EduBridge

### Classroom Environment & Interaction Analyzer

EduBridge is an AI-based mini project designed to understand the overall classroom learning environment using **LangChain, Large Language Models (LLM), and Fuzzy Logic**.

The system analyzes anonymous student feedback and evaluates factors such as:

- Teacher–student communication
- Teaching behaviour and style
- Student comfort
- Student participation
- Classroom atmosphere

The system generates an **Overall Classroom Environment Score** and provides constructive suggestions for creating a more positive and supportive learning environment.

> EduBridge focuses on the overall classroom environment and does not rate or judge individual teachers.

---

## 🚀 Features

- 💬 Anonymous student feedback input
- 🤖 AI-based feedback analysis using LangChain
- 🧠 LLM-based extraction of classroom factors
- 🌫️ Genuine Fuzzy Logic inference system
- 📊 Overall classroom environment score
- 💡 AI-generated constructive suggestions
- 🌐 Interactive Streamlit web interface
- ☁️ Can be deployed using Streamlit Community Cloud

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | LLM application framework |
| OpenAI LLM | Natural language analysis |
| Scikit-Fuzzy | Fuzzy inference system |
| NumPy | Numerical operations |
| SciPy | Scientific computing |
| NetworkX | Fuzzy logic dependency |
| python-dotenv | Environment variable management |

---

## 🔄 System Workflow

```text
Student Feedback
       ↓
LangChain + LLM
       ↓
Extract Classroom Factors
       ↓
Communication
Teaching Behaviour
Student Comfort
Participation
Classroom Atmosphere
       ↓
Fuzzification
       ↓
Fuzzy Rule Evaluation
       ↓
Defuzzification
       ↓
Overall Environment Score
       ↓
AI Insights & Suggestions

🧠 AI Component

EduBridge uses LangChain to connect the classroom feedback with an LLM.

The LLM analyzes natural-language student feedback and extracts approximate scores from 0 to 10 for:

Communication
Teaching Behaviour
Student Comfort
Participation
Classroom Atmosphere

These values are then passed to the fuzzy inference system.

🌫️ Fuzzy Logic Component

The project uses a genuine fuzzy inference system implemented using Scikit-Fuzzy.

Input Variables

Each input has three membership functions:

Low
Medium
High
Output Variable

The fuzzy system produces an overall environment score from 0 to 100.

The output is represented using:

Poor
Moderate
Good
Excellent
Example Fuzzy Rules
IF communication is high
AND teaching is high
AND comfort is high
THEN environment is excellent.
IF communication is low
OR teaching is low
THEN environment is poor.
IF participation is low
AND atmosphere is low
THEN environment is poor.

The final score is obtained through fuzzy inference and defuzzification.

📁 Project Structure
EduBridge/
│
├── app.py
├── fuzzy_system.py
├── llm_chain.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

.env contains private API credentials and should never be uploaded to GitHub.

⚙️ Installation
1. Clone the repository
git clone https://github.com/mohinitate/EduBridge.git
cd EduBridge
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project folder:

OPENAI_API_KEY=your_api_key_here

Never share or upload your API key publicly.

▶️ Run the Application

Run:

streamlit run app.py

The application will open in your browser at:

http://localhost:8501
☁️ Deployment

EduBridge can be deployed using Streamlit Community Cloud.

The deployment requires:

A GitHub repository
app.py
requirements.txt

After deployment, Streamlit provides a public .streamlit.app URL.

🎯 Project Objective

The objective of EduBridge is to demonstrate how Artificial Intelligence and Fuzzy Logic can work together to analyze qualitative classroom feedback and convert it into a meaningful assessment of the overall learning environment.

The project combines:

Natural Language Understanding → AI Analysis → Fuzzy Inference → Score → Constructive Suggestions

👩‍💻 Author

Mohini Tate

College Mini Project
AI + Fuzzy Logic

📌 Disclaimer

EduBridge is an academic mini project intended to demonstrate the integration of AI, LangChain, and fuzzy logic. The generated analysis should be considered an indicative interpretation of anonymous feedback rather than an official evaluation of teaching quality.


### One important thing ❤️

Your GitHub repository should now have:

```text
app.py
fuzzy_system.py
llm_chain.py
requirements.txt
.gitignore
README.md
