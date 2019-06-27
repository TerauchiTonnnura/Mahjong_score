# Mahjong_score
Djangoを用いて麻雀のスコア管理をしよう．
また，これを通してGitでのバージョン管理方法に触れよう．


## 基本構想

### 点数入力画面 (saki)

#### 画面 1
東風，半荘の選択を行う．
各プレイヤの最終点数を入力する -> 1局ごと？まとめて？

#### 画面 2
入力された点数が pt に変換されて，これまでの対局の各 pt と累積の pt を表示される．
何かグラフとか出力しても良いかも．

### 管理者画面 (admin)
新しいプレイヤの追加やウマオカの設定などを行う．
詳しいことは未定．


## 発展
・ 最終的にスマホからブラウザで入力を行えるようにしたい．
・ その他諸々の拡張機能の追加


## 開発に関して

### 新しくページを追加したい
ページの実体はhtmlファイル．
1. まずはsaki/templates/saki/ の中に[ページ名].htmlファイルを作る．例としてhoge.htmlの追加をする．
2. views.py に作成したページとサーバを紐づける関数を定義する．renderは第一引数にrequestをとり，第二引数にページのhtmlのURIをとる．
```
def hoge(request): # この関数の名前をページの名前にする．引数にはrequestをいれる．
		return render(request, 'saki/hoge.html')
```
3. Django のプロジェクトが作成したページを認識できるように，saki/urls.py のurlpatternsに以下を追加
例えばindexのページを
```
urlpatterns = [
		path('', views.index, name='index'),
        path('hoge', views.hoge, name='hoge') # ここに追加した
]
```
と変更する．
path に指定した'hoge'はlocalhost:8000/saki/hoge でサイトにアクセスできるようにしますよという意味．
views.hoge はviewsに追加したhogeという関数とつながっているという意味．
name はとりあえずページ名と同じものをいれておけばOK

ここまででひとまずページへアクセスできることを確認しておく．manage.py のある階層で以下を実行．
```
$ python manage.py runserver
```
表示されたURLにアクセス．デフォルトでは以下になる．(ページ名はurls.pyに記載した第一引数であることに注意．)
```
localhost:8000/saki/<ページ名>
```

空のページが表示されれば完成．中身を作っていきましょう．

### 入力フォームを作りたい
入力フォームとは，
Webページにおいて名前やパスワード等を記載して送信する場所のこと．
基本は html に直接記載する形で書かれているが，Django ではわざわざ書かなくても簡単にPython風に書けるものが存在する．
html で実際にどう書かれているか知るためには「html フォーム作成」等で検索してみるとよいです．

saki/forms.py にこんな感じで書く．forms.Formを継承して作成する．

```
class HogeForm(forms.Form):
		name = forms.CharField()
        age = forms.IntegerField()
        		.
        		.
        		.
```
これでフォームのひな型ができたのでこれを作ったページに埋め込めばよいです．

views.py で作成したフォームをインポート．render の第三引数でhtmlにフォームを渡す．

```
from .forms import HogeForm
def hoge(request):
    f = HogeForm()
    return render(request, 'saki/hoge.html', {'form': f})
```

あとはhtml側でフォームを展開します．hoge.htmlは以下のようになる．form.as_table以外にもいろいろな展開方法があるので試してみてください．

```
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <table>
        {{form.as_table}}
        <tr><td colspan='2'><input type="submit" value="Make"></td></tr>
    </table>
</form>
```

## モデルを作りたい，使いたい．

### モデルを作りたい
モデルはmodels.pyに記述されてます．作りたいときはほかのモデルを参考にしながら作ってください．DBにたまっていく部分です．
モデルを作ったら manage.py と同階層に入って以下を実行．(変更がmigrationsにたまります)
```
$ python manage.py makemigrations saki
```
次に実際のDBに反映させるために以下を実行．
```
$ python manage.py migrate
```
作成したモデルがちゃんと運用できるかどうかはadminで適当にインスタンスを作るか,tests.pyにテストコードを記載する．(できればこっちのほうがいい)
スーパーユーザーの作り方は以下の通り．
```
$ python manage.py createsuperuser
```
テストの実行は以下の通り．
```
$ python manage.py test
```

### モデルを使いたい
使いたいときは (基本的にviews.pyの中)まず定義したモデルをsaki/views.pyにインポートしてください．
ここではHogeモデルを以下のように作っているとします．

```
class Hoge(models.Model):
    name = models.CharField(max_length=50)
    age= models.IntegerField()
```

```
from .models import Hoge
```

#### データベースから全部持ってくる
```
all = Hoge.objects.all()
```
#### 条件に合うものだけ持ってくる
```
filter = Hoge.objects.filter(name='suzuki')  # 名前がsuzukiのデータをもってくる
```
#### 新規作成, 保存
```
new = Hoge(name='tanaka', age=32)
new.save()  # この一文で実際のデータベースに反映される．
```
#### 更新
```
update = Hoge.objects.get(id=3)  # idが3のデータを取得
update.age = 33   # age を更新
update.save()  # 反映 (.delete()で削除もできる)
```
こんな感じで使ってみてください．


## html を動的に動かしたい (JavaScript がかきたい)
JavaScriptはhtmlを操作するためのスクリプトです．
例えば．．．
1. 画面に表示している文字，数字を変えたい．
2. 画面を表示した瞬間にしたい処理がある．
3. 電光掲示板的なものを作りたい．
...

等，やれることは山のようにあります．非同期処理とかもできます．
html ファイルと js ファイルは分けて書きましょう．saki/static/js/ に.jsファイルを追加．(ここではhoge.jsを追加するとする)

html から作成したjsファイルをインポートしたいので，html のヘッダに以下を追加
```
<script type="text/javascript" src="{% static 'saki/js/hoge.js' %}"></script>
```
この一文でhtml内でhoge.jsに記述した関数が使えるようになります．
JavaScript(JQuery) の書き方はきりがないので省略．適宜調べてください．

## bootstrapについて
### bootstrap とは？
HTML を簡単におしゃれに書くためのフレークワーク．
利点としては...
1. レスポンシブデザインに対応できる
	- スマホやPC等，画面サイズに応じた表示ができます．
2. おしゃれなコンポーネント
	- bootstrapであらかじめ用意されてるクラスを指定することでおしゃれなパーツが使える．

などが挙げられます．

例えば，bootstrapで用意されてるボタンを使うには...

```
<a href="#" class="btn btn-success">BootStrapのボタン</a>
```

のように書けばいい感じのボタンができる．

bootstrapの強みはなんといっても2番のレスポンシブデザインが簡単にかけるということにあります．
bootstrapでは画面を12分割したグリッド単位で考えるうんぬんの話が下に書いているので読むといいと思います．非常に重要．

[Bootstrapのグリッドシステムの使い方を初心者に向けておさらいする](http://websae.net/twitter-bootstrap-grid-system-21060224/)

グリッドシステムの基本的な使い方：
1. `<div class="container">`で囲む
2. 上記のcontainerクラスの中で`<div class="row">`で一行を定義する
3. 上記のrowクラスの中で`<div class="col-{prefix}-{列数(1〜12)}">`で何分割するかを定義する

以下，PC用画面(lg)で2分割するサンプル
```
<div class="container">
    <h1>PC用画面(lg)のときは2分割する</h1>
    <div class="row">
        <div class="col-lg-6 skyblue">
            1(6/12)
        </div>
        <div class="col-lg-6 pink">
            2(6/12)
        </div>
    </div>
</div>
```


## bootstrapの本体は？
CSSファイルとJSファイルです．
今回のプロジェクトにおいてはstatic/ 以下にあるcssとjsに入っている
bootstrap.cssとかbootstrap.js
のようなファイルです．

## bootstrapを自分のページで使いたい．
bootstrapでは，大本となるデザインを記したhtmlファイルを作ってbase.htmlのような形でおいておくのが一般的です．
本プロジェクトではtemplates/ においてます．base.htmlを呼び出すには，自分のページの先頭行で

```
{% extends "base.html" %}
```
を書き，さらに

```
{% block contents %}

{% endblock %}
```
を作り，この中に自分の作りたいページを埋め込んでいきましょう．また，スクリプトを埋め込みたい場合は
```
{% block scripts %}

{% endblock %}
```
の中に書いてください．この辺はすでにできてるページとかを参考にしながらやってみてください．ちなみに見たらわかりますがbase.htmlでさきほどのcssとかjsファイルを読み込んでいます．これのおかげでbase.htmlをextendした自作のページでもbootstrapが使えるということです．

基本的な概要と使い方は以上で終わりです．
適当に調べながらやっていきましょう．
