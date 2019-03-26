from g2p_en import g2p


def delete_alpha_str(string, ind):
    out_str = str()
    out_str = string[0: ind] + string[ind + 1:]
    return out_str


def process_text(list_P, file_name):
    # list_not_alpha = list()
    # for ind, ele in enumerate(text):
    #     if (not ele.isalpha()) and (ele != ' '):
    #         list_not_alpha.append(ind)

    # # print(list_not_alpha)

    # cnt = 0
    # for ind in list_not_alpha:
    #     text = delete_alpha_str(text, ind - cnt)
    #     cnt = cnt + 1

    # # print(text + "######")

    # list_P = g2p(text)

    temp_word = str()
    temp_P_list = list()
    word_P_dict = dict()
    len_list_P = len(list_P)

    for ind, P in enumerate(list_P):
        # print(P)
        if P != " ":
            temp_word = temp_word + P
            temp_P_list.append(P)
        else:
            # word_list.append(str(temp_word))
            word_P_dict.update({temp_word: list(temp_P_list)})
            temp_word = str()
            temp_P_list.clear()

        if ind == len_list_P - 1:
            # word_list.append(str(temp_word))
            word_P_dict.update({temp_word: list(temp_P_list)})
            temp_word = str()
            temp_P_list.clear()

    # print(word_P_dict)
    # with open(file_name + "_dict.txt", "w") as f:
    #     for key in word_P_dict:
    #         temp_str_P = str()
    #         for P in word_P_dict[key]:
    #             temp_str_P = temp_str_P + P + " "
    #         str_write = key + "    " + temp_str_P
    #         f.write(str_write + "\n")

    with open(file_name, "w") as f:
        for word in word_P_dict:
            f.write(word + " ")

    return word_P_dict


# if __name__ == "__main__":
#     # Test
#     test_text = "I love, &&*&*^%$^&*&^$$^^&you......"
#     process_text(test_text, "out")
