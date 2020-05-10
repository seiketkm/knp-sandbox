import responder
import pyknp
from marshmallow import Schema, fields

description = "knp-sandbox"
terms_of_service = "use your own risk"
contact = {
    "name": "@seiketkm",
    "url": "https://twitter.com/seiketkm",
}
license = {
    "name": "MIT",
    "url": "",
}

api = responder.API(
    title="knp-sandbox",
    version="1.0",
    openapi="3.0.2",
    docs_route='/docs',
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    license=license
    )


@api.schema("KnpRequest")
class KnpRequest(Schema):
    text = fields.Str(
        required=True,
        default="望遠鏡で泳ぐ少女を見た。",
        example="望遠鏡で泳ぐ少女を見た。"
    )


@api.schema("KnpResult")
class KnpResult(Schema):
    all = fields.Str(
        example="# S-ID:1 KNP:4.20-CF1.1 DATE:2020/05/08 SCORE:-29.47639\n* 1D <文頭><デ><助詞><体言><係:デ格><区切:0-0><格要素><連用要素><正規化代表表記:望遠/ぼうえん+鏡/きょう><主辞代表表記:鏡/きょう><主辞’代表表記:望遠/ぼうえん+鏡/きょう>\n+ 1D <文節内><係:文節内><文頭><体言><名詞項候補><先行詞候補><正規化代表表記:望遠/ぼうえん>\n望遠 ぼうえん 望遠 名詞 6 普通名詞 1 * 0 * 0 \"代表表記:望遠/ぼうえん カテゴリ:抽象物\" <代表表記:望遠/ぼうえん><カテゴリ:抽象物><正規化代表表記:望遠/ぼうえん><文頭><漢字><かな漢字><名詞相当語><自立><内容語><タグ単位始><文節始>\n+ 2D <デ><助詞><体言><係:デ格><区切:0-0><格要素><連用要素><一文字漢字><名詞項候補><先行詞候補><正規化代表表記:鏡/きょう><解析格:デ>\n鏡 きょう 鏡 名詞 6 普通名詞 1 * 0 * 0 \"代表表記:鏡/きょう カテゴリ:人工物-その他 漢字読み:音\" <代表表記:鏡/きょう><カテゴリ:人工物-その他><漢字読み:音><正規化代表表記:鏡/きょう><漢字><かな漢字><名詞相当語><自立><複合←><内容語><タグ単位始><文節主辞>\nで で で 助詞 9 格助詞 1 * 0 * 0 NIL <かな漢字><ひらがな><付属>\n* 2D <連体修飾><用言:動><係:連格><レベル:B><区切:0-5><ID:（動詞連体）><連体節><動態述語><正規化代表表記:泳ぐ/およぐ><主辞代表表記:泳ぐ/およぐ>\n+ 3D <連体修飾><用言:動><係:連格><レベル:B><区切:0-5><ID:（動詞連体）><連体節><動態述語><正規化代表表記:泳ぐ/およぐ><用言代表表記:泳ぐ/およぐ><時制-未来><格関係1:デ:鏡><格関係3:ガ:少女><格解析結果:泳ぐ/およぐ:動10:ガ/N/少女/3/0/1;ニ/U/-/-/-/-;ト/U/-/-/-/-;デ/C/鏡/1/0/1;カラ/U/-/-/-/-;マデ/U/-/-/-/-;時間/U/-/-/-/-;修飾/U/-/-/-/-;ノ/U/-/-/-/-;ガ２/U/-/-/-/-;ニツヅク/U/-/-/-/-;外の関係/U/-/-/-/->\n泳ぐ およぐ 泳ぐ 動詞 2 * 0 子音動詞ガ行 4 基本形 2 \"代表表記:泳ぐ/およぐ\" <代表表記:泳ぐ/およぐ><正規化代表表記:泳ぐ/およぐ><かな漢字><活用語><自立><内容語><タグ単位始><文節始><文節主辞>\n* 3D <SM-主体><SM-人><ヲ><助詞><体言><係:ヲ格><区切:0-0><格要素><連用要素><正規化代表表記:少女/しょうじょ><主辞代表表記:少女/しょうじょ>\n+ 4D <SM-主体><SM-人><ヲ><助詞><体言><係:ヲ格><区切:0-0><格要素><連用要素><名詞項候補><先行詞候補><正規化代表表記:少女/しょうじょ><解析連格:ガ><解析格:ヲ>\n少女 しょうじょ 少女 名詞 6 普通名詞 1 * 0 * 0 \"代表表記:少女/しょうじょ カテゴリ:人\" <代表表記:少女/しょうじょ><カテゴリ:人><正規化代表表記:少女/しょうじょ><漢字><かな漢字><名詞相当語><自立><内容語><タグ単位始><文節始><文節主辞>\nを を を 助詞 9 格助詞 1 * 0 * 0 NIL <かな漢字><ひらがな><付属>\n* -1D <文末><補文ト><時制-過去><句点><用言:動><レベル:C><区切:5-5><ID:（文末）><係:文末><提題受:30><主節><格要素><連用要素><動態述語><正規化代表表記:見る/みる><主辞代表表記:見る/みる>\n+ -1D <文末><補文ト><時制-過去><句点><用言:動><レベル:C><区切:5-5><ID:（文末）><係:文末><提題受:30><主節><格要素><連用要素><動態述語><正規化代表表記:見る/みる><用言代表表記:見る/みる><主題格:一人称優位><格関係3:ヲ:少女><格解析結果:見る/みる:動5:ガ/U/-/-/-/-;ヲ/C/少女/3/0/1;ニ/U/-/-/-/-;ト/U/-/-/-/-;デ/U/-/-/-/-;カラ/U/-/-/-/-;ヨリ/U/-/-/-/-;マデ/U/-/-/-/-;時間/U/-/-/-/-;外の関係/U/-/-/-/-;修飾/U/-/-/-/-;ノ/U/-/-/-/-;ヲツウジル/U/-/-/-/-;トスル/U/-/-/-/-;ニムケル/U/-/-/-/->\n見た みた 見る 動詞 2 * 0 母音動詞 1 タ形 10 \"代表表記:見る/みる 自他動詞:自:見える/みえる 補文ト\" <代表表記:見る/みる><自他動詞:自:見える/みえる><補文ト><正規化代表表記:見る/みる><表現文末><かな漢字><活用語><自立><内容語><タグ単位始><文節始><文節主辞>\n。 。 。 特殊 1 句点 1 * 0 * 0 NIL <文末><英記号><記号><付属>\nEOS\n",
    )
    tree = fields.Str(
        example="'望遠n鏡nでp┐\u3000\u3000\n        泳ぐv┐\u3000\n       少女nをp┐\n            見たv\n'"
    )


@api.route("/")
async def toppage(req, resp):
    resp.html = api.template("page.html")
    
@api.route("/knp")
class knp:
    """A knp endpoint.
    ---
    post:
        description: analysis japanese text by KNP with jumanpp_v2_rc3
        requestBody: # リクエストボディ
            description: 解析対象テキスト
            content:
                application/json:
                    schema: 
                        $ref: '#/components/schemas/KnpRequest'
        responses:
            200:
                description: knp result
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/KnpResult'
                        example:
                            summary: "all"
                            value: {"all": "knp -tab output", "tree":"knp tree output"}
    """
    def __init__(self):
        self.knp = pyknp.KNP()

    async def on_post(self, req, resp):
        data = await req.media()
        result = self.knp.parse(data["text"])
        resp.media = {
            "tree": result.sprint_tree(),
            "all": result.spec()
        }

    async def on_delete(self, req, resp):
        self.knp = pyknp.KNP()

if __name__ == '__main__':
    api.run()
