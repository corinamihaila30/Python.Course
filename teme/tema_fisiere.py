taskuri = []
categorii = set()

while True:
    print("\nMeniu:")
    print("1. Adăugare categorie")
    print("2. Adăugare task")
    print("3. Listare date")
    print("0. Ieșire")

    optiune = input("Alegeți o opțiune: ")

    if optiune == "1":
        categorie = input("Introduceți o categorie: ")
        categorii.add(categorie)
    elif optiune == "2":
        task = input("Introduceți un task: ")
        data_limita = input("Introduceți data limită (format: DD.MM.YYYY HH:MM): ")
        persoana_responsabila = input("Introduceți persoana responsabilă: ")
        
        while True:
            categorie = input("Introduceți categoria: ")
            if categorie in categorii:
                break
            else:
                print("Categoria nu există. Introduceți o categorie validă.")

        task_nou = {
            "task": task,
            "data_limita": data_limita,
            "persoana_responsabila": persoana_responsabila,
            "categorie": categorie
        }

        taskuri.append(task_nou)
    elif optiune == "3":
        taskuri_sortate = sorted(taskuri, key=lambda x: x['categorie'])
        for task in taskuri_sortate:
            print(f"Task: {task['task']}, Data limită: {task['data_limita']}, Persoană responsabilă: {task['persoana_responsabila']}, Categorie: {task['categorie']}")
    elif optiune == "0":
        break
    else:
        print("Opțiune invalidă. Alegeți din nou.")
