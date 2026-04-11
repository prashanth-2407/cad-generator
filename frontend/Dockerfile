# Build stage
FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install

COPY . .
RUN npm run build


# Serve stage
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

# 🔥 THIS IS THE FIX
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]