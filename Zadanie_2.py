def get_grades():
    return [5, 4, "3", 2, 1]

def calculate_average(grades):
    grades = [int(g) for g in grades]
    return sum(grades) / len(grades)

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

show_result()