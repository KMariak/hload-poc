Прототип веб-додатку, який імітує роботу системи з високим навантаженням


- Підтримує аутентифікацію через AWS Cognito 🚫 (LocalStack AWS Congito лише у Pro версії)
- Зберігає текстові файли в AWS S3 (LocalStack) ✅
- Обробляє задачі у фоновому режимі через Celery ✅
- Відображає результати з затримкою у 10 секунд ✅


Для запуску прототипу виконайте наступні команди:

git clone git@github.com:KMariak/hload-poc.git

cd hload-poc

docker-compose up --build

Перейдіть за посиланням:
http://localhost:5173/

