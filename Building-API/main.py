from flask import Flask
from flask_restful import Resource ,Api
import random

data = [
 " 日 (nichi, jitsu) day, sun",
 " 一 (ichi, hito) one",
 " 国 (koku, kuni) country",
 " 人 (jin, hito) person",
 " 年 (nen, toshi) year",
 " 大 (dai, tai, ookii) large, big",
 " 十 (juu) ten, 10",
 " 二 (ni, futatsu) two, 2",
 " 本 (hon, moto) book, true",
 " 中 (chuu, naka) inside, center",
 " 長 (chou, nagai) long, superior",
 " 出 (shutsu, deru) exit",
 " 三 (san, mitsu) three, 3",
 " 時 (ji, toki) time, hour",
 " 行 (kou, iku) going, line",
 " 見 (ken, miru) to see, to show",
 " 月 (getsu, tsuki) month, moon",
 " 分 (bun, wakeru) part, minute",
 " 後 (go, ato) behind, later",
 " 前 (zen, mae) in front, before",
 " 生 (sei, ikiru, nama) life",
 " 五 (go, itsutsu) five, 5",
 " 間 (kan, aida) interval, space",
 " 上 (ue, kami, jou) above, up",
 " 東 (tou, higashi) east",
 " 四 (shi, yotsu) four, 4",
 " 今 (ima, kon) now",
 " 金 (kin, kane) gold",
 " 九 (kyuu, ku) nine, 9",
 " 入 (nyuu, hairu) enter",
 " 学 (gaku, manabu) study",
 " 高 (kou, takai) tall, expensive",
 " 円 (en, marui) circle, yen",
 " 子 (shi, ko) child",
 " 外 (gai, soto) outside",
 " 八 (hachi, yatsu) eight, 8",
 " 六 (roku, mutsu) six, 6",
 " 下 (ka, shita) below, down",
 " 来 (rai, kuru) come",
 " 気 (ki) spirit, air",
 " 小 (shou, chiisai) little, small",
 " 七 (shichi, nana) seven, 7",
 " 山 (san, yama) mountain",
 " 話 (wa, hanashi) tale, talk",
 " 女 (jo, onnna) woman, female",
 " 北 (hoku, kita) north",
 " 午 (go) noon",
 " 百 (hyaku) hundred",
 " 書 (sho, kaku) write",
 " 先 (sen, mazu) before",
 " 名 (mei, na) name",
 " 川 (sen, kawa) river, stream",
 " 千 (sen) thousand",
 " 水 (sui, mizu) water",
 " 半 (han) half",
 " 男 (dan, otoko) male",
 " 西 (sei, nishi) west",
 " 電 (den) electricity",
 " 校 (kou) school",
 " 語 (go, kataru) word, language",
 " 土 (do, tsuchi) ground",
 " 木 (boku, ki) tree, wood",
 " 聞 (bun, kiku) to hear/ask",
 " 食 (shoku, taberu) eat, food",
 " 車 (sha, kuruma) car",
 " 何 (nani) what",
 " 南 (nan, minami) south",
 " 万 (man) ten thousand",
 " 毎 (mai) every",
 " 白 (haku, shiroi) white",
 " 天 (ten) heavens, sky",
 " 母 (haha) mother",
 " 火 (ka, hi) fire",
 " 右 (yuu, migi) right",
 " 読 (doku, yomu) to read",
 " 友 (yuu, tomo) friend",
 " 左 (sa, hidari) left",
 " 休 (kyuu, yasumu) rest, day off",
 " 父 (chichi, tou) father",
 " 雨 (u, ame) rain"
]

kanjis = []
for i in data:
    kanji = str(i.split(" ")[1])
    kanjis.append(kanji)


app = Flask(__name__)
api = Api(app)

class EndPoint(Resource):
    def get(self):
        return{"Kanji": f"{random.choice(kanjis)}",
               "Api": "Krooz"}
    
api.add_resource(EndPoint, '/rand')


if __name__ == "__main__":
    app.run(debug=True)
