# restaurants_searcher.py

# ---------------------------------------------------------
# ホットペッパーから渋谷駅のレストラン名を検索してCSV出力
# ---------------------------------------------------------
# import csv
# import json
# import requests

# # 初期設定
# KEYID = "c60a9b6c274543c2"
# COUNT = 100
# PREF = "Z011"
# FREEWORD = "渋谷駅"
# FORMAT = "json"

# PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}

# def write_data_to_csv(params):
#     restaurants = []
#     json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
#     response = json.loads(json_res)
#     if "error" in response["results"]:
#         return print("エラーが発生しました！")
#     for restaurant in response["results"]["shop"]:
#         restaurant_name = restaurant["name"]
#         restaurants.append(restaurant_name)
#     with open("restaurants_list.csv", "w") as f:
#         writer = csv.writer(f)
#         writer.writerow(restaurants)
#     return print(restaurants)

# write_data_to_csv(PARAMS)


# ---------------------------------------------------------------
# ホットペッパーから渋谷駅のレストラン情報を取得してCSV出力
# ---------------------------------------------------------------

import json
import csv
import requests

# 初期設定
KEYID = "c60a9b6c274543c2"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

#パラメータ設定
PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}

def write_data_to_csv(params):
    restaurants = [["名称","営業日","住所","アクセス"]]
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["open"], restaurant["address"], restaurant["access"]]
        restaurants.append(rest_info)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)