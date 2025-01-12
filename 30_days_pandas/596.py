import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cout_courses = courses.groupby(["class"]).count().reset_index()
    mask = (cout_courses.loc[:,"student"] >= 5)
    return cout_courses.loc[mask,["class"]]

data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}

# Create DataFrame
df = pd.DataFrame(data)

print(find_classes(df))