import requests

url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
request=requests.get(url)

if request.status_code==200:
    response=request.json()
    natija=f" Sana :{response[0]['Date']}\n\n"
    for r in response:
        if r["Ccy"] in ["USD","EUR","RUB","GBP"]:
            natija+=f"1 {r['CcyNm_UZ']} ~ {r['Rate']} so'm \n"
    print(natija)



else:
    print("Xatolik")



