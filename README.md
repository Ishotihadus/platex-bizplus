# platex-bizplus

[MORISAWA BIZ+](https://www.morisawa.co.jp/products/fonts/bizplus/) を pLaTeX / upLaTeX で使えるようにするスクリプトです。

UD 新ゴ + UD 黎ミン + UD 新丸ゴのセットです。

## 必要な要件

- Python >= 3.0?
- macOS
- MORISAWA BIZ+ の契約・インストール・同期

## 使い方

```sh
git clone https://github.com/Ishotihadus/platex-bizplus
cd platex-bizplus
sudo python run.py

# --jis2004 は使えません
sudo kanji-config-updmap --sys --mode=ja bizplus
```
