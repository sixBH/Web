import requests
import os
import json

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'referer': 'https://weibo.com/u/7871239944',
    'cookie': input('请输入你的cookies：')
}

def fetch_weibo_comments(id, uid):
    params = {
        'id': id,
        'is_show_bulletin': '2',
        'uid': uid,
        'fetch_level': '0',
        'locale': 'zh-CN',
    }
    response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params, headers=headers)
    data = response.json()
    return data

def main():
    id = input('请输入主页id：')
    uid = input('请输入主页uid：')
    
    # 获取单页完整JSON数据
    json_data = fetch_weibo_comments(id, uid)
    
    # 写入当前目录的json.txt文件
    with open('json.txt', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    
    print("完整JSON数据已保存至当前目录的json.txt文件中")

if __name__ == '__main__':
    main()