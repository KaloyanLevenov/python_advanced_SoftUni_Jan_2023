def students_credits(*args):
    register = dict()
    result = []
    total_credits = 0
    for data in args:
        name, credits, max_points, student_points = data.split('-')
        credits_earned = int(credits) * (int(student_points) / int(max_points))
        register[name] = credits_earned
        total_credits += credits_earned
    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.")

    sorted_register = dict(sorted(register.items(), key=lambda x: -x[1]))
    for key, value in sorted_register.items():
        string = f"{key} - {value:.1f}"
        result.append(string)
    return "\n".join(result)