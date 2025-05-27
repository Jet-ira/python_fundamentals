#!/usr/bin/python
"""Write a function that takes a nested dictionary like:"""
{
    "Math": {"Ali": 90, "Zara": 88},
    "Science": {"Ali": 80, "Zara": 95}
}
{
    "Ali": {"Math": 90, "Science": 80},
    "Zara": {"Math": 88, "Science": 95}
}

def transpose_scores(data):
    """
    Transposes a nested dictionary from subject -> student -> score
    to student -> subject -> score.

    Example:
        Input:
        {
            "Math": {"Ali": 90, "Zara": 88},
            "Science": {"Ali": 80, "Zara": 95}
        }

        Output:
        {
            "Ali": {"Math": 90, "Science": 80},
            "Zara": {"Math": 88, "Science": 95}
        }
    """
    result = {}
    for subject, scores in data.items():
        for student, score in scores.items():
            if student not in result:
                result[student] = {}
            result[student][subject] = score
    return result

grades = {
    "Math": {"Ali": 90, "Zara": 88},
    "Science": {"Ali": 80, "Zara": 95}
}

transposed = transpose_scores(grades)
print(transposed)

