from nose.tools import *
from publish2wp import publisher


def test_file():
    username = 'testuser'
    password = 'testuser'
    site = 'https://publish2wptesting.wordpress.com/'
    state = 'draft'
    testpublisher = publisher.publish2wp(username, password, site, state)
    filestatus = testpublisher.getfile('tests/wrongfile.txt')
    assert_equal(filestatus, 'Invalid Syntax for input file')
    filestatus = testpublisher.getfile('tests/wrongfile2.txt')
    assert_equal(filestatus, 'Invalid Syntax for input file')
    filestatus = testpublisher.getfile('tests/nosuchfile.txt')
    assert_equal(filestatus, 'File not found')
    filestatus = testpublisher.getfile('tests/correctfile.txt')
    assert_equal(filestatus, 0)


def test_site():
    username = 'publish2wptest'
    password = 'publish2wptesting'
    site = 'https://publish2wptesting.wordpresss.com/'
    state = 'draft'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(
        teststatus, "Can't connect. Check URL and protocol (http vs https)")
    site = 'http://publish2wptesting.wordpress.com/'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(
        teststatus, "Can't connect. Check URL and protocol (http vs https)")
    site = 'https://publish2wptesting.wordpress.com/'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(teststatus, 0)


def test_credential():
    username = 'publish2wptest'
    password = 'asdf'
    site = 'https://publish2wptesting.wordpress.com/'
    state = 'draft'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(teststatus, 'Wrong Credentials')
    username = 'qewr'
    password = 'asdf'
    site = 'https://publish2wptesting.wordpress.com/'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(teststatus, 'Wrong Credentials')
    username = 'publish2wptest'
    password = 'publish2wptesting'
    site = 'https://publish2wptesting.wordpress.com/'
    testpublisher = publisher.publish2wp(username, password, site, state)
    teststatus = testpublisher.connect()
    assert_equal(teststatus, 0)
