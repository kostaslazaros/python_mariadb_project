import random

from crud_mariadb import BiodataAdmin

# from crud_sqlite import BiodataAdmin


dba = BiodataAdmin()


def create_random_pleiada():
    typ = random.choice(("RNA", "DNA"))
    if typ == "RNA":
        seq = "".join(random.choices("AUCG", k=10))
    else:
        seq = "".join(random.choices("ATCG", k=10))
    etos = str(random.choice(list(range(2000, 2024))))
    organism = random.choice(("Human", "Mouse"))
    return {"seq": seq, "typ": typ, "etos": etos, "organism": organism}


def print_menu():
    print("1 Δημιουργία/Διαγραφή Πίνακα")
    print("2 Εισαγωγή 10 πλειάδων")
    print("3 Εισαγωγή νέας πλειάδας")
    print("4 Διαγραφή όλων των πλειάδων")
    print("5 Διαγραφή συγκεκριμένης πλειάδας")
    print("6 Αναζήτηση με βάση το αναγνωριστικό")
    print("7 Έξοδος")
    print("")


def create_table():
    dba.create_table()
    print("\nΟ πίνακας δημιουργήθηκε\n")
    return True


def insert10():
    if not dba.table_exists():
        print("Δημιουργείστε πρώτα τον πίνακα παρακαλώ.")
        return True
    for _ in range(10):
        dba.insert(**create_random_pleiada())
    print("Εισάχθηκαν 10 πλειάδες")
    return True


def insert():
    if not dba.table_exists():
        print("Δημιουργείστε πρώτα τον πίνακα παρακαλώ.")
        return True
    print("\nΕισαγωγή πλειάδας")
    sequence = input("Ακολουθία : ")
    typos = input("Τύπος     : ")
    etos = input("Έτος      : ")
    organism = input("Οργανισμός: ")
    dba.insert(sequence, typos, etos, organism)
    print("Έγινε εισαγωγή μίας πλειάδας")
    return True


def delete_all():
    if not dba.table_exists():
        print("Δημιουργείστε πρώτα τον πίνακα παρακαλώ.")
        return True
    dba.delete_all()
    print("Διαγράφηκαν όλες οι πλειάδες")
    return True


def delete():
    if not dba.table_exists():
        print("Δημιουργείστε πρώτα τον πίνακα παρακαλώ.")
        return True
    anagnoristiko = input("Δώστε ακολουθία για διαγραφή: ")
    dba.delete_one(anagnoristiko)
    print(f"Διαγράφηκε η πλειάδα με αναγνωριστικό {anagnoristiko}")
    return True


def select():
    if not dba.table_exists():
        print("Δημιουργείστε πρώτα τον πίνακα παρακαλώ.")
        return True
    anagnoristiko = input("Δώστε αναγνωριστικό για αναζήτηση: ")
    record = dba.select_one(anagnoristiko)
    print(f"Επιλέχτηκε η πλειάδα με αναγνωριστικό {anagnoristiko}\n")
    print(f"{record} \n")
    return True


def exita():
    print("Έξοδος από την εφαρμογή. Καλή συνέχεια.")
    return False


options = {
    "1": create_table,
    "2": insert10,
    "3": insert,
    "4": delete_all,
    "5": delete,
    "6": select,
    "7": exita,
}


def menu():
    answer = "0"
    tries = 0
    while answer not in options:
        if tries > 0:
            print(f"Μη έγκυρη επιλογή {answer}. Προσπαθήστε ξανά.\n")
        print_menu()
        answer = input("Επιλεξτε ενέργεια: ")
        tries += 1
    return answer


def main():
    status = True
    while status:
        answer = menu()
        status = options[answer]()


if __name__ == "__main__":
    main()
