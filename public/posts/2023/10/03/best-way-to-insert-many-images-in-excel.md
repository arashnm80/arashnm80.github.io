---
layout: post
title:  "Best way to insert many images in excel"
date:   2023-10-03
categories: posts
---
If you've ever tried to insert multiple images in an excel file you know that excel's default method isn't very practical. Instead I present my vba method so you'll be able to add as many files as you want.

## Steps
1. create a macro-enabled file with `.xlsm` extension
2. put all your images in a folder called `png` beside the main excel file
3. create a module and write this vba code in it:
```
Sub open_hyperlink()
    extension = "png"

    folder = extension
    Path = ThisWorkbook.Path & "\" & folder & "\" & ActiveCell.Value & "." & extension
    If Dir(Path) <> "" Then
        ActiveWorkbook.FollowHyperlink (Path)
    End If
End Sub
```
4. you can set a keyboard shortcut to make it easier e.g. `ctrl + h`

You can do the same thing with any format that you want, the only needed thing is to use your desired format instead of `png` in the above steps.

## video guide in youtube
### English
<iframe width="560" height="315" src="https://www.youtube.com/embed/W8qwcFdJG10?si=Kq8qwwrUJGqFrGhd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Persian
<iframe width="560" height="315" src="https://www.youtube.com/embed/mEYojInQNCc?si=2oejIUy_xjtrdtEY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
