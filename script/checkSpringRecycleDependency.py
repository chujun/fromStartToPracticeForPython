# coding:utf-8

def get_file_content(file_name):
    with open(file_name) as file:
        content = file.read()
        #print(content)
        return content


if __name__ == '__main__':
    file_name = '/Users/chujun/PycharmProjects/ahs/script/data/error/dependency20200523.log'
    content = get_file_content(file_name)
    beans = []
    for string in content.split(" "):
        if (string.startswith("'") and (string.endswith("'") or string.endswith("':"))):
            beans.append(string.strip(":").lstrip("'").rstrip("'"))
    print(len(beans))
    print(beans)
    index = 1
    for bean_name in beans:
        str = ''
        for i in range(1, index):
            str += ' '
        str += '===>' + bean_name
        print(str)
        index += 1
