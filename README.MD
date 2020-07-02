# cleg -- simple blog software

cleg is a very simple blog software. It supports markdown and RSS feed.

## Installation

* Configure CGI on your web server (I recommend nginx)
* Drop the files where you want.
* There you go.

Put markdown files in the markdowns/ directory. And they will appear in the index. Only rule to name markdown is to use iso8601 dates (YYYYMMDD) so they appear in descendent order.

rss feed is located in /rss.cgi, so put that on a news reader (e.g. newsboat) and it will work.


