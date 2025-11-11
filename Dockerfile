#Start from lightweight python image (version)
From python:3.11-slim

#set working directory inside containers file system and not local machine
WORKDIR /app

#copy dependencies required for image to run and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copies rest of app files required to run flas app Copy everything from my current local directory (the one where this Dockerfile lives) into the current working directory inside the image (which we set earlier using WORKDIR /app
COPY . .

#Expose Flask port, tells docker what port the app uses
EXPOSE 5000

# Command used to run the app
CMD ["python", "app.py"]