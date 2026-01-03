# Deployment Guide

Complete deployment guide for Digital Fatigue Manager

## Local Development

### Prerequisites
- Python 3.10+
- Node.js 18+
- SQLite (comes with Python)
- Virtual environment (recommended)

### Backend Deployment

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Initialize database:**
   ```bash
   python -c "from backend.models.database import init_db; init_db()"
   ```

5. **Run backend:**
   ```bash
   # Development (with auto-reload)
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   
   # Or using the main.py script
   cd backend
   python main.py
   ```

### Frontend Deployment

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Run development server:**
   ```bash
   npm run dev
   ```

3. **Build for production:**
   ```bash
   npm run build
   ```

4. **Preview production build:**
   ```bash
   npm run preview
   ```

## Production Deployment

### Option 1: Docker (Recommended)

#### Backend Dockerfile

Create `Dockerfile` in project root:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY .env .env

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Frontend Dockerfile

Create `frontend/Dockerfile`:

```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/fatigue_manager
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=fatigue_manager
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Deploy:**
```bash
docker-compose up -d
```

### Option 2: Cloud Deployment

#### Backend (AWS/GCP/Azure)

**AWS (Elastic Beanstalk / ECS):**
1. Build Docker image
2. Push to ECR
3. Deploy to ECS or Elastic Beanstalk
4. Configure environment variables
5. Set up RDS (PostgreSQL) or use managed database

**GCP (Cloud Run / App Engine):**
1. Build and push container to GCR
2. Deploy to Cloud Run or App Engine
3. Configure environment variables
4. Set up Cloud SQL (PostgreSQL)

**Azure (App Service / Container Instances):**
1. Build and push to Azure Container Registry
2. Deploy to App Service or Container Instances
3. Configure application settings
4. Set up Azure Database for PostgreSQL

#### Frontend (Netlify / Vercel / AWS S3 + CloudFront)

**Netlify:**
1. Connect GitHub repository
2. Build command: `cd frontend && npm install && npm run build`
3. Publish directory: `frontend/dist`
4. Environment variables: Set `VITE_API_URL` to backend URL

**Vercel:**
1. Import project from GitHub
2. Framework preset: Vite
3. Root directory: `frontend`
4. Environment variables: Set `VITE_API_URL`

**AWS S3 + CloudFront:**
1. Build frontend: `cd frontend && npm run build`
2. Upload `dist/` to S3 bucket
3. Configure S3 bucket for static website hosting
4. Create CloudFront distribution
5. Set environment variables in build process

### Environment Variables

**Backend (.env):**
```env
# Application
DEBUG=False
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/fatigue_manager

# Gmail API
GMAIL_CLIENT_ID=your-gmail-client-id
GMAIL_CLIENT_SECRET=your-gmail-client-secret
GMAIL_REDIRECT_URI=https://your-domain.com/auth/gmail/callback

# Slack API
SLACK_CLIENT_ID=your-slack-client-id
SLACK_CLIENT_SECRET=your-slack-client-secret
SLACK_SIGNING_SECRET=your-slack-signing-secret
SLACK_BOT_TOKEN=xoxb-your-bot-token

# CORS
CORS_ORIGINS=https://your-frontend-domain.com

# Logging
LOG_LEVEL=INFO
```

**Frontend (.env):**
```env
VITE_API_URL=https://your-backend-domain.com/api
```

### Database Migration (SQLite → PostgreSQL)

1. **Install PostgreSQL adapter:**
   ```bash
   pip install psycopg2-binary
   ```

2. **Update DATABASE_URL:**
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/fatigue_manager
   ```

3. **Initialize database:**
   ```bash
   python -c "from backend.models.database import init_db; init_db()"
   ```

### SSL/HTTPS Setup

**Using Nginx (Recommended):**
1. Install Certbot
2. Get SSL certificate: `certbot certonly --nginx`
3. Configure Nginx reverse proxy
4. Update CORS_ORIGINS to use HTTPS

**Example Nginx config:**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }
}
```

### Monitoring & Logging

**Recommended tools:**
- **Application Monitoring**: Sentry, New Relic, Datadog
- **Logging**: ELK Stack, CloudWatch, Loggly
- **Uptime Monitoring**: UptimeRobot, Pingdom
- **Error Tracking**: Sentry

### Scaling

**Horizontal Scaling:**
- Use load balancer (AWS ELB, GCP Load Balancer)
- Multiple backend instances
- Session storage in Redis (if implementing auth)

**Database Scaling:**
- Use read replicas
- Connection pooling (SQLAlchemy with pgBouncer)
- Database indexing optimization

**Caching:**
- Redis for frequently accessed data
- Cache user settings
- Cache dashboard statistics

### Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Enable HTTPS/SSL
- [ ] Set DEBUG=False
- [ ] Configure CORS properly
- [ ] Implement authentication (JWT/OAuth)
- [ ] Use environment variables for secrets
- [ ] Enable database encryption
- [ ] Set up rate limiting
- [ ] Configure firewall rules
- [ ] Regular security updates
- [ ] Enable logging and monitoring
- [ ] Back up database regularly

### Backup & Recovery

**Database Backups:**
```bash
# PostgreSQL
pg_dump -U user fatigue_manager > backup.sql

# Automated backups (cron)
0 2 * * * pg_dump -U user fatigue_manager > /backups/backup_$(date +\%Y\%m\%d).sql
```

**Restore:**
```bash
psql -U user fatigue_manager < backup.sql
```

### Troubleshooting

**Backend not starting:**
- Check environment variables
- Verify database connection
- Check logs in `logs/` directory
- Ensure ports are not in use

**Frontend build errors:**
- Clear node_modules and reinstall
- Check Node.js version (18+)
- Verify environment variables

**API connection errors:**
- Check CORS configuration
- Verify backend URL in frontend
- Check firewall rules
- Verify SSL certificates

### Support

For deployment issues, check:
- Application logs
- Server logs
- Database logs
- Network/firewall logs

