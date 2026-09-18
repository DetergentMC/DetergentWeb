# DetergentWeb

DetergentMC の公式サイト。静的サイト。ページは `tools/build.py` が共通ヘッダ/フッタ付きで生成する
(生成物もコミットする。編集は `tools/build.py` 内の本文を直して `python tools/build.py`)。

ページ: ホーム / 仕組み / Core・Engine / ロードマップ / 対応バージョン
`main` への push で GitHub Pages に自動デプロイされる (`.github/workflows/pages.yml`)。

ローカル確認:

```bash
python -m http.server 8080
```
