import streamlit as st
import os
import frontmatter
import json
# import pyperclip

def load_prompts():
    prompts = []
    prompt_dir = "prompts"

    for filename in os.listdir(prompt_dir):
        if filename.endswith(".md"):
            with open(os.path.join(prompt_dir, filename), "r") as file:
                prompt = frontmatter.load(file)
                prompts.append({
                    "id": prompt.get("id"),
                    "title": prompt.get("title"),
                    "author": prompt.get("author"),
                    "paper": prompt.get("paperlink"),
                    "date": prompt.get("date"),
                    "language": prompt.get("language"),
                    "task": prompt.get("task"),
                    "version": prompt.get("version"),
                    "addedby": prompt.get("addedby"),
                    "keywords": prompt.get("keywords"),
                    "content": prompt.content
                })

    return prompts

def render_prompt_details(prompt):
    st.markdown(f"# Card: {prompt['title']}")
    st.write("---")
    st.write(f"**Author:** {prompt['author']}")
    st.write(f"**Paper:** {prompt['paper']}")
    st.write(f"**Date:** {prompt['date']}")
    st.write(f"**Language:** {prompt['language']}")
    st.write(f"**Task:** {prompt['task']}")
    st.write(f"**Keywords:** {prompt['keywords']}")
    st.write(f"**Version:** {prompt['version']}")
    st.write(f"_Added By: {prompt['addedby']}_")
    st.write("---")
    st.write(prompt["content"])

def render_prompt_card(prompt):
    card_style = """
    <style>
        .card {
            background-color: #f8f9fa;
            border: 1px solid #d9d9d9;
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .card-content {
            display: flex;
            flex-direction: column;
        }
        .button-style {
            background-color: #FFD700;
            border: none;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """

    st.markdown(card_style, unsafe_allow_html=True)

    card_container = st.container()

    with card_container:
        with st.container():
            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(f"### **Card:** {prompt['title']}")
                st.write(f"**Author:** {prompt['author']}")
                st.write(f"**Paper:** {prompt['paper']}")
                st.write(f"**Date:** {prompt['date']}")
                st.write(f"**Prompt Language:** {prompt['language']}")
                st.write(f"**Annotation Task:** {prompt['task']}")
                st.write(f"**Keywords:** {prompt['keywords']}")
                st.write(f"_Added by: {prompt['addedby']}_")

            with col2:
                if st.button("View details", key=f"view-details-{prompt['id']}"):
                    st.session_state.selected_prompt_id = prompt["id"]
                    st.experimental_rerun()

            st.markdown("<style>.button-style {background-color: #FFD700;}</style>", unsafe_allow_html=True)

    card_container.container().write("---")

def main():
    if "selected_prompt_id" not in st.session_state:
        st.session_state.selected_prompt_id = None

    st.title("Annotation PromptCards 🏷️ 📝 🤖")
    st.write("Welcome to the Prompt Archive! Click on the 'View details' button on each prompt card to see more information about the annotation prompt.")
    st.write("---")

    prompts = load_prompts()
    language_list = list(set([prompt['language'] for prompt in prompts]))
    task_list = list(set([prompt['task'] for prompt in prompts]))

    st.sidebar.header("**Annotation PromptCards**")

    st.sidebar.write("A collection of prompts for annotation tasks in NLP. This is a work in progress. Please contribute your prompts via GitHub [[Upload]](https://github.com/chkla/PromptCards) 🙏🏽.")

    # add a link to the GitHub repository
    st.sidebar.write("---")
    st.sidebar.write(f"**Total number of prompts:** {len(prompts)}")
    st.sidebar.write("---")

    st.sidebar.header("🧑🏽‍🚀 Explore:")
    search = st.sidebar.text_input("Search by title")
    language_filter = st.sidebar.selectbox("Filter by Language", ["All"] + language_list)
    task_filter = st.sidebar.selectbox("Filter by Task", ["All"] + task_list)

    if st.sidebar.button("Back to list"):
        st.session_state.selected_prompt_id = None
        st.experimental_rerun()

    if st.session_state.selected_prompt_id is None:
        filtered_prompts = [
            prompt for prompt in prompts
            if (search.lower() in prompt['title'].lower() or not search)
            and (prompt['language'] == language_filter or language_filter == "All")
            and (prompt['task'] == task_filter or task_filter == "All")
        ]

        for prompt in filtered_prompts:
            render_prompt_card(prompt)
    else:
        prompt = next((p for p in prompts if p["id"] == st.session_state.selected_prompt_id), None)
        if prompt:
            render_prompt_details(prompt)

    st.sidebar.write("---")
    st.sidebar.write("Made with ❤️ and 🤖 by [chkla](klamm.ai).")

if __name__ == "__main__":
    main()
