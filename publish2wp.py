#! /usr/bin/python
# Copyright 2015 Balasankar C <balasankarc@autistici.org>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# .
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# .
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import getpass
import wordpress_xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import os
import sys
import ssl


def getcredentials():
    '''Get credentials to authenticate with the site'''
    if 'publish2wpsite' in os.environ:
        site = os.environ['publish2wpsite']
    else:
        site = raw_input("Enter Site URL : ")
    if 'publish2wpusername' in os.environ:
        username = os.environ['publish2wpusername']
    else:
        username = raw_input("Enter Username : ")
    if 'publish2wppassword' in os.environ:
        password = os.environ['publish2wppassword']
    else:
        password = getpass.getpass(prompt="Enter Password : ")
    if site[-1] != '/':
        site = site + '/'
    site = site + 'xmlrpc.php'
    if 'http' not in site:
        site = 'http://' + site
    return site, username, password


def getpostdetails(postfile):
    '''Get details of the post to be published'''
    filecontent = postfile.readlines()
    filecontent = map(str.strip, filecontent)
    if '#POSTTITLE#' in filecontent and '#POSTBODY#' in filecontent:
        if filecontent[0] == '#POSTTITLE#':
            title = filecontent[1]
        else:
            print "Wrong syntax for input file"
            sys.exit(0)
        if filecontent[2] == '#POSTBODY#':
            content = '\n'.join(filecontent[3:])
        else:
            print "Wrong syntax for input file"
            sys.exit(0)
    return title, content

if len(sys.argv) < 2:
    print "Wrong number of arguments. Syntax is publish2wp <filename>"
    sys.exit(0)

try:
    postfile = open(sys.argv[1])
except:
    print "File not found"
    sys.exit(0)

title, content = getpostdetails(postfile)
site, username, password = getcredentials()

print "Connecting to " + site
try:
    client = Client(site, username, password)
    clientposts = client.call(posts.GetPosts())
    print "Connected. Saving post as draft"
except wordpress_xmlrpc.exceptions.InvalidCredentialsError:
    print "Wrong Credentials"
    sys.exit(0)
except (wordpress_xmlrpc.exceptions.ServerConnectionError,
        ssl.CertificateError):
    print "Can't connect to site. Check URL and protocl (http vs https)"
    sys.exit(0)
except IOError:
    print "Invalid URL"
    sys.exit(0)

post = WordPressPost()
post.title = title
post.content = content
post.id = client.call(posts.NewPost(post))
post.post_status = 'draft'
result = client.call(posts.EditPost(post.id, post))

if result is True:
    print "Saved as draft"
