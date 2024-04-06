FROM python:3.9



# Set the working directory in the container
WORKDIR /app

    
# Install dependencies
RUN pip install django
RUN pip install mysql-connector
RUN pip install boto3

# Copy the current directory contents into the container at /app
COPY  one /app/

# Expose port 8000 to allow communication to/from the container
EXPOSE 8000

# Run the Django development server
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]

