
# dirtree2md

`dirtree2md` は、ディレクトリ構造をマークダウン形式で出力するためのツールです。このツールを使うことで、ディレクトリ内のファイルやフォルダの構造を簡単に視覚化できます。

## インストール方法

`dirtree2md` をインストールするには、以下のコマンドを実行してください。

```bash
pip install dirtree2md
```

## 使い方

`dirtree2md` はコマンドラインツールとして動作します。以下のようにコマンドを実行することで、指定したディレクトリの構造をマークダウン形式で出力します。

```bash
dirtree2md /path/to/directory
```

### 例

例えば、次のようなディレクトリ構造があるとします：

```
/example_dir
    /sub_dir
        file2.txt
    file1.txt
```

このディレクトリに対して `dirtree2md` コマンドを実行すると、以下のようなマークダウン形式の出力が得られます：

```markdown
- example_dir/
    - file1.txt
    - sub_dir/
        - file2.txt
```

このように、ディレクトリ構造が見やすい形で表示されます。

## 開発への参加

このプロジェクトに貢献したい場合は、以下の手順に従ってください：

1. リポジトリをクローンします：
    ```bash
    git clone https://github.com/yourusername/dirtree2md.git
    cd dirtree2md
    ```

2. 必要な依存関係をインストールします：
    ```bash
    pip install -r requirements.txt
    ```

3. テストを実行します：
    ```bash
    python -m unittest discover tests
    ```

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下でライセンスされています。

## 作者

- あなたの名前 (your.email@example.com)

## コントリビューション

バグ報告や機能追加のリクエストは [GitHub Issues](https://github.com/yourusername/dirtree2md/issues) へお願いします。
