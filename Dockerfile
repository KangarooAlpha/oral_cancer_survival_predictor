FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Default command to run prediction script
CMD ["python3", "predict.py", "--Gender", "1", "--Tobacco_Use", "0", "--Family_History_of_Cancer", "1", "--Cancer_Stage", "2", "--Oral_Cancer_Diagnosis", "1"]