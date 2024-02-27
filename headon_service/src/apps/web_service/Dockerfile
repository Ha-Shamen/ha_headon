FROM python:3.11

ENV MAPTILER_API=sEnYawWlhALyqHmgBl4Z \
    OPENWEATHER_API=d89c5a28017072fec7ea15cd6a381120

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install 

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "api.web_service:app", "--bind", "0.0.0.0:3000"]