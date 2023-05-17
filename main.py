# import requests
# from os import environ as env
# from datetime import date, timedelta
#
# USERNAME = 'danielodoc'
# PIXELA_APIKEY = env['PIXELA_APIKEY']
# GRAPH_ID = 'test-graph'
# now = date.today() - timedelta(days= 1)
# date = str(now.strftime("%Y%m%d"))
# print(date)
# # parameters = {
# #     'id': 'test-graph',
# #     'name': 'test-graph-name',
# #     'unit': 'kcal',
# #     'type': 'int',
# #     'color': 'sora',
# #     'timezone': 'Australia/Sydney',
# # }
#
# parameters = {
#     'date': date,
#     # 'quantity': '1200',
#
# }
#
# headers = {
#     'X-USER-TOKEN': PIXELA_APIKEY
# }
# # request = requests.post(url='https://pixe.la/v1/users', json=parameters)
# # request.raise_for_status()
#
#
# # request = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs', json=parameters, headers=headers)
# # request.raise_for_status()
#
# request = requests.delete(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}', json=parameters, headers=headers)
# request.raise_for_status()
