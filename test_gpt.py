from openai import OpenAI

client = OpenAI(
    api_key="sk-sssaicode-2f8bcb9a825f90649349c4c6c0b5ae6c6c0f3b6fd084476c280c893c1d81528b",
    base_url="https://codex1.sssaicode.com/api/v1"
)

# 尝试不同模型
models = ["gpt-4", "gpt-4o", "gpt-3.5-turbo", "gpt-4-turbo", "claude-3-opus", "claude-3-sonnet"]

for model in models:
    print(f"\n尝试模型: {model}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Hi"}]
        )
        print(f"成功! 响应: {response.choices[0].message.content}")
        break
    except Exception as e:
        print(f"失败: {str(e)[:100]}")
