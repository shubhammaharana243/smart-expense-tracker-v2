from datetime import datetime, timedelta
import json

with open("expense.json", "r") as f:
    data_in_file = json.load(f)

current_date = datetime.now().strftime("%d-%m-%Y")


class Expense:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.category = data["category"]
        self.amount = data["amount"]
        self.description = data["description"]

expenses = []

for data in data_in_file:
    expenses.append(Expense(data))

class ExpenseTracker():
    def add_expense(self):
        data_list = []
        print("===== ADD EXPENSE =====")
        while True:
            try:
                amt = int(input("Enter amount: "))
                cate = input("Enter category: ")
                des = input("Enter description: ")

                break

            except ValueError :
                print("\n Please enter valid details\n")
                
        
        data = {
        "id": 1,
        "date": current_date,
        "category": cate.capitalize(),
        "amount": amt,
        "description": des.capitalize()
        }

        if len(expenses) ==0:
            data['id']=1
        else:
            data['id'] =max(expense.id for expense in expenses)+1

        new_expense = Expense(data)
        expenses.append(new_expense)

        for expense in expenses:
            data1 = {
                    "id": expense.id,
                    "date": expense.date,
                    "category": expense.category,
                    "amount": expense.amount,
                    "description": expense.description
                }
            data_list.append(data1)

        with open("expense.json", "w") as f:
            json.dump(data_list, f, indent=4)

        print("\nExpense added successfully! ✅")
        
    def view_expense(self):
        total_amt=0
        print("\n===== ALL EXPENSES =====\n")

        print("ID    Date          Category        Amount      Description")
        print("-----------------------------------------------------------")
        for i in expenses:
            total_amt +=i.amount
            print(f"{i.id:<6}{i.date:<14}{i.category:<16}{i.amount:<12}{i.description}")


        print("-----------------------------------------------------------")
        print(f"Total Expenses: ₹{total_amt}")
        
    def search_expense(self):
        total_found= 0
        total_amt=0
        
        print("\n===== SEARCH EXPENSE =====\n")

        print("Search by:\n"
            "1. Category\n"
            "2. Description\n"
            "3. Amount\n"
            "4. Date\n")

        src_choose = input("Choose: ")

        if src_choose == "1":
            src_data = input("Enter category: ").capitalize()
        elif src_choose == "2":
            src_data = input("Enter description: ").capitalize()
        elif src_choose == "3":
            while True:
                try:
                    src_data = int(input("Enter amount: "))
                    break
                except ValueError:
                    print("Enter correct amount")
        elif src_choose == "4":
            while True:
                try:
                    src_data = input("Enter Date(dd-mm-yyyy): ")
                    break
                except ValueError:
                    print("Enter date in valid formate (dd-mm-yyyy)")
        else:
            print("Enter valid options(1-4)")
            

        print("\n===== SEARCH RESULTS =====\n")
        print("ID    Date          Category        Amount      Description")
        print("-----------------------------------------------------------")

        for expense in expenses:
            if expense.category==src_data:
                total_amt +=expense.amount
                print(f"{expense.id:<6}{expense.date:<14}{expense.category:<16}{expense.amount:<12}{expense.description}")
                total_found +=1

            elif expense.description==src_data:
                total_amt +=expense.amount
                print(f"{expense.id:<6}{expense.date:<14}{expense.category:<16}{expense.amount:<12}{expense.description}")
                total_found +=1

            elif expense.amount==src_data:
                total_amt +=expense.amount
                print(f"{expense.id:<6}{expense.date:<14}{expense.category:<16}{expense.amount:<12}{expense.description}")
                total_found +=1

            elif expense.date==src_data:
                total_amt +=expense.amount
                print(f"{expense.id:<6}{expense.date:<14}{expense.category:<16}{expense.amount:<12}{expense.description}")
                total_found +=1


        print(f"\nTotal found: {total_found}")
        print(f"Total spent: ₹{total_amt}")
        
    def monthly_summary(self):
        no = 0
        monthly_total=0
        highest_expense = 0
        lowest_expense=0
        list =[]
        dic = {}
        data_in_month= []
        monthly_data = []

        def monthname(m):
            if m=='01':
                print(f"\n===== JANUARY {y} =====\n")
            elif m=='02':
                print(f"\n===== FEBRUARY {y} =====\n")
            elif m=='03':
                print(f"\n===== MARCH {y} =====\n")
            elif m=='04':
                print(f"\n===== APRIL {y} =====\n")
            elif m=='05':
                print(f"\n===== MAY {y} =====\n")
            elif m=='06':
                print(f"\n===== JUNE {y} =====\n")
            elif m=='07':
                print(f"\n===== JULY {y} =====\n")
            elif m=='08':
                print(f"\n===== AUGUST {y} =====\n")
            elif m=='09':
                print(f"\n===== SEPTEMBER {y} =====\n")
            elif m=='10':
                print(f"\n===== OCTOBER {y} =====\n")
            elif m=='11':
                print(f"\n===== NOVEMBER {y} =====\n")
            elif m=='12':
                print(f"\n===== DECEMBER {y} =====\n")
    
        while True:
            try:
                
                m = input("Enter month(MM): ")
                y = input("Enter year(YYYY): ")

                break

            except ValueError :
                print("\n Please enter valid details\n")

        data_found = False

        for expense in expenses:
            if f"{m}-{y}" in expense.date:
                data_found = True  

        if not data_found:
            print("No data found for this month in the database.")
            return

        if data_found:
            monthname(m)
                
            for expense in expenses:
                if expense.category not in list:
                    list.append(expense.category)


            for expense in expenses:
                date_in_list = expense.date.split('-')

                if date_in_list[1]==m and date_in_list[2]==y:    
                    data_in_month.append(expense)

                    monthly_total+= expense.amount
                    no +=1
                    if expense.amount> highest_expense:
                        highest_expense=expense.amount
        
            for i in data_in_month:    
                if i.category not in dic:
                    dic[i.category]=i.amount
                else:
                    dic[i.category] += i.amount

                                
            lowest_expense = min(data_in_month, key=lambda x:x.amount)        
            print(f"Total Expenses: ₹{monthly_total}\n")
            print(f"Number of Expenses: {no}\n")
            print(f"Highest Expense: ₹{highest_expense}")
            print(f"Lowest Expense: ₹{lowest_expense.amount}")
            print(f"Avarage Expense: ₹{(monthly_total/no):.2f}\n")

            print("Highest Spending Category:")
            highest_expense_in_dic = max(dic, key=dic.get)
            print(f"{highest_expense_in_dic} -> ₹{dic[highest_expense_in_dic]}\n")

            print("Lowest Spending Category:")
            lowest_expense_in_dic = min(dic, key=dic.get)
            print(f"{lowest_expense_in_dic} -> ₹{dic[lowest_expense_in_dic]}")
    
    def category_analysis(self):
        list = []
        dic ={}
        total_expenses = 0
        
        for expense in expenses:
            total_expenses +=expense.amount

        for expense in expenses:
            if expense.category not in list:
                list.append(expense.category)

        for expense in expenses:
            for j in range(0,len(list)):
                if list[j]==expense.category:
                    if expense.category not in dic:
                        di = {expense.category:expense.amount}
                        dic.update(di)
                    else:
                        dic[expense.category] = dic[expense.category] + expense.amount
        



        print("\n===== CATEGORY ANALYSIS =====\n")

        sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse =True)
        for key, value in sorted_dict:
            print(f"{key.capitalize():<16} ₹{value}")
            
        print("------------------------------")
        t="Total"
        print(f"{t:<16} ₹{total_expenses}")
        
    def budget_status(self):
        total_expenses = 0
        last_month_expense_data = []
        today = datetime.now()
        last_month_date = (today - timedelta(days=today.day))
        last_month = last_month_date.month
        last_month_year = last_month_date.year

        while True:
            try:
                monthly_budget = int(input("Enter your monthly budget: ₹"))
                
                break
            
            except ValueError :
                print("\n Please enter valid details\n")

        for expense in expenses:
            if f"{last_month}-{last_month_year}" in expense.date:
                last_month_expense_data.append(expense.amount)

        total_expenses = sum(last_month_expense_data)                
            
        
        print("\n===== BUDGET STATUS FOR LAST MONTH =====\n")

        print(f"Monthly Budget:    ₹{monthly_budget}")
        print(f"Total Spent in last month:       ₹{total_expenses}")
        print(f"Remaining:         ₹{monthly_budget-total_expenses}")

        print(f"\nUsed: {(total_expenses/monthly_budget*100):.2f}%")

        if monthly_budget>total_expenses:
            print("\nStatus: ✅ Within Budget")
        else:
            print("\nStatus: ⚠️ BUDGET EXCEEDED\n")
            print(f"You have exceeded your budget by ₹{total_expenses-monthly_budget}.\n")

        check = input("\nWould you like to see this month's expenses? (y/n): ")

        if check.lower() =="y":
            current_month_expense_data = []
            current_month = today.month
            current_month_year = today.year

            for expense in expenses:
                if f"{current_month}-{current_month_year}" in expense.date:
                    current_month_expense_data.append(expense.amount)

            current_month_total_expenses = sum(current_month_expense_data)  

            print("\n===== BUDGET STATUS FOR CURRENT MONTH =====\n")
            
            print(f"Monthly Budget:    ₹{monthly_budget}")
            print(f"Total Spent in this month:       ₹{current_month_total_expenses}")
            print(f"Remaining:         ₹{monthly_budget-current_month_total_expenses}")
    
            print(f"\nUsed: {(current_month_total_expenses/monthly_budget*100):.2f}%")
    
            if monthly_budget>current_month_total_expenses:
                print("\nStatus: ✅ Within Budget")
            else:
                print("\nStatus: ⚠️ BUDGET EXCEEDED\n")
                print(f"You have exceeded your budget by ₹{current_month_total_expenses-monthly_budget}.\n")

        elif check.lower() == "n":
            pass
        else:
            print("\nEnter Y and N\n")

    def update_expense(self):
        total_data_found = 0
        data_list = []
        update_list = []

        print("\n===== UPDATE EXPENSE =====\n")
        print("Enter the Date of expense you want to update")
        update_by_date = input("Formate (DD-MM-YYYY): ")
        print("\nSearching records...\n")

        for expense in expenses:
            if update_by_date in expense.date:
                data_list.append(expense)
                data_found = True
        if not data_list:
            data_found = False
            print(f"\nNo expenses found for date: {update_by_date}")

        if data_found:  
            total_data_found = len(data_list)

            print(f"\n===== EXPENSES FOR {update_by_date} =====\n")
            
            print("ID    Date          Category        Amount      Description")
            print("-----------------------------------------------------------")
            for i in data_list:
                print(f"{i.id:<6}{i.date:<14}{i.category:<16}{i.amount:<12}{i.description}")

            print(f"\nTotal found: {total_data_found}")
            found = False
            update_by_id = input("\nEnter the ID of the expense to update (or 0 to cancel): ")
            for i in data_list:
                if update_by_id == '0':
                    update = False
                    found = True
                elif i.id == int(update_by_id):
                    found = True
                    update = True
            if not found:
                print("Invalid Option")
                update = False

            if update:
                for i in data_list:
                    if i.id == int(update_by_id):
                        found = True
                        print("Enter new details (Press ENTER to KEEP current value):\n")
                        new_category = input(f"New Category [{i.category}]: ")
                        if new_category == '':
                            new_category = i.category

                        new_amount = input("New Amount: ")
                        if new_amount == '':
                            new_amount = i.amount

                        new_description = input(f"New description [{i.description}]: ")
                        if new_description == '':
                            new_description = i.description

                        print("\n==== CONFIRM CHANGES ====\n")

                        print(f"Old: {i.category} | {i.amount} | {i.description}")
                        print(f"New: {new_category} | {new_amount} | {new_description}")

                        update_or_not = input("\n⚠️  Save these changes? (y/n): ")
                        if update_or_not == "y":
                            for expense in expenses:
                                if expense.id == int(update_by_id):
                                    expense.category = new_category
                                    expense.amount = int(new_amount)
                                    expense.description = new_description
                            for j in expenses:
                                data2 = {
                                        "id": j.id,
                                        "date": j.date,
                                        "category": j.category,
                                        "amount": j.amount,
                                        "description": j.description
                                    }
                                update_list.append(data2)
                            with open("expense.json", "w") as f:
                                json.dump(update_list, f, indent=4)
                            print("\n✅ Expense updated successfully!")
                        elif update_or_not == 'n':
                            pass
                        else: 
                            print("Invalid option")
                        
    def delete_expense(self):
        total_data_found = 0
        print("\n======== DELTE EXPENSE ========\n")
        print("Search for the item you want to delete:\n"
                "1. Search by Category first\n"
                "2. Search by Description first\n"
                "3. Search by Date first\n"
                "4. Cancel and Go Back\n")

        choose = input("Choose: ")

        if choose == "1":
            update_list = []
            data_list = []
            delete_by = input("Enter category: ").capitalize()

            for expense in expenses:
                if delete_by in expense.category:
                    data_list.append(expense)
                    data_found = True
            if not data_list:
                data_found = False
                print(f"\nCategory '{delete_by}' does not exist")

            if data_found: 
                total_data_found = len(data_list)

                print("\n===== MATCHING EXPENSES =====\n")
                
                print("ID    Date          Category        Amount      Description")
                print("-----------------------------------------------------------")
                for i in data_list:
                    print(f"{i.id:<6}{i.date:<14}{i.category:<16}{i.amount:<12}{i.description}")

                print(f"\nTotal found: {total_data_found}")
                found = False
                delete_by_id = input("\nEnter the ID of the expense you want to DELETE (or 0 to cancel): ")
                for i in data_list:
                    if delete_by_id == "0":
                        delete_or_not =None
                        found = True
                        break

                    elif int(delete_by_id) == i.id:
                        delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()
                        found = True
                        break                     
                if not found:
                    print("Invalid Option")
                    delete_or_not = None
                if delete_or_not is not None:
                    while True:
                        if delete_or_not =="y":
                            expenses[:] = [item for item in expenses if item.id != int(delete_by_id)]
                            for expense in expenses:
                                data2 = {
                                        "id": expense.id,
                                        "date": expense.date,
                                        "category": expense.category,
                                        "amount": expense.amount,
                                        "description": expense.description
                                    }
                                update_list.append(data2)
                    
                            with open("expense.json", "w") as f:
                                json.dump(update_list, f, indent=4)

                            print("✅ Expense deleted successfully!")
                            break
                        elif delete_or_not =="n":
                            break
                            
                        else:
                            print("Invalid option")
                            delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()
                                               
        elif choose =="2":
            update_list = []
            data_list =[]
            delete_by = input("Enter description: ").capitalize()
            
            for expense in expenses:
                if delete_by in expense.description:
                    data_list.append(expense)
                    data_found = True
            if not data_in_file:
                data_found = False
                print(f"\n Description '{delete_by}' does not exist")

            if data_found:  
                total_data_found = len(data_list)

                print("\n===== MATCHING EXPENSES =====\n")
                
                print("ID    Date          Category        Amount      Description")
                print("-----------------------------------------------------------")
                for i in data_list:
                    print(f"{i.id:<6}{i.date:<14}{i.category:<16}{i.amount:<12}{i.description}")

                print(f"\n Total found: {total_data_found}")

                delete_by_id = input("\nEnter the ID of the expense you want to DELETE (or 0 to cancel): ")
                found = False

                for i in data_list:
                    if delete_by_id == "0":
                        delete_or_not =None
                        found = True
                        break

                    elif int(delete_by_id) == i.id:
                        delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()
                        found = True
                        break

                if not found:
                    print("Invalid Option")
                    delete_or_not = None
                    
                if delete_or_not is not None:
                    while True:
                        if delete_or_not =="y":
                            expenses[:] = [item for item in expenses if item.id != int(delete_by_id)]
                            for expense in expenses:
                                data2 = {
                                        "id": expense.id,
                                        "date": expense.date,
                                        "category": expense.category,
                                        "amount": expense.amount,
                                        "description": expense.description
                                    }
                                update_list.append(data2)
                    
                            with open("expense.json", "w") as f:
                                json.dump(update_list, f, indent=4)

                            print("✅ Expense deleted successfully!")
                            break
                        elif delete_or_not =="n":
                            break
                        else:
                            print("Invalid option")
                            delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()

        elif choose =="3":
            update_list = []
            data_list = []
            delete_by = input("Enter Date(DD-MM-YYYY): ")
            for expense in expenses:
                if delete_by in expense.date:
                    data_list.append(expense)
                    data_found = True
            if not data_in_file:
                data_found = False
                print(f"\nNo expenses found for date: {delete_by}")
            
            if data_found:  
                total_data_found = len(data_list)

                print("\n===== MATCHING EXPENSES =====\n")
                
                print("ID    Date          Category        Amount      Description")
                print("-----------------------------------------------------------")
                for i in data_list:
                    print(f"{i.id:<6}{i.date:<14}{i.category:<16}{i.amount:<12}{i.description}")

                print(f"\nTotal found: {total_data_found}")
                found = False
                delete_by_id = input("\nEnter the ID of the expense you want to DELETE (or 0 to cancel): ")
                for i in data_list:
                    while True:
                        if delete_by_id == "0":
                            delete_or_not =None
                            found = True
                            break

                        elif int(delete_by_id) == i.id:
                            delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()
                            found = True
                            break
                if not found:
                    print("Invalid Option")
                    delete_or_not = None

                if delete_or_not is not None:
                    while True:
                        if delete_or_not =="y":
                            expenses[:] = [item for item in expenses if item.id != int(delete_by_id)]
                            for expense in expenses:
                                data2 = {
                                        "id": expense.id,
                                        "date": expense.date,
                                        "category": expense.category,
                                        "amount": expense.amount,
                                        "description": expense.description
                                    }
                                update_list.append(data2)
                    
                            with open("expense.json", "w") as f:
                                json.dump(update_list, f, indent=4)

                            print("✅ Expense deleted successfully!")
                            break
                        elif delete_or_not =="n":
                            break
                        else:
                            print("Invalid option")
                            delete_or_not = input(f"\n⚠️  Are you sure you want to delete {i.id} [{i.category} | {i.amount} | {i.description}]? (y/n): ").lower()
                         
        elif choose =="4":
            pass
        else:
            print("Invalid option")
        
    def exit(self):
        print("\n===== SMART EXPENSE TRACKER =====\n")

        print("Thank you for using Smart Expense Tracker! \n")
        print("Your data has been saved successfully.\n")
        print("Goodbye!")

def main():
    tracker = ExpenseTracker()
    print("\n===== SMART EXPENSE TRACKER =====")

    while True:
        print("\nHere are the available options:\n"
                "1. Add Expense\n"
                "2. View Expenses\n"
                "3. Search Expense\n"
                "4. Monthly Summary\n"
                "5. Category Analysis\n"
                "6. Budget Check\n"
                "7. Update Expense\n"
                "8. Delete Expense\n"
                "9. Exit\n")

        choose = input("Choose: ")

        if choose == "1":
            tracker.add_expense()
        elif choose == "2":
            tracker.view_expense()
        elif choose == "3":
            tracker.search_expense()
        elif choose == "4":
            tracker.monthly_summary()
        elif choose == "5":
            tracker.category_analysis()
        elif choose == "6":
            tracker.budget_status()
        elif choose == "7":
            tracker.update_expense()
        elif choose == "8":
            tracker.delete_expense()
        elif choose == "9":
            exit()
            break
        else:
            print("\n⚠️Please enter avilable option(1-7)")

if __name__ == "__main__":
    main()