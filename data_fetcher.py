import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import json
from typing import Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MutualFundDataFetcher:
    """Fetcher for mutual fund data from various sources"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def fetch_amfi_data(self) -> Dict[str, Any]:
        """Fetch data from AMFI (Association of Mutual Funds in India)"""
        try:
            # AMFI NAV data URL
            url = "https://www.amfiindia.com/spages/NAVAll.txt"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Parse the NAV data
            data = self._parse_amfi_nav_data(response.text)
            logger.info(f"Successfully fetched AMFI data for {len(data)} funds")
            return data
            
        except Exception as e:
            logger.error(f"Error fetching AMFI data: {e}")
            return {}
    
    def fetch_tickertape_data(self, api_key: str = None) -> Dict[str, Any]:
        """Fetch data from TickerTape API"""
        try:
            # This would require actual API key and endpoints
            # For now, return sample data structure
            logger.info("TickerTape API integration would require valid API key")
            return self._get_sample_tickertape_data()
            
        except Exception as e:
            logger.error(f"Error fetching TickerTape data: {e}")
            return {}
    
    def fetch_moneycontrol_data(self) -> Dict[str, Any]:
        """Fetch data from MoneyControl website"""
        try:
            # MoneyControl mutual fund page
            url = "https://www.moneycontrol.com/mutual-funds/"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            data = self._parse_moneycontrol_data(soup)
            logger.info(f"Successfully fetched MoneyControl data")
            return data
            
        except Exception as e:
            logger.error(f"Error fetching MoneyControl data: {e}")
            return {}
    
    def fetch_yahoo_finance_data(self, fund_symbols: List[str]) -> Dict[str, Any]:
        """Fetch data from Yahoo Finance"""
        try:
            import yfinance as yf
            
            data = {}
            for symbol in fund_symbols:
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info
                    
                    # Extract relevant information
                    fund_data = {
                        'name': info.get('longName', symbol),
                        'nav': info.get('regularMarketPrice', 0),
                        'aum': info.get('totalAssets', 0),
                        'expense_ratio': info.get('expenseRatio', 0) * 100 if info.get('expenseRatio') else 0,
                        'category': info.get('category', 'Unknown'),
                        'fund_manager': info.get('fundFamily', 'Unknown')
                    }
                    
                    data[symbol] = fund_data
                    time.sleep(0.1)  # Rate limiting
                    
                except Exception as e:
                    logger.warning(f"Error fetching data for {symbol}: {e}")
                    continue
            
            logger.info(f"Successfully fetched Yahoo Finance data for {len(data)} funds")
            return data
            
        except Exception as e:
            logger.error(f"Error fetching Yahoo Finance data: {e}")
            return {}
    
    def _parse_amfi_nav_data(self, nav_text: str) -> Dict[str, Any]:
        """Parse AMFI NAV data"""
        funds = {}
        lines = nav_text.strip().split('\n')
        
        for line in lines[1:]:  # Skip header
            try:
                parts = line.split(';')
                if len(parts) >= 4:
                    fund_data = {
                        'scheme_code': parts[0],
                        'scheme_name': parts[1],
                        'nav': float(parts[2]) if parts[2] else 0,
                        'date': parts[3]
                    }
                    funds[parts[0]] = fund_data
            except Exception as e:
                logger.warning(f"Error parsing NAV line: {e}")
                continue
        
        return funds
    
    def _parse_moneycontrol_data(self, soup: BeautifulSoup) -> Dict[str, Any]:
        """Parse MoneyControl HTML data"""
        # This is a placeholder for actual parsing logic
        # In a real implementation, you would extract fund information from the HTML
        return {
            'source': 'MoneyControl',
            'timestamp': time.time(),
            'funds_count': 0
        }
    
    def _get_sample_tickertape_data(self) -> Dict[str, Any]:
        """Sample data structure for TickerTape API"""
        return {
            'source': 'TickerTape',
            'timestamp': time.time(),
            'funds': {
                'sample_fund_1': {
                    'name': 'Sample Fund 1',
                    'aum_cr': 5000,
                    'expense_ratio': 1.5,
                    'sip_5yr_return': 12.5,
                    'sip_10yr_return': 14.2,
                    'alpha': 2.1,
                    'beta': 0.95,
                    'sharpe_ratio': 0.85,
                    'sortino_ratio': 1.12
                }
            }
        }
    
    def get_fund_categories(self) -> Dict[str, List[str]]:
        """Get fund categories and their typical characteristics"""
        return {
            'large_cap': {
                'description': 'Funds that invest primarily in large-cap stocks (top 100 companies by market cap)',
                'risk_level': 'Low to Moderate',
                'expected_return': '8-12%',
                'suitable_for': 'Conservative investors, retirees, short-term goals'
            },
            'mid_cap': {
                'description': 'Funds that invest in mid-cap stocks (101st to 250th companies by market cap)',
                'risk_level': 'Moderate',
                'expected_return': '10-15%',
                'suitable_for': 'Moderate risk investors, medium-term goals'
            },
            'flexi_cap': {
                'description': 'Funds with flexible allocation across large, mid, and small-cap stocks',
                'risk_level': 'Moderate to High',
                'expected_return': '12-18%',
                'suitable_for': 'Investors seeking flexibility and professional management'
            },
            'small_cap': {
                'description': 'Funds that invest in small-cap stocks (beyond top 250 companies)',
                'risk_level': 'High',
                'expected_return': '15-25%',
                'suitable_for': 'Aggressive investors, long-term goals, high risk tolerance'
            },
            'multi_cap': {
                'description': 'Funds that invest across all market caps with professional allocation',
                'risk_level': 'Moderate',
                'expected_return': '10-16%',
                'suitable_for': 'Balanced investors, diversified approach'
            }
        }
    
    def validate_fund_data(self, fund_data: Dict[str, Any]) -> bool:
        """Validate fund data for completeness and accuracy"""
        required_fields = ['name', 'aum_cr', 'expense_ratio', 'sip_5yr_return']
        
        for field in required_fields:
            if field not in fund_data or fund_data[field] is None:
                return False
        
        # Validate numeric ranges
        if not (0 < fund_data.get('aum_cr', 0) < 100000):  # AUM in crores
            return False
        
        if not (0 < fund_data.get('expense_ratio', 0) < 5):  # Expense ratio in %
            return False
        
        if not (-50 < fund_data.get('sip_5yr_return', 0) < 50):  # Returns in %
            return False
        
        return True
    
    def calculate_fund_metrics(self, fund_data: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate additional fund metrics"""
        metrics = fund_data.copy()
        
        # Calculate risk-adjusted returns
        if 'sip_5yr_return' in metrics and 'std_dev' in metrics:
            if metrics['std_dev'] > 0:
                metrics['sharpe_ratio'] = metrics['sip_5yr_return'] / metrics['std_dev']
        
        # Calculate fund size category
        aum = metrics.get('aum_cr', 0)
        if aum > 10000:
            metrics['size_category'] = 'Large'
        elif aum > 5000:
            metrics['size_category'] = 'Medium'
        else:
            metrics['size_category'] = 'Small'
        
        # Calculate expense efficiency
        if 'expense_ratio' in metrics:
            if metrics['expense_ratio'] < 1.5:
                metrics['expense_efficiency'] = 'Excellent'
            elif metrics['expense_ratio'] < 2.0:
                metrics['expense_efficiency'] = 'Good'
            else:
                metrics['expense_efficiency'] = 'High'
        
        return metrics
    
    def get_grow_url(self, fund_name: str) -> str:
        """Generate GROW website URL for a mutual fund"""
        # GROW website URL structure: https://groww.in/mutual-funds/[fund-name]
        # Convert fund name to URL-friendly format
        fund_name_clean = fund_name.lower()
        fund_name_clean = fund_name_clean.replace(' ', '-')
        fund_name_clean = fund_name_clean.replace('(', '')
        fund_name_clean = fund_name_clean.replace(')', '')
        fund_name_clean = fund_name_clean.replace('.', '')
        fund_name_clean = fund_name_clean.replace(',', '')
        fund_name_clean = fund_name_clean.replace('&', 'and')
        
        # Remove common words that might not be in the URL
        fund_name_clean = fund_name_clean.replace('fund', '')
        fund_name_clean = fund_name_clean.replace('direct', '')
        fund_name_clean = fund_name_clean.replace('growth', '')
        fund_name_clean = fund_name_clean.replace('option', '')
        
        # Clean up multiple dashes
        fund_name_clean = '-'.join(filter(None, fund_name_clean.split('-')))
        
        return f"https://groww.in/mutual-funds/{fund_name_clean}"

# Example usage
if __name__ == "__main__":
    fetcher = MutualFundDataFetcher()
    
    # Fetch data from different sources
    print("Fetching mutual fund data...")
    
    # AMFI data
    amfi_data = fetcher.fetch_amfi_data()
    print(f"AMFI data: {len(amfi_data)} funds")
    
    # Fund categories
    categories = fetcher.get_fund_categories()
    print(f"Fund categories: {list(categories.keys())}")
    
    # Sample validation
    sample_fund = {
        'name': 'Test Fund',
        'aum_cr': 5000,
        'expense_ratio': 1.5,
        'sip_5yr_return': 12.5
    }
    
    is_valid = fetcher.validate_fund_data(sample_fund)
    print(f"Sample fund validation: {is_valid}")
    
    # Calculate metrics
    enhanced_fund = fetcher.calculate_fund_metrics(sample_fund)
    print(f"Enhanced fund data: {enhanced_fund}")
