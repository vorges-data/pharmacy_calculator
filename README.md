# Streamlit Date Calculator for Therapy Systems

This project is a **Date Calculator for Therapy Systems** built with **Streamlit**. The app allows users to input various data related to therapy plans, including medication cycles, dosages, and authorization times, and calculates important metrics such as the number of boxes per cycle, total shipments, and authorization times. The results are presented in a user-friendly web interface.

## Features

- Calculate medication cycle pauses
- Compute the total number of shipments based on input data
- Display medication box quantities and shipment schedules
- Automatically handle user inputs, validations, and result formatting
- Clean, simple user interface using Streamlit
- Deployed on Streamlit Cloud

## Installation

### Requirements

- Python 3.7 or higher
- Poetry (for managing dependencies)

### Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
   cd REPOSITORY_NAME
    ```

2. **Install dependencies using Poetry:**
```bash
   poetry install
```

3. **Activate the virtual environment:**
```bash
   poetry shell
```

4. **Run the Streamlit app:**
```bash
   streamlit run Home.py
```