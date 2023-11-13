curl --request GET \
     --url 'https://data-eu.mixpanel.com/api/2.0/export?project_id=2759992&from_date=2021-08-04&to_date=2023-09-27' \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'accept: text/plain' \
     --header 'authorization: Basic Rmlyc3QuOGVkMzNmLm1wLXNlcnZpY2UtYWNjb3VudDo1VkpPblVqanZsQzM5RzI2UTV5ZmwzVjE4c3NaUW9Ueg==' > export_8oct2023.json
