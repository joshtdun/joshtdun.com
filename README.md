## Why? [![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action) [![Known Vulnerabilities](https://snyk.io/test/github/joshtdun/joshtdun.com/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/joshtdun/joshtdun.com?targetFile=requirements.txt) [![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org) [![Django Version](https://img.shields.io/badge/django-2.15-brightgreen.svg)](https://djangoproject.com)
[![Build Status](https://travis-ci.com/joshtdun/joshtdun.com.svg?branch=master)](https://travis-ci.com/joshtdun/joshtdun.com)
### My personal website joshtdun.com 
Watch or Star this repo to follow my journey or visit the
website although chances are if you're reading this the site is still
under construction so not everything has been implemented

## The General Idea

* A website to showcase my work as a student learning to program
  * That could be in the form of code I have written to fufill a 
specific function (be that a script or an app)
  * Or a blog post filled with some of the technical knowledge I 
have gained over the years that I wish I knew alot sooner.
  * A tutorial to help out some of my fellow students who aren't
quite as far along on their journey

### Parts of the Website
* Blog
* About Me
* My Resume
* Authentication so that you can comment on my Blog or 
(maybe use an App I made)
  * Obviously the comment area will support markdown
* Email backend so that you can reset your password and 
**more importantly be subscribed to my mailing list!!!!**
  * (optional but why wouldn't you wanna be notified when I have a 
new blog post?)
* Gravatar support (you never really know where that's supported 
till you add a picture and it's popping up everywhere on the web)

### The Technical Parts (for those of you who don't read code)
* Written in Python! (of course!) I'm using Django you should 
check it out
* Mobile first design ( ;-) Google )
* Served up via NGINX on a Linux Machine(running on a cloud 
provider currently using DigitalOcean to host although I'm 
typing this out on an AWS instance with cloud9)
* Bootstrap (my how far we've come! When I started making websites 
(pre HTML5 and CSS3) it was table based layouts with hand written 
CSS for each of the major browsers)