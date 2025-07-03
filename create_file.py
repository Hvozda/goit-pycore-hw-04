with open('salaries.txt', 'w', encoding='utf-8') as f:
    f.write("""Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
""")
    total_salary("salaries.txt")


