import requests

s = requests.Session()

proxies = {
    'http': 'http://127.0.0.1:8889',
    'https': 'http://127.0.0.1:8889',
}

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=www,sentry-release=11.2.500-20221223.2355,sentry-public_key=d4fd99cefa4741af819754d0a79d3d82,sentry-trace_id=aa40d5da670a4fccaac9cbc197730678,sentry-sample_rate=1',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _dc_gtm_UA-25463556-1=1; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240163901; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=fOyDzF83Q3ViQTZlakxXUnVnNDBjOElvQmE4MXFXVjFQMFJKS05MbWtUZVhsJTJCWmVIaVNPclNLb28lMkZ1V055YTliSjI1cm1BeTV5OEJ6RTBwczdqbVZvbWNHWVFBMFhOdG1NM2l1NlVJSkFNWWo3Y25kb3NSJTJCT1VvZTk4NDNwdEJvbnhrVGY1NldvVHJ2N3BhOGdzd1pEd2dNbWZOSWJWUzcxdnJtblglMkJhTlE2WGhBcG9SVWU0YUFST0lObmZEcDdFalhCN3Bja29JS3E4NmRUN3A5Mk9oVXY5Q3V6MXd3NnpFJTJCcVJmZHdBNlpDT2dHRmdTck14OFZ4MndSMHdGTlc0VHJtc2k2YlJSdFZaQlRjNUx3Sm9CVmJXY1NlelIzT2d4cGFSUnlvZyUyQk9qalljRSUzRA; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _ga=GA1.2.199239929.1672240149; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240167.1672240158.1.1706404158358; _cs_s=2.5.0.1672241967550; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240176.0.0.0; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=12&tt=56423&obo=0&sh=1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598%2C1672236010746%3D8%3A0%3A42753&rl=1&ld=1672240167349&nu=https%3A%2F%2Fwww.moncler.com%2Fde-de%2Fherren%2Fmaentel-und-jacken%2Fkurze-daunenjacken%2Fmaya-kurze-daunenjacke-schwarz-H20911A5360068950999.html&cl=1672240185617"',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/herren/maentel-und-jacken/kurze-daunenjacken/maya-kurze-daunenjacke-schwarz-H20911A5360068950999.html',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'aa40d5da670a4fccaac9cbc197730678-ac543401c399dc6a-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'pid': 'H20911A5360068950999',
    'cachekill': '2022-12-28T15:09:45.624Z',
}

r = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/ProductApi-Product',
    params=params,
    headers=headers,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; lastRskxRun=1672240163901; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=fOyDzF83Q3ViQTZlakxXUnVnNDBjOElvQmE4MXFXVjFQMFJKS05MbWtUZVhsJTJCWmVIaVNPclNLb28lMkZ1V055YTliSjI1cm1BeTV5OEJ6RTBwczdqbVZvbWNHWVFBMFhOdG1NM2l1NlVJSkFNWWo3Y25kb3NSJTJCT1VvZTk4NDNwdEJvbnhrVGY1NldvVHJ2N3BhOGdzd1pEd2dNbWZOSWJWUzcxdnJtblglMkJhTlE2WGhBcG9SVWU0YUFST0lObmZEcDdFalhCN3Bja29JS3E4NmRUN3A5Mk9oVXY5Q3V6MXd3NnpFJTJCcVJmZHdBNlpDT2dHRmdTck14OFZ4MndSMHdGTlc0VHJtc2k2YlJSdFZaQlRjNUx3Sm9CVmJXY1NlelIzT2d4cGFSUnlvZyUyQk9qalljRSUzRA; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _ga=GA1.2.199239929.1672240149; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=12&tt=56423&obo=0&sh=1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598%2C1672236010746%3D8%3A0%3A42753&rl=1&ld=1672240167349&nu=https%3A%2F%2Fwww.moncler.com%2Fde-de%2Fherren%2Fmaentel-und-jacken%2Fkurze-daunenjacken%2Fmaya-kurze-daunenjacke-schwarz-H20911A5360068950999.html&cl=1672240185617"; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240186.1672240158.1.1706404158358; _cs_s=3.5.0.1672241986815; _dc_gtm_UA-25463556-1=1; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240301.0.0.0; _gat_measmerizeTracker=1; _gat_clientTracker=1',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/herren/maentel-und-jacken/kurze-daunenjacken/maya-kurze-daunenjacke-schwarz-H20911A5360068950999.html',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'pid': 'H20911A53600689509996',
    'quantity': '1',
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/Cart-AddProduct',
    headers=headers,
    data=data,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; lastRskxRun=1672240163901; cto_bundle=fOyDzF83Q3ViQTZlakxXUnVnNDBjOElvQmE4MXFXVjFQMFJKS05MbWtUZVhsJTJCWmVIaVNPclNLb28lMkZ1V055YTliSjI1cm1BeTV5OEJ6RTBwczdqbVZvbWNHWVFBMFhOdG1NM2l1NlVJSkFNWWo3Y25kb3NSJTJCT1VvZTk4NDNwdEJvbnhrVGY1NldvVHJ2N3BhOGdzd1pEd2dNbWZOSWJWUzcxdnJtblglMkJhTlE2WGhBcG9SVWU0YUFST0lObmZEcDdFalhCN3Bja29JS3E4NmRUN3A5Mk9oVXY5Q3V6MXd3NnpFJTJCcVJmZHdBNlpDT2dHRmdTck14OFZ4MndSMHdGTlc0VHJtc2k2YlJSdFZaQlRjNUx3Sm9CVmJXY1NlelIzT2d4cGFSUnlvZyUyQk9qalljRSUzRA; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _ga=GA1.2.199239929.1672240149; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=12&tt=56423&obo=0&sh=1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598%2C1672236010746%3D8%3A0%3A42753&rl=1&ld=1672240167349&nu=https%3A%2F%2Fwww.moncler.com%2Fde-de%2Fherren%2Fmaentel-und-jacken%2Fkurze-daunenjacken%2Fmaya-kurze-daunenjacke-schwarz-H20911A5360068950999.html&cl=1672240185617"; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240186.1672240158.1.1706404158358; _cs_s=3.5.0.1672241986815; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240302.0.0.0; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d',
    'referer': 'https://www.moncler.com/de-de/herren/maentel-und-jacken/kurze-daunenjacken/maya-kurze-daunenjacke-schwarz-H20911A5360068950999.html',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

r = s.get('https://www.moncler.com/de-de/checkout/', headers=headers)
print(r.url)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=www,sentry-release=11.2.500-20221223.2355,sentry-public_key=d4fd99cefa4741af819754d0a79d3d82,sentry-trace_id=21361dee387e41168f13fe6585cdf783,sentry-sample_rate=1',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; cto_bundle=fOyDzF83Q3ViQTZlakxXUnVnNDBjOElvQmE4MXFXVjFQMFJKS05MbWtUZVhsJTJCWmVIaVNPclNLb28lMkZ1V055YTliSjI1cm1BeTV5OEJ6RTBwczdqbVZvbWNHWVFBMFhOdG1NM2l1NlVJSkFNWWo3Y25kb3NSJTJCT1VvZTk4NDNwdEJvbnhrVGY1NldvVHJ2N3BhOGdzd1pEd2dNbWZOSWJWUzcxdnJtblglMkJhTlE2WGhBcG9SVWU0YUFST0lObmZEcDdFalhCN3Bja29JS3E4NmRUN3A5Mk9oVXY5Q3V6MXd3NnpFJTJCcVJmZHdBNlpDT2dHRmdTck14OFZ4MndSMHdGTlc0VHJtc2k2YlJSdFZaQlRjNUx3Sm9CVmJXY1NlelIzT2d4cGFSUnlvZyUyQk9qalljRSUzRA; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240186.1672240158.1.1706404158358; _cs_s=3.5.0.1672241986815; _dc_gtm_UA-25463556-1=1; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=12&tt=56423&obo=0&sh=1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598%2C1672236010746%3D8%3A0%3A42753&rl=1"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '21361dee387e41168f13fe6585cdf783-9f024083b661dba8-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutApi-CheckoutData',
    headers=headers,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=www,sentry-release=11.2.500-20221223.2355,sentry-public_key=d4fd99cefa4741af819754d0a79d3d82,sentry-trace_id=21361dee387e41168f13fe6585cdf783,sentry-sample_rate=1',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240186.1672240158.1.1706404158358; _cs_s=3.5.0.1672241986815; _dc_gtm_UA-25463556-1=1; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '21361dee387e41168f13fe6585cdf783-aa96f352eef7afd3-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'form': 'shipping',
}

resp = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/FormApi-GetForm',
    params=params,
    headers=headers,
)
print(resp.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240391.1672240158.1.1706404158358; _cs_s=4.5.0.1672242191783',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CSRF-Generate',
    headers=headers,
)
print(r.status_code)

csrf = r.json()["csrf"]["token"]

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240391.1672240158.1.1706404158358; _cs_s=4.5.0.1672242191783',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    resp.json()["form"]["shipmentUUID"]["dynamicHtmlName"]: '',
    resp.json()["form"]["productLineItemUUID"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["shippingMethodID"]["dynamicHtmlName"]: 'STD',
    resp.json()["form"]["shippingAddress"]["shippingAddressUseAsBillingAddress"]["dynamicHtmlName"]: 'true',
    resp.json()["form"]["shippingAddress"]["isGift"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["giftMessage"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["sendMail"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["emailGift"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["sendCopyMail"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["isAddressValidated"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["timeslotDate"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["timeslotTimeCode"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["addressId"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["firstName"]["dynamicHtmlName"]: 'Alexander',
    resp.json()["form"]["shippingAddress"]["addressFields"]["lastName"]["dynamicHtmlName"]: 'Wilisow',
    resp.json()["form"]["shippingAddress"]["addressFields"]["address1"]["dynamicHtmlName"]: 'Zum Kirchblick 1b',
    resp.json()["form"]["shippingAddress"]["addressFields"]["address2"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["city"]["dynamicHtmlName"]: 'Salzatal',
    resp.json()["form"]["shippingAddress"]["addressFields"]["postalCode"]["dynamicHtmlName"]: '06198',
    resp.json()["form"]["shippingAddress"]["addressFields"]["country"]["dynamicHtmlName"]: 'DE',
    resp.json()["form"]["shippingAddress"]["addressFields"]["title"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["phonePrefix"]["dynamicHtmlName"]: '+49',
    resp.json()["form"]["shippingAddress"]["addressFields"]["phone"]["dynamicHtmlName"]: '1752365251',
    resp.json()["form"]["shippingAddress"]["addressFields"]["preferred"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["translation"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["states"]["stateCode"]["dynamicHtmlName"]: '',
    'csrf_token': csrf,
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutShippingServices-SubmitShipping',
    headers=headers,
    data=data,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240391.1672240158.1.1706404158358; _cs_s=4.5.0.1672242191783',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'form': 'packaging',
}

res = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/FormApi-GetForm',
    params=params,
    headers=headers,
)
print(res.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672240391.0.0.0; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.1.1672240391.1672240158.1.1706404158358; _cs_s=4.5.0.1672242191783',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CSRF-Generate',
    headers=headers,
)

csrf = r.json()["csrf"]["token"]

data = {
    res.json()["form"]["packaging"]["dynamicHtmlName"]: 'standard',
    res.json()["form"]["isGift"]["dynamicHtmlName"]: '',
    res.json()["form"]["noMessage"]["dynamicHtmlName"]: '',
    res.json()["form"]["removePrice"]["dynamicHtmlName"]: '',
    res.json()["form"]["giftMessage"]["dynamicHtmlName"]: ' \n \n',
    res.json()["form"]["messageTitle"]["dynamicHtmlName"]: '',
    res.json()["form"]["messageText"]["dynamicHtmlName"]: '',
    res.json()["form"]["messageSign"]["dynamicHtmlName"]: '',
    res.json()["form"]["emailGift"]["dynamicHtmlName"]: '',
    'csrf_token': csrf,
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutApi-SubmitPackaging',
    headers=headers,
    data=data,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672241707.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242282.1672242282.1.1706404158358; _cs_s=1.5.0.1672244082279',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/Adyen-GetPaymentMethods',
    headers=headers,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672241707.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242282.1672242282.1.1706404158358; _cs_s=1.5.0.1672244082279',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CSRF-Generate',
    headers=headers,
)
print(r.status_code)

csrf = r.json()["csrf"]["token"]

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672241707.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242282.1672242282.1.1706404158358; _cs_s=1.5.0.1672244082279',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    resp.json()["form"]["shipmentUUID"]["dynamicHtmlName"]: '',
    resp.json()["form"]["productLineItemUUID"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["shippingMethodID"]["dynamicHtmlName"]: 'STD',
    resp.json()["form"]["shippingAddress"]["shippingAddressUseAsBillingAddress"]["dynamicHtmlName"]: 'true',
    resp.json()["form"]["shippingAddress"]["isGift"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["giftMessage"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["sendMail"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["emailGift"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["sendCopyMail"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["isAddressValidated"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["timeslotDate"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["timeslotTimeCode"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["addressId"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["firstName"]["dynamicHtmlName"]: 'Alexander',
    resp.json()["form"]["shippingAddress"]["addressFields"]["lastName"]["dynamicHtmlName"]: 'Wilisow',
    resp.json()["form"]["shippingAddress"]["addressFields"]["address1"]["dynamicHtmlName"]: 'Zum Kirchblick 1b',
    resp.json()["form"]["shippingAddress"]["addressFields"]["address2"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["city"]["dynamicHtmlName"]: 'Salzatal',
    resp.json()["form"]["shippingAddress"]["addressFields"]["postalCode"]["dynamicHtmlName"]: '06198',
    resp.json()["form"]["shippingAddress"]["addressFields"]["country"]["dynamicHtmlName"]: 'DE',
    resp.json()["form"]["shippingAddress"]["addressFields"]["title"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["phonePrefix"]["dynamicHtmlName"]: '+49',
    resp.json()["form"]["shippingAddress"]["addressFields"]["phone"]["dynamicHtmlName"]: '1752365251',
    resp.json()["form"]["shippingAddress"]["addressFields"]["preferred"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["translation"]["dynamicHtmlName"]: '',
    resp.json()["form"]["shippingAddress"]["addressFields"]["states"]["stateCode"]["dynamicHtmlName"]: '',
    'csrf_token': csrf,
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutShippingServices-SubmitShipping',
    headers=headers,
    data=data,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=www,sentry-release=11.2.500-20221223.2355,sentry-public_key=d4fd99cefa4741af819754d0a79d3d82,sentry-trace_id=2d9a0d91294d4143871dba4b8b8af528,sentry-sample_rate=1',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672241707.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242282.1672242282.1.1706404158358; _cs_s=1.5.0.1672244082279',
    'device': 'undefined',
    'referer': 'https://www.moncler.com/de-de/checkout/?step=payment',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '2d9a0d91294d4143871dba4b8b8af528-bfabef70a639b784-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'form': 'billing',
}

r = s.get(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/FormApi-GetForm',
    params=params,
    headers=headers,
)
print(r.status_code)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672242340.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242340.1672242282.1.1706404158358; _cs_s=2.5.0.1672244140203; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/?step=payment',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

res = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CSRF-Generate',
    headers=headers,
)
print(res.status_code)

csrf = res.json()["csrf"]["token"]

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672242340.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242340.1672242282.1.1706404158358; _cs_s=2.5.0.1672244140203; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/?step=payment',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    r.json()["form"]["shippingAddressUseAsBillingAddress"]["dynamicHtmlName"]: 'true',
    r.json()["form"]["requestTaxRefund"]["dynamicHtmlName"]: '',
    r.json()["form"]["paymentMethod"]["dynamicHtmlName"]: 'AdyenComponent',
    r.json()["form"]["subscribe"]["dynamicHtmlName"]: '',
    r.json()["form"]["invoiceFlag"]["dynamicHtmlName"]: '',
    r.json()["form"]["taxCode"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["addressId"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["firstName"]["dynamicHtmlName"]: 'Alexander',
    r.json()["form"]["addressFields"]["lastName"]["dynamicHtmlName"]: 'Wilisow',
    r.json()["form"]["addressFields"]["address1"]["dynamicHtmlName"]: 'Zum Kirchblick 1b',
    r.json()["form"]["addressFields"]["address2"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["city"]["dynamicHtmlName"]: 'Salzatal',
    r.json()["form"]["addressFields"]["postalCode"]["dynamicHtmlName"]: '06198',
    r.json()["form"]["addressFields"]["country"]["dynamicHtmlName"]: 'DE',
    r.json()["form"]["addressFields"]["title"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["phonePrefix"]["dynamicHtmlName"]: '+49',
    r.json()["form"]["creditCardFields"]["phone"]["dynamicHtmlName"]: '1752365251',
    r.json()["form"]["addressFields"]["isAddressValidated"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["preferred"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["translation"]["dynamicHtmlName"]: '',
    r.json()["form"]["addressFields"]["states"]["stateCode"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["email"]["dynamicHtmlName"]: 'alexlovesreeses@gmail.com',
    r.json()["form"]["creditCardFields"]["editNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["cardType"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["cardNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["cardOwner"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["expirationMonth"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["expirationYear"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["securityCode"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["saveCard"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["saveCardAdyen"]["dynamicHtmlName"]: '',
    r.json()["form"]["creditCardFields"]["adyenEncryptedData"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["adyenStateData"]["dynamicHtmlName"]: '{"paymentMethod":{"type":"klarna_paynow"},"clientStateDataIndicator":true}',
    r.json()["form"]["creditCardFields"]["selectedCardID"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["terminalId"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["issuer"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["dateOfBirth"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["telephoneNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["gender"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["socialSecurityNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["adyenFingerprint"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["bankAccountOwnerName"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["bankAccountNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["adyenPaymentFields"]["bankLocationId"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferBankInfoRequired"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferBankName"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferAccountName"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferBranchName"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferBranchNumber"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferAccountType"]["dynamicHtmlName"]: '',
    r.json()["form"]["billingbanktransfer"]["wiretransferAccountNumber"]["dynamicHtmlName"]: '',
    'adyenPaymentMethod': 'klarna_paynow',
    'adyenIssuerName': '',
    'brandCode': 'klarna_paynow',
    'csrf_token': csrf,
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutServices-SubmitPayment',
    headers=headers,
    data=data,
)
print(r.text)

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672242340.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242340.1672242282.1.1706404158358; _cs_s=2.5.0.1672244140203; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/?step=payment',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CSRF-Generate',
    headers=headers,
)
print(r.status_code)

csrf = r.json()["csrf"]["token"]

headers = {
    'authority': 'www.moncler.com',
    'accept': 'application/json',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'sid=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik; dwanonymous_249c920510bcbe3a8cb25bf01660cb9b=bcuNdsxdhj2zJYIa4h0TIN1L3o; dwsid=8LKEVlUU__24j9yPgrr2UBwXSeq2WYh2McXQ5otYnrsYvYt3D-ZI1i3HtREPR8WVTSYKn1PcmIgSC_Ahf7sV-A==; dw_locale=de_DE; rskxRunCookie=0; rCookie=mskf5wni4sevri2cycneblc7slwms; _cs_mk=0.38577010626448893_1672240148607; _gid=GA1.2.839717307.1672240149; __cq_dnt=0; dw_dnt=0; TC_PRIVACY_CENTER=1%2C2%2C3; _gcl_au=1.1.1794005586.1672240158; _cs_c=0; _tt_enable_cookie=1; _ttp=y-BqNtwj8jWyHnVQ_h6jLScKYa4; _pin_unauth=dWlkPVpEY3pZekpqWkdRdE56WTNOUzAwWlRnd0xUbGtNak10Wm1aa1lXWXdNR0psTnprNA; dwac_b4ce7a548292405615223d5b36=xj5QzhVnT8avY6pgmmC4siqbnXL2KjhNJik%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=bcuNdsxdhj2zJYIa4h0TIN1L3o; cquid=||; __cq_uuid=abfe8iGN1NhVMmhdgt0pjComxT; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __cq_bc=%7B%22bctd-MonclerEU%22%3A%5B%7B%22id%22%3A%22H20911A5360068950%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22H20911A5360068950999%22%7D%5D%7D; lastRskxRun=1672240390586; _ga=GA1.2.199239929.1672240149; _uetsid=309f440085b811edb90b376c162113df; _uetvid=309f433085b811ed9962cd9a3ce6875d; cto_bundle=PdCG-183Q3ViQTZlakxXUnVnNDBjOElvQmElMkYlMkJ2UHRDcWh3WjdDYyUyQk9mT2tZUkJVUG5EMzN4d1pBYTRuZDVVMFZ2V2QlMkZTZE0zc0tkYyUyQjVaYUlUMW5VMUZ0RVh3Y0x0MFRKc2VnWXlHcW5IYlF4TVFvN29JTW9pbmNaYTVsYnZFOUR5bkZuVW9hdTFDTUZkMWlvMzlqelN5Y3pzb1ZCUG5SaEYwZFE1N1BOdG8lMkZOazRxUHpUZDZlRks2cE9Gdzl5RzhxWHdGN3V0QzBMdTQ1RHBIWmNRcFA5JTJCR3ZlQyUyRlE4MXM1aTk4WnJBVkREOTl0aDJPejdlVW9rUmhnTEpxVUl4b3RJR2ZCMzlFVkdtMkhabiUyRkNxJTJGVHIlMkI0NWxFNUJvbDhuVDRtV3BxYUJ1RDRBbEUlM0Q; RT="dm=moncler.com&si=d041d3ea-9959-4d12-a75e-815a65e96f50&ss=1672232302596&sl=13&tt=58309&obo=0&sh=1672240391436%3D13%3A0%3A58309%2C1672240167349%3D12%3A0%3A56423%2C1672240152385%3D11%3A0%3A52025%2C1672236097748%3D10%3A0%3A46401%2C1672236017908%3D9%3A0%3A44598&rl=1&ld=1672240391436"; _ga_Z1W9QE10F0=GS1.1.1672239814.13.1.1672242340.0.0.0; _cs_id=5d54031e-963c-a92e-e8de-228d78638dc8.1672240158.2.1672242340.1672242282.1.1706404158358; _cs_s=2.5.0.1672244140203; kameleoonVisitorCode=_js_w4lflzv78ewvhlhz; _dc_gtm_UA-25463556-1=1',
    'device': 'undefined',
    'origin': 'https://www.moncler.com',
    'referer': 'https://www.moncler.com/de-de/checkout/?step=payment',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'csrf_token': csrf,
}

r = s.post(
    'https://www.moncler.com/on/demandware.store/Sites-MonclerEU-Site/de_DE/CheckoutServices-PlaceOrder',
    headers=headers,
    data=data,
)
print(r.text)