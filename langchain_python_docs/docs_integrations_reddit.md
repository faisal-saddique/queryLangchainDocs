Reddit
======

> [Reddit](/docs/integrations/www.reddit.com) is an American social news aggregation, content rating, and discussion website.

Installation and Setup[​](#installation-and-setup "Direct link to Installation and Setup")
------------------------------------------------------------------------------------------

First, you need to install a python package.

    pip install praw

Make a [Reddit Application](https://www.reddit.com/prefs/apps/) and initialize the loader with with your Reddit API credentials.

Document Loader[​](#document-loader "Direct link to Document Loader")
---------------------------------------------------------------------

See a [usage example](/docs/modules/data_connection/document_loaders/integrations/reddit.html).

    from langchain.document_loaders import RedditPostsLoader