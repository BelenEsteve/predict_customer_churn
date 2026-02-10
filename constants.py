'''
Docstring for predict_customer_churn.constants

Author: Belen Esteve
Date: Feb 2026
'''
# Paths
BANK_DATA_CSV_PATH = "./data/bank_data.csv"
OUTPUT_COLUMN_NAME = "Churn"
RESULTS_FOLDER_PATH = "./images/results/"
EDA_FOLDER_PATH = "./images/eda/"
MODELS_FOLDER_PATH = "./models/"
LOGS_PATH = "./logs/churn_library.log"

# Lists
CATEGORY_COLUMNS_LIST = [
    'Gender',
    'Education_Level',
    'Marital_Status',
    'Income_Category',
    'Card_Category'
]

QUANT_COLUMNS_LIST = [
    'Customer_Age',
    'Dependent_count',
    'Months_on_book',
    'Total_Relationship_Count',
    'Months_Inactive_12_mon',
    'Contacts_Count_12_mon',
    'Credit_Limit',
    'Total_Revolving_Bal',
    'Avg_Open_To_Buy',
    'Total_Amt_Chng_Q4_Q1',
    'Total_Trans_Amt',
    'Total_Trans_Ct',
    'Total_Ct_Chng_Q4_Q1',
    'Avg_Utilization_Ratio'
]
