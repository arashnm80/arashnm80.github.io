---
layout: post
title:  "Best way to insert many images in excel"
date:   2023-10-03
categories: posts
---
vba code:
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