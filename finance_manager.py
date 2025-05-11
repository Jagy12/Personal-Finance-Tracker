from datetime import datetime
import pickle

class Transaction():
    def __init__(self, amount, t_type, category, date = None):
        self.amount = amount
        self.type = t_type
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
    
    def __repr__(self):
        return f"{self.date} | {self.t_type} | {self.category} | Rs{self.amount}"

class FinanceManager():
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
    
    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.type == 'income')
        expense = sum(t.amount for t in self.transactions if t.type == 'expense')
        return income - expense

    def get_summary(self):
        summary = {}
        for t in self.transactions:
            if t.category not in summary:
                summary[t.category] = 0
            if t.type == "income":
                summary[t.category] += t.amount
            else:
                summary[t.category] -= t.amount
        return summary
    
    def save_to_file(self, filename = 'data.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.transactions, f)
    
    def load_from_file(self, filename = 'data.pkl'):
        try:
            with open(filename, 'rb') as f:
                self.transactions = pickle.load(f)
        except FileNotFoundError:
            self.transactions = []