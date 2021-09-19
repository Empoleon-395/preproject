# preproject
これは2021年9月22日発表予定、関東甲信越グループのデータ分析部分に当たります。  
## 説明
フォルダ内のpreproject/program/main.ipynbを実行すれば資料通りの結果が得られます。  
## 動作環境
pythonバージョン3.8を用い、poetryにてパッケージの管理を行っています。

git cloneでダウンロードし、フォルダ直下でpoetry installすれば環境が構築されます。  
この環境で使用しているパッケージのバージョンは以下の通りです。
```
[tool.poetry.dependencies]
python = "^3.8"
pandas = "^1.3.3"
torch = "^1.9.0"
transformers = "^4.10.2"
gensim = "^4.1.2"
Janome = "^0.4.1"
scikit-learn = "^0.24.2"
ipykernel = "^6.4.1"
fugashi = "^1.1.1"
ipadic = "^1.0.0"
```
