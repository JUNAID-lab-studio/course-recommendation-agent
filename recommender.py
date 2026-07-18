import json

class CourseRecommender:
    def __init__(self, course_file):
        with open(course_file, "r") as file:
            self.courses = json.load(file)

    def recommend(self, student):
        goal = student["goal"].lower()

        recommendations = []

        if "ai" in goal:
            keywords = [
                "Python Basics",
                "Advanced Python",
                "Machine Learning",
                "Deep Learning",
                "LangChain",
                "RAG Systems",
                "Git & GitHub"
            ]
        elif "web" in goal:
            keywords = [
                "Python Basics",
                "Git & GitHub"
            ]
        else:
            keywords = [course["name"] for course in self.courses]

        for course in self.courses:
            if course["name"] in keywords:
                recommendations.append({
                    "course": course["name"],
                    "level": course["level"],
                    "reason": f"Recommended for your goal: {student['goal']}"
                })

        return recommendations