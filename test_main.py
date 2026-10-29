
import unittest
from unittest.mock import patch, Mock

from main import search_wikipedia


class TestWikipediaSearch(unittest.TestCase):

    @patch("main.requests.get")
    def test_search_returns_results(self, mock_get):
        # 模拟服务器返回的数据
        mock_response = Mock()
        mock_response.json.return_value = {
            "query": {
                "search": [
                    {
                        "title": "Python",
                        "snippet": "A programming language"
                    }
                ]
            }
        }

        mock_get.return_value = mock_response

        # 调用我们要测试的函数
        results = search_wikipedia("Python")

        # 检查结果是否正确
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Python")

        # 检查是否发送了 HTTP 请求
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
