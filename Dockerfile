FROM python:3.13

# Create app directory
RUN mkdir -p /app

# Copy application files
COPY ./app.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set working directory
WORKDIR /app

# Expose the port that Streamlit runs on
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]