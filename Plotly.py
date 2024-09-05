# import plotly
# plotly.offline.init_notebook_mode(connected=True)
# import plotly.graph_objs as go
#
# # Printing the total number of unique categories
# num_categories = len(apps['Category'].unique())
# print('Number of categories = ', num_categories)
#
# # Counting the number of apps in each 'Category' and sort them in descending order
# num_apps_in_category = apps['Category'].value_counts().sort_values(ascending = False)
#
# data = [go.Bar(
#         x = num_apps_in_category.index, # index = category name
#         y = num_apps_in_category.values, # value = count
# )]
#
# plotly.offline.iplot(data)