import codecs

def delete_html_tags(file_html, result_file = 'cleaned.txt'):
    input_text = codecs.open(file_html, 'r', 'utf-8').read()
    output_text = ''
    flag = False
    for i in input_text:
        if i == '<':
            flag = True
        elif i == '>':
            flag = False
        elif not flag:
            output_text += i

    lines = [line.strip() for line in output_text.splitlines() if line.strip()]
    output_text = '\n'.join(lines)

    file_output = codecs.open(result_file, 'w', 'utf-8')
    file_output.write(output_text)
    file_output.close()

delete_html_tags('draft.html')