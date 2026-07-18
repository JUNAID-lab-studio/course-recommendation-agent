# Course Recommendation Agent

## Overview
The Course Recommendation Agent is an AI-powered application that recommends learning courses based on a student's education, existing skills, and career goals. It generates a personalized learning path with explanations for each recommendation.

## Features
- Personalized course recommendations
- Learning path generation
- Course prerequisite support
- AI-based recommendation logic
- Easy-to-use command-line interface

## Tech Stack
- Python
- JSON
- OpenAI/Groq API
- Git & GitHub

## Project Structure
```
course-recommendation-agent/
│── app.py
│── recommender.py
│── courses.json
│── students.json
│── requirements.txt
│── README.md
│── .env.example
│── sample_output.txt
```

## Installation

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your API key to a `.env` file.

Example:

```
GROQ_API_KEY=your_api_key_here
```

4. Run the project

```bash
python app.py
```

## Sample Input

- Name: Junaid
- Education: B.Tech CSE
- Skills: Python, SQL
- Goal: Become AI Engineer

## Sample Output

Recommended Courses:
- Python Basics
- Advanced Python
- Machine Learning
- Deep Learning
- LangChain
- RAG Systems
- Git & GitHub

## Future Improvements
- Web interface
- User authentication
- Course ratings
- PDF report generation

## Architecture

The application consists of the following components:

- app.py – Main entry point
- recommender.py – Recommendation engine
- ai_helper.py – AI model integration
- courses.json – Course database
- students.json – Student profiles

## AI Design

The agent follows these steps:

1. Read the student's profile.
2. Analyze education, skills, and career goal.
3. Match relevant courses.
4. Generate a personalized learning path.
5. Explain the reason behind each recommendation.

## Assumptions

- Student goals are clearly defined.
- Course data is stored in JSON format.
- Internet connection is available when using the AI model.

## Future Enhancements

- Web interface using Streamlit
- Database integration
- User login system
- PDF learning roadmap
- Multi-language support


## Author

Junaid Baig
