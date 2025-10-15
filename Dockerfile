FROM python:3.11-slim

WORKDIR /app

COPY dockerrequirements.txt .

RUN python -m pip install --upgrade pip && pip install -r dockerrequirements.txt

COPY . .

EXPOSE 7003

ENTRYPOINT [ "python", "app.py" ]

