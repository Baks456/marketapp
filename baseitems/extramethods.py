
rus_list = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',]
end_list = ['a','b','v','g','d','e','yo','zh','z','i','j','k','l','m','n','o','p','r','s','t','u','f','x','cz','ch','sh','shh','','w','','e','yu','ya',]
dict_list = dict(zip(rus_list,end_list))

def slug_from_rus_to_eng(st: str) -> str:
    x = st.lower().strip()
    if len(x) == 0:
        raise ValueError('Недостаточно символов в строке для преобразования в слаг')
    res = ''
    for letter in x:
        if letter in dict_list:
            res += dict_list[letter]
        else:
            res += letter
    return res



