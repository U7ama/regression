import pandas as pd
import json
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Function to load tree data
def load_tree_data(json_path):
    with open(json_path, 'r') as file:
        tree_data = json.load(file)
    return tree_data

# Function to flatten the tree data and create a mapping of street names to tree heights
def create_street_tree_mapping(tree_data):
    street_tree_map = {}
    for height_category, categories in tree_data.items():
        for category_type, subcategories in categories.items():
            for subcategory, streets in subcategories.items():
                if isinstance(streets, dict):
                    for street_name, value in streets.items():
                        street_tree_map[street_name.lower()] = value
                elif isinstance(streets, list):
                    for street in streets:
                        street_tree_map[str(street).lower()] = None  # Handle if list elements are not key-value pairs
                else:
                    street_tree_map[str(streets).lower()] = None
    return street_tree_map

# Function to preprocess property data
def preprocess_property_data(csv_path, street_tree_map):
    property_data = pd.read_csv(csv_path, delimiter=',', encoding='latin1')
    
    # Rename columns for easier access
    property_data.rename(columns={'Date of Sale (dd/mm/yyyy)': 'Date_of_Sale'}, inplace=True)
    
    # Clean Price column
    property_data['Price'] = property_data['Price'].apply(lambda x: float(re.sub(r'[^\d.]', '', x)))
    
    # Convert Date_of_Sale to datetime
    property_data['Date_of_Sale'] = pd.to_datetime(property_data['Date_of_Sale'], dayfirst=True)
    
    # Extract Year and Month from Date_of_Sale
    property_data['Year'] = property_data['Date_of_Sale'].dt.year
    property_data['Month'] = property_data['Date_of_Sale'].dt.month
    
    # Map Tree Height based on Street Name
    property_data['Street_Name_Lower'] = property_data['Street Name'].str.lower()
    property_data['Tree_Height_Value'] = property_data['Street_Name_Lower'].map(street_tree_map)
    
    # Handle unknown tree heights by assigning a default value or encoding as a separate category
    # Here, we'll assign the median tree height value
    median_tree_height = property_data['Tree_Height_Value'].median()
    property_data['Tree_Height_Value'] = property_data['Tree_Height_Value'].fillna(median_tree_height)

    # Alternatively, you can create a binary feature if the numerical values represent categories
    # property_data['Tree_Height_Category'] = property_data['Tree_Height_Value'].apply(lambda x: 1 if x > threshold else 0)
    
    return property_data

# Function to perform exploratory data analysis
def exploratory_data_analysis(df):
    # Plot distribution of prices
    plt.figure(figsize=(10,6))
    sns.histplot(df['Price'], bins=50, kde=True)
    plt.title('Distribution of Property Prices')
    plt.xlabel('Price (€)')
    plt.ylabel('Frequency')
    plt.show()
    
    # Boxplot of Price by Tree Height Category
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Tree_Height_Value', y='Price', data=df)
    plt.title('Property Prices by Tree Height Value')
    plt.xlabel('Tree Height Value')
    plt.ylabel('Price (€)')
    plt.show()
    
    # Correlation matrix
    plt.figure(figsize=(8,6))
    sns.heatmap(df[['Price', 'Tree_Height_Value', 'Year', 'Month']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

# Function to train and evaluate the model
def train_evaluate_model(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize models
    linear_model = LinearRegression()
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train Linear Regression
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)
    
    # Train Random Forest
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    
    # Evaluate Linear Regression
    mae_linear = mean_absolute_error(y_test, y_pred_linear)
    r2_linear = r2_score(y_test, y_pred_linear)
    rmse_linear = np.sqrt(mean_squared_error(y_test, y_pred_linear))
    
    # Evaluate Random Forest
    mae_rf = mean_absolute_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)
    rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
    
    # Cross-validation for Random Forest
    cv_scores = cross_val_score(rf_model, X, y, cv=5, scoring='r2')
    
    # Print Evaluation Metrics
    print("Linear Regression Performance:")
    print(f"MAE: {mae_linear:.2f}, RMSE: {rmse_linear:.2f}, R^2: {r2_linear:.2f}\n")
    
    print("Random Forest Performance:")
    print(f"MAE: {mae_rf:.2f}, RMSE: {rmse_rf:.2f}, R^2: {r2_rf:.2f}")
    print(f"Cross-Validation R^2 Scores: {cv_scores}")
    print(f"Average CV R^2 Score: {cv_scores.mean():.2f}")
    
    return rf_model

# Function to visualize model predictions
def visualize_model_performance(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    plt.figure(figsize=(10,6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
    plt.title('Actual vs Predicted Prices')
    plt.xlabel('Actual Prices (€)')
    plt.ylabel('Predicted Prices (€)')
    plt.show()
    
    # Feature importance for Random Forest
    if hasattr(model, 'feature_importances_'):
        feature_importances = pd.Series(model.feature_importances_, index=X_test.columns)
        feature_importances.sort_values(ascending=True).plot(kind='barh')
        plt.title('Feature Importances')
        plt.xlabel('Importance')
        plt.show()

def main():
    # Paths to data files
    tree_json_path = 'trees-data.json'
    property_csv_path = 'property-data.csv'
    
    # Load and preprocess data
    tree_data = load_tree_data(tree_json_path)
    street_tree_map = create_street_tree_mapping(tree_data)
    property_data = preprocess_property_data(property_csv_path, street_tree_map)
    
    # Exploratory Data Analysis
    exploratory_data_analysis(property_data)
    
    # Feature Selection
    features = ['Tree_Height_Value', 'Year', 'Month']
    X = property_data[features]
    y = property_data['Price']
    
    # Train and evaluate model
    model = train_evaluate_model(X, y)
    
    # Visualize model performance
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    visualize_model_performance(model, X_test, y_test)
    
    # Save the trained model for later use (e.g., in a React app)
    import joblib
    joblib.dump(model, 'property_price_model.joblib')
    print("Model saved as 'property_price_model.joblib'")

if __name__ == "__main__":
    main()
