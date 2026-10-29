
import streamlit as st
import re
import html
from urllib.parse import quote
from main import search_wikipedia


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 AI Research Assistant")
st.write(
    "Search for research materials using Wikipedia."
)

keyword = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Artificial Intelligence"
)

if st.button("Search", type="primary"):
    if not keyword.strip():
        st.warning("Please enter a research topic.")

    else:
        try:
            with st.spinner("Searching..."):
                results = search_wikipedia(keyword.strip())

            if not results:
                st.info("No results found.")
            else:
                st.subheader(f"Search results for: {keyword}")

                for index, item in enumerate(results, start=1):
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")

                    snippet = html.unescape(
                        re.sub(r"<.*?>", "", snippet)
                    )

                    article_url = (
                        "https://en.wikipedia.org/wiki/"
                        + quote(title.replace(" ", "_"), safe="()'")
                    )

                    st.markdown(f"### {index}. {title}")
                    st.write(snippet)
                    st.markdown(
                        f"[Read the full article]({article_url})"
                    )
                    st.divider()

        except Exception as error:
            st.error(
                "Something went wrong. "
                "Please check your connection and try again."
            )
            print(f"Error details: {error}")
