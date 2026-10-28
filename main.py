def get_answer(question):
    """暂时模拟回答，之后替换为真实的 API 调用。"""
    return f"你提出的问题是：{question}\n目前还没有连接 AI API。"


def main():
    question = input("请输入你想研究的问题：")

    if not question.strip():
        print("问题不能为空！")
        return

    answer = get_answer(question)
    print("\n研究结果：")
    print(answer)


if __name__ == "__main__":
    main()