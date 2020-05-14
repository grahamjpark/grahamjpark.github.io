import os
import time
import json
import markdown
# from flask import render_template

# Functionality to implement:
# - Parse all markdown files and create individual pages
# - Create page that has all blog posts
# - Populate home page with most recent posts
# - Update rss feed


def get_blog_metadata(blog_name):
    metadata_filepath = 'post-metadata/' + blog_name + '.json'
    metadata = {
        'date': int(time.time()),
        'filename': blog_name + '.html'
    }
    if os.path.isfile(metadata_filepath):
        with open(metadata_filepath, 'r') as f:
            metadata = json.loads(f.read())
    else:
        with open(metadata_filepath, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=4)
    return metadata


def get_blog_html(blog_name):
    with open("raw-posts/" + blog_name + ".md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        return markdown.markdown(text)


markdown_dir = os.fsencode('raw-posts')

for file in os.listdir(markdown_dir):
    blog_name = os.fsdecode(file)[:-3]
    metadata = get_blog_metadata(blog_name)
    html = get_blog_html(blog_name)
    [title, html] = html.split('\n', 1)
    title = title[4:-5]

    # with open('../blog/' + metadata['filename'], 'a') as f:
    #     f.write(render_template())
