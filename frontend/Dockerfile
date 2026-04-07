# filepath: frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy frontend source
COPY frontend/ ./

# Expose Vite dev server port
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
