##used DecisinTreeRegressor, SVM and KNeighborsRegressor and found KNeighborsRegressor to be
##more accurate. Here implemented only svm If u want to try other regressors 
##just remove commenting. It's a temporary uncleaned file , final cleaned file will be realeased soon.

import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
from sklearn import datasets
from sklearn import metrics
####from sklearn.tree import DecisionTreeRegressor
####from sklearn.neighbors import KNeighborsRegressor as KNR
from sklearn import svm


voice_data = pd.read_csv("feat.csv")
print "facial data read successfully!"
voicetest_data = pd.read_csv("feattest.csv")
print "test data read successfully:"

for d in [voice_data]:
    d[-1] = voice_data[voice_data.columns[-1]].apply(lambda im: np.fromstring(im, sep=' '))
####face_data = face_data[:40]
####face_data_1['Image'] = face_data_1['Image'].apply(lambda im: np.fromstring(im, sep=' '))

##there is no abnormality in data
##face_data = face_data.dropna()
####test_data = test_data.fillna(face_data.mean())
####face_data =face_data.astype(np.float)

 
total_samples = voice_data.shape[0]
total_features = voice_data.shape[1]
print"total_features", total_features
###print face_data.head()

##x_all = np.vstack(voice_data.ix[:, 'Image']).astype(np.float)
##x_all = np.vstack([voice_data[-1]]).astype(np.float)
x_all = np.vstack(voice_data.ix[:,-1]).astype(np.float)
print "x_all",x_all
y_all = voice_data.drop([voice_data.columns[-1]], axis=1).values
y_all = voice_data.drop('ImageId', axis=1).values

print "y_all", y_all
def preprocess_features(X):
    ''' Preprocesses the student data and converts non-numeric binary variables into
        binary (0/1) variables. Converts categorical variables into dummy variables. '''
    
    # Initialize new output DataFrame
    output = pd.DataFrame(index = X.index)
'''
    # Investigate each feature column for the data
    for col, col_data in X.iteritems():
        
        # If data type is non-numeric, replace all yes/no values with 1/0
        if col_data.dtype == object:
            col_data = col_data.replace(['english', 'hindi'], [1, 0])

        # If data type is categorical, convert to dummy variables
        if col_data.dtype == object:
            # Example: 'school' => 'school_GP' and 'school_MS'
            col_data = pd.get_dummies(col_data, prefix = col)  
        
        # Collect the revised columns
        output = output.join(col_data)
    
    return output
y_all = preprocess_features(y_all)
'''
####print "test_x_all",test_x_all
####test_y_all = test_data.drop('Image', axis=1).values
#####print "test_y_all", test_y_all
##print "feature columns:", feature_columns
##print "target columns:", target_columns



##print "features:", x_all.head()
##print "tagets:", y_all.head()


####test = 200
####x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size = test, random_state = 5)
####print x_train.shape[0]
####print y_train.shape[0]



##print x_train.column[1]
##print y_train.column[1]


####reg = DecisionTreeRegressor(max_depth=5)
####reg.fit(x_train,y_train)
####predicts = reg.predict(x_test)
####print "total_error:", metrics.mean_squared_error(y_test, predicts)
####print "accuracy:", reg.score(x_train, y_train)
####reg2 = KNR()
####reg2.fit(x_all, y_all)
####predicts2 = reg2.predict(x_test)
####print "total_error:", metrics.mean_squared_error(y_test, predicts2)

####print "accuracy:", reg2.score(x_all, y_all)

reg3 = svm.SVR()
reg3.fit(x_all, y_all) 
####SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',
####   kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
predicts3 = reg3.predict(x_test)
print "total_error:", metrics.mean_squared_error(y_test, predicts3)
####print "accuracy:", reg3.score(x_train, y_train)
###predictions = reg.predict(test_x_all)
###print predicts

###print "total error:", total_error
for d in [feattest_data]:
    d['Image'] = feattest_data['Image'].apply(lambda im: np.fromstring(im, sep=' '))
# stack all test images into one numpy array
test_x_all = np.vstack(voicetest_data.ix[:, 'Image']).astype(np.float)
####test_x_all = test_x_all.dropna()
test_x_all = voice_data.drop('ImageId', axis=1).values
# predict all keypoints for the images in Y
predictions = reg3.predict(test_x_all)
print predictions
# now create the result data and write to csv
