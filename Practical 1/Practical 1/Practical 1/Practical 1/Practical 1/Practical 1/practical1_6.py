def calculate_grade():
    # Accept number of courses
    num_courses = int(input())
    
    # Accept marks for the courses
    marks = list(map(int, input().split()))
    
    # Check if the student has failed any course (marks < 40)
    if any (mark < 40 for mark in marks):
        print("Fail")
    else:
        # Calculate the total marks and aggregate percentage
        total_marks = sum(marks)
        aggregate_percentage = (total_marks / (num_courses * 100)) * 100
        
        # Print the aggregate percentage
        print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
        
        # Determine the grade based on the aggregate percentage
        if aggregate_percentage > 75:
            print("Grade: Distinction")
        elif 60 <= aggregate_percentage < 75:
            print("Grade: First Division")
        elif 50 <= aggregate_percentage < 60:
            print("Grade: Second Division")
        elif 40 <= aggregate_percentage < 50:
            print("Grade: Third Division")

# Call the function to execute
calculate_grade()
