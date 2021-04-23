# def warn(*args, **kwargs):
#     pass
# import warnings
# warnings.warn = warn

#... import sklearn stuff...
import warnings
warnings.filterwarnings("ignore")

import pandas as pd

from scipy.special import expit
import joblib
import xgboost

df = pd.read_csv('mean_and_sd.csv')
df = df.set_index('Unnamed: 0')
dict_df = df.to_dict()

Customer_Age = 57
Months_on_book = 36
Total_Relationship_Count = 5
Months_Inactive_12_mon = 1
Contacts_Count_12_mon = 1
Credit_Limit = 1678
Total_Revolving_Bal = 1162
Avg_Open_To_Buy = 516
Total_Amt_Chng_Q4_Q1 = 0.722
Total_Trans_Amt = 4402
Total_Trans_Ct = 87 
Total_Ct_Chng_Q4_Q1 = 0.851
Avg_Utilization_Ratio = 0.692

data_dict = {'Customer_Age':Customer_Age,
'Months_on_book':Months_on_book,
'Total_Relationship_Count':Total_Relationship_Count,
'Months_Inactive_12_mon':Months_Inactive_12_mon,
'Contacts_Count_12_mon':Contacts_Count_12_mon,
'Credit_Limit':Credit_Limit,
'Total_Revolving_Bal':Total_Revolving_Bal,
'Avg_Open_To_Buy':Avg_Open_To_Buy,
'Total_Amt_Chng_Q4_Q1':Total_Amt_Chng_Q4_Q1,
'Total_Trans_Amt':Total_Trans_Amt,
'Total_Trans_Ct':Total_Trans_Ct,
'Total_Ct_Chng_Q4_Q1':Total_Ct_Chng_Q4_Q1,
'Avg_Utilization_Ratio':Avg_Utilization_Ratio}

data_dict_normalize = data_dict

for key in data_dict:
    data_dict = {'Customer_Age':Customer_Age,
                'Months_on_book':Months_on_book,
                'Total_Relationship_Count':Total_Relationship_Count,
                'Months_Inactive_12_mon':Months_Inactive_12_mon,
                'Contacts_Count_12_mon':Contacts_Count_12_mon,
                'Credit_Limit':Credit_Limit,
                'Total_Revolving_Bal':Total_Revolving_Bal,
                'Avg_Open_To_Buy':Avg_Open_To_Buy,
                'Total_Amt_Chng_Q4_Q1':Total_Amt_Chng_Q4_Q1,
                'Total_Trans_Amt':Total_Trans_Amt,
                'Total_Trans_Ct':Total_Trans_Ct,
                'Total_Ct_Chng_Q4_Q1':Total_Ct_Chng_Q4_Q1,
                'Avg_Utilization_Ratio':Avg_Utilization_Ratio}
    
    for km in dict_df['mean']:
        if key == km:
            mean = dict_df['mean'][km]            
    for ksd in dict_df['sd']:
        if key == ksd:
            sd = dict_df['sd'][ksd]
    for nor in data_dict:
        if key == nor:
            data_dict_normalize[nor] = (data_dict[nor]-mean)/sd

data_sig = pd.DataFrame(data_dict_normalize,index=[0])

data_sig2 = expit(data_sig)

data_sig3 = data_sig2.to_numpy()

data_sig4 = pd.DataFrame(data_sig3,columns=data_sig2.columns)

loaded_model = joblib.load('model5.json')

y_pred = loaded_model.predict_proba(data_sig4)

print (y_pred)