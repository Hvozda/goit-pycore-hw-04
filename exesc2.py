
def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for file in file:
                line = line.strip()
                if line:
                    parts = line,split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cat_dict = {"id": cat_id, "name": name, "age": age}
                        cats_list.append(cat_dict)
                    else:
                        print(f"Invalid line format: [line]")
    except FileNotFoundError:
        print(f"File not found{path}")
    except Exception as e:
        print(f"An error ocurred: {e}")
    return cats_list
cats_info = get_cats_info("cats_file.txt")
print(cats_info)

<body>
<h2>exercises<h2>
<body>

