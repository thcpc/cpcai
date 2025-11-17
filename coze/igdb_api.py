import requests

url = "https://www.igdb.com/games/claire-a-la-mode"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)
# for cookie in response.headers.get("Set-Cookie", "").split(";"):
#     print(cookie.strip())
cf_bm = response.headers.get("Set-Cookie", "").split(";")[0]
print(cf_bm)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "content-type": "application/json",
    "accept": "*/*",
    "Referer": "https://www.igdb.com/games/claire-a-la-mode",
    "origin": "https://www.igdb.com",
    "priority": "u=1,i",
    "baggage": "sentry-environment=production,sentry-public_key=180003e51d2e7e88f536de2391179869,sentry-trace_id=d87fe97258494f9a97d0d0b4351e95e5,sentry-org_id=278969,sentry-sampled=true,sentry-sample_rand=0.09096887755753602,sentry-sample_rate=1",
    "cookie":"country=156; force-login=1; __cf_bm=BEYQcd9T2sgsHDaEDQ.jy4Kus7Bi8kgu4vmDHJ4l57s-1763366295-1.0.1.1-d7dMEDM0FqwNICI3NeBNRuzGAw9_PlsNQiIlTVlnRajtWBr3TS5jHi3jGwgRPrKagUU98sDFoblD3Wl7Bz3RFogASn_zoWfVjFmnDvS_PjU; force-login=0; cf_clearance=Jst4S9CWvg2ACYbSbiQJ8a2huZNkLRZLU41UdZ.hjL4-1763366296-1.2.1.1-v9xU2XZ4lPhYgtVQt.jEtPG6bcF9zaznq1FvULUKVUh1SaJKXnr0ejyxgbORIpuSQBmoF3lk7pjTD_t8Md.N6o8O0B9VVnWEdy6XZvTz2Hrdq0_PbkGQ5To94zrs4pc5kXQpJWMdBvPIssXg9oCsQX3Iiwj1DkbWEnNxxkSIFYq0WEL6ayY84uKo1kV9mB8JljiImnFMUeHoiSwjB_LJ4mirxiIqJ1WJpbpX1RP6YrE; mp_c9b6d5ed3e9e4ad20b3fac745421a240_mixpanel=%7B%22distinct_id%22%3A%22%24device%3Aad2e6792-837b-4c43-a8a0-1d53fd88e186%22%2C%22%24device_id%22%3A%22ad2e6792-837b-4c43-a8a0-1d53fd88e186%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%7D; OptanonConsent=isIABGlobal=false&datestamp=Mon+Nov+17+2025+15%3A58%3A53+GMT%2B0800+(China+Standard+Time)&version=202210.1.0&consentId=842c5f6b-031c-4975-82d4-29ac5e67fe0a&interactionCount=1&landingPath=NotLandingPage&groups=BG41%3A1%2CC0001%3A1%2CC0003%3A1%2CC0002%3A0%2CBG42%3A0%2CC0004%3A0&hosts=H24%3A0%2CH10%3A0&genVendors=&AwaitingReconsent=false; csrf=y-P784w7MHPszRdIcnxWzxFxglmMt3sge7CszM92QLqnidFeTCSwvv3_-j2-0psr8o7bGtFD7zttT75pEhf4og; _server_session=ZDU8klC%2B6n2wCvyUTianEwo9YTnCLidRoIzxdb0IOIG7oeK8CsTGbyVNM6mEsqB61Q37CrlSzyTMTXNN6Qymn4rNmS2%2FdYpgOn5%2FrAbaMX6OZdhTNEBq7dvKoxUeI9s%2FM5NJycmQwMYtG2Kq1iWLp5%2FCnsERezqb5nYGTj96nWqz%2BsrormofZItzJfBeNmxnXU6qprWNI%2BrFs%2FqvAp7Sk9jFQttyHRL7Rm43SinR7VZ48Ocl2OufOFAcyWYyiQNWFhS9PL5mWm50tzDB4yBaiU4IDM05RXVTW1BiaANQfkUmdO1jE00CTMM%2FwrizlKfH1G8aCbIBrIun9tStrZOTPNQD3cMl8FkOK90FGTJL0QH5--FSyVJpIYrWePW0gQ--3TnLLGCQ2ra4MeALHZ%2FcrA%3D%3D"
}
url = "https://www.igdb.com/gql"
data = {"operationName": "GetGamePageMediaData", "variables": {"gameSlug": "claire-a-la-mode"},
        "query": "query GetGamePageMediaData($gameSlug: String!) {\n  game(input: {slug: $gameSlug}) {\n    id\n    slug\n    name\n    originalCover {\n      mediaSrc(imageType: \"cover_big\")\n      __typename\n    }\n    localizations {\n      id\n      name\n      cover {\n        mediaSrc(imageType: \"cover_big\")\n        __typename\n      }\n      region {\n        name\n        __typename\n      }\n      __typename\n    }\n    screenshots {\n      id\n      subtitle\n      imageHeight\n      imageWidth\n      mediaSrc(imageType: \"720p\")\n      __typename\n    }\n    logoArtworks {\n      id\n      subtitle\n      imageHeight\n      imageWidth\n      mediaSrc(imageType: \"720p\")\n      __typename\n    }\n    conceptArtworks {\n      id\n      subtitle\n      imageHeight\n      imageWidth\n      mediaSrc(imageType: \"720p\")\n      __typename\n    }\n    keyArtArtworks {\n      id\n      subtitle\n      imageHeight\n      imageWidth\n      mediaSrc(imageType: \"720p\")\n      __typename\n    }\n    genericArtworks {\n      id\n      subtitle\n      imageHeight\n      imageWidth\n      mediaSrc(imageType: \"720p\")\n      __typename\n    }\n    videos {\n      id\n      videoId\n      name\n      __typename\n    }\n    __typename\n  }\n}"}

response = requests.post(url, json=data, headers=headers)
print(response)
