from collections import defaultdict

class CashFlowMinimizer:
    def __init__(self):
        self.graph = defaultdict(dict)  # Represent the cash flow graph as an adjacency list

    def add_transaction(self, lender, borrower, amount):
        """
        Adds a transaction to the graph.
        lender: the person who lent the money
        borrower: the person who borrowed the money
        amount: the amount borrowed
        """
        self.graph[lender][borrower] = self.graph[lender].get(borrower, 0) + amount
        self.graph[borrower][lender] = self.graph[borrower].get(lender, 0) - amount

    def minimize_cash_flow(self):
        """
        Minimizes cash flow by finding net amounts for each individual.
        Returns a list of transactions that minimize the cash flow.
        """
        # Step 1: Calculate net balance of each person
        net_balance = defaultdict(int)
        for lender in self.graph:
            for borrower, amount in self.graph[lender].items():
                net_balance[lender] += amount

        # Step 2: Separate creditors and debtors
        creditors = [(person, balance) for person, balance in net_balance.items() if balance > 0]
        debtors = [(person, -balance) for person, balance in net_balance.items() if balance < 0]

        # Sort creditors and debtors by balance
        creditors.sort(key=lambda x: x[1], reverse=True)
        debtors.sort(key=lambda x: x[1], reverse=True)

        # Step 3: Settle debts
        transactions = []

        while creditors and debtors:
            creditor, credit_amount = creditors.pop(0)
            debtor, debt_amount = debtors.pop(0)

            # Determine the minimum amount to settle
            settle_amount = min(credit_amount, debt_amount)
            transactions.append((debtor, creditor, settle_amount))

            # Update balances
            if credit_amount > settle_amount:
                creditors.insert(0, (creditor, credit_amount - settle_amount))
            if debt_amount > settle_amount:
                debtors.insert(0, (debtor, debt_amount - settle_amount))

        return transactions

# Example usage
if __name__ == "__main__":
    cf = CashFlowMinimizer()

    # Add transactions (lender, borrower, amount)
    cf.add_transaction("A", "B", 100)
    cf.add_transaction("B", "C", 50)
    cf.add_transaction("C", "A", 40)

    # Minimize cash flow
    optimized_transactions = cf.minimize_cash_flow()

    print("Optimized Transactions:")
    for debtor, creditor, amount in optimized_transactions:
        print(f"{debtor} pays {creditor} {amount}")

