"""
CaCause plugin for Pelican
==========================

This plugin allows you to define a LICENSE setting and adds the contents of that
license variable to the article's context, making that variable available to use
from within your theme's templates.
"""

import sys
import os
import hashlib
from pelican import signals
from pelican import readers


cacause_context = {}


def get_article_id(source_filename):
    m = hashlib.md5()
    m.update(source_filename)
    return m.hexdigest()


def read_comment(comment_file, header=True):

    content = None
    if comment_file[-4:] == '.rst':
        reader = readers.RstReader({})
        body, metadata = reader.read(comment_file)
        content = metadata if header else body
    elif comment_file[-3:] == '.md':
        reader = readers.MarkdownReader({})
        body, metadata = reader.read(comment_file)
        content = metadata if header else body
    # return header or body
    return content


def read_comments(comment_dir):
    cacause_context['comments'] = {}
    comment_files = os.listdir(comment_dir)
    for file in comment_files:
        absolute_comment_file = '/'.join([comment_dir, file])
        cfg = read_comment(absolute_comment_file)
        cfg['comment'] = absolute_comment_file
        article_id = cfg['article']
        if article_id:
            if not article_id in cacause_context['comments']:
                cacause_context['comments'][article_id] = []
            cacause_context['comments'][article_id].append(cfg)


def build_comment_context(generator):

    if not 'comments' in cacause_context:
        if not 'CACAUSE_DIR' in generator.settings.keys():
            print "cacause: can't find CACAUSE_DIR in pelicanconf.py"
            sys.exit(1)
        cacause_dir = generator.settings['CACAUSE_DIR']
        read_comments(cacause_dir)
    # DEBUG
    print "build cacause context"
    print cacause_context


def enhance_article(sender):

    # DEBUG
    print "enhance article %s : %s" % \
        (sender.get_relative_source_path(), sender.metadata)
    article_id = get_article_id(sender.get_relative_source_path())
    if article_id in cacause_context['comments']:
        posts = []
        for post in cacause_context['comments'][article_id]:
            filename = post['comment']
            body = read_comment(filename, False)
            post['body'] = body
            posts.append(post)
        # DEBUG
        print "Related comments: %d" % len(posts)
        print posts
        sender.cacause_comment = posts


def register():
    signals.initialized.connect(build_comment_context)
    signals.content_object_init.connect(enhance_article)
