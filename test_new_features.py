#!/usr/bin/env python3
"""
Test script for new features:
1. Top 5 mutual funds by category
2. PDF download functionality
"""

import requests
import json

def test_top_funds():
    """Test the top funds endpoint"""
    print("Testing Top Funds Feature...")
    
    categories = ['large_cap', 'mid_cap', 'flexi_cap', 'small_cap', 'multi_cap']
    
    for category in categories:
        try:
            response = requests.post(
                'http://localhost:5000/top-funds',
                json={'category': category},
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    print(f"✅ {category.replace('_', ' ').title()}: {len(data['funds'])} funds returned")
                    if data['funds']:
                        print(f"   Top fund: {data['funds'][0]['name']} (Score: {data['funds'][0]['score']})")
                else:
                    print(f"❌ {category}: {data['error']}")
            else:
                print(f"❌ {category}: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"❌ {category}: {str(e)}")
    
    print()

def test_personalized_recommendations():
    """Test the personalized recommendations endpoint"""
    print("Testing Personalized Recommendations...")
    
    test_user = {
        'name': 'Test User',
        'age': 30,
        'annual_income': 1000000,
        'investment_amount': 100000,
        'risk_tolerance': 'moderate',
        'investment_goal': 'wealth_creation',
        'investment_horizon': '5-10 years',
        'monthly_sip': 5000,
        'existing_investments': 50000,
        'tax_bracket': 30,
        'emergency_fund': 'yes',
        'fund_type_preference': 'direct',
        'esg_preference': 'no_preference',
        'dividend_preference': 'growth',
        'lumpsum_investment': 50000,
        'sip_investment': 5000
    }
    
    try:
        response = requests.post(
            'http://localhost:5000/analyze',
            json=test_user,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                print("✅ Personalized recommendations generated successfully")
                print(f"   Risk Profile: {data['recommendations']['risk_profile']}")
                print(f"   Categories: {list(data['recommendations']['recommendations'].keys())}")
                print(f"   Total Funds: {sum(len(funds) for funds in data['recommendations']['recommendations'].values())}")
            else:
                print(f"❌ Error: {data['error']}")
        else:
            print(f"❌ HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    print()

def test_website_access():
    """Test if the website is accessible"""
    print("Testing Website Access...")
    
    try:
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print("✅ Website is accessible")
            if "Your Mutual Fund Advisor" in response.text:
                print("✅ Website title updated correctly")
            else:
                print("❌ Website title not found")
        else:
            print(f"❌ Website not accessible: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Error accessing website: {str(e)}")
    
    print()

if __name__ == "__main__":
    print("🧪 Testing New Features for Your Mutual Fund Advisor")
    print("=" * 60)
    
    test_website_access()
    test_top_funds()
    test_personalized_recommendations()
    
    print("🎉 Testing completed!")
    print("\n📝 Next steps:")
    print("1. Open http://localhost:5000 in your browser")
    print("2. Test the 'View Top 5 Funds of the Month' feature")
    print("3. Test the personalized recommendations")
    print("4. Test the PDF download functionality")
