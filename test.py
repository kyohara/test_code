import pandas as pd
import numpy as np

def main():
    #txtファイルの読み込み
    df = pd.read_csv("input.txt")
    #数字と文字を分離する. 
    df = df.iloc[:,0].str.split(":", expand=True)
    df.columns = ["number", "word"]
    df["number"] = df["number"].astype(np.int16)
    #数字と文字がセットである行だけをピックアップし, ソートする.
    number_word_df = df.iloc[:-1,:].sort_values("number")
    #インデックスの振り直し
    number_word_df.index = range(number_word_df.shape[0])
    #ひとつの整数m
    test_number = df.iloc[-1,0]
    ans_str = ""
    #約数が存在する場合, 1つずつ連結
    for i in range(number_word_df.shape[0]):
        if int(test_number) % int(number_word_df["number"][i]) == 0:
            ans_str += number_word_df["word"][i]
    #約数が1つも存在しない場合の処理        
    if ans_str == "":
        ans_str = test_number
    #解答を出力
    print(ans_str)


if __name__ == "__main__":
    main()