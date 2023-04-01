# Mastodon as a Microblog

![](https://images.unsplash.com/photo-1669311576866-d77abb31f4ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80)

[Mastodon](https://joinmastodon.org/) has been gaining a lot of steam lately. I don't know how many people actually migrated from Twitter to Mastodon, but there are certainly more people talking about it than a year or two ago. I personally have been hesitant to jump on board. I've wanted to love Mastodon. I love its stance on privacy, data ownership, and trying to create healthier communities, but those stances also limit its ability to replace Twitter's ease of use and discoverability. Because of this it never stuck when I tried it out. Now I'm returning to Mastodon though, not as a Twitter replacement but to fill a different use case.

## Needs

I've been searching for a while to find a convenient way to catalog articles and videos I may want to reference later. What I'm imagining is a system that:

- Allows me to quickly save items from mobile or desktop
- Is not a social network, but can be browsed by friends
- Can sort, tag, and search

I've yet to find a single product targetting my (arguably niche) use case, but there's several that work "well enough".

## Previous Solutions

So far I've tried:

- [Pocket](https://getpocket.com): Pocket offers the ability to share articles from within the app. I'm a fan of Mozilla, but I couldn't get this to work for me. Pocket makes it super easy to save articles from Firefox or on mobile, but this just saves them to your reading list. Sharing to your public feed requires operating from within the app, which I've never consistently done.
- Note-taking app: This could be any number of apps. I've considered [Bear](https://bear.app/), [Notion](https://www.notion.so/), and [Airtable](https://www.airtable.com). I liked how extensible each of these was. I could tag and sort items easily. I also appreciated the lack of social features. Even though I don't intend to use this catalog as media, it's easy to get sucked in if the option is there. The main drawback here though was the clunkiness to save items.
- [Micro.blog](https://micro.blog/): I liked the idea of Micro.blog, but it emphasized the social element a lot and was missing features like tagging and a streamlined saving flow.

None of these platforms fit my needs well enough for me to start using them, but then when poking around a Mastodon recently I realized it may work.

## How I use Mastodon

My current setup is:

- Set my profile and posts to "unlisted" visibility. This means that my information can be seen when explicitly searched for or followed, but won't be suggested to people I don't know.
- Share items via the mobile app, [browser extension](https://github.com/corbindavenport/share-to-mastodon), or [straight from Feedbin](https://feedbin.com/blog/2023/01/05/mastodon-and-microposts/)
- Mastodon also supports RSS, which means that if I have accounts I want to view without getting sucked into the app I can just add them into Feedbin. The same is true if someone wants to see my posts.

So in practice, I rarely open the Mastodon app. Its role is to easily enable sharing articles from all different platforms and consuming them via RSS wherever you like. I imagine most tech companies wouldn't be okay with this sort of approach, but because Mastodon doesn't depend on ad revenue for people using their app they can. I have set up a recurring contribution to the maintainers of my mastodon instance to help cover server costs, but this isn't required.


## Drawbacks

There are still a few drawbacks to Mastodon for me:

- No tagging. I could use hashtags and see how well that works when searching, but it would still be a subpar experience compared to something like Notion and Airtable.
- Open protocols mean some things just won't be possible. While trying to further limit the social media aspect of my Mastodon profile, I was investigating disabling comments/replies to my posts. I came across [this four-year-old thread](https://github.com/mastodon/mastodon/issues/8565) that is still active. The current consensus is that such a change would be hard to implement across the variety of services that implement the ActivityPub protocol. Moxie (Signal's founder) had a [great talk on this topic](https://www.youtube.com/watch?v=Nj3YFprqAr8) where he explained why centralized systems can innovate so much faster. I love open standards but agree with his points.
- Search functionality may not be sufficient. I'm not certain on this one, but from a couple of test searches so far I could see myself finding the search functionality lacking. If this is the case, I could most likely lean on Feedbin's searching of Mastodon's RSS, but let's hope it doesn't come to that.
- It's social. Even though I locked my profile down, a couple posts had their permissions set wrong and got promoted to others. After getting a couple like, I begin to fall back into the chasing of validation that I wanted to separate from. Even without this promotion, I still find myself wanting to write clever captions with some posts, even though I know most posts will probably go unread by anyone but me.

Despite all these, I'm still pretty happy with it. I plan to continue sharing all the interesting things I come across, so feel free to check out my history, or even give me a follow:

[https://mastodon.nl/@grahamjpark](https://mastodon.nl/@grahamjpark)