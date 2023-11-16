# Stage 1: Build
FROM python:3.10.2 AS build

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10.2-slim AS runtime

WORKDIR /app
COPY --from=build /app .
COPY src .

CMD [ "uvicorn", "src.entrypoints.http.v1.controllers:app", "--reload", "--host", "0.0.0.0", "--port", "3000" ]