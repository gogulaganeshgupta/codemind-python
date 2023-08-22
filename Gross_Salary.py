bs = int(input())
if bs<=10000:
    da=(bs*80)/100
    hra=(bs*20)/100
    gs=bs+da+hra
    print(f"{gs:.2f}")
elif bs<=20000:
    da=(bs*90)/100
    hra=(bs*25)/100
    gs=bs+da+hra
    print(f"{gs:.2f}")
elif bs>20000:
    da=(bs*95)/100
    hra=(bs*30)/100
    gs=bs+da+hra
    print(f"{gs:.2f}")
    
    