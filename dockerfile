FROM python:3.11.4-slim-bookworm

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8050

CMD ["python", "./ocean_leonid/run.py"]