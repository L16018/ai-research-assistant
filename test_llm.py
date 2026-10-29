
import unittest
from unittest.mock import patch, Mock

from llm import summarize_research


class TestLLMSummary(unittest.TestCase):

    @patch("llm.OpenAI")
    def test_summarize_returns_model_answer(self, mock_openai):
        # 模拟 DeepSeek 客户端
        mock_client = Mock()
        mock_openai.return_value = mock_client

        # 模拟模型返回的回答
        mock_choice = Mock()
        mock_choice.message.content = (
            "智慧农业利用技术提高农业生产效率。"
        )

        mock_response = Mock()
        mock_response.choices = [mock_choice]

        mock_client.chat.completions.create.return_value = (
            mock_response
        )

        # 使用测试密钥，不会真正调用 API
        with patch("llm.API_KEY", "test-api-key"):
            result = summarize_research(
                "smart agriculture",
                [
                    {
                        "title": "Smart agriculture",
                        "snippet": "Technology in agriculture",
                    }
                ],
            )

        # 验证返回内容
        self.assertEqual(
            result,
            "智慧农业利用技术提高农业生产效率。",
        )

        # 验证模型调用了一次
        mock_client.chat.completions.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
