
import requests
import re
import html


def search_wikipedia(keyword):
    """Search Wikipedia for relevant articles."""

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "format": "json",
        "srlimit": 3
    }

    headers = {
        "User-Agent": "AIResearchAssistant/0.1"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return data.get("query", {}).get("search", [])


def main():
    keyword = input("请输入你想研究的主题：").strip()

    if not keyword:
        print("研究主题不能为空！")
        return

    try:
        results = search_wikipedia(keyword)

        if not results:
            print("没有找到相关资料。")
            return

        print(f"\n关于“{keyword}”的搜索结果：\n")

        for index, item in enumerate(results, start=1):
            title = item.get("title", "")
            snippet = item.get("snippet", "")

            snippet = html.unescape(
                re.sub(r"<.*?>", "", snippet)
            )

            print(f"{index}. {title}")
            print(f"   {snippet}\n")

    except requests.RequestException as error:
        print("请求失败，请检查网络连接。")
        print("错误信息：", error)


if __name__ == "__main__":
    main()
