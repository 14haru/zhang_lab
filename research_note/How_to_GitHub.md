# Git，GitHubの学習
## VScodeによるGit環境のセットアップ

参考\
https://breezegroup.co.jp/202102/vscode-github-windows/

### commitできないとき
fatal: unable to auto-detect email address.

アカウントが特定できていないためエラーが出た

これの解決法

```
git config user.email
git config user.name
```

これでGitHubに登録された情報が表示されなければ以下で変更

```
git config --global user.email ここに自分のGitHubのアドレス
git config --global user.name ここに自分のGitHubの名前
```

### pushできないとき
```
fatal: refusing to merge unrelated histories
```

ファイルの祖先がない状態でプッシュ，プル，マージなどしようとするとこのエラーが出る

これの解決法\
ブランチがmasterのとき
```
git merge --allow-unrelated-histories origin/master
```

ブランチがmainのとき
```
git merge --allow-unrelated-histories origin/main
```

参考\
https://qiita.com/w-tdon/items/24348728c9256e5bf945


## GitのVScode上の操作方法

参考\
https://qiita.com/y-tsutsu/items/2ba96b16b220fb5913be

