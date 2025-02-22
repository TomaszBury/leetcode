import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(is_this_triangle, axis=1)
    return triangle

def is_this_triangle(row:pd.Series) -> bool:
    x,y,z = row["x"], row["y"], row["z"]

    if (x + y <= z) or (y + z <= x) or (z + x <= y):
        return "No"
    return "Yes"


# Create the DataFrame
data = {
    'x': [13, 10],
    'y': [15, 20],
    'z': [30, 15]
}

df = pd.DataFrame(data)

print(triangle_judgement(df))