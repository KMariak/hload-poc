# Використовуємо офіційний Node.js образ
FROM node:latest

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо package.json і package-lock.json, щоб встановити залежності
COPY package.json package-lock.json /app/

# Встановлюємо залежності
RUN npm install

# Копіюємо всі файли проекту в контейнер
COPY . /app/

# Відкриваємо порт для додатка
EXPOSE 3000

# Запускаємо додаток
CMD ["npm", "start"]