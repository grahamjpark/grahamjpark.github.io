import os
import time
import json
import markdown
import jinja2
import datetime
from bs4 import BeautifulSoup
from rfeed import Item, Guid, Feed, Image

# Functionality to implement:
# - Parse all markdown files and create individual pages - done
# - Create page that has all blog posts - done
# - Update rss feed - done
# - Populate home page with most recent posts - done

post_metadatas = []

def get_write_metadata(file_name, title, html):
    metadata_filepath = 'raw-posts/' + file_name + '.json'
    metadata = {
        'raw_date': int(time.time()),
        'date': time.strftime('%B %d, %Y', time.localtime(time.time())),
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
                post_metadatas.append(metadata)
                return metadata

    with open(metadata_filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    post_metadatas.append(metadata)
    return metadata


def get_blog_html(blog_name):
    with open("raw-posts/" + blog_name + ".md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        return markdown.markdown(text)


################## Parse Markdown and create individual pages ##################
markdown_dir = os.fsencode('raw-posts')
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)
blog_template_file = "blog.html.jinja2"
blog_template = template_env.get_template(blog_template_file)

for file in os.listdir(markdown_dir):
    if not os.fsdecode(file).endswith(".md"):
        continue

    file_name = os.fsdecode(file)[:-3]

    html = get_blog_html(file_name)
    [title, html] = html.split('\n', 1)
    title = title[4:-5]

    metadata = get_write_metadata(file_name, title, html)

    with open('../blog/' + metadata['filename'], 'w') as f:
        f.write(blog_template.render(title=title, post_body=html,
                                     date=metadata["date"]))

########################## Create catalog of all posts ###########################
all_posts_template_file = "all-posts.html.jinja2"
all_posts_template = template_env.get_template(all_posts_template_file)
post_metadatas = sorted(post_metadatas, key=lambda post: -post["raw_date"])

with open('../blog/all-posts.html', 'w') as f:
    f.write(all_posts_template.render(posts=post_metadatas))

######################### Update index with recent posts #########################
index_template_file = "index.html.jinja2"
index_template = template_env.get_template(index_template_file)

with open('../index.html', 'w') as f:
    f.write(index_template.render(posts=post_metadatas[:2]))

################################ Update rss feed #################################
rss_items = []
for post in post_metadatas:
    url = f"https://grahamjpark.com/blog/{post['filename']}"
    rss_items.append(
        Item(
            title = post["title"],
            link = url,
            description = post["snippet"] + "...",
            author = "Graham Park",
            guid = Guid(url),
            pubDate = datetime.datetime.fromtimestamp(post["raw_date"])
        )
    )

image = Image(
    url = "https://grahamjpark.com/assets/gp_small_new.png",
    title = "GP Logo",
    link = "https://grahamjpark.com/blog/all-posts.html",
)

feed = Feed(
    title = "Graham Park's Blog",
    link = "https://grahamjpark.com/blog/rss.xml",
    description = "Writings from Graham about whatever happens to be on his mind",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = rss_items,
    image = image
)

with open('../blog/rss.xml', 'w') as f:
    f.write(feed.rss())