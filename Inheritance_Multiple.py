class HRPolicy:
    def show_policy(self):
        return "HR Policy: 5-day work week, 2 paid leaves/month"

class FinancePolicy:
    def show_finance(self):
        return "Finance Policy: ₹5000 monthly bonus for top performers"

class CompanyRules(HRPolicy, FinancePolicy):
    def show_all(self):
        return f"{self.show_policy()}\n{self.show_finance()}"


rules = CompanyRules()
print(rules.show_all())
