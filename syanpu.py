# リスト
# ----------------------------------
shampoos = ({
    #シャンプー名           ：メーカー
    ("ヒマワリ", "himawari"): "クラシエ",
    "いち髪"                : "クラシエ",
    "アジエンス"            : "花王",
    ("ラックス", "lux")     : "ユニリーバ", 
    "メリット"              : "花王"
    })

temp_mes = ["ちなみにお使いの", "のメーカーは", "です。"]
l = shampoos["ラックス", "lux"]
h = shampoos["ヒマワリ", "himawari"]

input_kinds = input("使っているシャンプーの種類を教えてください。：")
print("あなたの使っているシャンプーは" + input_kinds + "なんですね。")
# input_kindsがシャンプーの種類を保存している

# --------メーカー解析開始--------
# ヒマワリの場合
if input_kinds == "ヒマワリ":
    print(temp_mes[0] + input_kinds + temp_mes[1] + h + temp_mes[2])
elif input_kinds == "himawari":
    print(temp_mes[0] + input_kinds + temp_mes[1] + h + temp_mes[2])

# いち髪の場合
elif input_kinds == "いち髪":
    print(temp_mes[0] + input_kinds + temp_mes[1] + shampoos["いち髪"] + temp_mes[2])

# アジエンスの場合
elif input_kinds == "アジエンス":
    print(temp_mes[0] + input_kinds + temp_mes[1] + shampoos["アジエンス"] + temp_mes[2])

# ラックスの場合
elif input_kinds == "ラックス":
    print(temp_mes[0] + input_kinds + temp_mes[1] + l + temp_mes[2])
elif input_kinds == "lux":
    print(temp_mes[0] + input_kinds + temp_mes[1] + l + temp_mes[2])

# メリットの場合
elif input_kinds == "メリット":
    print(temp_mes[0] + input_kinds + temp_mes[1] + shampoos["メリット"] + temp_mes[2])
# 対応していない場合
else:
    print("あなたの入力したシャンプーはこのメーカー検索にまだ対応していません・・・")


# 以下覚書---------------------------------------------
    # dictionary（以下dic）を使って作った。行数が多すぎてエラーが出た。
    # 行数が多いエラーは動かないわけではないが見にくいようだ。
    # ｛｝の先頭と最後に（）を付ければ、（）内が文章として認識してくれる。
    # 下の行はインデントが必要である。
    # if文とelif文、else文のprintはインデント下げないといけないのを忘れていた。
    # elseで条件を締めくくった後は、改行したら終わりの合図になる。

    # dicで複数キーが欲しい時は、
    # X = {(キーA, キーB) : 値}
    # y = x[キーA, キーB]
    # print(y)＝値
    # とする。