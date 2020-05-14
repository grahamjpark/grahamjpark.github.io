import os
import time
import json
import markdown
import jinja2
from bs4 import BeautifulSoup

# Functionality to implement:
# - Parse all markdown files and create individual pages - done
# - Create page that has all blog posts
# - Update rss feed
# - Populate home page with most recent posts


def get_write_metadata(file_name, title, html):
    metadata_filepath = 'post-metadata/' + file_name + '.json'
    metadata = {
        'date': int(time.time()),
        'filename': file_name + '.html',
        'title': title,
        'snippet': BeautifulSoup(html, "lxml").text [:300]
    }

    if os.path.isfile(metadata_filepath):
        with open(metadata_filepath, 'r') as f:
            metadata = json.loads(f.read())
            # If this happens, the title in the markdown has been updated, so update metadata
            if metadata["title"] != title:
                metadata["title"] = title
            else:
                return metadata

    with open(metadata_filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)

    return metadata


def get_blog_html(blog_name):
    with open("raw-posts/" + blog_name + ".md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        return markdown.markdown(text)


markdown_dir = os.fsencode('raw-posts')
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
blog_template_file = "blog.html"
blog_template = template_env.get_template(blog_template_file)
output_text = blog_template.render()

for file in os.listdir(markdown_dir):
    file_name = os.fsdecode(file)[:-3]

    html = get_blog_html(file_name)
    [title, html] = html.split('\n', 1)
    title = title[4:-5]

    metadata = get_write_metadata(file_name, title, html)

    with open('../blog/' + metadata['filename'], 'w') as f:
        f.write(blog_template.render(title=title, post_body=html,
                                     date=time.strftime('%B %d, %Y', time.localtime(metadata["date"]))))
