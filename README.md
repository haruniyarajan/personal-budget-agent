# 🤖 Personal Budget Agent

An intelligent agent-based budget calculator that helps individuals manage their monthly finances, track expenses, and receive personalized financial recommendations.

## 🌟 Features

- **Expense Tracking**: Categorize and track all your monthly expenses
- **Budget Goal Setting**: Set and monitor budget targets for different categories
- **Intelligent Analysis**: Get insights into your spending patterns
- **Personalized Recommendations**: Receive AI-driven financial advice
- **Data Persistence**: Save and load your budget data from JSON files
- **Budget Health Monitoring**: Real-time assessment of your financial health

## 🏗️ Architecture

This project uses an agent-based approach where the `BudgetAgent` acts as an intelligent financial advisor that:
- Analyzes spending behavior
- Provides contextual recommendations
- Monitors budget goals
- Suggests optimal budget allocations

## 📊 Expense Categories

- Housing (Rent, Mortgage)
- Food (Groceries, Dining)
- Transportation (Car, Public Transit)
- Utilities (Electricity, Water, Internet)
- Entertainment (Movies, Games, Subscriptions)
- Healthcare (Insurance, Medical bills)
- Savings (Emergency fund, Investments)
- Debt Payment (Credit cards, Loans)
- Other (Miscellaneous expenses)

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- No external dependencies required (uses only standard library)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/personal-budget-agent.git
cd personal-budget-agent
```

2. Run the application:
```bash
python budget_agent.py
```

### Basic Usage

```python
from budget_agent import BudgetAgent, ExpenseCategory

# Initialize the agent with your monthly income
agent = BudgetAgent(monthly_income=4000)

# Add expenses
agent.add_expense(ExpenseCategory.HOUSING, 1200, "Monthly rent")
agent.add_expense(ExpenseCategory.FOOD, 400, "Groceries")

# Set budget goals
agent.set_budget_goal(ExpenseCategory.HOUSING, 1300, priority=1)

# Get analysis and recommendations
agent.print_budget_summary()
```

## 💡 Key Methods

### Core Functionality
- `add_expense(category, amount, description)` - Track a new expense
- `set_budget_goal(category, target_amount, priority)` - Set spending targets
- `analyze_spending_patterns()` - Get detailed spending analysis
- `generate_recommendations()` - Receive personalized financial advice
- `print_budget_summary()` - Display comprehensive budget overview

### Data Management
- `save_to_file(filename)` - Save budget data to JSON
- `load_from_file(filename)` - Load existing budget data
- `create_budget_plan()` - Generate recommended budget allocation

## 📈 Sample Output

```
💰 PERSONAL BUDGET SUMMARY
==================================================
Monthly Income: $4,000.00
Total Expenses: $2,750.00
Remaining Budget: $1,250.00
Budget Health: GOOD

📊 EXPENSE BREAKDOWN:
------------------------------
Housing        : $ 1200.00 (30.0%)
Food           : $  400.00 (10.0%)
Transportation : $  300.00 (7.5%)
Utilities      : $  150.00 (3.8%)
Entertainment  : $  200.00 (5.0%)
Savings        : $  500.00 (12.5%)

💡 RECOMMENDATIONS:
------------------------------
1. 💰 Increase savings to at least 20% of income. Add $300.00 to savings.
2. 🚨 Build an emergency fund of $24,000.00 (6 months of income) for financial security.
```

## 🎯 Financial Rules & Guidelines

The agent follows these built-in financial best practices:
- **Housing**: Maximum 30% of income
- **Savings**: Minimum 20% of income
- **Emergency Fund**: 6 months of expenses
- **Entertainment**: Maximum 10% of income

## 🗂️ Project Structure

```
personal-budget-agent/
│
├── budget_agent.py          # Main application code
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies (empty - uses stdlib)
├── budget_data.json       # Saved budget data (generated)
└── examples/              # Usage examples
    └── sample_usage.py    # Demonstration script
```

## 🔧 Customization

You can easily customize the financial rules by modifying the `financial_rules` dictionary:

```python
agent.financial_rules = {
    "housing_max_percentage": 0.25,    # Reduce housing to 25%
    "savings_min_percentage": 0.25,    # Increase savings to 25%
    "entertainment_max_percentage": 0.05,  # Reduce entertainment to 5%
    "emergency_fund_months": 3         # 3-month emergency fund
}
```

## 📝 Example Use Cases

1. **Monthly Budget Planning**: Set up your income and track all expenses
2. **Financial Goal Tracking**: Monitor progress toward savings and spending targets
3. **Expense Analysis**: Understand where your money is going each month
4. **Financial Health Check**: Get recommendations for improving your budget
5. **Budget Optimization**: Receive suggestions for better money allocation

## 🚦 Getting Started

1. **First Time Setup**: Enter your monthly income and start adding expenses
2. **Daily Usage**: Add expenses as they occur throughout the month
3. **Weekly Review**: Check your budget summary and recommendations
4. **Monthly Planning**: Analyze spending patterns and adjust goals for next month

## 🤝 Contributing

Contributions are welcome! Here are some ways to improve the project:

- Add new expense categories
- Implement more sophisticated financial analysis
- Create a web interface using Flask/Django
- Add data visualization with matplotlib
- Implement machine learning for spending predictions
- Add bill reminder functionality
- Create mobile app integration


## 🔮 Future Enhancements

- [ ] Web dashboard with charts and graphs
- [ ] Integration with bank APIs for automatic expense tracking
- [ ] Machine learning for spending pattern prediction
- [ ] Multi-user support for families
- [ ] Mobile app companion
- [ ] Integration with popular budgeting apps
- [ ] Advanced reporting and analytics
- [ ] Debt payoff planning tools

---

⭐ **If you find this project helpful, please give it a star!** ⭐
