def solution(list_urls):
    new_url_list = []
    for url in list_urls:
        try:
            index_plus = url.index('+')
        except:
            index_plus = -1
        try:
            index_dog = url.index('@')
        except:
            index_dog = -1
        if index_plus == -1:
            if new_url_list.count(url) == 1:
                continue
            new_url_list.append(url)
            continue
        if index_plus > index_dog:
            if new_url_list.count(url) == 1:
                continue
            new_url_list.append(url)
            continue

        new_url = url[0:index_plus] + url[index_dog:]
        if new_url_list.count(new_url) == 1:
            continue
        new_url_list.append(new_url)
    new_urls_set = set(new_url_list)
    return len(new_url_list)
