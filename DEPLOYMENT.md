# Deploying to Vercel

## Prerequisites
1. Install Vercel CLI: `npm i -g vercel`
2. Make sure you have a Vercel account (sign up at vercel.com)

## Important Fixes Applied
✅ **Python Version**: Set to Python 3.11 (compatible with all dependencies)
✅ **Dependencies**: Updated to Python 3.11 compatible versions
✅ **Configuration**: Optimized vercel.json for better deployment

## Deployment Steps

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login to Vercel
```bash
vercel login
```

### 3. Deploy your application
```bash
vercel
```

### 4. Follow the prompts:
- Set up and deploy: `Y`
- Which scope: Select your account
- Link to existing project: `N`
- Project name: `mutual-fund-analyzer` (or your preferred name)
- In which directory is your code located: `./` (current directory)
- Want to override the settings: `N`

### 5. Environment Variables
After deployment, you'll need to set up environment variables in the Vercel dashboard:
- Go to your project dashboard
- Navigate to Settings > Environment Variables
- Add your environment variables (e.g., API keys, SECRET_KEY)

### 6. Custom Domain (Optional)
- In your project dashboard, go to Settings > Domains
- Add your custom domain

## What Was Fixed

1. **Python Version Issue**: Changed from Python 3.12 to 3.11
   - Python 3.12 removed `distutils` which older pandas/numpy versions need
   - Updated `runtime.txt` and `vercel.json` accordingly

2. **Dependency Compatibility**: 
   - pandas==2.0.3 (compatible with Python 3.11)
   - numpy==1.24.3 (compatible with Python 3.11)
   - All other dependencies are Python 3.11 compatible

3. **Build Configuration**:
   - Added `maxLambdaSize: "50mb"` to handle larger dependencies
   - Set explicit Python version in vercel.json

## Important Notes

1. **File Size Limits**: Vercel has a 50MB limit for serverless functions. Your Excel file might cause issues.
2. **Environment Variables**: Make sure to set all required environment variables in Vercel dashboard.
3. **Dependencies**: All Python packages in requirements.txt will be installed automatically.
4. **Cold Starts**: Serverless functions may have cold start delays.

## Troubleshooting

- If you encounter build errors, check the Vercel build logs
- Ensure all dependencies are compatible with Python 3.11
- Check that your environment variables are properly set
- Verify that your Excel file path is correct for the deployed environment

## Alternative: Use Vercel Dashboard

You can also deploy directly from the Vercel dashboard:
1. Go to vercel.com
2. Click "New Project"
3. Import your GitHub repository
4. Configure build settings
5. Deploy

## Pre-deployment Test

Before deploying, test locally:
```bash
# Clean up
rm -rf __pycache__/
rm -rf *.pyc

# Install dependencies
pip install -r requirements.txt

# Test import
python -c "import app; print('App imported successfully')"

# Run locally
python app.py
```
