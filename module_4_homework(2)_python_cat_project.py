def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')  
                if len(parts) != 3:
                    continue
                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": int(parts[2])
                }
                cats_list.append(cat_dict)  
        return cats_list  
        
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except PermissionError:
        print(f"Немає доступу до файлу {path}")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
    
cats = get_cats_info("cat_name_id_age.txt")
print (cats)