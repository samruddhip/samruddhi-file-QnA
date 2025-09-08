# Configuration Guide

This document explains all the configurable parameters for the PDF Chatbot application.

## 🔧 Environment Variables

All configuration is done through environment variables. You can set them in several ways:

1. **Using .env file** (Recommended for development)
2. **Environment variables** (Recommended for production)
3. **Using setup_env.py script** (Interactive setup)

## 📋 Configuration Parameters

### OpenAI API Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | Required | Your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys) |
| `OPENAI_MODEL` | `gpt-3.5-turbo` | OpenAI model to use (gpt-3.5-turbo, gpt-4, etc.) |
| `OPENAI_TEMPERATURE` | `0` | Response creativity (0-1, where 0 is deterministic) |
| `OPENAI_MAX_TOKENS` | `1000` | Maximum tokens in response |

### Text Processing Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `CHUNK_SIZE` | `1000` | Size of text chunks for processing |
| `CHUNK_OVERLAP` | `150` | Overlap between chunks |
| `CHUNK_SEPARATORS` | `\n` | Text separators for chunking (comma-separated) |

### UI Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_TITLE` | `PDF Chatbot - Ask Questions About Your Documents` | Main application title |
| `SIDEBAR_TITLE` | `Your Documents` | Sidebar title |
| `FILE_UPLOADER_TEXT` | `Upload a PDF file and start asking questions` | File uploader text |
| `QUESTION_INPUT_TEXT` | `Type your question here` | Question input placeholder |

### Advanced Configuration (Optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` | OpenAI API base URL |
| `OPENAI_ORGANIZATION` | None | OpenAI organization ID |
| `STREAMLIT_SERVER_PORT` | `8501` | Streamlit server port |
| `STREAMLIT_SERVER_ADDRESS` | `localhost` | Streamlit server address |

## 🚀 Quick Setup

### Method 1: Interactive Setup (Recommended)
```bash
python setup_env.py
```

### Method 2: Manual .env File
Create a `.env` file with your configuration:
```bash
# Required
OPENAI_API_KEY=your_key_here

# Optional - customize as needed
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1
CHUNK_SIZE=1500
APP_TITLE=My Custom PDF Chatbot
```

### Method 3: Environment Variables
```bash
export OPENAI_API_KEY="your_key_here"
export OPENAI_MODEL="gpt-4"
export CHUNK_SIZE="1500"
streamlit run chatbot.py
```

## 🎯 Configuration Examples

### Development Configuration
```bash
OPENAI_API_KEY=sk-dev-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0
CHUNK_SIZE=1000
CHUNK_OVERLAP=150
APP_TITLE=PDF Chatbot - Dev
```

### Production Configuration
```bash
OPENAI_API_KEY=sk-prod-key-here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1
CHUNK_SIZE=2000
CHUNK_OVERLAP=200
APP_TITLE=Enterprise PDF Assistant
```

### High-Performance Configuration
```bash
OPENAI_API_KEY=sk-key-here
OPENAI_MODEL=gpt-4-turbo
OPENAI_TEMPERATURE=0
OPENAI_MAX_TOKENS=2000
CHUNK_SIZE=3000
CHUNK_OVERLAP=300
```

## 🔒 Security Best Practices

1. **Never commit .env files** - They're automatically ignored by git
2. **Use different keys** for development and production
3. **Rotate API keys** regularly
4. **Use environment variables** in production deployments
5. **Monitor API usage** through OpenAI dashboard

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Ensure `OPENAI_API_KEY` is set correctly
   - Check for typos in the variable name
   - Verify the key starts with `sk-`

2. **Invalid Configuration Values**
   - Temperature must be between 0 and 1
   - Chunk size and overlap must be positive integers
   - Max tokens must be a positive integer

3. **Model Not Found**
   - Verify the model name is correct
   - Check if you have access to the model
   - Ensure your API key has the right permissions

### Validation

The application will validate configuration values and show helpful error messages if something is wrong.

## 📊 Performance Tuning

### For Large Documents
- Increase `CHUNK_SIZE` (2000-3000)
- Increase `CHUNK_OVERLAP` (200-300)
- Use `gpt-4` for better understanding

### For Speed
- Decrease `CHUNK_SIZE` (500-800)
- Decrease `CHUNK_OVERLAP` (50-100)
- Use `gpt-3.5-turbo` for faster responses

### For Quality
- Use `gpt-4` model
- Increase `OPENAI_MAX_TOKENS`
- Fine-tune `OPENAI_TEMPERATURE` (0.1-0.3)

## 🔄 Configuration Updates

To update configuration:
1. Modify your `.env` file or environment variables
2. Restart the Streamlit application
3. Changes take effect immediately

## 📝 Notes

- All string values should be quoted if they contain spaces
- Numeric values are automatically converted to appropriate types
- Boolean values should be `true`/`false` or `1`/`0`
- Comments in `.env` files start with `#`
