# Показывает какой фреймворк используется
FROM node

# Рабочая директория 
WORKDIR /app

COPY package.json /app

# Запускается один раз
RUN npm install

COPY . .

ENV PORT 4200

# Рабочий сервер
EXPOSE $PORT

# Запускается постоянно
CMD ["node", "app.js"]