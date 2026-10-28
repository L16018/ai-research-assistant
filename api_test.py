import requests


def create_post(title, body):
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()


def main():
    title = input("请输入文章标题：")
    body = input("请输入文章内容：")

    if not title.strip() or not body.strip():
        print("标题和内容不能为空！")
        return

    try:
        result = create_post(title, body)
        print("\n请求成功！")
        print("返回标题：", result["title"])
        print("返回 ID：", result["id"])

    except requests.RequestException as error:
        print("请求失败：", error)


if __name__ == "__main__":
    main()