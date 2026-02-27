from langchain_community.tools import YouTubeSearchTool
tool = YouTubeSearchTool()
tool.run("lex fridman,3")