
import html
import re

import streamlit as st
import requests

from main import search_wikipedia
from llm import summarize_research


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="centered",
)

st.title("🔎 AI Research Assistant")
st.write(
    "Search research materials and summarize them with DeepSeek."
)

if "results" not in st.session_state:
    st.session_state.results = []

if "summary" not in st.session_state:
    st.session_state.summary = ""


keyword = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Artificial Intelligence",
)

if st.button("Search", type="primary"):
    if not keyword.strip():
        st.warning("Please enter a research topic.")
    else:
        st.session_state.results = []
        st.session_state.summary = ""

        try:
            with st.spinner("Searching Wikipedia..."):
                results = search_wikipedia(keyword.strip())

            st.session_state.results = results

            if not results:
                st.info("No results found.")

        except requests.RequestException:
            st.error(
                "Search failed. Please check your network "
                "connection and try again."
            )


results = st.session_state.results

if results:
    st.subheader(f"Search results for: {keyword}")

    for index, item in enumerate(results, start=1):
        title = item.get("title", "")
        snippet = item.get("snippet", "")

        snippet = html.unescape(
            re.sub(r"<.*?>", "", snippet)
        )

        st.markdown(f"### {index}. {title}")
        st.write(snippet)

        st.markdown(
            f"https://en.wikipedia.org/wiki/"
            f"{title.replace(' ', '_')}"
        )

        st.divider()

    if st.button("✨ Summarize with DeepSeek"):
        try:
            with st.spinner("DeepSeek is summarizing..."):
                summary = summarize_research(
                    keyword.strip(),
                    results,
                )

            st.session_state.summary = summary

        except Exception as error:
            st.error(
                f"AI summary failed ({type(error).__name__}). "
                "Check your API key, account quota, and network."
            )

    if st.session_state.summary:
        st.subheader("🤖 AI Summary")
        st.markdown(st.session_state.summary)
