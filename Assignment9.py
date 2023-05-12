import plotly.express as px
df = px.data.tips()
df.head()

#bar plot - complete

import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")
fig.show()

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="day", barmode="group")
fig.show()


#scatter plot

df = px.data.tips()
fig = px.scatter(df, x = "total_bill", y = "tip", color = "sex", facet_col="smoker")
fig.show()

df = px.data.tips()
fig = px.scatter(df, x = "total_bill", y = "tip", color = "sex", facet_col = "smoker", trendline = "ols")
fig.show()

# complete
df = px.data.tips()
fig = px.scatter(df, x = "total_bill", y = "tip", facet_row = "time", facet_col = "day",
          category_orders = {"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Dinner", "Lunch"]})
fig.show()


# histogram - complete
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="tip", marginal="rug")
fig.show()

# boxplot - complete
import plotly.express as px
df = px.data.tips()
fig = px.box(df, x="smoker", y="tip", color="smoker")
fig.show()