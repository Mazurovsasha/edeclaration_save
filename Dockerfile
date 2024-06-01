# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install PyInstaller
RUN pip install pyinstaller

# Specify the Python script to run
ENV PYTHON_SCRIPT main.py

# Build the Python script into a standalone executable
RUN pyinstaller --onefile $PYTHON_SCRIPT

# Set the output directory where the executable will be saved
ENV EXE_DIR /app/dist

# Copy the generated exe file to the user's Desktop with the name "Save_declaration.exe"
CMD cp $EXE_DIR/*.exe /mnt/c/Users/sasha/Desktop/Save_declaration.exe
