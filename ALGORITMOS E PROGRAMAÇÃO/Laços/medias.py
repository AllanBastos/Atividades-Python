media1 = float(input())
media2 = float(input())
media3 = float(input())
media = 0
if media1 <= 10 and media2 <=10 and media3 <= 10:


    if (media1 >= 5.0 or media2 >= 5.0 or media3 >= 5.0):
        media = 1

        if (media1 >= 5.0 and media2 >= 5.0 or media1 >= 5.0 and media3 >= 5.0 or media2 >= 5.0 and media3 >= 5.0):
            media = 2
            if(media1 >= 5.0 and media2 >= 5.0 and media3 >= 5.0):
                media = 3
    print(media)