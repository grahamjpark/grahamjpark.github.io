# My security suggestions

![](https://miro.medium.com/max/1920/1*HpmYbgeuahmpSnArtjw0sw.png)


I find myself recommending things to my friends a lot (sometimes it’s even because they asked me for my recommendations!), and I get a lot of enjoyment out of recommending things I love. So I decided I wanted create a series of posts about things I like to endorse.
Given my background working in cyber security, for the first post in the series I wanted to give some advice to improve your personal security. This article isn’t geared to get you to the top-notch level of security, but give you some practical things you can do to dramatically improve your security. Feel free to comment or message me with any questions!

# Low Hanging Fruit

If I just have a minute of your attention, there are a few quick things you can do to help improve your security online.

First off, **always update your devices and apps**. It may not always be convenient, but by not updating your apps, you’re exposing yourself open to be hacked. If the update fixes something security related, someone is probably out there trying to exploit the vulnerability by targeting users who haven’t applied the update yet. Related to this, be sure to **back up your files**. The most popular malware right now locks up all your files and demands money for them.

Another quick thing: **install** [**uBlock Origin**](https://github.com/gorhill/uBlock/#installation) **and** [**HTTPS Everywhere**](https://www.eff.org/https-everywhere). uBlock Origin is an ad blocker that you can trust. What does adblocking have to do with security? Well when there’s an ad on a website, it’s allowing anyone to insert something into the page you’re visiting. When malicious actors pay to show an ad on legitimate websites, they can use it to install malware on your machine (known as malvertising). This doesn’t just happen on little sites, websites like the New York Times, the BBC, and the NFL have hosted malvertising campaigns (Source: [theguardian](https://www.theguardian.com/technology/2016/mar/16/major-sites-new-york-times-bbc-ransomware-malvertising)). You can find the link to install uBlock Origin [here](https://github.com/gorhill/uBlock/#installation) (also, if you ever search for uBlock Origin online, make sure not to get it confused with uBlock. There’s a lot of drama there, use uBlock Origin). HTTPS Everywhere helps make sure that your connection to a website is using a secure connection when offered. This can help prevent people eavesdropping on your connection or getting in the middle between you and who you’re connected with. You can install it [here](https://www.eff.org/https-everywhere).

To add an extra layer of security, set up **two-factor authentication**. You may already use two-factor authentication (2FA) on some accounts and not even know it. If you have to get texted a code to log into your bank, that’s 2FA. If the option is offered, I would recommend using the “Google Authenticator” option over receiving an text message code. Text codes are hard to intercept (see more in the phones section). Further, instead of the actual Google Authenticator app I like to **use** [**authy**](https://authy.com/)**,** which works anywhere the Google Authenticator App is supported. The main difference is that Authy offers the option to back up your codes for when you upgrade or lose your phone. For a good list of which sites offer 2FA and how to enable it, check out the site [twofactorauth.org](https://twofactorauth.org/#).

To help secure your identity, I would recommend you **sign up for credit and identity monitoring.** [Creditwise](https://creditwise.capitalone.com/) and [Credit Karma](https://www.creditkarma.com) are both useful tools to track changes on your credit report. Even better, with both services you get some free identity monitoring services. Both sites offer features that will alert you to things like new accounts opened under your name, and if your personal information shows up on the dark web. As a disclaimer, Creditwise is owned by Capital One (where I work), but am not receiving any benefit by suggesting Creditwise. Also, you don’t need to be a Capital One customer to signup for Creditwise! If you don’t want another app, or what to go f you want to go the extra mile, read how to freeze your credit for free in [this article](https://www.usatoday.com/story/money/2018/09/21/equifax-free-credit-freeze-new-law/1377815002/).

The final quick tip: **don’t trust wifi networks that don’t require a password**. If you’re using a insecure wifi network, anyone can set up and snoop on some of your internet activity! You can learn more about that in [this podcast](https://pca.st/23YG) where the hosts set up in a coffee shop and watch people’s traffic go by! All public wifi in general comes with risk, but I’ll touch on that in the VPN section. Just to be clear, the network should have a lock icon or “Secure” next to it and require a password as soon as you click it. If it opens up a page in the browser and asks for a password, that’s not secure.

# Passwords

It’s a well known fact that people are bad at choosing passwords, and they’re bad about using the same passwords across a ton of sites. I don’t think I can stress enough how much repeat password usage is a problem. Sites get hacked a lot, and those hackers take passwords they got from one site and try them against other sites. It’s actually pretty common. For example, they might try a password they got from one of the Yahoo hacks and try to login to your uber account. If it works, then they sell it to a guy in Russia who can get some free rides (as showcased in [this podcast](https://pca.st/4Q6Y)).

Try typing in your email at [haveibeenpwned.com](https://haveibeenpwned.com/). Which may reveal that your email and password showed up in a security breach that was made public. If nothing shows up, that may just mean that your password was leaked but hasn’t been made public yet.

So what do you do instead? You could make a unique complex password for every site, or you could use a password manager. A password manager generates and stores secure passwords for you. Right now, I recommend [Lastpass](https://lastpass.com/f?12852242). If you sign up for Lastpass, use [this link](https://lastpass.com/f?12852242) for my referral and you get a free month of premium.

Some people argue that storing all (or most) of your passwords in one place is even more risky, but I trust their security more than I trust my ability to create and remember good passwords. If you’d like to check out other options, [1password](https://1password.com/) is also a good, and [Bitwarden](https://bitwarden.com/) is a newer option that I’ve seriously considered switching to, but it currently only has one guy maintaining it fulltime.

Using a password manager can also save you from falling for some phishing attacks. For example, if a bad guy sets up a fake dropbox site at drobox.com, your password manager won’t confuse it for dropbox.com, but you might.

I realize this is the biggest ask. Switching over to a password manager can be intimidating. But just set up the extension and gradually let it capture all of your sites passwords, then over time update them with generated passwords. Or you can carve out some time and just get all your passwords updated in a day, whatever it takes.

Once you switch to a password manager, you will still need to create some passwords. Like your master password for a password manager, or for sites that you don’t want to keep in your password manager (like the email for the password manager, or for the logon to your computer). When you do create them, here are some ideas you should combine:

- Come up with a phrase. You could create a phrase that’s a few words and try shifting you hands up or down on the keyboard to make it appear random. For example the phrase “I’m bad at Poker” shifted up would become “*{jgqeq5)9i34”. If it’s longer, you could pick a certain letter of each word to create a portion of your password. An example of this is picking first letter from “The sea turtles really like to swim fast to get places” would be “tstrltsftgp”. Either of these could be used as a portion of your password.
- You can also use a site like random.org which has a [section to generate random passwords](https://www.random.org/passwords/). Most people struggle to memorize a random password for each site (hence the password manager), but I like to memorize a few random characters and include it as a part of my password.
- If you really want to use the same password across a group of sites, I’d recommend at least adding in some variation. An easy way to do this is come up with some way to use the name of the site to come up with part. For example, take the first letter from the site and mix it in or find the number that’s directly above the first letter on the keyboard and include it (for example, facebook would be 4). These tips wouldn’t be hard to crack if someone focused on your password, but if they are just looping through passwords they have without checking it would help you.
- Finally, if the password is for something you want to go the extra mile for, include a few random words at the beginning or end. I like to generate a list of 20 or so words and then three or four words. You could use [this site](https://www.randomlists.com/random-words) to help.

Also, if you ever have to write down a password or recovery code change it somehow or leave a portion of it off. For example if you have a code that’s a4u25, shift all letters by two so it becomes c4w25. Or maybe you have a grandparent who insists on writing down all their passwords, make then have every password end with “deg” and then leave that off the paper.

# Phones

Spam calls are one of the universal pains everyone deals with. And lately they’ve been getting crazy. If you’re getting a lot of calls from unknown numbers, my recommendation is to just let it go to voicemail. If they do leave a voicemail and claim to be some organization (like the IRS), look up the organization’s official website and call the phone number listed there. Also, a lot of spam calls use faked phone numbers, so even if you try to text them or call them it will just be some random unsuspecting person. To help protect yourself from spam calls, you can install an app like [Hiya,](https://hiya.com/) which will screen out known spam numbers, and show profiles for businesses when they call.

If you’re looking for a new phone, I would recommend Apple’s iPhone or Google’s [Pixel](https://store.google.com/product/pixel_2). Android phones have a bad reputation security-wise, but a large part of that is because a majority of Android phones are very slow to get updates. If Google wants to update Android phone, it first has to go through all of the different phone manufacturers (e.g. Samsung). This could mean that your phone has security vulnerabilities for a long time before it actually gets patched. With iPhones or Android phones made by Google (the Pixel), updates get pushed immediately.

Whichever you pick, make sure to only install apps from the official App Store or Google Play store. You shouldn’t trust whoever is running any other app store.

On a related note, phones numbers (or more specifically calls or texts to that number) are used in some sites as a base layer of security. Unfortunately, it’s not as hard as you might think to get your phone number transferred to a bad guy. [This podcast](https://pca.st/episode/370b800b-5506-4c04-a449-e404162cc118) from Replay All does a really good job explaining this as it investigates a case where it happened. Basically, the bad guy calls your cell phone provider pretending to be a worker needing to upgrade you to a new phone. The carrier switches things over, and now they get your calls and texts. To protect yourself, follow the steps in [this article](https://motherboard.vice.com/en_us/article/zm8a9y/how-to-protect-yourself-from-sim-swapping-hacks) and switch to using [Authy](https://authy.com/) when possible.

# VPN

When you’re on a public wifi connection, it’s a good idea to use a VPN. Basically a VPN creates a secure tunnel between your computer and the VPN’s server. Then the VPN server talks to whatever websites you’re connecting to. This prevents the owner of the wifi connection from snooping on your traffic or inserting malware or ads into your traffic.

If you want to use a VPN, it should be one you’re paying for. Free VPNs have been caught selling your data, transmitting data insecurely, and inserting more advertisements onto websites ([check out this article for more info](https://www.extremetech.com/internet/274548-if-youre-using-a-free-vpn-youre-being-farmed-for-data)). I’ve been using [Private Internet Access](https://www.privateinternetaccess.com/pages/buy-vpn?invite=U2FsdGVkX196NdVbmI3HywBMnX3BGeig9w7-QmbnpwY%2Cl1He0lT3bceC_tw2b1l0b-Xmc9A) for awhile now and I like it. If you decide to use it please use my [referral link](https://www.privateinternetaccess.com/pages/buy-vpn?invite=U2FsdGVkX196NdVbmI3HywBMnX3BGeig9w7-QmbnpwY%2Cl1He0lT3bceC_tw2b1l0b-Xmc9A) and we’ll both get 30 days free. If you have trust issues with companies based in the US, I’ve heard good things about [NordVPN](https://nordvpn.com/) or you could use [this chart](https://thatoneprivacysite.net/simple-vpn-comparison-chart/) to compare a ton of VPNs.

# Network Monitoring

This section may not be as crucial as the others, but I really have enjoyed having Glasswire installed on my computer. It basically keeps track of all network connections coming from your computer and what applications are reaching out to the web. It also gives you all kinds of useful alerts for when bad things might have happened with your network. You can check it out [here](https://www.glasswire.com/), or use my referral codes for each product (code for [basic](https://store.glasswire.com/1309/?affiliate=48817&scope=checkout&cart=156795), for [pro](https://store.glasswire.com/1309/?affiliate=48817&scope=checkout&cart=156796), and for [elite](https://store.glasswire.com/1309/?affiliate=48817&scope=checkout&cart=156797)). Each of those links is for the one time purchase price, but I also have codes for the subscription pricing too, just let me know if you want that.

If you’re on a Mac, I believe a similar product is [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html).

# Tools and More Info

If you’re interested in security but aren’t super technical, I recommend a few different podcasts. They are all about security and do a good job boiling things down. I’ll let you read the descriptions yourself:

- [Hackable](https://pca.st/podcast/9a290c90-4a11-0135-902b-63f4b61a9224)
- [Breach](https://pca.st/podcast/47261020-0de8-0136-c264-7d73a919276a)
- [Cyber](https://pca.st/podcast/78a90df0-c5e0-0136-7b94-27f978dac4db)

Two sites you might find useful if you have a suspicious link are [urlscan](https://urlscan.io/) and [VirusTotal](https://www.virustotal.com/#/home/upload). Urlscan allows you allows you to submit a link and it’ll return a screenshot and a ton of other information. VirusTotal can take links or files and run them against 60+ different antivirus programs to see their result. You should be careful when copying and pasting a link not to visit it, but they can provide some interesting info!

Finally, if you want to know more security tips, check out the website [watchyourhack.com](https://watchyourhack.com/) or [Motherboard’s Guide to Not Getting Hacked](https://motherboard.vice.com/en_us/article/d3devm/motherboard-guide-to-not-getting-hacked-online-safety-guide). Both cover a lot of the same things I mentioned here, but have way more tips. Definitely worth scrolling through at least!

Thanks for taking the time to read through this list! If you have any questions or disagree with something I said let me know. Hope this helped!

EDIT [12/30/2018]
Included the section about spam calls and Hiya. Thanks for the recommendations [Ethan](https://www.linkedin.com/in/ethanpedoeim/)!

