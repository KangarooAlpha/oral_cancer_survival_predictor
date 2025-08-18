import pandas as pd
import numpy as np
import xgboost 
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.feature_selection import RFE, SelectKBest, mutual_info_classif
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("oral_cancer_prediction_dataset.csv")

def clean(data):
        
    data = data.replace("?", np.nan)
    data = data.replace({'No':0,'Yes':1})
    data = data.replace({'Male':0, 'Female':1})

    def classify(t):
        match t:
            case "No Treatment":
                return 0
            case "Surgery":
                return 1
            case "Radiation":
                return 2
            case "Targeted Therapy":
                return 3
            case "Chemotherapy":
                return 4
    data["Treatment Type"] = data["Treatment Type"].apply(classify)
    data = data.replace({'Low':0,'Moderate':1,'High':2})
    data = data.dropna().drop_duplicates()
    data = data.drop(columns=["ID", "Country"])
    
    return data

data = clean(data)

'''att = ['Age','Gender','Tobacco Use','Alcohol Consumption','HPV Infection','Betel Quid Use',
       'Chronic Sun Exposure','Poor Oral Hygiene', 'Diet (Fruits & Vegetables Intake)',
       'Family History of Cancer','Compromised Immune System','Oral Lesions','Unexplained Bleeding',
       'Difficulty Swallowing','White or Red Patches in Mouth','Early Diagnosis', 
       'Tumor Size (cm)','Cancer Stage','Treatment Type',
       'Cost of Treatment (USD)','Economic Burden (Lost Workdays per Year)',
       'Early Diagnosis','Oral Cancer (Diagnosis)']'''
att = ['Gender', 'Tobacco Use', 'Family History of Cancer', 'Cancer Stage',
       'Oral Cancer (Diagnosis)']
#att = ['Tumor Size (cm)', 'Cancer Stage', 'Cost of Treatment (USD)',
#       'Economic Burden (Lost Workdays per Year)', 'Oral Cancer (Diagnosis)']
x = data[att]
y = data["Survival Rate (5-Year, %)"]

y = pd.cut(y,bins=[0,20,40,60,80,100],labels=["Very Low (<20%)", "Low (20% - 40%)",
                            "Moderate (40% - 60%)", "High (60% - 80%)",
                            "Very High (>80%)"])

xtrain, xtest, ytrain, ytest = train_test_split(x,y,train_size=0.7,random_state=6)


# Feature Selection
corr_matrix = data.corr()
plt.figure(figsize=(20, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.savefig('output/hm.png')
plt.show()

plt.figure(figsize=(5, 10))
y.value_counts().plot(kind='bar')
plt.savefig('output/bar.png')
plt.show()


model = LogisticRegression(max_iter=1000)
selector = RFE(estimator=model, n_features_to_select=5)
selector = selector.fit(x, y)
selected_features = x.columns[selector.support_]
print('Logistic Regression features:',selected_features)

selector = SelectKBest(score_func=mutual_info_classif, k=5)
xn = selector.fit_transform(x, y)
selected_features = x.columns[selector.get_support()]
print("KBest features:", selected_features)


#Models

#1 Decision Tree
tree = DecisionTreeClassifier(criterion="entropy", splitter='best',
                              class_weight="balanced", max_depth=6)

tree = tree.fit(xtrain,ytrain)
ypred = tree.predict(xtest)


plt.figure(figsize=(30,10))
plot_tree(tree, feature_names=att, class_names=["Very Low (<20%)", "Low (20%% - 40%)",
                            "Moderate (40%% - 60%)", "High (60%% - 80%)",
                            "Very High (>80%)"], filled=True, fontsize=4)
plt.savefig('output/tree1.png')
plt.show()

print('Decision Tree Accuracy: ',accuracy_score(ytest,ypred))
print(cross_val_score(tree, xtest, ytest, cv=10, scoring='accuracy').mean())
cfm = confusion_matrix(ytest,ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/dt_cfm1.png')
plt.show()

#2 Knn
knn_model = KNeighborsClassifier(n_neighbors=5)
sc = StandardScaler()
xtrain = sc.fit_transform(xtrain)
xtest = sc.fit_transform(xtest)
knn_model.fit(xtrain, ytrain)

ypred = knn_model.predict(xtest)
print('KNN Accuracy: ',accuracy_score(ytest,ypred))
print(cross_val_score(knn_model, xtest, ytest, cv=10, scoring='accuracy').mean())
cfm = confusion_matrix(ytest,ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/knn_cfm1.png')
plt.show()


#3 SVM
#data = pd.read_csv("oral_cancer_prediction_dataset.csv")
#data = clean(data)
x = data[att]
y = data["Survival Rate (5-Year, %)"]

y = pd.cut(y,bins=[0,20,40,60,80,100],labels=["Very Low (<20%)", "Low (20% - 40%)",
                            "Moderate (40% - 60%)", "High (60% - 80%)",
                            "Very High (>80%)"])

xtrain, xtest, ytrain, ytest = train_test_split(x,y,train_size=0.7,random_state=6)
sv = svm.SVC(kernel='rbf')
sv.fit(xtrain,ytrain)

ypred = sv.predict(xtest)
print('SVM Accuracy:', accuracy_score(ytest, ypred))
print(cross_val_score(sv, xtest, ytest, cv=10, scoring='accuracy').mean())
cfm = confusion_matrix(ytest,ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/svm_cfm1.png')

#4 XGboost
y = pd.cut(data["Survival Rate (5-Year, %)"], bins=5, labels=[0,1,2,3,4])
x = data[att]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, random_state=6)
xgb = xgboost.XGBClassifier()
xg = xgb.fit(xtrain, ytrain)

ypred = xg.predict(xtest)
print('XGBoost Accuracy: ', accuracy_score(ytest, ypred))
print(cross_val_score(xg, xtest, ytest, cv=10, scoring='accuracy').mean())
cfm = confusion_matrix(ytest, ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/xg_cfm1.png')

#5 MLP
mlp = MLPClassifier(hidden_layer_sizes=(50,50),max_iter=1000)
mlp.fit(xtrain,ytrain)
ypred = mlp.predict(xtest)

print('MLP Accuracy: ', accuracy_score(ytest, ypred))
print(cross_val_score(mlp, xtest, ytest, cv=10, scoring='accuracy').mean())
cfm = confusion_matrix(ytest,ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/mlp_cfm1.png')


#6 Gausian Naive Bayes
gnb = GaussianNB()
data = data[att]
data = pd.get_dummies(x)
xtrain, xtest, ytrain, ytest = train_test_split(data,y,train_size=0.8,random_state=6)
nb = gnb.fit(xtrain,ytrain)
ypred = gnb.predict(xtest)
print('GNB Accuracy:',accuracy_score(ytest,ypred))
p = pd.DataFrame({'Age':[22], 'Gender':[1], 'Tobacco Use':[0], 'Alcohol Consumption':[0],
                  'HPV Infection':[0], 'Betel Quid Use':[0], 'Chronic Sun Exposure':[0],
                  'Poor Oral Hygiene':[0], 'Diet (Fruits & Vegetables Intake)':[1], 
                  'Family History of Cancer':[0], 'Compromised Immune System':[0],
                  'Oral Lesions':[0], 'Unexplained Bleeding':[0],'Difficulty Swallowing':[0],
                  'White or Red Patches in Mouth':[0],'Early Diagnosis':[0], 'Tumor Size (cm)':[0],
                  'Cancer Stage':[0], 'Treatment Type':[0], 'Cost of Treatment (USD)':[0], 
                  'Economic Burden (Lost Workdays per Year)':[0],'Early Diagnosis':[0], 'Oral Cancer (Diagnosis)':[0]
})
p = pd.get_dummies(p)
p = p.reindex(columns=xtrain.columns, fill_value=0)
print('GNB Probabilities: ', nb.predict_proba(p))
print(cross_val_score(nb, xtest, ytest, cv=10, scoring='accuracy').mean())

cfm = confusion_matrix(ytest,ypred)
disp = ConfusionMatrixDisplay(confusion_matrix=cfm)
disp.plot()
plt.savefig('output/gnb_cfm1.png')

joblib.dump(tree, 'models/dt.pkl')
joblib.dump(knn_model, 'models/knn.pkl')
joblib.dump(sc, 'models/scaler.pkl')
joblib.dump(sv, 'models/svm.pkl')
joblib.dump(xg, 'models/xgb.pkl')
joblib.dump(mlp, 'models/mlp.pkl')
joblib.dump(nb, 'models/gnb.pkl')