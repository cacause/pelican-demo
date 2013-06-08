pelican-demo
============

CaCause is a Pelican plugin for managing blog comments. Unlike comment systems
like Disqus which carry comments from a third-party platform to the client browser,
CaCause make comments part of the static blog. We feel this approach is in line
with strong ideas which stand behind static blogs:

*    own your data, don't delegate to 3rd-party, 
*    be able to rebuild the entire blog offline.

**How it works**

Main idea is that approved comments exist on disk in Markup format and 
CaCause pluging is called during blog build to embed article pages with related
comments. You probably think "that sounds great! But how are created the
comments? How is managed the approval process?". Well, that's another chapter 
of the CaCause story which is still under development. But CaCause plugin for
Pelican is the first piece to achieve our goal. 

**Plugin usage**

A sub-directory is dedicated to store comments. Each comment is a file in REST 
or Markdown format (.rst or .md file extension). The header is used to define
comment metadata: author name, author email, published date.

Customize Pelican blog configuration defined in *pelicanconf.py*

    # register cacause plugin
    PLUGINS = ['cacause',]

    # configure cacause
    CACAUSE_DIR = "comments"
    CACAUSE_GRAVATAR = True 

Parameters: 

*   *CACAUSE_DIR* is a directory under Pelican root directory where comments are
stored in REST or Markdown format.
*   *CACAUSE_GRAVATAR* is a boolean to enable or disable Gravatar support.

**Example**

Have a look to this tiny pelican blog 

