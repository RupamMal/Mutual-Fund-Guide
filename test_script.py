#!/usr/bin/env python3
import json
from mutual_fund_analyzer import MutualFundAnalyzer
from llm_recommender import LLMRecommender
from data_fetcher import MutualFundDataFetcher # Added for testing

def test_mutual_fund_analyzer():
    """Test the mutual fund analyzer functionality"""
    print("\n📊 Testing Mutual Fund Analyzer...")
    try:
        analyzer = MutualFundAnalyzer()
        
        # Test user info
        user_info = {
            'name': 'John Doe',
            'age': 30,
            'annual_income': 800000,
            'investment_amount': 100000,
            'risk_tolerance': 'moderate',
            'investment_horizon': '5-10 years'
        }
        
        recommendations = analyzer.get_recommendations(user_info)
        
        print(f"✅ Risk Profile: {recommendations['risk_profile']}")
        print(f"✅ Total Funds Recommended: {sum(len(funds) for funds in recommendations['recommendations'].values())}")
        
        # Test GROW URL generation
        test_fund = "HDFC Top 100 Fund"
        grow_url = analyzer.get_grow_url(test_fund)
        print(f"✅ GROW URL for {test_fund}: {grow_url}")
        
    except Exception as e:
        print(f"❌ Mutual fund analyzer test failed: {e}")

def test_llm_recommender():
    """Test the LLM recommender functionality"""
    print("\n🤖 Testing LLM Recommender...")
    try:
        recommender = LLMRecommender()
        
        # Test with sample data
        user_info = {
            'name': 'Jane Smith',
            'age': 35,
            'annual_income': 1200000,
            'investment_amount': 200000,
            'risk_tolerance': 'moderate',
            'investment_horizon': '5-10',
            'investment_goal': 'wealth_creation',
            'monthly_sip': 10000,
            'existing_investments': 50000,
            'tax_bracket': 20,
            'emergency_fund': 'yes',
            'fund_type_preference': 'direct',
            'esg_preference': 'no_preference',
            'dividend_preference': 'growth'
        }
        
        fund_data = {
            'risk_profile': 'moderate',
            'recommendations': {
                'large_cap': [{
                    'name': 'Test Fund',
                    'aum_cr': 5000,
                    'fund_manager': 'Test Manager',
                    'expense_ratio': 1.5,
                    'sip_5yr_return': 12.0,
                    'sip_10yr_return': 14.0,
                    'alpha': 2.0,
                    'beta': 0.95,
                    'sharpe_ratio': 0.85,
                    'sortino_ratio': 1.1,
                    'esg_score': 7.5,
                    'volatility_rank': 'low',
                    'peer_rank': 1,
                    'risk_adjusted_return': 8.5,
                    'diversification_score': 85
                }]
            },
            'advanced_analysis': {
                'projections': {
                    'monthly_sip': 10000,
                    'total_investment': 840000,
                    'projected_value': 1200000,
                    'expected_return': 12.0,
                    'time_period': 7
                },
                'diversification_score': {
                    'score': 120,
                    'categories': 3,
                    'total_funds': 4,
                    'assessment': 'Excellent - Well diversified across categories'
                }
            }
        }
        
        analysis = recommender.generate_recommendations(user_info, fund_data)
        
        print(f"✅ Analysis generated: {len(analysis)} sections")
        print(f"✅ Summary length: {len(analysis.get('summary', ''))} characters")
        
    except Exception as e:
        print(f"❌ LLM recommender test failed: {e}")

def test_sample_recommendation():
    """Test a complete recommendation flow"""
    print("\n🎯 Testing Complete Recommendation Flow...")
    try:
        analyzer = MutualFundAnalyzer()
        recommender = LLMRecommender()
        
        user_info = {
            'name': 'Test User',
            'age': 28,
            'annual_income': 600000,
            'investment_amount': 50000,
            'risk_tolerance': 'moderate',
            'investment_horizon': '3-5 years'
        }
        
        # Get recommendations
        recommendations = analyzer.get_recommendations(user_info)
        
        # Add GROW URLs
        for category, funds in recommendations['recommendations'].items():
            for fund in funds:
                fund['grow_url'] = analyzer.get_grow_url(fund['name'])
        
        # Generate LLM analysis
        llm_analysis = recommender.generate_recommendations(user_info, recommendations)
        
        print(f"✅ Complete flow successful!")
        print(f"✅ Risk Profile: {recommendations['risk_profile']}")
        print(f"✅ Funds with GROW URLs: {sum(len(funds) for funds in recommendations['recommendations'].values())}")
        print(f"✅ LLM Analysis sections: {len(llm_analysis)}")
        
    except Exception as e:
        print(f"❌ Complete recommendation test failed: {e}")

def test_data_fetcher():
    """Test the data fetcher functionality"""
    print("\n🔍 Testing Data Fetcher...")
    try:
        from data_fetcher import MutualFundDataFetcher
        fetcher = MutualFundDataFetcher()
        
        # Test GROW URL generation
        test_funds = [
            "HDFC Top 100 Fund",
            "Axis Bluechip Fund Direct Growth",
            "SBI Small Cap Fund",
            "ICICI Prudential Flexi Cap Fund"
        ]
        
        print("Testing GROW URL generation:")
        for fund_name in test_funds:
            url = fetcher.get_grow_url(fund_name)
            print(f"  {fund_name} -> {url}")
        
        print("✅ Data fetcher tests completed")
        
    except Exception as e:
        print(f"❌ Data fetcher test failed: {e}")

def test_grow_urls():
    """Test GROW URL generation specifically"""
    print("\n🔗 Testing GROW URL Generation...")
    try:
        from mutual_fund_analyzer import MutualFundAnalyzer
        analyzer = MutualFundAnalyzer()
        
        test_funds = [
            "HDFC Top 100 Fund",
            "Axis Bluechip Fund Direct Growth",
            "SBI Small Cap Fund",
            "ICICI Prudential Flexi Cap Fund",
            "Kotak Emerging Equity Fund",
            "Nippon India Large Cap Fund"
        ]
        
        print("Generated GROW URLs:")
        for fund_name in test_funds:
            url = analyzer.get_grow_url(fund_name)
            print(f"  {fund_name}")
            print(f"    -> {url}")
            print()
        
        print("✅ GROW URL generation tests completed")
        
    except Exception as e:
        print(f"❌ GROW URL test failed: {e}")

def main():
    print("🚀 Starting AI Mutual Fund Advisor Tests\n")
    print("=" * 50)
    test_mutual_fund_analyzer()
    test_llm_recommender()
    test_data_fetcher()
    test_grow_urls()
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
