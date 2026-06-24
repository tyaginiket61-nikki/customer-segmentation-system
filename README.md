# Customer Segmentation Using K-Means Clustering

## Overview

Customer Segmentation is a Machine Learning project that groups customers into different segments based on their purchasing behavior and demographic characteristics. The goal is to help businesses better understand their customers and create targeted marketing strategies.

This project uses the **K-Means Clustering** algorithm to identify customer groups with similar characteristics.

---

## Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Scaling
- Optimal Cluster Selection using Elbow Method
- Customer Segmentation using K-Means Clustering
- Data Visualization of Customer Groups
- Business Insights Generation

---

## Dataset

The dataset contains customer information including:

- Customer ID
- Gender
- Age
- Annual Income
- Spending Score

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook

---

## Project Workflow

### 1. Data Collection
Loaded and explored the customer dataset.

### 2. Data Preprocessing
- Checked missing values
- Removed inconsistencies
- Selected relevant features

### 3. Exploratory Data Analysis
- Analyzed customer distributions
- Identified patterns and trends

### 4. Feature Scaling
Standardized numerical features to improve clustering performance.

### 5. Finding Optimal Clusters
Used the Elbow Method to determine the optimal number of customer segments.

### 6. Customer Segmentation
Applied K-Means Clustering to divide customers into meaningful groups.

### 7. Visualization
Visualized clusters to understand customer behavior and segment characteristics.

---

## Results

The model successfully segmented customers into distinct groups based on annual income and spending behavior.

Example customer segments:

| Cluster | Customer Type |
|----------|--------------|
| 0 | High Income, High Spending |
| 1 | High Income, Low Spending |
| 2 | Average Customers |
| 3 | Low Income, High Spending |
| 4 | Low Income, Low Spending |

These insights can help businesses improve marketing strategies, customer retention, and product recommendations.

---

## Project Structure

```text
Customer-Segmentation/
│
├── Customer_Segmentation.ipynb
├── Mall_Customers.csv
├── README.md
├── requirements.txt
└── images/
    ├── elbow_method.png
    └── customer_clusters.png
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/customer-segmentation.git
```

### Navigate to Project Directory

```bash
cd customer-segmentation
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
jupyter notebook
```

Open `Customer_Segmentation.ipynb` and run all cells.

---

## Sample Visualizations

### Elbow Method
Used to determine the optimal number of clusters.

### Customer Clusters
Visualization of customer groups based on spending score and annual income.

> Add screenshots of your visualizations in the `images` folder and display them here.

```markdown
![Elbow Method](images/elbow_method.png)

![Customer Clusters](images/customer_clusters.png)
```

---

## Business Impact

- Enables targeted marketing campaigns
- Improves customer retention strategies
- Helps identify high-value customers
- Supports data-driven business decisions

---

## Future Enhancements

- Deploy the model using FastAPI or Streamlit
- Implement DBSCAN and Hierarchical Clustering
- Add interactive dashboards
- Use real-world customer datasets

---

## Key Skills Demonstrated

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Unsupervised Learning
- K-Means Clustering
- Data Visualization
- Business Analytics

---

## Author

**Niket Tyagi**

Aspiring Machine Learning Engineer passionate about Machine Learning, NLP, and Data Science.

### Connect With Me

- LinkedIn: [linkdin.com/in/niket-tyagi29]
- GitHub: [tyaginiket61-nikki]

---
