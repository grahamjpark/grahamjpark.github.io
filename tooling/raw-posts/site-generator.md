# Creating a Static Blog Generator

![](https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80)


Recently I went about revamping my website. After creating my homepage, I decided I wanted to add a blog to it. Below you’ll find an overview of my approach and an explanation of how I created a short python script to do the job.

A quick note: there isn’t anything novel about a static site generator. A [simple search](https://duckduckgo.com/?q=best+static+site+generator) turns up plenty of options that are mature and feature-packed. However, I had the desire to write my own, so that’s what I chose to do. If you’re looking to not roll your own, those existing options have great documentation or tutorials you can find.

Also, this post is to share my approach rather than give a step-by-step. I’ll explain the general process and include some code snippets, but if you’re taking the time to write your own generator, the process of writing it is probably your main driver, so copying and pasting things would defeat the purpose. To see the complete project you can look [here](https://github.com/grahamjpark/grahamjpark.github.io/tree/master/tooling).

# Existing Site

I think it’s worth mentioning that coming into this I already had a landing page for my site which is hosted on Github pages. I followed the [Interneting Is Hard tutorials](https://www.internetingishard.com/) to brush up on my HTML/CSS and [Github pages’ site](https://pages.github.com/) to figure out how to get it hosted for free.

# Requirements

To start I needed to outline the behavior I wanted my site to have. For me, it boiled down to:

- Generating new posts from markdown (which is how my notes program exports notes)
- Creating a page with all posts
- Having recent posts listed on my homepage
- Publishing an RSS feed people can subscribe to
# Generating Posts

#### Parsing Markdown
The first step I took was making sure there was an easy way to generate the HTML from my markdown files. I looked around for a solution and found python’s [markdown library](https://python-markdown.github.io/reference/) which made it a lot easier than I was expecting. A call to  `markdown.markdown(text)` was all I needed to generate the HTML.

After playing around with the markdown library in the REPL to verify it’s output, I created a function for generating the HTML. The function opens up and reads the markdown file, then populates the HTML with the markdown library. I also chose to split the title of the post from the rest of the content by splitting on the first newline character.

    def parse_markdown(file_name):
        with open("raw-posts/" + file_name + ".md", "r", encoding="utf-8") as input_file:
            text = input_file.read()
            full_html = markdown.markdown(text)
            [title, html] = full_html.split('\n', 1)
            title = title[4:-5]
            return title, html

#### Metadata
With the HTML content created, I had to tackle generating some metadata about the posts. In particular, I want to make sure to have the date the post was published and a preview of the post I can show. I considered embedding this information at the top of the file, but it seemed cleaner to keep a separate metadata JSON file. As I write more posts this might get a little more chaotic, but for now, I like not muddling the two in one file.

To get the clean text I use [Beautiful Soup](https://pypi.org/project/beautifulsoup4/).  Beautiful Soup is great for parsing and traversing HTML in python. I don’t need to do anything crazy, just get the raw text without any HTML elements. After passing in the HTML to Beautiful soup I could get this from `.text`. I clean the snippet up a little bit more by removing the newline characters and removing spaces at the beginning and end.

    snippet = BeautifulSoup(html, "lxml").text[0:SNIPPET_LEN]
    snippet = snippet.replace('\n', ' ').strip()

I then use the snippet in populating a default metadata dictionary. I also store the date (both as raw epoch and formatted), the title from our last section, and the filename to make linking to the post easy.

    metadata = {
        'raw_date': int(time.time()),
        'date': time.strftime('%B %d, %Y', time.localtime(time.time())),
        'filename': file_name + '.html',
        'title': title,
        'snippet': snippet
    }

With that created, I then check if there’s an existing metadata file. If there is that means we’ve seen this post before and I don’t want to overwrite the date. However, if the title and preview snippet have changed I’ll want to update those.

    if os.path.isfile(metadata_filepath):
        with open(metadata_filepath, 'r') as f:
            metadata = json.loads(f.read())
            # If this happens, the markdown has been updated
            if metadata["title"] != title or
                    metadata["snippet"] != snippet:
                metadata["title"] = title
                metadata["snippet"] = snippet
            else:
                return metadata

    with open(metadata_filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=4)
    return metadata

Now we have both functions working, I loop over the markdown files to create all the HTML and metadata files. For convenience sake, I went ahead and created an array of all of the metadata dictionaries to use later when creating an RSS feed.

    for file in os.listdir(markdown_dir):
        if not os.fsdecode(file).endswith(".md"):
            continue

        file_name = os.fsdecode(file)[:-3]

        title, html = parse_markdown(file_name)

        metadata = get_write_metadata(file_name, title, html)
        post_metadatas.append(metadata)

#### Templating
Now that I’ve got the HTML for the content, I had to figure out how to insert that into a standard page for a post. I’d worked some with [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) before, so it made sense to use it here. Jinja will let me create templates for my pages and then insert the body of my posts.

To see what that looks like, here’s a simplified version of my blog template. Note the three variables I’ve passed in to insert into the template: `title`, `date`, and `post_body`.

    <!DOCTYPE html>
    <html lang='en'>

    <head>
        <meta charset='UTF-8' />
        <title>{{ title }} - Graham Park</title>
        ...
    </head>

    <body>
        <header>
        ...
        </header>
        <div class="article-container">
            <article>
                <h1 class="title">{{ title }}</h1>
                <p class='subtitle'>Published on {{ date }}</p>
                {{ post_body }}
            </article>
        </div>
    </body>
    </html>

To fill in these variables lets circle back to our python script. First, I had to add some code to get my jijna environment [set up](https://github.com/grahamjpark/grahamjpark.github.io/blob/master/tooling/generate-blogs.py#L56-L59). Then I was able to call .render() on my template and pass in the variables. Here I just passed in some dummy data to make sure everything was working.

    template_loader = jinja2.FileSystemLoader(searchpath="./templates")
    template_env = jinja2.Environment(loader=template_loader)
    blog_template_file = "blog.jinja2.html"
    blog_template = template_env.get_template(blog_template_file)

    print(blog_template.render(title="Test", post_body="<p>My test</p>", date="May 4, 2020"))

With that working, I went back to where I was looping over the files and rendered the blog post, writing the output to a file. So now we have all of our blog post pages!

    with open('../blog/' + metadata['filename'], 'w') as f:
        f.write(blog_template.render(title=title, post_body=html,
                                     date=metadata["date"]))

One quick note before moving onto the next task: if you look at my current blog template you’ll see that I pulled the header out to its own template and I’m importing it via `{% include 'header.jinja2.html' %}`. This way I can share the header across the next couple pages we create.

# Listing All Posts

Now that I have all of my blog posts generated, I needed a way to display all of them. I opted not to have anything too fancy, one page to list all the posts with short snippets. Looking ahead, I know I’m also going to have article previews on my home page, so I decided to create a template just for the snippet first.

This article snippet template will take in the metadata dictionary we were working with earlier, so I can just pull out all the information I need and populate a little preview with a link to the rest of the article.

    <div class="snippet-header">
        <a href='/blog/{{ post["filename"] }}'>
            <h2>{{ post["title"] }}</h2>
        </a>
        <p class="post-date">{{ post["date"] }}</p>
    </div>
    <p>{{ post\["snippet"\][:240] }}...</p>
    <a href='/blog/{{ post["filename"] }}'>
        <p class='link'>Read More →</p>
    </a>

With that made, all I need to do to list all of the posts is loop over the list of post metadatas we created earlier.  For each post, I’ll call the post snippet template and the metadata dictionary in. To specify a variable value when including another template I use the `with` statement. Below is the templating logic to do that, but you can see the full template [here](https://github.com/grahamjpark/grahamjpark.github.io/blob/master/tooling/templates/all-posts.jinja2.html).

    {% for post in posts %}
        {% with post=post %}
            {% include 'post_snippet.jinja2.html'%}
        {% endwith %}
    {% endfor %}

In the python file, I added a section to sort the metadatas, then generate and write the page from this template:

    all_posts_template_file = "all-posts.jinja2.html"
    all_posts_template = template_env.get_template(all_posts_template_file)
    post_metadatas = sorted(post_metadatas, key=lambda post: -post["raw_date"])

    with open('../blog/all-posts.html', 'w') as f:
        f.write(all_posts_template.render(posts=post_metadatas))
# Update Homepage with Recent Posts

With the snippet template created, I added a section for the recent blog posts to my existing home page. I loop over the metadata dictionary exactly like we just did. You can see the template [here](https://github.com/grahamjpark/grahamjpark.github.io/blob/master/tooling/templates/index.jinja2.html).

In the python script, I included an almost identical section for the all-posts page but spliced the posts list to only include the most recent 2 articles. You can see that [here](https://github.com/grahamjpark/grahamjpark.github.io/blob/master/tooling/generate-blogs.py#L84).

# RSS Feed

I really value RSS Feeds. They’ve fallen out of style lately, but they’re a great way for apps to subscribe to websites for the latest content. Soon I’ll write a post going into how I use RSS in my day-to-day, but the biggest perk for me is control. I can choose which RSS app I use and which articles I want to see. Because of this, I wanted to figure out how to implement my own RSS feed.

Looking through stack overflow I found a lot of solutions about how to generate the XML for an RSS feed manually, but I wanted something a little more abstracted. Thankfully, the [rfeed](https://github.com/svpino/rfeed) library is just what I wanted. Reading through the readme I learned enough to get started.

All I had to do was loop over the post metadatas to create an `Item`, then use those to create a `Feed`. With the feed created I called `.rss()` and then wrote that to a file.

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
        link = "https://grahamjpark.com/blog/all-posts.html"
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
# Analytics and Email Collection

Two other things I have in my blog that I chose not to go into detail here about are my analytics implementation and collecting emails if people want email updates.

For analytics, I use [Simple Analytics](https://referral.simpleanalytics.com/graham), which is a privacy respecting analytics solution. Since they don’t track your users to sell them ads, it’s not free. But if you use [my referral here](https://referral.simpleanalytics.com/graham), you can get your first month free. For my setup, I pretty much followed all their documentation (with the exception of making the tracking of link clicks a little more precise [here](https://github.com/grahamjpark/grahamjpark.github.io/blob/master/tooling/templates/blog.jinja2.html#L37-L59)).

For email collection, I used [EmailOctopus](https://emailoctopus.com/?urli=5HsHZ), which worked great for me because they provide the HTML for an email collection form. I don’t see myself getting outside of their free tier anytime soon. That being said, if you use [my referral](https://emailoctopus.com/?urli=5HsHZ) we’ll both get 15 dollars credit.

# Future Improvements

Some of the future improvements that are coming to the site include:

#### Tagging
I’m not sure what topics will show up in my blog, but I imagine they won’t all be about the same thing, so tagging or categories would be a nice-to-have.

#### Richer Blog Post Pages
The blog post structure is a little bland. I might consider adding navigation to the previous or next post or adding more information about myself in a footer of some sort.

#### Commenting
I’ve tossed around the idea of including commenting. Services exist that manage the commenting backend for you, but I’m not sure if it would be that much of a value add. [Disqus](https://disqus.com/) is probably to most popular of these, but I really love how clean and privacy-friendly [Commento](https://www.commento.io/) is.

# Thanks for reading

If you’ve made it all the way here, thanks! This is my first right up like this and I’m still trying to figure out how to convey my process to people who might hope to learn from it. If you have any feedback feel free to let me know!

