import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()

# LLMからの回答を取得する関数
def get_llm_response(input_text, expert_type):
    # 専門家の種類に応じたシステムメッセージを設定
    system_messages = {
        "料理": "あなたは一流のシェフです。料理に関する質問に答えてください。",
        "AI": "あなたはAIの専門家です。人工知能や機械学習に関する質問に答えてください。",
        "グーグルリスティング": "あなたはグーグルリスティングの専門家です。SEOや広告運用に関する質問に答えてください。",
    }
    system_message = system_messages.get(expert_type, "あなたは知識豊富な専門家です。")

    # LangChain の ChatOpenAI モデルを使用
    chat = ChatOpenAI(temperature=0.7)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text),
    ]
    response = chat(messages)
    return response.content

# Streamlit アプリの構築
st.title("専門家に質問できるアプリ")
st.write("このアプリでは、専門家に質問を投げかけることができます。以下のフォームに質問を入力し、専門家の種類を選択してください。")

# 入力フォーム
input_text = st.text_input("質問を入力してください：", placeholder="例: 美味しいパスタの作り方を教えてください")
expert_type = st.radio(
    "専門家の種類を選択してください：",
    ("料理", "AI", "グーグルリスティング")
)

# 送信ボタン
if st.button("送信"):
    if input_text.strip():
        with st.spinner("回答を生成中..."):
            response = get_llm_response(input_text, expert_type)
        st.success("回答が生成されました！")
        st.write("### 専門家の回答:")
        st.write(response)
    else:
        st.error("質問を入力してください。")