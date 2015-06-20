#! /usr/bin/python
#
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

import wordpress_xmlrpc
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import ssl


class publish2wp:

    def getpostdetails(self, postfile):
        '''Get details of the post to be published'''
        filecontent = postfile.readlines()
        filecontent = map(str.strip, filecontent)
        postoptions = {}
        option = ''
        value = ''
        for line in filecontent:
            if ':' in line:
                option = line.split(':')[0]
                value = line.split(':')[1]
            else:
                value = value + '\n' + line
            postoptions[option] = value
        return postoptions

    def __init__(self, username, password, site, state):
        self.username = username
        self.password = password
        self.site = site
        self.state = state
        if self.site[-1] != '/':
            self.site = self.site + '/'
        self.site = self.site + 'xmlrpc.php'
        if 'http' not in self.site:
            self.site = 'http://' + self.site

    def getfile(self, filename):
        try:
            self.postfile = open(filename)
        except:
            return "File not found"
        postoptions = self.getpostdetails(self.postfile)
        self.terms_names = {}
        try:
            if 'title' not in postoptions or 'content' not in postoptions:
                return 'Invalid Syntax for input file'
            for option in postoptions:
                if option == 'tags':
                    tags = postoptions[option].split(',')
                    tags = map(str.strip, tags)
                    self.terms_names['post_tag'] = tags
                elif option == 'categories':
                    categories = postoptions[option].split(',')
                    categories = map(str.strip, categories)
                    self.terms_names['category'] = categories
                else:
                    setattr(self, option, postoptions[option])
        except:
            return 'Invalid Syntax for input file'
        return 0

    def connect(self):
        try:
            self.client = Client(self.site, self.username, self.password)
            self.clientposts = self.client.call(posts.GetPosts())
        except wordpress_xmlrpc.exceptions.InvalidCredentialsError:
            return "Wrong Credentials"
        except (wordpress_xmlrpc.exceptions.ServerConnectionError,
                ssl.CertificateError):
            return "Can't connect. Check URL and protocol (http vs https)"
        except IOError:
            return "Invalid URL"
        return 0

    def publishit(self):
        self.post = WordPressPost()
        self.post.title = self.title
        self.post.content = self.content
        self.post.terms_names = self.terms_names
        self.post.id = self.client.call(posts.NewPost(self.post))
        self.post.post_status = self.state
        self.result = self.client.call(posts.EditPost(self.post.id, self.post))
        if self.result is True:
            return 1
