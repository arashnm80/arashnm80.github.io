# My Personal Website

## to-do
- ~~post excerpts~~✅
- ~~how to remove .html from end of links~~✅
- test this for youtube: https://gist.github.com/joelverhagen/1805814
- to read: https://blog.briandrupieski.com/generate-anchors-in-jekyll-blog-post

## document
- example usage of `excerpt_separator: <!--more-->` exists in `2023-10-01-ton-october-challenges`

## how to use in github codespaces
- install: `bundle install`
- run: `bundle exec jekyll serve`

```
node quotes.js; bundle install; bundle exec jekyll serve;
```

## map jekyll port of vps to my pc (got permission denied error)
```
ssh -L 4000:localhost:4000 root@5.161.154.70
```

## add, commit, push
```
node quotes.js; git add .; git commit -am "edit"; git push;
```

## combination

```
node quotes.js; git add .; git commit -am "edit"; git push; bundle install; bundle exec jekyll serve;
```

## good sources:
- jekyll table of contents: https://www.seanbuscay.com/blog/jekyll-toc-markdown/
- detilas tag (I didn't need to use _includes/details.html file): https://spinningnumbers.org/a/details.html
- pagination: https://laura.rochaprado.com/done/web/development/2019/04/02/jekyll-github-page-pagination.html

## to read later:
- https://jekyll-themes.com/category/bootstrap

## to delegate later:
- make all pages lose characters like no-time-for-caution to emphasize speed of losing time.