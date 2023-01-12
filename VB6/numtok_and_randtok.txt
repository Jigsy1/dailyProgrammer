' Two functions I wrote in Visual Basic 6 when I was back in college (around 2003).
'
' I do not remember what for. Use at your own peril.

Public Function Numtok(Text As String, Delimeter As Integer) As Integer
    If Text <> "" And Delimeter >= 1 And Delimeter <= 255 Then
        Dim I As Integer, X As Integer
        X = 0
        For I = 1 To Len(Text)
            If Asc(Mid(Text, I, 1)) = Delimeter Then
                X = X + 1
            End If
        Next
        Numtok = X
    Else
        Numtok = 0
    End If
End Function

Public Function Randtok(Text As String, Delimeter As Integer) As String
    Randomize
    If Text <> "" And Delimeter >= 1 And Delimeter <= 255 Then
        Dim I As Integer
        I = Val(Rnd * Numtok(Text, Delimeter))
        SplitString = Split(Text, Chr(Delimeter))
        Randtok = SplitString(I)
    Else
        Randtok = ""
    End If
End Function

' EOF
