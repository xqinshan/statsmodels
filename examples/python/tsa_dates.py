# coding: utf-8

# DO NOT EDIT
# Autogenerated from the notebook tsa_dates.ipynb.
# Edit the notebook and then sync the output with this file.
#
# flake8: noqa
# DO NOT EDIT

# # 时间序列模型的日期

import statsmodels.api as sm
import numpy as np
import pandas as pd

# ## 入门

data = sm.datasets.sunspots.load()

# 现在，一个年度日期系列必须是该年底的日期时间。

from datetime import datetime
dates = sm.tsa.datetools.dates_from_range('1700', length=len(data.endog))

# ## 使用 Pandas
#
# 生成一个 pandas 时间序列或 DataFrame

endog = pd.Series(data.endog, index=dates)

# 实例化模型

ar_model = sm.tsa.AR(endog, freq='A')
pandas_ar_res = ar_model.fit(maxlag=9, method='mle', disp=-1)

# Out-of-sample 预测

pred = pandas_ar_res.predict(start='2005', end='2015')
print(pred)

# ## 使用明确的日期

ar_model = sm.tsa.AR(data.endog, dates=dates, freq='A')
ar_res = ar_model.fit(maxlag=9, method='mle', disp=-1)
pred = ar_res.predict(start='2005', end='2015')
print(pred)

# 这只是返回一个常规数组，但是由于模型具有日期附带信息，您可以通过回旋方式获取预测日期。

print(ar_res.data.predict_dates)

# 注意：只有调用了 predict 时，此属性才存在。它保存与上次预测的调用关联的日期。