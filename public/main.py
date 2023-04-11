from flask import Flask, render_template, url_for, redirect, abort, request
import requests
import yaml
import os
import frontmatter
import markdown

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prompt/')
def prompt_without_id():
    return redirect(url_for('home'))

"""
@app.route('/')
def home():
    prompts = fetch_prompts()
    total_prompts = len(prompts)
    return render_template('index.html', prompts=prompts, total_prompts=total_prompts)
"""

@app.route('/', methods=['GET'])
def home():
    prompts = fetch_prompts()
    total_prompts = len(prompts)

    prompts_by_language = {}
    for prompt in prompts:
        language = prompt['language']
        prompts_by_language[language] = prompts_by_language.get(language, 0) + 1

    prompts_by_task = {}
    for prompt in prompts:
        task = prompt['task']
        prompts_by_task[task] = prompts_by_task.get(task, 0) + 1

    search_query = request.args.get('search_query', '')
    filter_language = request.args.get('filter_language', '')
    filter_task = request.args.get('filter_task', '')

    filtered_prompts = [p for p in prompts if (search_query.lower() in p['title'].lower() or search_query.lower() in p['task'].lower()) and (not filter_language or p['language'] == filter_language) and (not filter_task or p['task'] == filter_task)]

    return render_template(
        'index.html',
        prompts=filtered_prompts,
        total_prompts=total_prompts,
        prompts_by_language=prompts_by_language,
        prompts_by_task=prompts_by_task,
        search_query=search_query,
        filter_language=filter_language,
        filter_task=filter_task
    )

@app.route('/prompt/<id>')
def prompt(id):
    prompts = fetch_prompts()
    print(prompts)
    prompt = next((p for p in prompts if p['id'] == id), None)
    if prompt is None:
        abort(404)
    return render_template('prompt.html', prompt=prompt)
"""
def fetch_prompts():
    # Replace with your GitHub username and repository name
    url = 'https://api.github.com/repos/chkla/NLP-PolSci-Workshop/contents/test'
    files = requests.get(url).json()

    prompts = []
    for file in files:
        content = requests.get(file['download_url']).text
        prompt = yaml.safe_load(content)
        prompts.append(prompt)

    return prompts


def fetch_prompts():
    prompts_dir = '/Users/cklamm/repositories/PromptCards/website/prompt'
    prompts = []

    for file_name in os.listdir(prompts_dir):
        if file_name.endswith('.yaml'):
            file_path = os.path.join(prompts_dir, file_name)
            with open(file_path, 'r') as file:
                prompt = yaml.safe_load(file)
                prompts.append(prompt)

    return prompts
"""

def fetch_prompts():
    prompts_dir = './prompt'
    prompts = []

    for file_name in os.listdir(prompts_dir):
        if file_name.endswith('.md'):
            file_path = os.path.join(prompts_dir, file_name)
            with open(file_path, 'r') as file:
                post = frontmatter.load(file)
                prompt = {
                    "id": post["id"],
                    "title": post["title"],
                    "author": post["author"],
                    "addedby": post["addedby"],
                    "date": post["date"],
                    "language": post["language"],
                    "task": post["task"],
                    "version": post["version"],
                    "content": markdown.markdown(post.content)
                }
                prompts.append(prompt)
    return prompts

if __name__ == '__main__':
    app.run()
