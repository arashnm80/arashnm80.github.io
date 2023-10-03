---
layout: post
title:  "Best way to insert many images in excel"
date:   2023-10-03
categories: posts
---
## Steps
1. create a macro-enabled file with `.xlsm` extension
2. create a module and write this vba code in it:
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
3. optional: you can set a keyboard shortcut for it

## video guide in youtube
- English:
- Persian: [https://youtu.be/mEYojInQNCc](https://youtu.be/mEYojInQNCc)