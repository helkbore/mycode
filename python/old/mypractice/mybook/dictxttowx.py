import re
def main():
    source_path = u"D:\\词典\\11.txt"
    final_path = u"D:\\词典\\word-list.js"

    # 读取字典
    f = open(source_path, encoding='utf-8')
    line = f.readline()

    i = 0
    pattern_content = re.compile(r'\d{1,2}, \w+\s?\w+')
    # pattern_pron = re.compile(r'\s\s\[[\S*|\S?\s\S?]?')

    words = []
    word = {}
    while line:

        i = i + 1;
        if (i % 2 == 0):
            # print(re.search(pattern_content, line))
            word['definition'] = line.replace('\n', '').strip()
            words.append(word)
            word = {}
            # print(word)

        else:
            word['content'] = re.sub(r'\d{1,2},\s' ,'', re.search(pattern_content, line).group(0)).strip()
            # word['pron'] = (re.search(r'\s\s\[(\S*|\S+\s\S+)]', line).group(0).strip()) == '[]' ? [] : (re.search(r'\s\s\[(\S*|\S+\s\S+)]', line).group(0).strip())
            pron = re.search(r'\s\s\[(\S*|\S+\s\S+)]', line).group(0).strip()
            word['pron'] = pron if pron != '[]' else ''
            # print(word)
        line = f.readline()
        # exit()

    # print(result)

    start = "var word_list = "
    end = "\n\nmodule.exports = {\n\twordList: word_list\n}"
    result = start + str(words) + end
    print(result)

    with open(final_path, 'w', encoding='utf-8') as file:
        file.write(result)

    # text = f.read()


    # print(text)

    # 单词

    # content = pattern_content.findall(text)
    # print(content)
    # print(len(content))

    # 音标

    # pron = pattern_pron.findall(text)

    # 定义
    # pattern_definition = re.compile(r'\n\S+\n')
    # definition = pattern_definition.findall(text)
    # print(definition)
    # print(len(definition))

    # print(pron)
    # print(len(pron))

    # for i in range(0, 53):
    #     print(result[i])
    #     print(result2[i])

    # str = u'[proˈsɛs;(for n,)prɑsɛs]'
    # print(str)
    #
    # pattern = re.compile(r'\[[\s\S]*]')
    # print(pattern.findall(str))


    # ttest = []
    # test = {}
    # test['a'] = 'aabbcc'
    # test['b'] = 'eeffgg'
    # ttest.append(test)
    # ttest.append(test)
    # print("begin---" + str(ttest) + "----end")
main()