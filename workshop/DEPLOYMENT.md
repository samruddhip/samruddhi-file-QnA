# Deployment Guide

This guide covers different deployment options for your PDF Chatbot application.

## 🚀 Deployment Options

### 1. Streamlit Cloud (Recommended - Free)

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set environment variables in Streamlit Cloud dashboard
5. Deploy!

**Environment Variables to Set:**
```
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0
CHUNK_SIZE=1000
APP_TITLE=PDF Chatbot
```

### 2. Docker Deployment

**Local Development:**
```bash
# Build and run with docker-compose
docker-compose up --build

# Or run directly with Docker
docker build -t pdf-chatbot .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key_here pdf-chatbot
```

**Production with Docker:**
```bash
# Build image
docker build -t your-username/pdf-chatbot .

# Push to registry
docker push your-username/pdf-chatbot

# Run on server
docker run -d \
  --name pdf-chatbot \
  -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  -e OPENAI_MODEL=gpt-4 \
  your-username/pdf-chatbot
```

### 3. Vercel Deployment

**Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Set environment variables in Vercel dashboard
4. Deploy!

### 4. Railway Deployment

**Steps:**
1. Connect GitHub repository to Railway
2. Set environment variables
3. Deploy automatically!

### 5. Heroku Deployment

**Steps:**
1. Create `Procfile`:
```
web: streamlit run chatbot.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy:
```bash
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_key_here
git push heroku main
```

## 🔐 Environment Variables Setup

### Required Variables
- `OPENAI_API_KEY` - Your OpenAI API key

### Optional Variables
- `OPENAI_MODEL` - Model to use (default: gpt-3.5-turbo)
- `OPENAI_TEMPERATURE` - Response creativity (default: 0)
- `OPENAI_MAX_TOKENS` - Max response tokens (default: 1000)
- `CHUNK_SIZE` - Text chunk size (default: 1000)
- `CHUNK_OVERLAP` - Chunk overlap (default: 150)
- `APP_TITLE` - Application title
- `SIDEBAR_TITLE` - Sidebar title
- `FILE_UPLOADER_TEXT` - File uploader text
- `QUESTION_INPUT_TEXT` - Question input text

## 🔧 CI/CD Setup

### GitHub Secrets Required

Go to your repository → Settings → Secrets and variables → Actions

**Required Secrets:**
```
OPENAI_API_KEY=your_actual_api_key_here
```

**Optional Secrets (for different deployments):**
```
# Streamlit Cloud
STREAMLIT_CLOUD_TOKEN=your_streamlit_token
STREAMLIT_APP_URL=your_app_url

# Docker Hub
DOCKER_USERNAME=your_docker_username
DOCKER_PASSWORD=your_docker_password

# Vercel
VERCEL_TOKEN=your_vercel_token
VERCEL_ORG_ID=your_org_id
VERCEL_PROJECT_ID=your_project_id
```

### Workflow Features
- ✅ **Automated testing** on every push
- ✅ **Linting** with flake8
- ✅ **Multi-platform deployment** (Streamlit, Docker, Vercel)
- ✅ **Security scanning** for vulnerabilities
- ✅ **Automatic deployment** on main branch

## 🐳 Docker Commands

### Build and Run Locally
```bash
# Build image
docker build -t pdf-chatbot .

# Run container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  pdf-chatbot

# Run with docker-compose
docker-compose up --build
```

### Production Deployment
```bash
# Build for production
docker build -t pdf-chatbot:latest .

# Tag for registry
docker tag pdf-chatbot:latest your-registry/pdf-chatbot:latest

# Push to registry
docker push your-registry/pdf-chatbot:latest

# Deploy to server
docker run -d \
  --name pdf-chatbot \
  --restart unless-stopped \
  -p 8501:8501 \
  -e OPENAI_API_KEY=your_production_key \
  -e OPENAI_MODEL=gpt-4 \
  your-registry/pdf-chatbot:latest
```

## 🔍 Monitoring and Logs

### View Logs
```bash
# Docker logs
docker logs pdf-chatbot

# Docker Compose logs
docker-compose logs -f
```

### Health Check
The application includes health checks:
- **Endpoint**: `http://localhost:8501/_stcore/health`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds

## 🚨 Troubleshooting

### Common Issues

1. **API Key Not Found**
   - Ensure `OPENAI_API_KEY` is set in environment variables
   - Check if the key is valid and has sufficient credits

2. **Port Already in Use**
   - Change port: `docker run -p 8502:8501 ...`
   - Or stop existing service: `docker stop pdf-chatbot`

3. **Memory Issues**
   - Increase Docker memory limit
   - Reduce `CHUNK_SIZE` in environment variables

4. **Build Failures**
   - Check Python version compatibility
   - Ensure all dependencies are in requirements.txt

### Debug Mode
```bash
# Run with debug logging
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  -e STREAMLIT_LOGGER_LEVEL=debug \
  pdf-chatbot
```

## 📊 Performance Optimization

### For High Traffic
- Use `gpt-3.5-turbo` for faster responses
- Increase `CHUNK_SIZE` to 2000-3000
- Use multiple replicas with load balancer

### For Better Quality
- Use `gpt-4` model
- Increase `OPENAI_MAX_TOKENS`
- Fine-tune `OPENAI_TEMPERATURE`

## 🔄 Updates and Maintenance

### Rolling Updates
```bash
# Pull latest image
docker pull your-registry/pdf-chatbot:latest

# Update running container
docker-compose up -d --no-deps pdf-chatbot
```

### Backup
```bash
# Backup environment variables
docker exec pdf-chatbot env > backup.env

# Backup application data (if any)
docker cp pdf-chatbot:/app/data ./backup-data
```

## 📈 Scaling

### Horizontal Scaling
- Use Docker Swarm or Kubernetes
- Implement load balancing
- Use shared storage for file uploads

### Vertical Scaling
- Increase container resources
- Optimize chunk sizes
- Use faster models

## 🛡️ Security Considerations

- ✅ Use HTTPS in production
- ✅ Set up proper CORS policies
- ✅ Implement rate limiting
- ✅ Monitor API usage
- ✅ Regular security updates
- ✅ Use secrets management
