FROM python:3-alpine3.15
ENV APP_ENV=production
ENV APP_DEBUG=False
ENV API_KEY=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
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD python ./App.py
