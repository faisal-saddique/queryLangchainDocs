YouTubeSearchTool
=================

This notebook shows how to use a tool to search YouTube

Adapted from [https://github.com/venuv/langchain\_yt\_tools](https://github.com/venuv/langchain_yt_tools)

    #! pip install youtube_search

    from langchain.tools import YouTubeSearchTool

    tool = YouTubeSearchTool()

    tool.run("lex friedman")

        "['/watch?v=VcVfceTsD0A&pp=ygUMbGV4IGZyaWVkbWFu', '/watch?v=gPfriiHBBek&pp=ygUMbGV4IGZyaWVkbWFu']"

You can also specify the number of results that are returned

    tool.run("lex friedman,5")

        "['/watch?v=VcVfceTsD0A&pp=ygUMbGV4IGZyaWVkbWFu', '/watch?v=YVJ8gTnDC4Y&pp=ygUMbGV4IGZyaWVkbWFu', '/watch?v=Udh22kuLebg&pp=ygUMbGV4IGZyaWVkbWFu', '/watch?v=gPfriiHBBek&pp=ygUMbGV4IGZyaWVkbWFu', '/watch?v=L_Guz73e6fw&pp=ygUMbGV4IGZyaWVkbWFu']"