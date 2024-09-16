---
title: "How We Produce an Episode"
meta_title: "How We Produce an Episode"
description: "How We Produce an Episode"
image: "/images/podcats.png"
draft: false
---

Below is the documentation on how our team produce one PyPodcats episode.

There are various stages involved to produce a PyPodcats episode:
1. Speaker invitation
2. Episode recording
3. Editing
4. Reviewing
5. Transcribing
6. Publishing

## Detailed Documentation on How to publish an Episode of PyPodcats

Notes: 
- Links with the lock icon 🔐 are private and can only be accessed by PyPodcats team members.
- If you are a PyPodcats team member and having trouble accessing the links, please reach out on Slack.

As a PyPodcats team member, you should have access to the following:
- [PyPodcats Google Drive](https://drive.google.com/drive/folders/1LoSeAn2iJaVUuYF2ac7_kHKyEKCORfeh) 🔐 
- [PyPodcats Episodes on Google Drive](https://drive.google.com/drive/folders/1Lqnu_7Og5khMTa_k-QD3tlWF2MFypaAX) 🔐 
- [PyPodcats Speaker Info Form](https://docs.google.com/forms/d/e/1FAIpQLSeLuOx6dDc2D38q7gYyFiOlRft9sumium1nFbIwwIE4JQYNrw/viewform?usp=sf_link )
- [Veed.io](https://veed.io)
- [Streamyard](https://streamyard.com)
- [Buffer](https://buffer.com)
- [Calendly](https://calendly.com)

Credentials for the above are found on Notion.

Tools that are needed for the **"Publishing"** step:
- Python
- [ffmpeg](https://www.ffmpeg.org/ffmpeg.html)
- [ffprobe](https://www.ffmpeg.org/ffprobe.html)
- [Hugo](https://gohugo.io/) static site generator

### Detailed Steps

#### 1. Speaker Invitation

- Write an email inviting them to the podcast
  - Send the email using meow@pypodcats.live email address, hosted through Fastmail
- Prepare a collaboration doc on Google Docs
- Ask the speaker to fill in Speaker Information form
  - https://docs.google.com/forms/d/e/1FAIpQLSeLuOx6dDc2D38q7gYyFiOlRft9sumium1nFbIwwIE4JQYNrw/viewform?usp=sf_link 
- Schedule a prep call & tech check session: 30 minutes, schedule through Calendly
- Schedule the episode recording: 1 hour, schedule through Calendly

#### 2. Episode Recording

- Create the StreamYard recording link
- Share the StreamYard recording link with speaker
- Include the StreamYard recording link on the Prep Notes for easy discovery

#### 3. Editing

- Download raw videos from Streamyard: the composite video, and individual local recordings
- Create new folder on Google Drive under the **PyPodcats** > **[Episodes](https://drive.google.com/drive/folders/1Lqnu_7Og5khMTa_k-QD3tlWF2MFypaAX)** 🔐  folder
  - Example folder name: **"Ep 6 - Niharika Vadluri"**
  - Example folder path: **PyPodcats > Episodes > Ep 6 - Niharika Vadluri**
- Upload the raw videos to this folder
- Let Georgi know that the videos are ready for editing
- Produce:
  - trailer video
  - full episode video
  - artwork (using provided photo and information from the speaker info form)
  - necessary promotional materials
- Upload all assets to the Speaker folder on PyPodcats > Episodes > Speaker folder
- Folder structure:
  + PyPodcats
    + Episodes
      + Ep 1 - Speaker Name
        + Ep 1 - trailer
        + Ep 1 - full
        + Ep 1 - raw
      + Ep 2 - Speaker Name
        + Ep 2 - trailer
        + Ep 2 - full
        + Ep 2 - raw

#### 4. Reviewing

- Let other team members know that the episode is ready for review
- Share the trailer and full episode with the speaker for review
- Make any further editing based on feedback from other team members and speaker
- Reupload any updates to the same folder

#### 5. Transcribing

- Once episode is approved, proceed to transcribe and subtitle using Veed.io
- Go to veed.io, providing the pypodcats.live email address
- The login info will be sent to the email address, click on it to login
- On veed.io, Create a new project, upload the video/ trailer
- Choose the "Subtitle" on the left. Options:
  - Language: English 
  - Detect speakers: yes
  - Click the "auto-subtitle" button
- Review the generated subtitle, listen to the video, and make edits.
  - fix any typos
  - Ensure proper capitalization, eg PyPodcats, Python, PSF, PyLadies, etc
  - If necessary, clarify spellings with the speaker.
- Ensure the subtitle is readable on the video
  - The subtitle text should have black background
- Once finished, Download the subtitle as `.SRT` file
- Export the video. Options:
  - Click "Done" button on the top right
  - Burn Subtitles: yes
  - Click the "Export Video" button
- Once exported, download the video as both MP3 and MP4.
  - MP4 is to be uploaded to YouTube
- Repeat this for both the trailer and the full episode
- Upload the subtitled videos, and the .SRT files to the Speaker Episode folder on Google Drive.
  - Ensure to include "captioned" in the filename so that we can distinguish between the video with subtitle and without 

#### 6. Publishing

##### Internal team workflow

- Gather all the videos, transcript (at this point, everything should have been on one folder on Google Drive)
- Create the webpage for the episode/trailer
  - Create a new branch under the [psf/the-invisibles](https://github.com/psf/the-invisibles) GitHub repository, e.g. **add-ep-6-trailer**
  - Create new files (you can copy/look at content from previous episodes):
    - **f"assets/images/ep{episode_number}-{speaker_name}.jpg"**: The cover image for the episode (png works too)
    - **f"assets/images/{speakername}.jpg"**: The speaker photo (download from the Speaker Info Form. png works too)
    - **f"content/english/episodes/ep{number}-trailer.md"**: write up about the trailer episode (more details below)
    - **f"content/english/episodes/ep{number}.md"**: write up about the full episode (more details below)
    - **f"content/english/speakers/{speaker_name}.md"** : speaker bio page: photos, links, etc
    - **f"static/audio/hidden-figures-ep{number}-trailer.mp3:"**: mp3 of the trailer
    - **f"static/audio/hidden-figures-ep{number}.mp3:"**: mp3 of the full episode
    - **f"static/audio/transcript/hidden-figures-of-pyhon-ep{number}-trailer.srt:"**: transcript of the trailer
    - **f"static/audio/transcript/hidden-figures-of-pyhon-ep{number}.srt:"**: transcript of the full episode
  - Commit, push, and create a pull request
  - Example Pull request: https://github.com/psf/the-invisibles/pull/40
  - Preview the episode (check the Netlify Deploy Preview), share the preview with teammates and speaker
  - Validate the RSS feed format
    - Once Netlify preview has been built, go to {netlify preview url}/episodes/index.xml. This is the RSS Feed url.
    - Enter the RSS Feed url to https://www.castfeedvalidator.com/ 
    - Ensure everything is green

##### YouTube workflow

- Once videos, transcript, and writeups are done, share the Speaker Folder with The PSF (Marie Nordin)
  - At this point: the artwork and writepups should also be on the Speaker Google Drive folder
  - Provide the YouTube title and description via Google Docs (include the docs on Google Drive)
  - DM her on The PSF Slack
- Let her know that the episode is ready for publishing to YouTube
  - Schedule it for publishing
  - Usually we do it on 6 AM US Eastern timezone
- Once YouTube video has been uploaded, update the webpage with the YouTube ID in the frontmatter

##### Scheduling

- Set the desired schedule dates into the webpage frontmatter
- Ensure YouTube video ID is updated
- Commit and merge the pull request
- There is a scheduled GitHub action that rebuilds the site every hour. The content will eventually be published
  automatically
- Promote on social media
  - Draft the announcement on buffer. Credentials in Notion.

#### Publishing to Spotify/Apple Podcast etc

This happens automatically, so there is nothing else to do.
They are configured to pick up changes from our RSS Feed (pypodcats.live/episodes/index.xml).

As long as our rss feed is valid, any new episodes will appear. That is why we need to always validate the RSS feed
before merging.

#### More technical details on the Episode Write up


Episode/Trailer writeup should be created under the **content/english/episodes/** directory as a new
markdown file, e.g **f"content/english/episodes/ep{number}-trailer.md"**

Update the episode frontmatter with the correct information.

The information on this frontmatter is used to generate the RSS Feed for our podcast (on /episodes/index.xml), which
is consumed by podcast apps like Spotify, Apple Podcast, Overcast.fm, etc.

Therefore, it is important to have these info as accurate and correct as possible.

Example frontmatter for a full episode. (You can always just copy from any previous episode)
```
title: "Episode 5: with Mona Obedoza"
meta_title: "Episode 5 with Mona Obedoza"
description: "Learn about Mona Obedoza from the Philippines to hear about her journey in technology. She started learning to code at five years old, and now she is teaching other kids to code."
date: 2024-07-24T05:00:00-07:00
host: [ "Georgi", "Tereza"]
draft: false
tags: ["python", "public speaking", "coding for kids", "youth", "Philippines", "mental health"]
publish_date: 2024-07-24T05:00:00-07:00
podcast_file: "/audio/hidden-figures-ep5.mp3"
podcast_duration: 2372.257959
episode_image: "images/ep5-mona.png"
podcast_bytes: "55887490" # the length of the episode in bytes
images: ["images/ep5-mona.png", "images/mona_obedoza.png"]
explicit: false 
type: 'episode'
episode: '5'
season: 1
transcript: '/transcript/hidden-figures-of-python-ep5.srt'
episode_type: full
layout: episode
youtube_id: SDipvSE21Es
```

The fields should be self-explanatory (hopefully), but here are some fields that might need special attention:

- **episode_type**: It should be either **episode** or **trailer**
- **youtube_id**: This is the ID from the YouTube video that got uploaded to The PSF's YouTube channel
  The HTML template will pick this field up automatically to render the YouTube video in each episode
- **podcast_bytes** and **podcast_duration**: This is generated using the print_metadata.py script.

##### Printing the metadata using Python

Create and activate a virtual environment.

```
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```
pip install -U pip
pip install -r requirements.txt
```

From the root of this repository, run the script:

```
python print_metadata.py {path to the audio/video file}
```

Copy the values printed to the **podcast_byes** and **podcast_duration** in the frontmatter.

##### Other useful ffmpeg commands

1. Extracting audio from video

Use this to generate mp3 audio file from a video

```
ffmpeg -i filename.mp4 filename.mp3
```

2. Scale the video/audio down

Sometimes you may need to scale down the video/trailer before sharing on social media.
It can be scaled down using ffmpeg.

To scale half size: 
```
ffmpeg -i input.mkv -vf "scale=trunc(iw/4)*2:trunc(ih/4)*2" new_file_half_the_size.mkv
```

To scale one-quarter size:

```
ffmpeg -i input.mkv -vf "scale=trunc(iw/8)*2:trunc(ih/8)*2" new_file_quarter_the_size.mkv
```

Read more on [ffmpeg scaling](https://trac.ffmpeg.org/wiki/Scaling) doc.
