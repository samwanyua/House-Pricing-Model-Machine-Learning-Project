# 🏠 California Housing Price Prediction

## 🚀 Project Overview
This project involves predicting housing prices in California using machine learning techniques. It employs data preprocessing, exploratory data analysis (EDA), and machine learning algorithms to build a predictive model for median house value based on selected features.

## 🚀 Live Demo

You can access the live demo of the application here:  
🔗 [Live Demo URL](https://web-production-273c.up.railway.app/)


---

## 📊 Exploratory Data Analysis (EDA)

### Dataset Overview

We analyzed the **California Housing dataset**, a well-known dataset used for regression tasks.

**Dataset Characteristics:**
- **Number of Instances:** 20,640  
- **Number of Attributes:** 8 numeric attributes & 1 target variable  
- **Target Variable:** Median House Value (`MedHouseVal`)  
- **Features:**  
  - `MedInc`: Median income in the block group  
  - `HouseAge`: Median house age in the block group  
  - `AveRooms`: Average number of rooms per household  
  - `AveBedrms`: Average number of bedrooms per household  
  - `Population`: Block group population  
  - `AveOccup`: Average number of household members  
  - `Latitude`: Block group latitude  
  - `Longitude`: Block group longitude  

---

### Data Sample

The first few rows of the dataset are as follows:

| MedInc   | HouseAge | AveRooms  | AveBedrms | Population | AveOccup | Latitude | Longitude | **Price** |
|---------|----------|-----------|-----------|-------------|----------|----------|------------|------------|
| 8.3252  | 41       | 6.984127  | 1.023810  | 322         | 2.555556 | 37.88    | -122.23   | 4.526     |
| 8.3014  | 21       | 6.238137  | 0.971880  | 2401        | 2.109842 | 37.86    | -122.22   | 3.585     |
| 7.2574  | 52       | 8.288136  | 1.073446  | 496         | 2.802260 | 37.85    | -122.24   | 3.521     |
| 5.6431  | 52       | 5.817352  | 1.073059  | 558         | 2.547945 | 37.85    | -122.25   | 3.413     |
| 3.8462  | 52       | 6.281853  | 1.081081  | 565         | 2.181467 | 37.85    | -122.25   | 3.422     |

---

### Key Insights from EDA
After preprocessing and visualization, the following observations were made:

- **Median Income vs House Prices:** A strong positive correlation was observed between median income (`MedInc`) and house prices.
- **House Age and Occupancy Patterns:** Analysis showed dependencies between `HouseAge`, average number of people per household (`AveOccup`) and house prices.
- **Geographical patterns:** Variations in geographical location (`Latitude`, `Longitude`) were considered to examine their effect on house prices.

---

### Correlation Matrix

We calculated correlations among all features to determine their relationship with the target variable:

| Feature      | Correlation with House Prices |
|---------------|-----------------------------|
| `MedInc`      | 0.688075                   |
| `HouseAge`     | 0.105623                   |
| `AveRooms`     | 0.151948                   |
| `AveBedrms`    | -0.046701                  |
| `Population`   | -0.024650                  |
| `AveOccup`     | -0.023737                  |
| `Latitude`     | -0.144160                  |
| `Longitude`    | -0.045967                  |

---

### Visualizations
Regression plots and scatter plots were created to visualize key features' relationships with house prices. They include:

1. **Median Income vs House Prices**  
2. **Average Occupancy vs House Prices**  
3. **Geographical Variances** by mapping house prices across latitude and longitude features.

These visualizations revealed trends and dependencies for feature engineering and further model development.

---

## 🛠️ Tech Stack

- **Python** with **scikit-learn**, **pandas**, **matplotlib**, and **seaborn** for data analysis and visualization.  
- Machine Learning techniques applied include Regression models to predict the **Price**.  
- **Docker** for containerization to ensure consistent application environments.  
- **Railway** for deployment of the application to a live environment.  
- **GitHub Actions** for automating CI/CD workflows to streamline testing and deployment.  


---

## 💻 Installation

To get started with this project, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/yourrepository.git
```
### 2. Navigate into the project directory
```bash
cd yourrepository
```

### 3. Create a virtual environment
```bash
python -m venv venv
```

### 4. Activate the virtual environment
```bash
source venv/bin/activate
```
### 5. Install dependencies
```bash
pip install -r requirements.txt
```

## 📈 Next Steps

- Preprocessing data for better model compatibility  
- Train/test split and model training with different regression models  
- Hyperparameter tuning using cross-validation  
- Visualization of predictions vs actual house prices for insights.  



© 2024 | Made with ❤️ by Wanyua



