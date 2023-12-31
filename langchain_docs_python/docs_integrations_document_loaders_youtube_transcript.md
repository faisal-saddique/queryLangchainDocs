YouTube transcripts
===================

> [YouTube](https://www.youtube.com/) is an online video sharing and social media platform created by Google.

This notebook covers how to load documents from `YouTube transcripts`.

    from langchain.document_loaders import YoutubeLoader

    # !pip install youtube-transcript-api

    loader = YoutubeLoader.from_youtube_url(    "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True)

    loader.load()

### Add video info[](#add-video-info "Direct link to Add video info")

    # ! pip install pytube

    loader = YoutubeLoader.from_youtube_url(    "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True)loader.load()

### Add language preferences[](#add-language-preferences "Direct link to Add language preferences")

Language param : It's a list of language codes in a descending priority, `en` by default.

translation param : It's a translate preference when the youtube does'nt have your select language, `en` by default.

    loader = YoutubeLoader.from_youtube_url(    "https://www.youtube.com/watch?v=QsYGlZkevEg",    add_video_info=True,    language=["en", "id"],    translation="en",)loader.load()

YouTube loader from Google Cloud[](#youtube-loader-from-google-cloud "Direct link to YouTube loader from Google Cloud")
------------------------------------------------------------------------------------------------------------------------

### Prerequisites[](#prerequisites "Direct link to Prerequisites")

1.  Create a Google Cloud project or use an existing project
2.  Enable the [Youtube Api](https://console.cloud.google.com/apis/enableflow?apiid=youtube.googleapis.com&project=sixth-grammar-344520)
3.  [Authorize credentials for desktop app](https://developers.google.com/drive/api/quickstart/python#authorize_credentials_for_a_desktop_application)
4.  `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib youtube-transcript-api`

### 🧑 Instructions for ingesting your Google Docs data[](#-instructions-for-ingesting-your-google-docs-data "Direct link to 🧑 Instructions for ingesting your Google Docs data")

By default, the `GoogleDriveLoader` expects the `credentials.json` file to be `~/.credentials/credentials.json`, but this is configurable using the `credentials_file` keyword argument. Same thing with `token.json`. Note that `token.json` will be created automatically the first time you use the loader.

`GoogleApiYoutubeLoader` can load from a list of Google Docs document ids or a folder id. You can obtain your folder and document id from the URL: Note depending on your set up, the `service_account_path` needs to be set up. See [here](https://developers.google.com/drive/api/v3/quickstart/python) for more details.

    from langchain.document_loaders import GoogleApiClient, GoogleApiYoutubeLoader# Init the GoogleApiClientfrom pathlib import Pathgoogle_api_client = GoogleApiClient(credentials_path=Path("your_path_creds.json"))# Use a Channelyoutube_loader_channel = GoogleApiYoutubeLoader(    google_api_client=google_api_client,    channel_name="Reducible",    captions_language="en",)# Use Youtube Idsyoutube_loader_ids = GoogleApiYoutubeLoader(    google_api_client=google_api_client, video_ids=["TrdevFK_am4"], add_video_info=True)# returns a list of Documentsyoutube_loader_channel.load()