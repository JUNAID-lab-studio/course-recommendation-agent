import json

from ai_helper import generate_learning_path

def main():
    recommender = CourseRecommender("courses.json")

    with open("students.json", "r") as file:
        students = json.load(file)

    print("=" * 50)
    print("AI Course Recommendation Agent")
    print("=" * 50)
    
    for student in students:
       print("=" * 60)
       print(generate_learning_path(student))

    for student in students:
        print(f"\nStudent: {student['name']}")
        print(f"Education: {student['education']}")
        print(f"Skills: {', '.join(student['skills'])}")
        print(f"Career Goal: {student['goal']}")

        recommendations = recommender.recommend(student)

        print("\nRecommended Courses:")
        for i, course in enumerate(recommendations, start=1):
            print(f"{i}. {course['course']} ({course['level']})")
            print(f" Reason: {course['reason']}")

        print("-" * 50)

if __name__ == "__main__":
    main()
