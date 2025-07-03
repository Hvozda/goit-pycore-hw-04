def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
             salaries = []
             for line in file:
                 line = line.strip()
                 if line:
                     try:
                         parts - line.split(',')
                         salary = float(parts[1])
                         salaries.append(salary)
                     except: (ValueError, IndexError)
             print(f" Error processing line: {line}")
        else
    print(f"line format: {line}")
             
    if not salaries:
            return (0, 0)
    total = sum(salaries)
    average = total / len(salaries)
    return (total, average)
    except FileNotFoundError:
    print('file not found')
    return(0, 0)
result = total_salary('salaries.txt')
print("Total salarry:" result[0])
print("Average salary:", result[1])


