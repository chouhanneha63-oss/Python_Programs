class Company:
    def company_info(self):
        print("Company: Infosys Ltd")

class Analyst(Company):
    def analyst_info(self):
        print("Role: Data Analyst")
        print("Tools: Python, pandas, SQL")

class Engineer(Company):
    def engineer_info(self):
        print("Role: Data Engineer")
        print("Tools: Spark, Airflow, SQL")

class HybridEmployee(Analyst, Engineer):
    def hybrid_info(self):
        print("Hybrid Role: Analytics Engineer")
        print("Combines Analyst + Engineer responsibilities")

# Create object of most derived class
emp = HybridEmployee()

# Call methods from all inherited classes
emp.company_info()
emp.analyst_info()
emp.engineer_info()
emp.hybrid_info()
