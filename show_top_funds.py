#!/usr/bin/env python3
"""
Script to display top 5 mutual funds for each category
"""

from mutual_fund_analyzer import MutualFundAnalyzer

def display_top_funds():
    """Display top 5 mutual funds for each category"""
    
    analyzer = MutualFundAnalyzer()
    
    categories = {
        'large_cap': 'Large Cap',
        'mid_cap': 'Mid Cap', 
        'flexi_cap': 'Flexi Cap',
        'small_cap': 'Small Cap',
        'multi_cap': 'Multi Cap'
    }
    
    print("🏆 TOP 5 MUTUAL FUNDS OF THE MONTH")
    print("=" * 80)
    print("Based on: AUM(cr), Expense Ratio, 5Y/10Y SIP Returns, Alpha, Beta, Std. Dev, Sharpe Ratio, Sortino Ratio")
    print()
    
    for category_key, category_name in categories.items():
        print(f"📊 {category_name.upper()} FUNDS")
        print("-" * 60)
        
        try:
            top_funds = analyzer.get_top_funds(category_key)
            
            for i, fund in enumerate(top_funds, 1):
                print(f"\n{i}. {fund['name']}")
                print(f"   📈 AUM: ₹{fund['aum_cr']} cr | Expense Ratio: {fund['expense_ratio']}%")
                print(f"   📊 5Y SIP Return: {fund['sip_5yr_return']}% | 10Y SIP Return: {fund['sip_10yr_return']}%")
                print(f"   📋 Alpha: {fund['alpha']} | Beta: {fund['beta']} | Std Dev: {fund['std_dev']}%")
                print(f"   ⭐ Sharpe Ratio: {fund['sharpe_ratio']} | Sortino Ratio: {fund['sortino_ratio']}")
                print(f"   👨‍💼 Fund Manager: {fund['fund_manager']}")
                print(f"   🏆 Composite Score: {fund['score']}")
                print(f"   🔗 GROW URL: {fund['grow_url']}")
                
        except Exception as e:
            print(f"❌ Error fetching {category_name} funds: {str(e)}")
        
        print("\n" + "=" * 80 + "\n")

if __name__ == "__main__":
    display_top_funds()
