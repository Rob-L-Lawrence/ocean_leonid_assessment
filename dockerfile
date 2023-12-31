FROM python:3.11

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8050

CMD ["python", "main.py"]