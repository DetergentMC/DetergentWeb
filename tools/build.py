#!/usr/bin/env python3
"""ページ生成。共通のヘッダ/フッタを各ページに展開して、リポジトリ直下に HTML を書き出す。

    python tools/build.py

生成物 (index.html など) はそのままコミットする (GitHub Pages はリポジトリ直下をそのまま配信する)。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NAV = '''  <header class="nav">
    <a class="brand" href="./" aria-label="DetergentMC">
      <svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true"><rect x="2" y="2" width="28" height="28" rx="7" fill="var(--accent)"/><path d="M10 9h6.5a6.5 7 0 0 1 0 14H10z" fill="none" stroke="#0b0f14" stroke-width="3.2"/></svg>
      <span>DetergentMC</span>
    </a>
    <nav>
      <a href="./"{home}>ホーム</a>
      <a href="how.html"{how}>仕組み</a>
      <a href="products.html"{products}>Core / Engine</a>
      <a href="roadmap.html"{roadmap}>ロードマップ</a>
      <a href="versions.html"{versions}>対応バージョン</a>
      <a href="https://github.com/DetergentMC" rel="noopener">GitHub</a>
    </nav>
  </header>
'''

FOOT = '''  <footer>
    <div class="footgrid">
      <div>
        <strong>DetergentMC</strong>
        <p>外から見れば Java。中身は Rust。</p>
      </div>
      <div>
        <a href="how.html">仕組み</a> · <a href="products.html">Core / Engine</a> · <a href="roadmap.html">ロードマップ</a> · <a href="versions.html">対応バージョン</a><br>
        <a href="https://github.com/DetergentMC/DetergentCore" rel="noopener">DetergentCore</a> · <a href="https://github.com/DetergentMC/DetergentWeb" rel="noopener">このサイトのソース</a>
      </div>
    </div>
    <p class="disclaimer">© 2026 DetergentMC · DetergentMC は Mojang Studios / Microsoft の公式製品ではなく、承認も受けていません。"Minecraft" は Mojang Synergies AB の商標です。</p>
  </footer>
</body>
</html>
'''


def page(name, title, desc, body):
    active = {k: (' class="active"' if k == name else '') for k in ['home', 'how', 'products', 'roadmap', 'versions']}
    head = f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
'''
    return head + NAV.format(**active) + '  <main>\n' + body + '  </main>\n' + FOOT


pages = {}

pages['index.html'] = page('home', 'DetergentMC — Paper 互換を目指す Rust 製 Minecraft サーバー',
    'DetergentMC は Rust で書かれた高速・軽量な Minecraft Java Edition サーバー。DetergentCore はオープンソース、DetergentEngine は Paper / Sponge プラグイン互換を備えた製品版。', '''
    <section class="hero">
      <p class="eyebrow">Minecraft Java Edition · Rust · 現在 1.20.4 対応</p>
      <h1>外から見れば Java。<br>中身は Rust。</h1>
      <p class="lead">
        DetergentMC は Rust で書かれた高速・軽量な Minecraft サーバーです。<br>
        Paper と同じ <code>java -jar</code> で起動し、同じ <code>plugins/</code> にプラグインを置く。<br>
        ワールド・ネットワーク・ティックは JVM を通りません。
      </p>
      <div class="cta">
        <a class="btn primary" href="https://github.com/DetergentMC/DetergentCore" rel="noopener">DetergentCore を見る<span class="tag">OSS · Apache-2.0</span></a>
        <a class="btn" href="products.html">DetergentEngine について<span class="tag">開発中</span></a>
      </div>
      <pre class="term" aria-label="起動コマンド"><span class="prompt">$</span> java -Xmx2G -jar detergentengine.jar
<span class="dim">INFO  DetergentEngine running inside host JVM 21.0.10
INFO  DetergentCore 1.20.4 listening on 0.0.0.0:25565 (12 net threads)</span></pre>
    </section>

    <section class="section">
      <div class="grid">
        <a class="card link" href="how.html"><h3>仕組み →</h3><p>JVM をホストにして Rust のサーバー本体を同居させる構造。何が速くなり、何が変わらないか。</p></a>
        <a class="card link" href="products.html"><h3>Core と Engine →</h3><p>オープンソースの Core と、プラグイン互換・高速化を加えた有料の Engine。ライセンスと配布形態。</p></a>
        <a class="card link" href="roadmap.html"><h3>ロードマップ →</h3><p>1.20.4 の完成から、1.0〜最新までの全バージョン対応、エイプリルフール版まで。</p></a>
      </div>
    </section>

    <section class="section">
      <h2>目指すところ</h2>
      <div class="goals">
        <div class="goal"><span class="num">1</span><div><h3>Paper プラグインがそのまま動く Rust サーバー</h3><p>既存の Paper / Sponge プラグインを修正なしで持ち込める。乗り換えコストをゼロに近づける。</p></div></div>
        <div class="goal"><span class="num">2</span><div><h3>Minecraft のすべてのバージョンに対応する</h3><p>まず 1.20.4 を完成させ、その後 <strong>1.0 から最新バージョンまで</strong>を順に対応する。<a href="versions.html">対応バージョン一覧</a></p></div></div>
        <div class="goal"><span class="num">3</span><div><h3>エイプリルフール版も作る</h3><p>2.0、15w14a、20w14∞、24w14potato、25w14craftmine といった<strong>エイプリルフール版のサーバーも制作対象</strong>にする。</p></div></div>
      </div>
    </section>
''')

pages['how.html'] = page('how', '仕組み — DetergentMC', 'DetergentMC の構造。JVM をホストにして Rust 製サーバー本体を同居させる方法と、設計上の決定。', '''
    <section class="page-head">
      <h1>仕組み</h1>
      <p class="lead">Paper は JVM の中にサーバー全体が入っています。DetergentEngine では JVM は<strong>プラグインを動かすための同居人</strong>で、サーバー本体はネイティブコードです。</p>
    </section>

    <section class="section">
      <h2>プロセスの構造</h2>
      <div class="diagram">
        <div class="box">
          <h3>Paper</h3>
          <div class="stack">
            <div class="layer jvm">JVM
              <div class="layer">サーバー本体 (Java)</div>
              <div class="layer">プラグイン (Java)</div>
            </div>
          </div>
        </div>
        <div class="box highlight">
          <h3>DetergentEngine</h3>
          <div class="stack">
            <div class="layer jvm">JVM (ホスト)
              <div class="layer rust">サーバー本体 (Rust, ネイティブ)</div>
              <div class="layer">Java シム + プラグイン (Java)</div>
            </div>
          </div>
        </div>
        <div class="box">
          <h3>DetergentCore</h3>
          <div class="stack">
            <div class="layer rust">サーバー本体 (Rust, ネイティブ)<br><small>JVM なし</small></div>
          </div>
        </div>
      </div>
      <p><code>java -jar detergentengine.jar</code> を実行すると、jar 内のネイティブライブラリ (Windows / Linux / macOS 用を同梱) が展開・読み込まれ、Rust のサーバーが JVM のプロセス内で起動します。JVM は二重に起動しません。<code>-Xmx</code> はそのままプラグイン用ヒープに効きます。</p>
    </section>

    <section class="section">
      <h2>何が速くなり、何が変わらないか</h2>
      <ul class="facts">
        <li><strong>速くなるもの</strong> — チャンク生成・送信、ライティング、エンティティ/ブロックのティック、ネットワーク I/O、圧縮・暗号化。通常のサーバー負荷の大半で、すべて Rust が処理します。</li>
        <li><strong>変わらないもの</strong> — プラグインの Java コード自体。JVM 上の Java は Java のままです。</li>
        <li><strong>正直な注意点</strong> — Rust ⇄ Java の境界 (JNI) には 1 回あたりマイクロ秒オーダーのコストがあります。Java 側が購読しているイベントだけを転送し、頻出データはハンドル経由で渡す設計でこれを抑えます。</li>
        <li><strong>メモリ</strong> — JVM ヒープはプラグイン分だけ。バニラサーバー本体が JVM に載らないので Paper より小さく済みます。Core 単体なら JVM は起動しません。</li>
      </ul>
    </section>

    <section class="section">
      <h2>設計上の決定</h2>
      <div class="grid">
        <div class="card"><h3>専用スレッドのゲームループ</h3><p>20 TPS のティックは tokio に載せず専用 OS スレッドで回します。ネットワーク遅延がティック時間に影響しません。</p></div>
        <div class="card"><h3>ゼロ再エンコードのチャンク</h3><p>チャンクセクションはワイヤ形式と同じパレット + packed bits で保持し、送信時にそのままコピーします。</p></div>
        <div class="card"><h3>Bukkit と同じイベント順序</h3><p>LOWEST → MONITOR の優先度モデルを Rust 側のイベントバスで一元管理。Java 側は転送先のリスナーです。順序とキャンセル判定は Rust が持ちます。</p></div>
        <div class="card"><h3>Mojang のデータは同梱しない</h3><p>初回起動時に EULA 同意の上で公式 server.jar からデータを生成します。配布物に Mojang 由来のバイトは含まれません。</p></div>
        <div class="card"><h3>1 つの jar で全 OS</h3><p>Engine の jar には Windows x64 / Linux x64 / Linux arm64 / macOS arm64 のネイティブライブラリが同梱され、実行環境に合うものを展開します。</p></div>
        <div class="card"><h3>クリーンルーム実装</h3><p>CraftBukkit / Spigot / Paper Server のコードは参照しません。API 実装は Paper API と Sponge API (MIT) を対象にします。</p></div>
      </div>
    </section>

    <section class="section">
      <h2>初回起動の流れ</h2>
      <ol class="steps">
        <li><code>detergent.toml</code> と <code>eula.txt</code> が生成されて停止します。</li>
        <li><a href="https://aka.ms/MinecraftEULA" rel="noopener">Minecraft EULA</a> に同意するなら <code>eula.txt</code> を <code>eula=true</code> にします。</li>
        <li>再起動すると公式 server.jar をダウンロード (SHA-1 検証) し、データジェネレータで <code>data/1.20.4/</code> を生成します。<strong>この時だけ Java 17+ が必要</strong>です (Engine では常に JVM があるので意識不要)。</li>
        <li>以降の起動ではそのデータを読むだけです。</li>
      </ol>
    </section>

    <section class="section">
      <h2>よくある疑問</h2>
      <dl class="faq">
        <dt>Paper は Rust ですか?</dt><dd>いいえ、Paper は 100% Java です。Spigot → Paper → Purpur / Pufferfish / Folia の系譜はすべて JVM 上で動きます。</dd>
        <dt>jar で起動するなら速度は Java と同じでは?</dt><dd>違います。jar は皮で、サーバー本体は同じプロセス内の Rust ネイティブコードです。JVM が実行するのはプラグインと Java シムだけです。</dd>
        <dt>Rust は .rs のまま実行できないのですか?</dt><dd>Rust はコンパイル言語なので、ネイティブバイナリ (.exe / .so / .dylib) が「Rust がネイティブで動いている」状態です。Engine の jar にはそのバイナリが同梱されています。</dd>
        <dt>他の Rust 製サーバーとの違いは?</dt><dd>Pumpkin、Valence、FerrumC などはバニラ互換までで Paper プラグインは動きません。「Paper プラグインが動く Rust サーバー」が DetergentEngine の狙いです。</dd>
      </dl>
    </section>
''')

pages['products.html'] = page('products', 'Core と Engine — DetergentMC', 'オープンソースの DetergentCore と、プラグイン互換・高速化を加えた製品版 DetergentEngine の違い。', '''
    <section class="page-head">
      <h1>Core と Engine</h1>
      <p class="lead">DetergentCore は単体で完動するオープンソースのサーバー。DetergentEngine は Core を取り込み、プラグイン互換と高速化を加えた別バイナリです。</p>
    </section>

    <section class="section">
      <div class="compare">
        <table>
          <thead>
            <tr><th></th><th>DetergentCore</th><th>DetergentEngine</th></tr>
          </thead>
          <tbody>
            <tr><td>公開</td><td>オープンソース (Apache-2.0)</td><td>非公開・有料</td></tr>
            <tr><td>配布形態</td><td>OS 別ネイティブバイナリ</td><td><code>detergentengine.jar</code> (全 OS 対応)</td></tr>
            <tr><td>起動</td><td><code>./detergentcore</code></td><td><code>java -jar detergentengine.jar</code></td></tr>
            <tr><td>バニラ互換サーバー</td><td>○</td><td>○</td></tr>
            <tr><td>Rust ネイティブプラグイン</td><td>○</td><td>○</td></tr>
            <tr><td>Paper / Sponge プラグイン互換</td><td>—</td><td>○ (開発中)</td></tr>
            <tr><td>領域並列ティック</td><td>—</td><td>○ (予定)</td></tr>
            <tr><td>管理パネル・サポート</td><td>—</td><td>○ (予定)</td></tr>
            <tr><td>JVM</td><td>不要</td><td>ホストとして使用</td></tr>
            <tr><td>リポジトリ</td><td><a href="https://github.com/DetergentMC/DetergentCore" rel="noopener">DetergentMC/DetergentCore</a></td><td>非公開</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="section">
      <h2>なぜこの分け方か</h2>
      <p>「Core だけでは動かない」ようにはしていません。動かないものはコミュニティが試さず、バグ報告も来ないからです。Core はバニラ互換の完動サーバーとして公開し、Engine は<strong>プラグイン互換という最も難しく価値の大きい部分</strong>を担います。Core が単体で動くことは、Engine の品質保証にもなります (ネットワーク層やワールド処理のバグを Core のユーザーが先に踏んでくれる)。</p>
    </section>

    <section class="section">
      <h2>ライセンス方針</h2>
      <div class="grid">
        <div class="card"><h3>Core は Apache-2.0</h3><p>許諾型なので Engine (非公開) が Core にリンクできます。外部コントリビュートも受け付けます。</p></div>
        <div class="card"><h3>Engine は独自 EULA</h3><p>ソース非公開。ライセンス認証と配布条件は製品化時に公開します。</p></div>
        <div class="card"><h3>Paper API / Sponge API (MIT) を対象</h3><p>Java シムは MIT ライセンスの API に対して実装します。Spigot 固有 API は非対応です。</p></div>
        <div class="card"><h3>GPL コードは参照しない</h3><p>CraftBukkit / Spigot / Paper Server (GPLv3) のコードは参照も流用もしないクリーンルーム実装です。</p></div>
        <div class="card"><h3>Mojang のデータ・コードを配布しない</h3><p>Core も Engine も、初回起動時にユーザーの EULA 同意の上で生成します。</p></div>
        <div class="card"><h3>非公式</h3><p>Mojang / Microsoft の公式製品ではなく、承認も受けていません。製品名に "Minecraft" を含めません。</p></div>
      </div>
    </section>

    <section class="section">
      <h2>入手</h2>
      <p>DetergentCore は <a href="https://github.com/DetergentMC/DetergentCore/releases" rel="noopener">GitHub Releases</a> から。DetergentEngine の販売形態と価格は未定です。準備ができ次第このページで案内します。</p>
    </section>
''')

pages['roadmap.html'] = page('roadmap', 'ロードマップ — DetergentMC', 'DetergentMC の開発状況と今後の計画。1.20.4 の完成、Paper API 互換、1.0〜最新の全バージョン対応、エイプリルフール版。', '''
    <section class="page-head">
      <h1>ロードマップ</h1>
      <p class="lead">開発初期です。数値はヘッドレステストクライアントでの計測で、実クライアントでの検証はこれからです。</p>
    </section>

    <section class="section">
      <h2>現在の状態</h2>
      <div class="stats">
        <div><span class="num">44<small>ms</small></span><span class="label">ログイン → ワールド参加 (ローカル)</span></div>
        <div><span class="num">52<small>MB</small></span><span class="label">常駐メモリ (JVM ホスト込み)</span></div>
        <div><span class="num">1.20.4</span><span class="label">対応バージョン (protocol 765)</span></div>
      </div>
      <ul class="roadmap">
        <li class="done">Handshake / Status / Login (暗号化・圧縮) / Configuration / Play</li>
        <li class="done">フラットワールドのチャンク送信、移動、チャット、Keep Alive</li>
        <li class="done">初回起動時のバニラデータ生成 (Mojang データ非同梱)</li>
        <li class="done"><code>java -jar</code> からの起動、ホスト JVM へのブリッジ接続</li>
        <li class="done">CI: Core 4 OS バイナリ / Engine 4 ネイティブ同梱 jar</li>
        <li class="done">Java シムの同梱、Paper API の最小サブセット (Server / PluginManager / Scheduler / 権限 / イベント)</li>
        <li class="done">Paper プラグインの読み込み・有効化・イベント受信・同期/非同期タスク・broadcast (テストプラグインで確認)</li>
        <li>実クライアントでの検証</li>
        <li>Player / World API、Rust イベント → Bukkit イベント変換</li>
        <li>エンティティ同期、ブロック設置・破壊、ワールド保存</li>
      </ul>
    </section>

    <section class="section">
      <h2>今後の活動</h2>
      <div class="phases">
        <div class="phase">
          <span class="phase-no">フェーズ 1</span>
          <h3>1.20.4 を完成させる</h3>
          <p>プレイヤー同士が見える、ブロックを置ける・壊せる、ワールドが保存される。バニラとして遊べる状態。</p>
        </div>
        <div class="phase">
          <span class="phase-no">フェーズ 2</span>
          <h3>Paper プラグイン互換</h3>
          <p>軽量プラグインの <code>onEnable</code>・イベント・スケジューラまでは到達済み。次は Player / World API → 主要プラグインが動く。</p>
        </div>
        <div class="phase">
          <span class="phase-no">フェーズ 3</span>
          <h3>1.0 から最新バージョンまで、すべてに対応する</h3>
          <p>1.20.4 の次は、<strong>1.0 から最新リリースまでを順に対応</strong>します。プロトコル層をバージョン別モジュールにし、ワールドとティックの実装は共有します。対応状況は<a href="versions.html">対応バージョン</a>で公開します。</p>
        </div>
        <div class="phase">
          <span class="phase-no">フェーズ 4</span>
          <h3>エイプリルフール版も作る</h3>
          <p>2.0 (2013)、15w14a (2015)、1.RV-Pre1 (2016)、3D Shareware v1.34 (2019)、20w14∞ (2020)、22w13oneBlockAtATime (2022)、23w13a_or_b (2023)、24w14potato (2024)、25w14craftmine (2025) など、<strong>エイプリルフール版のサーバーも制作対象</strong>です。今後のエイプリルフール版も対応します。</p>
        </div>
        <div class="phase">
          <span class="phase-no">継続</span>
          <h3>高速化</h3>
          <p>領域並列ティック (Folia 的)、ホットパスイベントのハンドル化、チャンク送信のさらなる最適化。</p>
        </div>
      </div>
    </section>
''')

releases = [
    ("1.0", "2011-11"), ("1.1", "2012-01"), ("1.2.x", "2012-03"), ("1.3.x", "2012-08"), ("1.4.x", "2012-10"),
    ("1.5.x", "2013-03"), ("1.6.x", "2013-07"), ("1.7.x", "2013-10"), ("1.8.x", "2014-09"), ("1.9.x", "2016-02"),
    ("1.10.x", "2016-06"), ("1.11.x", "2016-11"), ("1.12.x", "2017-06"), ("1.13.x", "2018-07"), ("1.14.x", "2019-04"),
    ("1.15.x", "2019-12"), ("1.16.x", "2020-06"), ("1.17.x", "2021-06"), ("1.18.x", "2021-11"), ("1.19.x", "2022-06"),
    ("1.20 – 1.20.3", "2023-06"), ("1.20.4", "2023-12"), ("1.20.5 – 1.20.6", "2024-04"), ("1.21.x", "2024-06"),
    ("26.1 以降 (新番号体系)", "2026-"),
]
rows = []
for v, d in releases:
    if v == "1.20.4":
        rows.append(f'<tr><td><strong>{v}</strong></td><td>{d}</td><td><span class="badge wip">作業中</span></td><td>Login〜Play まで動作。バニラ機能を実装中</td></tr>')
    else:
        rows.append(f'<tr><td>{v}</td><td>{d}</td><td><span class="badge plan">予定</span></td><td></td></tr>')

aprils = [
    ("2.0", "2013", "「Minecraft 2.0」。ピンクのウィザー、エッチングされたガラスなど"),
    ("15w14a", "2015", "The Love and Hugs Update"),
    ("1.RV-Pre1", "2016", "Trendy Update"),
    ("3D Shareware v1.34", "2019", "1994 年風のジョーク版"),
    ("20w14∞", "2020", "Ultimate Content update。無限ディメンション"),
    ("22w13oneBlockAtATime", "2022", "1 ブロックずつしか持てない"),
    ("23w13a_or_b", "2023", "The Vote Update"),
    ("24w14potato", "2024", "Poisonous Potato Update"),
    ("25w14craftmine", "2025", "Craftmine Update"),
]
arows = [f'<tr><td>{v}</td><td>{y}</td><td><span class="badge plan">予定</span></td><td>{n}</td></tr>' for v, y, n in aprils]
NL = "\n            "

pages['versions.html'] = page('versions', '対応バージョン — DetergentMC', 'DetergentMC の対応バージョン一覧。1.20.4 から始めて 1.0〜最新まで、エイプリルフール版も含めて対応していく。', f'''
    <section class="page-head">
      <h1>対応バージョン</h1>
      <p class="lead">まず 1.20.4 を完成させ、その後 <strong>1.0 から最新バージョンまで</strong>を順に対応します。エイプリルフール版も対象です。</p>
      <p class="legend"><span class="badge done">対応済</span> 実クライアントで検証済 <span class="badge wip">作業中</span> 実装中 <span class="badge plan">予定</span> 未着手</p>
    </section>

    <section class="section">
      <h2>リリース版</h2>
      <div class="compare">
        <table class="versions">
          <thead><tr><th>バージョン</th><th>リリース</th><th>状態</th><th>備考</th></tr></thead>
          <tbody>
            {NL.join(rows)}
          </tbody>
        </table>
      </div>
      <p class="note">1.20.4 の実装が固まり次第、隣接バージョン (1.20.5+ / 1.21.x) から広げ、古いバージョンへは 1.19 → 1.0 の順に遡る予定です。プロトコルの差分はバージョン別モジュールとして分離し、ワールド・ティックの実装は共有します。</p>
    </section>

    <section class="section">
      <h2>エイプリルフール版</h2>
      <p class="sub">Mojang が毎年 4 月 1 日に公開するジョーク版。通常のリリースとプロトコルもゲーム内容も異なるため、それぞれ専用の対応を行います。今後のエイプリルフール版も継続して対応します。</p>
      <div class="compare">
        <table class="versions">
          <thead><tr><th>バージョン</th><th>年</th><th>状態</th><th>備考</th></tr></thead>
          <tbody>
            {NL.join(arows)}
          </tbody>
        </table>
      </div>
    </section>
''')

for name, html in pages.items():
    (ROOT / name).write_text(html, encoding='utf-8', newline='\n')
print('wrote', ', '.join(pages))
