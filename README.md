# Your Mutual Fund Advisor

A comprehensive AI-powered mutual fund recommendation system that provides personalized investment advice based on user profiles, risk tolerance, and financial goals. The system uses Google Gemini AI to generate intelligent recommendations and analyzes mutual funds across multiple categories.

**This is only to educate you about Mutual Fund.**

## Features

### 🤖 AI-Powered Recommendations
- **Google Gemini AI Integration**: Advanced AI analysis for personalized investment advice
- **Risk Profile Assessment**: Automatic risk calculation based on age, income, and investment amount
- **Intelligent Fund Selection**: Multi-factor analysis including AUM, returns, risk ratios, and fund manager expertise
- **Advanced User Profiling**: Comprehensive input collection including investment goals, tax bracket, ESG preferences, and emergency fund status
- **Top 5 Funds of the Month**: View the best performing funds across all categories based on comprehensive metrics
- **PDF Report Download**: Download your personalized recommendation report as a PDF for offline reference

### 📊 Comprehensive Fund Analysis
- **Multiple Categories**: Large Cap, Mid Cap, Flexi Cap, Small Cap, and Multi Cap funds
- **Key Metrics**: AUM, Expense Ratio, 5-Year & 10-Year SIP Returns, Alpha, Beta, Standard Deviation, Sharpe Ratio, Sortino Ratio
- **Fund Manager Information**: Track record and expertise analysis

### 🎯 Portfolio Optimization
- **Smart Allocation**: AI-suggested portfolio allocation based on risk profile
- **Visual Charts**: Interactive pie charts for portfolio distribution
- **Detailed Breakdown**: Percentage and amount allocation for each category
- **Advanced Analytics**: Risk-adjusted rankings, diversification scoring, expense impact analysis, and volatility assessment
- **Investment Projections**: SIP-based wealth projection calculator with expected returns
- **Peer Comparison**: Detailed analysis of why recommended funds outperform alternatives

### 💻 Modern Web Interface
- **Beautiful Design**: Enhanced UI with animations, gradients, and modern styling
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Real-time Analysis**: Instant recommendations with loading animations
- **Interactive Elements**: Hover effects, smooth transitions, and modern UI
- **GROW Integration**: Direct links to view funds on GROW website for easy investment
- **Educational Features**: Tooltips, risk warnings, and comprehensive explanations for investment terms
- **Advanced Visualizations**: Enhanced charts and metrics display with ESG scores and volatility indicators
- **Navigation Options**: Choose between personalized recommendations or top funds view

## Technology Stack

- **Backend**: Python Flask
- **AI/ML**: Google Gemini AI (formerly Google PaLM)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Charts**: Chart.js for data visualization
- **Data Processing**: Pandas, NumPy
- **Web Scraping**: BeautifulSoup4, Requests

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Git

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd mutual-fund-advisor
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
1. Copy the environment template:
```bash
cp env_example.txt .env
```

2. Edit `.env` file and add your Google Gemini API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
SECRET_KEY=your_secret_key_here
```

### Step 5: Get Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

### Step 6: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### 1. Choose Your Option
- **Personalized Recommendations**: Get AI-powered advice based on your profile
- **Top 5 Funds of the Month**: View the best performing funds across all categories

### 2. Input Your Information (for Personalized Recommendations)
- **Personal Details**: Name, age, annual income
- **Investment Details**: Amount to invest, risk tolerance, investment horizon
- **Preferences**: Conservative, moderate, or aggressive risk profile

### 3. Get AI Recommendations
- Click "Get AI Recommendations" to analyze your profile
- The system will process your information and generate personalized advice

### 4. Review Results
- **Investment Profile**: Your risk assessment and financial summary
- **AI Analysis**: Comprehensive analysis and recommendations
- **Portfolio Allocation**: Visual breakdown of suggested investments
- **Fund Recommendations**: Top funds in each category with detailed metrics
- **Key Insights**: Important considerations and next steps
- **Download Report**: Save your personalized report as a PDF

## Fund Categories Covered

### Large Cap Funds
- Invest in large, established companies
- Lower risk, stable returns
- Suitable for conservative investors

### Mid Cap Funds
- Invest in medium-sized companies
- Balanced risk and return profile
- Good for moderate risk tolerance

### Flexi Cap Funds
- Flexible allocation across market caps
- Dynamic portfolio management
- Adapts to market conditions

### Small Cap Funds
- Invest in small companies
- Higher risk, potential for high returns
- Suitable for aggressive investors

### Multi Cap Funds
- Diversified across all market caps
- Professional fund management
- Balanced approach to growth

## Key Metrics Explained

### AUM (Assets Under Management)
- Total value of assets managed by the fund
- Higher AUM often indicates stability and trust

### Expense Ratio
- Annual fee charged by the fund
- Lower ratios are generally better for investors

### SIP Returns
- Returns on Systematic Investment Plans
- 5-year and 10-year performance indicators

### Risk Metrics
- **Alpha**: Excess return compared to benchmark
- **Beta**: Volatility relative to market
- **Sharpe Ratio**: Risk-adjusted return measure
- **Sortino Ratio**: Downside risk-adjusted return

## API Integration (Future Enhancements)

The system is designed to integrate with real financial data APIs:

- **AMFI API**: Official mutual fund data from Association of Mutual Funds in India
- **TickerTape API**: Real-time fund information and analytics
- **MoneyControl API**: Comprehensive financial data and news
- **Yahoo Finance API**: Global market data and fund information

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

⚠️ **Important**: This application is for educational and informational purposes only. It does not constitute financial advice. Always consult with a qualified financial advisor before making investment decisions. Past performance does not guarantee future returns.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation for common issues

## Roadmap

- [ ] Real-time data integration with financial APIs
- [ ] Advanced portfolio backtesting
- [ ] Tax optimization recommendations
- [ ] Mobile app development
- [ ] Multi-language support
- [ ] Advanced risk modeling
- [ ] Integration with trading platforms
