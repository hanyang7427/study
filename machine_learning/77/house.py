import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm
housing = sd.load_boston()
feature_names = housing.feature_names
#     CRM - 城镇人均犯罪率
#      ZN - 住宅用地超过25000平方英尺的比例
#   INDUS - 城镇非零售商用土地比例
#    CHAS - 河空变量(边界为河流1，否则0)
#     NOX - 一氧化氮浓度
#      RM - 住宅平均间数
#     AGE - 1940年之前建成的自用房屋比例
#     DIS - 到波士顿五个中心区的加权距离
#     RAD - 辐射性公路的接近指数
#     TAX - 每10000美元的全值财产税率
# PTRATIO - 城镇师生比例
#       B - 黑人比例
#   LSTAT - 人口中地位低下者的比例
x, y = su.shuffle(housing.data, housing.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x = x[:train_size]
train_y = y[:train_size]
model_dt = st.DecisionTreeRegressor(max_depth=4)
model_dt.fit(train_x, train_y)
model_ab = se.AdaBoostRegressor(st.DecisionTreeRegressor(
	max_depth=4), n_estimators=400, random_state=7)
model_ab.fit(train_x, train_y)
test_x = x[train_size:]
test_y = y[train_size:]
pred_test_y_dt = model_dt.predict(test_x)
pred_test_y_ab = model_ab.predict(test_x)
r2s = sm.r2_score(test_y, pred_test_y_dt)
print(r2s)
r2s = sm.r2_score(test_y, pred_test_y_ab)
print(r2s)


