---
layout: post
title:  "Best way to insert many images in excel"
date:   2023-10-03
categories: posts
---
vba code:
```
Sub open_png()
    Name = ActiveCell.Value
    folder = "png images"
    Path = ThisWorkbook.Path & "\" & folder & "\" & Name & ".png"
    If Dir(Path) <> "" Then
        ActiveWorkbook.FollowHyperlink (Path)
    End If
End Sub
```