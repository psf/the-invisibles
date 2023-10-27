---
title: "Gender Diversity and Representation in Popular Python Community Podcasts"
meta_title: "Gender Diversity and Representation in Popular Python Community Podcasts"
description: "Gender Diversity and Representation in Popular Python Community Podcasts"
date: 2023-10-27T05:00:00Z
categories: ["Blog Post",]
author: "Mariatta"
tags: ["python", "data", "diversity", "community"]
draft: false
---

Throughout the years, the Python community as a whole has made significant effort
in improving diversity. This can be seen in improvements in speaker diversity
at Python conferences, and among PSF Board of Directors.

However, when looking at popular podcasts in the Python community, we noticed
that women are still under-represented compared to men. We could not find
an existing analysis about this, therefore we decided to do our own research
to gather data about gender diversity at podcasts about Python.

# Our Findings

We published our data using [Datasette](https://datasette.io). You are welcome to
view and explore the data yourself at the following URL:
https://python-podcast-datasette-8c9c837ad30f.herokuapp.com/python_podcast_datasette

In this post, we will be referring to the data from the above Datasette. We will
also explain in more detail on how we obtained and collected the data.

# Popular Python Podcasts we looked into

We looked into data from the following three Python-related podcasts: [Real Python Podcast](https://realpython.com/podcasts/rpp/),
[Python Bytes](https://pythonbytes.fm/), and [Talk Python to Me](https://talkpython.fm/). 

We chose to look into these podcasts for the following reasons:
- When using several search engines with keywords "Python Podcast" (Bing, Google, Duck Duck Go), these are the podcasts that appeared on the first page of the search result.
- The hosts of these podcasts regularly invite guests to their show
- The podcasts are well established, each of them have been running for years, and having hosted more than 100 episodes in which guests were invited to appear on the show

# Basic Stats about Each Podcast

Before we dwell more into the data of gender diversity from these podcasts, let's
review some basic information about each of the podcasts.

Note that the data below were collected on September 21, 2023.
Therefore, we only have information up until September 21, 2023.

## Real Python Podcast

- Total number of episodes: 173.
- Total number of episodes with a guest: 138
- First episode: March 20, 2020 (3 years)
- Website: https://realpython.com/podcasts/rpp/
- About:
> A weekly Python podcast hosted by Christopher Bailey with interviews, coding tips, and conversation with guests from the Python community.
> The show covers a wide range of topics including Python programming best practices, career tips, and related software development topics.
> Join us every Friday morning to hear what’s new in the world of Python programming and become a more effective Pythonista.

## Python Bytes

- Total number of episodes: 353
- Total number of episodes with a guest: 100
- First episode: November 7, 2016 (7 years)
- Website: https://pythonbytes.fm/
- About:
> Python Bytes is a weekly podcast hosted by Michael Kennedy and Brian Okken. Python Bytes podcast delivers headlines directly to your earbuds.


## Talk Python To Me

- Total number of episodes: 428
- Total number of episodes with a guest: 428
- First episode: March 21, 2015 (8 years)
- Website: https://talkpython.fm/
- About:
> Talk Python to Me is a weekly podcast hosted by Michael Kennedy. The show covers a wide array of Python topics as well as many related topics.
> The format is a casual 1-hour conversation with industry experts.



| Podcast Title       |            First Episode            |          Number of Episodes          | Number of Episodes featuring Guests | 
|---------------------|:-----------------------------------:|:------------------------------------:|:-----------------------------------:|
| Real Python Podcast |      March 20, 2020 (3 years)       |         173                          |                 138                 |
| Python Bytes        |    November 7, 2016 (7 years)       |                 353                  |           100                       |
| Talk Python To Me   |      March 21, 2015 (8 years)       |                 428                  |                 428                 |


# Collecting Data about Invited Guests

We looked at each of the podcasts website, and reviewed each episodes. We wrote a Python script, using the BeautifulSoup Library, to collect
as many data as possible automatically. Most of the data about speaker name, episode date, episode title, were collected using the script. This
script then produced a csv (comma-separated value) file. In
cases where the script were not able to populate the data correctly (it is very basic script and we did not use AI for it!), we filled the
data manually by reading the podcast website.

We collected the following info from the three podcasts mentioned above:
- The name of the guest,
- The date the episode aired,
- The episode number for the specific podcast series,
- The podcast title,
- The name of the episode sponsor, if any


# Determining the guests' gender

We recognize that a person's gender identity is a personal matter. For each of the invited guests (544 of them),
we looked at their name, their photo, visited their website/social media, and checked their pronoun.
In many cases, we personally know the guest speaker  and therefore we used our personal knowledge about their gender identity.

We recognize that during this analysis we might have misgendered some of the guests, and we profoundly apologize if this happened.
It is not our intention to offend anyone. We welcome any correction and we will update our record accordingly.

# Determining which episodes to include

We looked only at episodes where there is an invited guest to the show.
Episodes in which there are only the Host or Co-host, are not included in our analysis.

# The results

From the three podcasts, we found the following statistics.

## Episodes in which women are featured

| Podcast Title       | Episodes with guests | Episodes featuring Women | Percentage of episodes featuring women |
|---------------------|:--------------------:|:------------------------:|:--------------------------------------:|
| Real Python Podcast |         138          |            26            |                 18.84%                 |
| Python Bytes        |         100          |            33            |                  33%                   |
| Talk Python To Me   |         428          |     58                   |                 13.55%                 |
| **Combined**        |       **666**        |         **117**          |               **17.56%**               |

The three podcasts produced 666 episodes in which guests were invited to appear on the show.
In Real Python Podcast, out of the 138 episodes with invited guest, only 26 of the episodes feature women (18.84%).
In Python Bytes, out of the 100 episodes with invited guest, only 33 of the episodes feature women (33%).
In Talk Python To Me podcast, out of 428 episodes with invited guest, only 58 episodes feature women (13.55%).

In total, out of the **666 episodes**, only **117 (17.56%)** episodes feature women.

Note that in some cases, there are more than one invited guests. When calculating which episodes feature
a woman, it could include episode in which both man and woman appeared together on the show.

## How many women were invited to the show

Some women appeared more than once in the podcast series. So even though there are 117 episodes in which 
women were invited, it does not mean there are 117 different women who have appeared on the show.

The table below shows a comparison of the total number of guests
in each show, vs how many of the guests are women.

| Podcast Title       | Unique Guests | Unique Guests who are women | Percentage of unique guests who are women |
|---------------------|:-------------:|----------------------------:|------------------------------------------:|
| Real Python Podcast |      95       |                          24 |                                       25% |
| Python Bytes        |      88       |                          29 |                                       32% |
| Talk Python To Me   |      433      |                          57 |                                       13% |
| Combined            |      544      |                          96 |                                     17.6% |

In Real Python Podcast, there have been 95 unique guests, and 24 (25%) of them are women.
In Python Bytes, there have been 88 unique guests, and 29 (32%) of them are women.
In Talk Python To Me, there have been 433 unique guests, and 57 (13%) of them are women.

Across the three podcasts, there have been 544 unique guests, and 96 (17.6%) of them are women.


## Most frequently invited guests

We then looked at the top repeat guests at each podcast series.

## Talk Python To Me


| Guest Name    | Number of episodes | 
|---------------|:------------------:|
| Brian Okken   |         11         |
| Brett Cannon  |         9          |
| Anthony Shaw  |         9          |
| Jay Miller    |         6          |
| Dan Bader     |         6          |
| Łukasz Langa  |         5          |
| Paul Everitt  |         5          |
| Cecil Phillip |         5          |
| **Combined**  |       **56**       |  

Talk Python To me has a total of 428 episodes with invited guests. Most guests appeared
at most once, some twice. There are 8 people who appeared 5 times and more, totaling to 56 episodes.
This is a stark difference compared to the 57 total women who have ever appeared on the same podcast.

On this podcast, the most a woman has re-appeared on the show is 4 times. Most appeared only once.
Only 7 women have appeared more than once.

| Guest Name       | Number of episodes | 
|------------------|:------------------:|
| Ines Montani     |         4          |
| Emily Morehouse  |         4          |
| Carol Willing    |         4          |
| Katharine Jarmul |         3          |
| Gina Häußge      |         2          |
| Ewa Jodlowska    |         2          |
| Anna-Lena Popkes |         2          |
| **Combined**     |    **21**          |  

## Real Python Podcast


| Guest Name          | Number of episodes | 
|---------------------|:------------------:|
| David Amos          |         29         |
| Geir Arne Hjelle    |         7          |
| Martin Breuss       |         6          |
| Brett Cannon        |         5          |
| Al Sweigart         |         4          |
| Christopher Trudeau |         4          |
| Jodie Burchell      |         4          |
| **Combined**        |       **59**       |  

Real Python Podcast has a total of 138 episodes with invited guests. Most guests appeared
at most once, some twice. There are 7 people who appeared 4 times and more, totaling to 59 episodes.
Out of the seven popular repeat guests, only one of them is a woman (Jodie Burchell).

On this podcast, the most a woman has re-appeared on the show is 4 times. Most appeared only once.
There are 23 people who appeared more than once, only 4 women have appeared more than once.


| Guest Name          | Number of episodes | 
|---------------------|:------------------:|
| Jodie Burchell      |         4          |
| Sadie Parker        |         2          |
| Nina Zakharenko     |         2          |
| Joanna Jablonski    |         2          |
| **Combined**        |       **10**       |  

## Python Bytes

| Guest Name             | Number of episodes | 
|------------------------|:------------------:|
| Brett Cannon           |         4          |
| Calvin Hendryx-Parker  |         4          |
| Anthony Shaw           |         3          |
| Kelly Schuster-Paredes |         3          |
| **Combined**           |       **14**       |  

Python Bytes has a total of 100 episodes with invited guests. Most guests appeared
at most once, some twice. There are 4 people who appeared more than twice, totaling to 14 episodes.

On this podcast, the most a woman has re-appeared on the show is 3 times. Most appeared only once.
There are 12 people who appeared more than once, only 3 women have appeared more than once.


| Guest Name              | Number of episodes | 
|-------------------------|:------------------:|
| Kelly Schuster-Paredes  |         3          |
| Nina Zakharenko         |         2          |
| Ines Montani            |         2          |
| **Combined**            |       **14**       |  

# Popular guests

We notice several guests have appeared in more than one podcasts. The following
are the most popular guest speaker from the above podcasts, guests who appeared more than five times.

| Guest Name            | Number of episodes | Number of podcasts | 
|-----------------------|:------------------:|:------------------:|
| David Amos            |         30         |         2          |
| Brett Cannon          |         18         |         3          |
| Anthony Shaw          |         14         |         3          |
| Brian Okken           |         11         |         1          |
| Dan Bader             |         9          |         3          |
| Jay Miller            |         8          |         2          |
| Łukasz Langa          |         7          |         2          |
| Pablo Galindo Salgado |         7          |         2          |
| Geir Arne Hjelle      |         7          |         1          |
| Cecil Phillip         |         7          |         3          |
| Calvin Hendryx-Parker |         7          |         2          |
| Al Sweigart           |         7          |         3          |
| Steve Dower           |         6          |         2          |
| Paul Everitt          |         6          |         2          |
| Matt Harrison         |         6          |         3          |
| Martin Breuss         |         6          |         1          |
| Ines Montani          |         6          |         2          |

Out of the 16 people who have appeared more than 5 times, only one of them is a woman (Ines Montani).

10 people have appeared in all three podcasts. Out of the 10 people, only 2 of them are women. (Nina Zakharenko and Kelly Schuster-Paredes).

| Guest Name              | Total appearances (in all 3 podcasts) | 
|-------------------------|:-------------------------------------:|
| Brett Cannon            |                  18                   |
| Anthony Shaw            |                  14                   |
| Dan Bader               |                   9                   |
| Al Sweigart             |                   7                   |
| Cecil Phillip           |                   7                   |
|  Matt Harrison          |                   6                   |
| Keylly Schuster-Paredes |                   5                   |
| Nina Zakharenko         |                   5                   |
| Sean Tibor              |                   4                   |
| Will McGugan            |                   3                   |

# Comments from the hosts

We have reached out to the hosts of the above podcasts for comment. Here are
their replies:

## Talk Python To Me

Michael Kennedy, founder of Talk Python explains the process of inviting podcast guests:

> Here's how the planning on a show goes on Talk Python To Me:
> - A listener suggests some topic I am not familiar with but seems worthwhile
> - I find the project page and use their contact us form to see if someone from the project is interested in coming on the show
> - 9/10 times that person is a man
> - When it seems reasonable I do even explicitly ask if there is a woman on the project that could join, sometimes there is

He explains the reason of why there are less women on the show:

> I do specifically keep my eye out for women doing amazing things (there are certainly some good examples) and invite them. Even then, I would say women are 2x or more likely to say no thanks and decline relative to men.

He also added:

> I'm also against having women on the show who maybe aren't doing as deep of technical work but they are women. When I have a woman (or any one) on the show, I want people to think "Wow that's amazing. I really respect that work." I don't think it serves women well to seem to be there to fill a quota. They should be there because they are really awesome, and I would say the women I have had on are in that category. … I don't want people to think "women are here to manage community and write the docs, men do the hard coding" No, women do too. Maybe not in as high of numbers, but they do. And I try to feature them.

Despite the above, he said:

> I plan to keep search for women doing amazing things

## Python Bytes

Here is the response from Michael Kennedy regarding their other podcast Python Bytes:

> Python Bytes is a little different and we can explicitly identify women and invite them because it's rarely about their projects but just their take on the news. We make a conscious effort to do this and that's why the numbers are the best of the bunch on that show.

So there you go, there is still more work to be done to empower women and celebrate
the achievement of women in the community.


# Conclusions

We are quite disappointed to see such low representation of women in the popular Python
podcasts. These podcasts are considered as "top podcasts" with large number
of listeners. Appearing in the podcast can be seen as a privilege and comes
with the power to influence the rest of Python community. We are sad to see
that women appeared to not be given the same opportunity afforded to men.

Seeing the lack of women representation is one of our motivating factors in
starting the Hidden Figures of Python Podcast series, to ensure that the rest
of the Python community can also learn more of the women and other underrepresented
minorities in our community.

