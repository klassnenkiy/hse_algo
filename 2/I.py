input_string = input()
current_xml = input_string

stack = []
tags = current_xml.replace('<', ' ').replace('>', ' ').split()
open_error_tag = None

for tag in tags:
    if tag.isalpha():
        stack.append(tag)
    elif tag.startswith('/') and tag[1:] in stack:
        stack.remove(tag[1:])
    else:
        open_error_tag = tag
        break

if len(stack) != 0 or open_error_tag is not None:
    replace_candidates = [ch for elem in (stack if stack else [open_error_tag]) for ch in elem]
    replace_candidates.extend(['<', '>', '/'])

    current_xml = list(input_string)
    valid_answers = []

    for index in range(len(current_xml)):
        for replacement in '<>/qwertyuiopasdfghjklzxcvbnm':
            if current_xml[index] in set(replace_candidates):
                current_xml[index] = replacement
                modified_xml = ''.join(current_xml)

                stack_check = []
                tags_check = modified_xml.replace('<', ' ').replace('>', ' ').split()
                is_valid = True

                for tag_check in tags_check:
                    if tag_check.isalpha():
                        stack_check.append(tag_check)
                    elif tag_check.startswith('/') and tag_check[1:] in stack_check:
                        stack_check.remove(tag_check[1:])
                    else:
                        is_valid = False
                        break

                if is_valid and len(stack_check) == 0:
                    result = ''.join([f'<{tag}>' for tag in tags_check])
                    if len(result) == len(input_string):
                        valid_answers.append(result)
                else:
                    current_xml = list(input_string)

    print(max(valid_answers))
else:
    print(''.join([f'<{tag}>' for tag in tags]))
