import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
data = pd.read_csv('/Users/krinapatel/Documents/GitHub/Stroke_Prediction/stroke.csv')

#Data Cleaning

#identify missing values in the data
data.isna().sum()

#BMI: Replace all missing BMI values with the median BMI
index=data['bmi'].fillna(value=data['bmi'].median())
data['index']= index

#BMI INDEX: Identify health status (underweight, healtly, overweight or obese) based on bmi
data['health_status'] = data['bmi'].apply (lambda x: "Underweight" if x <= 18.5 else
                                              ("Healtly" if x > 18.5 and x < 25 else
                                              ("Overweight" if x > 25 and x < 30 else "Obese")))
data['health_status'] = data['health_status']


#GENDER: Replace 'other' gender with mode
data['gender'].value_counts()
data['F/M'] = data['gender'].replace('Other', list(data.gender.mode().values)[0])

#AGE
#Drop age less than 20
Age_Range = data.drop(data[data['age']< 20].index, inplace = True)

#make age groups
data['age_group'] = data['age'].apply (lambda x: "21-30" if x <= 30 else
                                              ("31-40" if x > 31 and x < 40 else
                                              ("41-50" if x > 41 and x < 50 else
                                              ("51-60" if x > 51 and x < 60 else
                                              ("61-71" if x > 61 and x < 71 else "71-80")))))

#Dataframe for prevelance of stroke in each age group
Stroke_prevalence_agegroup = data.groupby(["age_group"])["stroke"].count()

# Explanatory Data Analysis
# Effects of smoking on glucose tolerance

#Effects of smoking on glucose tolerance
Glucose_tolerance = sns.boxplot(x="smoking_status", y="avg_glucose_level", hue="F/M",data=data)
Glucose_tolerance.set_ylabel("Glucose levels")
Glucose_tolerance.set_xlabel("Smoking Status", fontsize = 10)
Glucose_tolerance.set_title("Effects of Smoking on Glucose Tolerance")
#Conclusion: Increase in glucose levels in men who formerly smoked suggests that smoking may have an significant effect on glucose tolerance


# Which age group is more Likely to experience a stroke?
#sort data by age_group in order to see age groups in order on the graph
data.sort_values(by=['age_group'], inplace=True)

#Prevelence of stroke in age groups
plt.subplots(figsize=(10,10))
plt.xlim(10,90,20)
plt.ylim(0,.2)
Age_vs_stroke = sns.barplot(x='age_group',y='stroke', data = data)
Age_vs_stroke.tick_params(labelsize=10)
Age_vs_stroke.set_ylabel("Prevalence of Stroke")
Age_vs_stroke.set_xlabel("Age Group", fontsize = 10)
Age_vs_stroke.set_title("Stroke Prevalence in Various Age Groups")

#Effect of Age on Hypertension
data.sort_values(by=['age_group'], inplace=True)
Age_vs_hypertension = sns.barplot(x="age_group", y="hypertension", hue="F/M",data=data)
Age_vs_hypertension.set_ylabel("Age Range")
Age_vs_hypertension.set_xlabel("Hypertension", fontsize = 10)
Age_vs_hypertension.set_title("Does Hypertension increase with age?")

# Does Work and Marriage life increase your chances of stroke
work_vs_Stroke = sns.barplot(x="work_type", y="stroke", hue="ever_married",data=data)
work_vs_Stroke.set_ylabel("Stroke Prevelance")
work_vs_Stroke.set_xlabel("Work Life", fontsize = 10)
work_vs_Stroke.set_title("Does Work and Marriage life increase your chances of stroke")



