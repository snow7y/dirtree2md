
# dirtree2md🌳

`dirtree2md` は、ディレクトリ構造をマークダウン形式で出力するためのツールです。このツールを使うことで、ディレクトリ内のファイルやフォルダの構造を簡単に視覚化できます。

## 目次

- [dirtree2md🌳](#dirtree2md)
  - [目次](#目次)
  - [インストール方法](#インストール方法)
  - [使い方](#使い方)
    - [オプション](#オプション)
      - [例](#例)
    - [ディレクトリ構造の例](#ディレクトリ構造の例)
  - [開発への参加](#開発への参加)
  - [ライセンス](#ライセンス)
  - [作者](#作者)
  - [コントリビューション](#コントリビューション)

## インストール方法

`dirtree2md` をインストールするには、以下のコマンドを実行してください。

```bash
pip install git+https://github.com/yukikimoto/dirtree2md.git
```

## 使い方

`dirtree2md` はコマンドラインツールとして動作します。以下のようにコマンドを実行することで、指定したディレクトリの構造をマークダウン形式で出力します。

```bash
dirtree2md /path/to/directory
```

### オプション

`dirtree2md` には以下のオプションがあります：

- `-f`, `--file` : 指定された場合、マークダウン形式の出力を指定したファイルに保存します。

#### 例

- 標準出力に出力する場合：

```bash
dirtree2md /path/to/directory
```

- ファイルに出力する場合：

```bash
dirtree2md /path/to/directory -f output.md
```

### ディレクトリ構造の例

例えば、次のようなディレクトリ構造があるとします：

/example_dir
    /sub_dir
        file2.txt
    file1.txt

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

- @yukikimoto (<https://github.com/yukikimoto>)

## コントリビューション

バグ報告や機能追加のリクエストは [GitHub Issues](https://github.com/yukikimoto/dirtree2md/issues) へお願いします。
