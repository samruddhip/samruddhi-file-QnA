# Streamlit Cloud Deployment Guide

This guide shows you how to deploy your PDF Chatbot to Streamlit Cloud - the easiest and free way to get your app online.

## 🚀 Streamlit Cloud Deployment (Recommended)

### Why Streamlit Cloud?
- ✅ **100% Free** - No cost for hosting
- ✅ **No technical setup** - Just point and click
- ✅ **Automatic updates** - Updates when you push to GitHub
- ✅ **Custom domain** - Get your own URL
- ✅ **Secure** - Environment variables are encrypted

### Step-by-Step Deployment

#### Step 1: Prepare Your Code
Make sure your code is pushed to GitHub:
```bash
git add .
git commit -m "Ready for Streamlit Cloud deployment"
git push origin main
```

#### Step 2: Go to Streamlit Cloud
1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"

#### Step 3: Configure Your App
1. **Repository**: Select `samruddhip/samruddhi-file-QnA`
2. **Branch**: Select `main`
3. **Main file path**: Enter `chatbot.py`
4. **App URL**: Choose a custom URL (optional)
5. Click "Deploy!"

#### Step 4: Set Environment Variables
1. Go to your app's dashboard
2. Click "Settings" → "Secrets"
3. Add your API key:
   ```
   OPENAI_API_KEY = your_actual_api_key_here
   ```
4. Click "Save"

#### Step 5: Restart Your App
1. Go to "Manage app"
2. Click "Restart app"
3. Wait for it to restart
4. Your app is now live! 🎉

### Environment Variables You Can Set

**Required:**
```
OPENAI_API_KEY=your_actual_api_key_here
```

**Optional (to customize your app):**
```
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0
OPENAI_MAX_TOKENS=1000
CHUNK_SIZE=1000
CHUNK_OVERLAP=150
APP_TITLE=PDF Chatbot - Ask Questions About Your Documents
SIDEBAR_TITLE=Your Documents
FILE_UPLOADER_TEXT=Upload a PDF file and start asking questions
QUESTION_INPUT_TEXT=Type your question here
```

## 🔧 Local Development

### Run Locally
```bash
# Set your API key
export OPENAI_API_KEY='your_key_here'

# Run the app
streamlit run chatbot.py
```

### Customize Your App
You can customize your app by setting environment variables:

```bash
# Basic customization
export OPENAI_API_KEY='your_key_here'
export OPENAI_MODEL='gpt-4'
export APP_TITLE='My Custom PDF Assistant'

# Run with custom settings
streamlit run chatbot.py
```

## 🚨 Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Make sure you set `OPENAI_API_KEY` in Streamlit Cloud secrets
   - Check if the key is valid and has sufficient credits

2. **App Won't Start**
   - Check the logs in Streamlit Cloud dashboard
   - Ensure all dependencies are in requirements.txt

3. **Import Errors**
   - Make sure all packages are in requirements.txt
   - Check Python version compatibility

4. **Memory Issues**
   - Reduce `CHUNK_SIZE` in environment variables
   - Use smaller PDF files for testing

### Getting Help
- Check Streamlit Cloud logs
- Review the error messages
- Ensure your API key is correct
- Test locally first with `streamlit run chatbot.py`

## 🎉 Success!

Once deployed, your PDF Chatbot will be available at a public URL that you can share with anyone. The app will automatically update whenever you push changes to your GitHub repository.

### Next Steps
- Share your app URL with others
- Monitor usage in Streamlit Cloud dashboard
- Customize the app with different environment variables
- Add more features and push updates