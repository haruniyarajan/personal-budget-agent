"""
Sample usage examples for the Personal Budget Agent
This file demonstrates various ways to use the BudgetAgent class
"""

from budget_agent import BudgetAgent, ExpenseCategory

def example_basic_usage():
    """Basic usage example - setting up a budget and tracking expenses"""
    print("=== BASIC USAGE EXAMPLE ===")
    
    # Create a budget agent for someone earning $5000/month
    agent = BudgetAgent(monthly_income=5000)
    
    # Add typical monthly expenses
    expenses = [
        (ExpenseCategory.HOUSING, 1500, "Apartment rent"),
        (ExpenseCategory.FOOD, 600, "Groceries and dining"),
        (ExpenseCategory.TRANSPORTATION, 400, "Car payment and gas"),
        (ExpenseCategory.UTILITIES, 200, "Electricity, water, internet"),
        (ExpenseCategory.ENTERTAINMENT, 300, "Movies, subscriptions, hobbies"),
        (ExpenseCategory.HEALTHCARE, 150, "Health insurance premium"),
        (ExpenseCategory.SAVINGS, 800, "Retirement and emergency fund"),
        (ExpenseCategory.OTHER, 100, "Miscellaneous expenses")
    ]
    
    for category, amount, description in expenses:
        agent.add_expense(category, amount, description)
    
    # Set some budget goals
    agent.set_budget_goal(ExpenseCategory.HOUSING, 1400, priority=1)  # Try to reduce rent
    agent.set_budget_goal(ExpenseCategory.SAVINGS, 1000, priority=1)  # Increase savings
    agent.set_budget_goal(ExpenseCategory.FOOD, 500, priority=2)      # Reduce food spending
    
    # Show the budget summary
    agent.print_budget_summary()
    
    return agent

def example_budget_optimization():
    """Example showing how to use recommendations for budget optimization"""
    print("\n=== BUDGET OPTIMIZATION EXAMPLE ===")
    
    # Create agent with lower income to show budget challenges
    agent = BudgetAgent(monthly_income=3500)
    
    # Add expenses that might be problematic
    agent.add_expense(ExpenseCategory.HOUSING, 1400, "Expensive apartment")  # Over 30%
    agent.add_expense(ExpenseCategory.FOOD, 500, "Eating out frequently")
    agent.add_expense(ExpenseCategory.TRANSPORTATION, 450, "Car payment + insurance")
    agent.add_expense(ExpenseCategory.UTILITIES, 180, "All utilities")
    agent.add_expense(ExpenseCategory.ENTERTAINMENT, 400, "Entertainment overspending")  # Over 10%
    agent.add_expense(ExpenseCategory.SAVINGS, 200, "Minimal savings")  # Under 20%
    agent.add_expense(ExpenseCategory.DEBT, 300, "Credit card payments")
    
    print("Initial budget with financial issues:")
    agent.print_budget_summary()
    
    print("\n" + "="*50)
    print("💡 APPLYING RECOMMENDATIONS...")
    print("="*50)
    
    # Show what the optimized budget could look like
    optimized_budget = agent.create_budget_plan()
    print("\nOptimized budget allocation:")
    for category, amount in optimized_budget.items():
        print(f"{category:15}: ${amount:8.2f}")

def example_data_persistence():
    """Example showing how to save and load budget data"""
    print("\n=== DATA PERSISTENCE EXAMPLE ===")
    
    # Create and populate a budget
    agent = BudgetAgent(monthly_income=4200)
    
    # Add some expenses
    agent.add_expense(ExpenseCategory.HOUSING, 1100, "Rent")
    agent.add_expense(ExpenseCategory.FOOD, 350, "Groceries")
    agent.add_expense(ExpenseCategory.SAVINGS, 800, "Monthly savings")
    
    # Set a goal
    agent.set_budget_goal(ExpenseCategory.SAVINGS, 900, priority=1)
    
    # Save to file
    agent.save_to_file("example_budget.json")
    
    # Create a new agent and load the data
    new_agent = BudgetAgent(0)  # Start with 0 income
    new_agent.load_from_file("example_budget.json")
    
    print("Loaded budget data:")
    new_agent.print_budget_summary()

def example_advanced_analysis():
    """Example showing advanced analysis features"""
    print("\n=== ADVANCED ANALYSIS EXAMPLE ===")
    
    agent = BudgetAgent(monthly_income=6000)
    
    # Add varied expenses to show different spending patterns
    agent.add_expense(ExpenseCategory.HOUSING, 1800, "Mortgage payment")
    agent.add_expense(ExpenseCategory.FOOD, 400, "Groceries")
    agent.add_expense(ExpenseCategory.FOOD, 200, "Restaurants")
    agent.add_expense(ExpenseCategory.TRANSPORTATION, 300, "Car payment")
    agent.add_expense(ExpenseCategory.TRANSPORTATION, 150, "Gas and maintenance")
    agent.add_expense(ExpenseCategory.UTILITIES, 250, "All utilities")
    agent.add_expense(ExpenseCategory.ENTERTAINMENT, 180, "Streaming services")
    agent.add_expense(ExpenseCategory.ENTERTAINMENT, 120, "Hobbies")
    agent.add_expense(ExpenseCategory.HEALTHCARE, 200, "Insurance and medical")
    agent.add_expense(ExpenseCategory.SAVINGS, 1200, "Retirement + emergency")
    agent.add_expense(ExpenseCategory.OTHER, 100, "Miscellaneous")
    
    # Get detailed analysis
    analysis = agent.analyze_spending_patterns()
    
    print("Detailed spending analysis:")
    print(f"Budget health: {analysis['budget_health']}")
    print(f"Savings rate: {(analysis['expense_breakdown'].get('Savings', {}).get('percentage', 0)):.1f}%")
    
    # Show category breakdown
    print("\nSpending by category:")
    for category, data in analysis['expense_breakdown'].items():
        print(f"  {category}: ${data['amount']:.2f} ({data['percentage']:.1f}% of income)")
    
    # Show all recommendations
    recommendations = agent.generate_recommendations()
    print(f"\nGenerated {len(recommendations)} recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")

def example_custom_financial_rules():
    """Example showing how to customize financial rules"""
    print("\n=== CUSTOM FINANCIAL RULES EXAMPLE ===")
    
    agent = BudgetAgent(monthly_income=4000)
    
    # Customize the financial rules for a more aggressive savings approach
    agent.financial_rules = {
        "housing_max_percentage": 0.25,    # Reduce housing to 25% (from 30%)
        "savings_min_percentage": 0.30,    # Increase savings to 30% (from 20%)
        "entertainment_max_percentage": 0.05,  # Reduce entertainment to 5% (from 10%)
        "emergency_fund_months": 12        # Increase emergency fund to 12 months
    }
    
    # Add some expenses
    agent.add_expense(ExpenseCategory.HOUSING, 1000, "Modest housing")
    agent.add_expense(ExpenseCategory.FOOD, 400, "Groceries")
    agent.add_expense(ExpenseCategory.TRANSPORTATION, 300, "Transportation")
    agent.add_expense(ExpenseCategory.UTILITIES, 150, "Utilities")
    agent.add_expense(ExpenseCategory.ENTERTAINMENT, 100, "Minimal entertainment")
    agent.add_expense(ExpenseCategory.SAVINGS, 1200, "Aggressive savings")
    
    print("Budget with custom financial rules (aggressive savings):")
    agent.print_budget_summary()

if __name__ == "__main__":
    # Run all examples
    example_basic_usage()
    example_budget_optimization()
    example_data_persistence()
    example_advanced_analysis()
    example_custom_financial_rules()
    
    print("\n" + "="*50)
    print("🎉 All examples completed successfully!")
    print("="*50)
