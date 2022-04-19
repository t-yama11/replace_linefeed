
def replace_enter(tar_str, char_before_rep, char_after_rep):
    if not (isinstance(tar_str, str) and \
            isinstance(char_before_rep, str) and \
            isinstance(char_after_rep, str)):
        return 
    
    return tar_str.replace(char_before_rep, char_after_rep)

if __name__ == "__main__":
    # カーソルでコピーしたテキストを読み込む. 
    # テキストの改行文字を削除する.
    # 改行文字を削除したテキストを貼り付ける. 
    print(replace_enter())