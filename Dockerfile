FROM python:3.14

WORKDIR /app











# FROM python:3.11-slim

# WORKDIR /code

# COPY requirement.txt .
# RUN pip install -r requirement.txt

# COPY . .

# ENV PYTHONPATH=/code

# CMD ["uvicorn", "testapp.main:app", "--host", "0.0.0.0", "--port", "8000"]





# FROM python:3

# RUN mkdir -p fastapi

# COPY . /testapp

# RUN pip install --no-cache-dir -r requirement.txt


# CMD ["uvicorn","testapp.main:app","--reload"]



# WORKDIR /code


# COPY requirement.txt .
# RUN pip install --no-cache-dir -r requirement.txt

# COPY . .
 

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]