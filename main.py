from finance_manager import Transaction,FinanceManager

Fm = FinanceManager()
Fm.load_from_file()

# Fm.add_transaction(Transaction(50000, "income", 'salary'))
# Fm.add_transaction(Transaction(10000, "expense", 'rent'))
# Fm.add_transaction(Transaction(5000, "expense", 'food'))
# Fm.add_transaction(Transaction(7000, "expense", 'clothes'))
# Fm.add_transaction(Transaction(3000, "expense", 'transport'))
# Fm.add_transaction(Transaction(30000, "income", 'stock'))

print("Balance: ", Fm.get_balance())
print("Summary of this month: ", Fm.get_summary())

Fm.save_to_file()