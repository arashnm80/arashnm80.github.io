---
layout: post
title:  "How to create line breaks in Markdown"
date:   2024-06-26
categories: posts
excerpt_separator: <!--more-->
---
In Markdown language single line breaks are ignored by default. I have a few solutions for it.
<!--more-->

if you want to insert line break these are possible options:
- writing `2 spaces` at the end of the line (it's not a tag, type regular space button on keyboard)

```
Line 1<space><space>
Line 2
```
- writing html `<br>` tag

```
Line 1<br>
Line 2
```
- creating an exra empty line

```
Line 1

Line 2
```