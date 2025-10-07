import mysql.connector as con1

try:
    c1 = con1.connect(
        host="localhost",
        user="root",
        password="",
        database="details",
        port=3307
    )
    cr = c1.cursor()

    def insert_data():
        try:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            city = input("Enter city: ")
            qry = "INSERT INTO mytb1 (name, age, city) VALUES (%s, %s, %s)"
            vals = (name, age, city)                                                  #tuple
            cr.execute(qry, vals)
            c1.commit()
            print(f"{cr.rowcount} Data inserted successfully")
        except Exception as e:
            print("Error inserting data:", e)

    def update_data():
        try:
            name = input("Enter name to update: ")
            new_age = int(input("Enter new age: "))
            new_city = input("Enter new city: ")
            qry = "UPDATE mytb1 SET age = %s, city = %s WHERE name = %s"
            vals = (new_age, new_city, name)
            cr.execute(qry, vals) 
            c1.commit()
            print(f"{cr.rowcount} Data updated successfully")
        except Exception as e:
            print("Error updating data:", e)

    def delete_data():
        try:
            name = input("Enter name to delete: ")
            qry = "DELETE FROM mytb1 WHERE name = %s"
            vals = (name,)
            cr.execute(qry, vals)
            c1.commit()
            print(f"{cr.rowcount} Data deleted successfully")
        except Exception as e:
            print("Error deleting data:", e)

    def show_all_data():
        try:
            qry = "SELECT * FROM mytb1"
            cr.execute(qry)
            rows = cr.fetchall()
            if rows:
                print("\nAll Records:")
                i = 1
                for r in rows:
                    #print(f"Person {i} : {r[0]}\t {r[1]}\t {r[2]}")
                    print(f"\nPerson {i}:")
                    print(f"Name:{r[0]}")
                    print(f"Age:{r[1]}")
                    print(f"City:{r[2]}")
                    i += 1
            else:
                print("No data found.")
        except Exception as e:
            print("Error fetching data:", e)

    def show_by_name():
        try:
            name = input("Enter name to search: ")
            qry = "SELECT * FROM mytb1 WHERE name = %s"
            vals = (name,)
            cr.execute(qry, vals)
            results = cr.fetchall()
            if results:
                print("\n Records matching name:")
                for row in results:
                    print(row)
            else:
                print("No data found for that name.")
        except Exception as e:
            print("Error searching data:", e)

    def total_rows():
        try:
            qry = "SELECT COUNT(*) FROM mytb1"
            cr.execute(qry)
            count = cr.fetchone()[0]
            print(f"Total number of rows: {count}")
        except Exception as e:
            print("Error counting rows:", e)

    while True:
        print("\nMENU OPTIONS")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Show All Data")
        print("5. Show by Name")
        print("6. Total Number of Rows")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                insert_data()
            case 2:
                update_data()
            case 3:
                delete_data()
            case 4:
                show_all_data()
            case 5:
                show_by_name()
            case 6:
                total_rows()
            case 7:
                print("Exiting program!!!")
                break
            case _:
                print("Invalid choice. Please try again.")

    c1.close()

except Exception as e:
    print("Could not connect to database:", e)
