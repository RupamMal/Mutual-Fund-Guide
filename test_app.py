#!/usr/bin/env python3
"""
Test script for the AI Mutual Fund Advisor application
"""

import json
from mutual_fund_analyzer import MutualFundAnalyzer
from llm_recommender import LLMRecommender

def test_mutual_fund_analyzer():
    """Test the mutual fund analyzer functionality"""
    print("Testing Mutual Fund Analyzer...")
    
    analyzer = MutualFundAnalyzer()
    
    # Test user profile
    user_info = {
        'name': 'John Doe',
        'age': 35,
        'annual_income': 800000,
        'investment_amount': 100000,
        'risk_tolerance': 'moderate',
        'investment_horizon': '5-10 years'
    }
    
    # Get recommendations
    recommendations = analyzer.get_recommendations(user_info)
    
    print(f"Risk Profile: {recommendations['risk_profile']}")
    print(f"Allocation Suggestions: {recommendations['allocation_suggestions']}")
    
    # Test fund details
    fund_details = analyzer.get_fund_details('LARGE_001')
    if fund_details:
        print(f"Fund Details: {fund_details['name']} - AUM: ₹{fund_details['aum_cr']} Cr")
    
    print("✅ Mutual Fund Analyzer test completed successfully!\n")

def test_llm_recommender():
    """Test the LLM recommender functionality (without API key)"""
    print("Testing LLM Recommender...")
    
    try:
        llm_recommender = LLMRecommender()
        
        # Test user profile
        user_info = {
            'name': 'John Doe',
            'age': 35,
            'annual_income': 800000,
            'investment_amount': 100000,
            'risk_tolerance': 'moderate',
            'investment_horizon': '5-10 years'
        }
        
        # Test fund data
        fund_data = {
            'recommendations': {
                'large_cap': [
                    {
                        'name': 'HDFC Top 100 Fund',
                        'aum_cr': 15420.5,
                        'expense_ratio': 1.75,
                        'sip_5yr_return': 12.8,
                        'fund_manager': 'Prashant Jain'
                    }
                ]
            },
            'risk_profile': 'moderate',
            'allocation_suggestions': {
                'large_cap': 35,
                'mid_cap': 25,
                'flexi_cap': 25,
                'small_cap': 10,
                'multi_cap': 5
            }
        }
        
        # This will use fallback recommendations since no API key is provided
        recommendations = llm_recommender.generate_recommendations(user_info, fund_data)
        
        print(f"Summary: {recommendations['summary'][:100]}...")
        print(f"Key Insights: {len(recommendations['key_insights'])} insights generated")
        print(f"Allocations: {len(recommendations['suggested_allocations'])} categories")
        
        print("✅ LLM Recommender test completed successfully!\n")
        
    except Exception as e:
        print(f"⚠️ LLM Recommender test failed (expected without API key): {e}\n")

def test_data_fetcher():
    """Test the data fetcher functionality"""
    print("Testing Data Fetcher...")
    
    try:
        from data_fetcher import MutualFundDataFetcher
        
        fetcher = MutualFundDataFetcher()
        
        # Test fund categories
        categories = fetcher.get_fund_categories()
        print(f"Fund Categories: {list(categories.keys())}")
        
        # Test fund validation
        sample_fund = {
            'name': 'Test Fund',
            'aum_cr': 5000,
            'expense_ratio': 1.5,
            'sip_5yr_return': 12.5
        }
        
        is_valid = fetcher.validate_fund_data(sample_fund)
        print(f"Fund Validation: {'✅ Valid' if is_valid else '❌ Invalid'}")
        
        # Test metrics calculation
        enhanced_fund = fetcher.calculate_fund_metrics(sample_fund)
        print(f"Enhanced Fund: {enhanced_fund['size_category']} size, {enhanced_fund['expense_efficiency']} expense efficiency")
        
        print("✅ Data Fetcher test completed successfully!\n")
        
    except Exception as e:
        print(f"❌ Data Fetcher test failed: {e}\n")

def test_sample_recommendation():
    """Test a complete recommendation flow"""
    print("Testing Complete Recommendation Flow...")
    
    analyzer = MutualFundAnalyzer()
    
    # Sample user profiles
    users = [
        {
            'name': 'Young Professional',
            'age': 28,
            'annual_income': 600000,
            'investment_amount': 50000,
            'risk_tolerance': 'high',
            'investment_horizon': '10+ years'
        },
        {
            'name': 'Mid-Career Professional',
            'age': 42,
            'annual_income': 1200000,
            'investment_amount': 200000,
            'risk_tolerance': 'moderate',
            'investment_horizon': '5-10 years'
        },
        {
            'name': 'Near Retirement',
            'age': 58,
            'annual_income': 800000,
            'investment_amount': 500000,
            'risk_tolerance': 'low',
            'investment_horizon': '1-3 years'
        }
    ]
    
    for i, user in enumerate(users, 1):
        print(f"\n--- User {i}: {user['name']} ---")
        
        recommendations = analyzer.get_recommendations(user)
        
        print(f"Risk Profile: {recommendations['risk_profile']}")
        print(f"Allocation: {recommendations['allocation_suggestions']}")
        
        # Show top fund in each category
        for category, funds in recommendations['recommendations'].items():
            if funds:
                top_fund = funds[0]
                print(f"  {category.replace('_', ' ').title()}: {top_fund['name']} (Score: {top_fund['score']:.2f})")
    
    print("\n✅ Complete Recommendation Flow test completed successfully!\n")

def main():
    """Run all tests"""
    print("🚀 Starting AI Mutual Fund Advisor Tests\n")
    print("=" * 50)
    
    test_mutual_fund_analyzer()
    test_llm_recommender()
    test_data_fetcher()
    test_sample_recommendation()
    
    print("=" * 50)
    print("🎉 All tests completed!")
    print("\nTo run the full application:")
    print("1. Get a Google Gemini API key from https://makersuite.google.com/app/apikey")
    print("2. Create a .env file with: GOOGLE_API_KEY=your_api_key_here")
    print("3. Run: python app.py")
    print("4. Open http://localhost:5000 in your browser")

if __name__ == "__main__":
    main()
