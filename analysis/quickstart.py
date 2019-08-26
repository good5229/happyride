# Create your views here.
import re
import numpy
from sklearn import svm
from xgboost import XGBClassifier

csv = []
with open('./raw_data/train.csv', 'r', encoding='utf-8-sig') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

jb_csv = []
with open('./raw_data/test.csv', 'r', encoding='utf-8-sig') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n: float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        jb_csv.append(cols)

total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(total_len):
    data = csv[i][0:38]
    label = csv[i][39]  # 일단은 운행횟수만 기록
    train_data.append(data)
    train_label.append(label)

for i in range(len(jb_csv)):
    data = jb_csv[i][0:38]
    label = jb_csv[i][39]
    test_data.append(data)
    test_label.append(label)

for i in range(len(train_data)):
    for j in range(len(train_data[i])):
        float(train_data[i][j])

for i in range(len(test_data)):
    for j in range(len(test_data[i])):
        try:
            float(test_data[i][j])
        except:
            print(test_data[i][j])

print(test_data)
# clf = svm.SVR(C=2000)  # gamma랑 C값 어떻게 바꿔야지?
# clf.fit(train_data, train_label)
# pre = clf.predict(test_data)


model = XGBClassifier()
model.fit(numpy.array(train_data), train_label)
predict = model.predict(numpy.array(test_data))

correct = 0
for i in range(len(test_label)):
    if test_label[i] * 0.9 <= predict[i] <= test_label[i] * 1.1:
        correct += 1

print(correct / len(test_label))