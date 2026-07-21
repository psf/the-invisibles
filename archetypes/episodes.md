{{- /* Usage: hugo new episodes/ep-13.md  (or ep-13-trailer.md)
     The episode number is derived from the filename.
     Fill in every TODO before publishing. */ -}}
{{- $num := replaceRE `[^0-9]` "" .Name -}}
{{- $trailer := in .Name "trailer" -}}
---
{{ if $trailer -}}
title: "Trailer: Episode {{ $num }} with TODO_SPEAKER_NAME"
meta_title: "Trailer: Episode {{ $num }} with TODO_SPEAKER_NAME"
description: "A preview of our chat with TODO_SPEAKER_NAME. Watch the full episode on TODO_FULL_EPISODE_DATE"
{{- else -}}
title: "Episode {{ $num }}: with TODO_SPEAKER_NAME"
meta_title: "Episode {{ $num }} with TODO_SPEAKER_NAME"
description: "TODO: one or two sentences about the episode. This appears in podcast apps and the RSS feed."
{{- end }}

date: {{ .Date }}
host: ["TODO", "TODO"] # who hosted this episode, e.g. Cheuk, Mariatta
draft: true # set to false when ready to publish
tags: ["python", "TODO"]
publish_date: {{ .Date }} # set both dates to the desired publish time
podcast_file: "/audio/hidden-figures-ep{{ $num }}{{ if $trailer }}-trailer{{ end }}.mp3"
podcast_duration: 0 # TODO: run: python print_metadata.py static/audio/hidden-figures-ep{{ $num }}{{ if $trailer }}-trailer{{ end }}.mp3
episode_image: "images/ep{{ $num }}-TODO_SPEAKER_FIRST_NAME.png"
podcast_bytes: "0" # TODO: from print_metadata.py, the length of the episode in bytes
images: ["images/ep{{ $num }}-TODO_SPEAKER_FIRST_NAME.png", "images/TODO_SPEAKER_NAME.jpg"]
explicit: false
type: 'episode'
episode: '{{ $num }}'
season: 2
transcript: '/transcript/hidden-figures-of-python-ep{{ $num }}{{ if $trailer }}-trailer{{ end }}.srt'
episode_type: {{ if $trailer }}trailer{{ else }}full{{ end }}
layout: episode
youtube_id: "" # TODO: once the video is uploaded to the PyPodcats YouTube channel

speaker:
  url: "/speakers/TODO-speaker-slug/"
  title: "TODO_SPEAKER_NAME"
  image: "/images/TODO_SPEAKER_NAME.jpg"
  description: "
TODO: speaker bio from the Speaker Info Form.
"
  social:
  - name: github
    icon: fa-brands fa-github
    link: https://github.com/TODO

  - name: linkedin
    icon: fa-brands fa-linkedin
    link: https://www.linkedin.com/in/TODO/

  - name: web
    icon: fa-solid fa-globe
    link: https://TODO

---

{{ if $trailer -}}
Sneak Peek of our chat with TODO_SPEAKER_NAME, hosted by TODO_HOSTS.

TODO: short speaker introduction and what the episode covers.

Full episode is coming on **TODO_FULL_EPISODE_DATE**! Subscribe to our podcast now!
{{- else -}}
We interviewed TODO_SPEAKER_NAME.

TODO: speaker introduction paragraph.

TODO: paragraph about what the episode covers.

Be sure to listen to the episode to learn all about TODO_SPEAKER_FIRST_NAME's inspiring story!

## Topic discussed

- Introductions
- Getting to know TODO_SPEAKER_FIRST_NAME
- TODO

## Links from the show

- TODO: https://TODO
{{- end }}
