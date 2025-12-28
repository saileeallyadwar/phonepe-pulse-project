# 📊 PhonePe Pulse Data Visualization and Exploration  
### A User-Friendly Tool Using Streamlit and Plotly

---

## 🧾 Project Overview

This project is an end-to-end **Data Science and Data Visualization application** developed using the **PhonePe Pulse open dataset**.  
The objective of this project is to extract large-scale digital payment data from the PhonePe Pulse GitHub repository, transform and store it in a **MySQL database**, and build an **interactive, user-friendly dashboard** using **Streamlit and Plotly** to visualize key insights.

The dashboard enables users to dynamically explore digital payment trends through multiple dropdown filters and interactive visualizations.

---

## 🏦 Domain

**FinTech (Financial Technology)**

---

## 🛠️ Technologies Used

- GitHub (Dataset Cloning)
- Python
- Pandas
- MySQL
- mysql-connector-python
- Streamlit
- Plotly

---

## 🎯 Problem Statement

The PhonePe Pulse GitHub repository contains a large amount of digital payment data related to transactions, users, and insurance across India.  
The goal of this project is to extract, process, store, and visualize this data in a **user-friendly and insightful manner**.

The solution includes:
- Extracting data from GitHub using scripting
- Cleaning and transforming JSON data using Python and Pandas
- Storing transformed data in MySQL
- Building an interactive Streamlit dashboard
- Fetching data dynamically from MySQL
- Providing multiple dropdowns for user-driven analysis

---

## 🧠 Project Approach

### 1️⃣ Data Extraction
- Cloned the official **PhonePe Pulse GitHub repository**
- Extracted JSON files programmatically using Python
- Traversed state, year, and quarter-level data folders

### 2️⃣ Data Transformation
- Parsed nested JSON structures
- Extracted relevant fields:
  - State
  - Year
  - Quarter
  - Transaction Type
  - Transaction Count
  - Transaction Amount
- Cleaned and structured data using Pandas DataFrames

### 3️⃣ Database Insertion
- Created a MySQL database named `phonepe_pulse`
- Designed tables to store transaction data
- Inserted transformed data using `mysql-connector-python`

### 4️⃣ Dashboard Creation
- Developed an interactive dashboard using **Streamlit**
- Used **Plotly** to create:
  - KPI cards
  - Bar charts
  - Donut charts
  - Line charts
  - State comparison views
- Designed a clean and intuitive UI with multiple dropdown filters

### 5️⃣ Data Retrieval
- Dashboard fetches data directly from the MySQL database
- All visualizations update dynamically based on user input

### 6️⃣ Deployment & Testing
- Tested the application locally
- Ensured portability and maintainability
- Ready for public demo and evaluation

---

## 📂 Project Folder Structure

phonepe-pulse-project/ │ ├── dashboard/ │ └── app.py │ ├── data_transformation/ │ └── transform_data.py │ ├── database/ │ └── insert_aggregated_transaction.py │ ├── requirements.txt └── README.md
`

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
bash git clone https://github.com/PhonePe/pulse.git
`

### Step 2: Create Virtual Environment (Optional)
bash python -m venv venv source venv/bin/activate
### Step 3: Install Dependencies
bash pip install -r requirements.txt
### Step 4: Run Data Transformation
bash python data_transformation/transform_data.py
### Step 5: Insert Data into MySQL
bash python database/insert_aggregated_transaction.py
### Step 6: Launch Streamlit Dashboard
bash python -m streamlit run dashboard/app.py
Open the browser at:
http://localhost:8501
---

## 📊 Dashboard Features

* 📌 KPI Cards

  * Total Transaction Amount
  * Total Transaction Count
  * Average Transaction Value

* 🏆 Top States by Transactions

* 🍩 Transaction Type Distribution

* 📈 Year & Quarter-wise Transaction Trends

* 🔍 State Comparison using Multi-select

* 📂 Raw Data Viewer

* 🎛️ More than 10 interactive dropdown filters

---

## ✅ Project Evaluation Compliance

✔ Modular and maintainable code
✔ Portable across operating systems
✔ Public GitHub repository
✔ Proper README documentation
✔ PEP-8 coding standards followed
✔ Interactive dashboard with dynamic updates
✔ LinkedIn demo video (mandatory)

---

## 📈 Results & Insights

* Identified top-performing states in digital transactions
* Analyzed growth trends across quarters and years
* Observed transaction category distribution
* Enabled dynamic, user-driven data exploration

---

## 🎓 Learning Outcomes

* GitHub-based data extraction
* Handling large nested JSON datasets
* Relational database design using MySQL
* Interactive dashboard development using Streamlit
* Data visualization using Plotly
* End-to-end project implementation

---

## 🔗 Dataset Source

**PhonePe Pulse GitHub Repository**
[https://github.com/PhonePe/pulse](https://github.com/PhonePe/pulse)

---

## 🧑‍💻 Author

**Sailee Prashant Allyadwar**
Data Science & Analytics Enthusiast
---