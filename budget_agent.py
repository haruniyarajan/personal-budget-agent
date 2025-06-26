"""
Personal Budget Agent - An intelligent budget calculator and advisor
Author: Your Name
Description: An agent-based system that calculates monthly budgets, 
tracks expenses, and provides financial recommendations.
"""

import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class ExpenseCategory(Enum):
    HOUSING = "Housing"
    FOOD = "Food" 
    TRANSPORTATION = "Transportation"
    UTILITIES = "Utilities"
    ENTERTAINMENT = "Entertainment"
    HEALTHCARE = "Healthcare"
    SAVINGS = "Savings"
    DEBT = "Debt Payment"
    OTHER = "Other"

@dataclass
class Expense:
    category: ExpenseCategory
    amount: float
    description: str
    date: str = None
    
    def __post_init__(self):
        if self.date is None:
            self.date = datetime.date.today().isoformat()

@dataclass
class BudgetGoal:
    category: ExpenseCategory
    target_amount: float
    priority: int  # 1-5, where 1 is highest priority

class BudgetAgent:
    """
    An intelligent agent that manages personal budgets, tracks expenses,
    and provides financial recommendations based on spending patterns.
    """
    
    def __init__(self, monthly_income: float):
        self.monthly_income = monthly_income
        self.expenses: List[Expense] = []
        self.budget_goals: List[BudgetGoal] = []
        self.financial_rules = {
            "housing_max_percentage": 0.30,
            "savings_min_percentage": 0.20,
            "entertainment_max_percentage": 0.10,
            "emergency_fund_months": 6
        }
    
    def add_expense(self, category: ExpenseCategory, amount: float, description: str) -> None:
        """Add a new expense to the tracking system."""
        expense = Expense(category, amount, description)
        self.expenses.append(expense)
        print(f"✅ Added expense: {description} - ${amount:.2f}")
    
    def set_budget_goal(self, category: ExpenseCategory, target_amount: float, priority: int = 3) -> None:
        """Set a budget goal for a specific category."""
        goal = BudgetGoal(category, target_amount, priority)
        
        # Remove existing goal for this category if it exists
        self.budget_goals = [g for g in self.budget_goals if g.category != category]
        self.budget_goals.append(goal)
        
        print(f"🎯 Set budget goal: {category.value} - ${target_amount:.2f}")
    
    def calculate_category_totals(self) -> Dict[ExpenseCategory, float]:
        """Calculate total spending by category."""
        totals = {}
        for expense in self.expenses:
            if expense.category not in totals:
                totals[expense.category] = 0
            totals[expense.category] += expense.amount
        return totals
    
    def get_remaining_budget(self) -> float:
        """Calculate remaining budget after all expenses."""
        total_expenses = sum(expense.amount for expense in self.expenses)
        return self.monthly_income - total_expenses
    
    def analyze_spending_patterns(self) -> Dict[str, any]:
        """Analyze spending patterns and provide insights."""
        category_totals = self.calculate_category_totals()
        total_expenses = sum(category_totals.values())
        
        analysis = {
            "total_income": self.monthly_income,
            "total_expenses": total_expenses,
            "remaining_budget": self.get_remaining_budget(),
            "expense_breakdown": {},
            "budget_health": "good"
        }
        
        # Calculate percentages
        for category, amount in category_totals.items():
            percentage = (amount / self.monthly_income) * 100 if self.monthly_income > 0 else 0
            analysis["expense_breakdown"][category.value] = {
                "amount": amount,
                "percentage": percentage
            }
        
        # Determine budget health
        if self.get_remaining_budget() < 0:
            analysis["budget_health"] = "critical"
        elif self.get_remaining_budget() < self.monthly_income * 0.1:
            analysis["budget_health"] = "concerning"
        
        return analysis
    
    def generate_recommendations(self) -> List[str]:
        """Generate personalized financial recommendations."""
        recommendations = []
        category_totals = self.calculate_category_totals()
        
        # Check housing expenses
        housing_amount = category_totals.get(ExpenseCategory.HOUSING, 0)
        housing_percentage = housing_amount / self.monthly_income
        if housing_percentage > self.financial_rules["housing_max_percentage"]:
            recommendations.append(
                f"🏠 Housing costs ({housing_percentage:.1%}) exceed recommended 30%. "
                f"Consider reducing by ${housing_amount - (self.monthly_income * 0.30):.2f}"
            )
        
        # Check savings
        savings_amount = category_totals.get(ExpenseCategory.SAVINGS, 0)
        savings_percentage = savings_amount / self.monthly_income
        if savings_percentage < self.financial_rules["savings_min_percentage"]:
            recommendations.append(
                f"💰 Increase savings to at least 20% of income. "
                f"Add ${(self.monthly_income * 0.20) - savings_amount:.2f} to savings."
            )
        
        # Check entertainment spending
        entertainment_amount = category_totals.get(ExpenseCategory.ENTERTAINMENT, 0)
        entertainment_percentage = entertainment_amount / self.monthly_income
        if entertainment_percentage > self.financial_rules["entertainment_max_percentage"]:
            recommendations.append(
                f"🎭 Entertainment spending ({entertainment_percentage:.1%}) is high. "
                f"Consider reducing by ${entertainment_amount - (self.monthly_income * 0.10):.2f}"
            )
        
        # Check if overspending
        if self.get_remaining_budget() < 0:
            recommendations.append(
                f"⚠️ You're overspending by ${abs(self.get_remaining_budget()):.2f}. "
                "Review expenses and cut non-essential items."
            )
        
        # Emergency fund recommendation
        emergency_fund_target = self.monthly_income * self.financial_rules["emergency_fund_months"]
        recommendations.append(
            f"🚨 Build an emergency fund of ${emergency_fund_target:.2f} "
            f"(6 months of income) for financial security."
        )
        
        return recommendations
    
    def create_budget_plan(self) -> Dict[str, float]:
        """Create a recommended budget allocation based on income."""
        return {
            "Housing": self.monthly_income * 0.30,
            "Food": self.monthly_income * 0.15,
            "Transportation": self.monthly_income * 0.15,
            "Utilities": self.monthly_income * 0.10,
            "Savings": self.monthly_income * 0.20,
            "Entertainment": self.monthly_income * 0.05,
            "Healthcare": self.monthly_income * 0.03,
            "Other": self.monthly_income * 0.02
        }
    
    def save_to_file(self, filename: str = "budget_data.json") -> None:
        """Save budget data to a JSON file."""
        data = {
            "monthly_income": self.monthly_income,
            "expenses": [asdict(expense) for expense in self.expenses],
            "budget_goals": [asdict(goal) for goal in self.budget_goals],
            "last_updated": datetime.datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        print(f"💾 Budget data saved to {filename}")
    
    def load_from_file(self, filename: str = "budget_data.json") -> None:
        """Load budget data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.monthly_income = data["monthly_income"]
            
            # Load expenses
            self.expenses = []
            for expense_data in data.get("expenses", []):
                expense = Expense(
                    ExpenseCategory(expense_data["category"]),
                    expense_data["amount"],
                    expense_data["description"],
                    expense_data["date"]
                )
                self.expenses.append(expense)
            
            # Load budget goals
            self.budget_goals = []
            for goal_data in data.get("budget_goals", []):
                goal = BudgetGoal(
                    ExpenseCategory(goal_data["category"]),
                    goal_data["target_amount"],
                    goal_data["priority"]
                )
                self.budget_goals.append(goal)
            
            print(f"📂 Budget data loaded from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Starting with empty budget.")
    
    def print_budget_summary(self) -> None:
        """Print a comprehensive budget summary."""
        print("\n" + "="*50)
        print("💰 PERSONAL BUDGET SUMMARY")
        print("="*50)
        
        analysis = self.analyze_spending_patterns()
        
        print(f"Monthly Income: ${analysis['total_income']:,.2f}")
        print(f"Total Expenses: ${analysis['total_expenses']:,.2f}")
        print(f"Remaining Budget: ${analysis['remaining_budget']:,.2f}")
        print(f"Budget Health: {analysis['budget_health'].upper()}")
        
        print("\n📊 EXPENSE BREAKDOWN:")
        print("-" * 30)
        for category, data in analysis['expense_breakdown'].items():
            print(f"{category:15}: ${data['amount']:8.2f} ({data['percentage']:.1f}%)")
        
        print("\n🎯 BUDGET GOALS:")
        print("-" * 30)
        if self.budget_goals:
            for goal in sorted(self.budget_goals, key=lambda x: x.priority):
                actual = analysis['expense_breakdown'].get(goal.category.value, {}).get('amount', 0)
                status = "✅" if actual <= goal.target_amount else "❌"
                print(f"{goal.category.value:15}: ${goal.target_amount:8.2f} (Actual: ${actual:8.2f}) {status}")
        else:
            print("No budget goals set.")
        
        print("\n💡 RECOMMENDATIONS:")
        print("-" * 30)
        recommendations = self.generate_recommendations()
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
        
        print("\n📋 SUGGESTED BUDGET ALLOCATION:")
        print("-" * 30)
        suggested_budget = self.create_budget_plan()
        for category, amount in suggested_budget.items():
            print(f"{category:15}: ${amount:8.2f}")


def main():
    """Demonstration of the Budget Agent in action."""
    print("🤖 Welcome to your Personal Budget Agent!")
    print("Let's set up your monthly budget...")
    
    # Initialize the agent
    monthly_income = float(input("Enter your monthly income: $"))
    agent = BudgetAgent(monthly_income)
    
    # Try to load existing data
    agent.load_from_file()
    
    # Demo: Add some sample expenses
    print("\n📝 Adding sample expenses...")
    agent.add_expense(ExpenseCategory.HOUSING, 1200, "Rent payment")
    agent.add_expense(ExpenseCategory.FOOD, 400, "Groceries")
    agent.add_expense(ExpenseCategory.TRANSPORTATION, 300, "Car payment + gas")
    agent.add_expense(ExpenseCategory.UTILITIES, 150, "Electricity + Water")
    agent.add_expense(ExpenseCategory.ENTERTAINMENT, 200, "Movies + Dining out")
    agent.add_expense(ExpenseCategory.SAVINGS, 500, "Monthly savings")
    
    # Set budget goals
    print("\n🎯 Setting budget goals...")
    agent.set_budget_goal(ExpenseCategory.HOUSING, 1300, 1)
    agent.set_budget_goal(ExpenseCategory.FOOD, 350, 2)
    agent.set_budget_goal(ExpenseCategory.SAVINGS, 600, 1)
    
    # Show comprehensive summary
    agent.print_budget_summary()
    
    # Save data
    agent.save_to_file()
    
    print("\n✨ Budget analysis complete! Check budget_data.json for saved data.")


if __name__ == "__main__":
    main()
