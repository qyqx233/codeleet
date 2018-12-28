### git 出现 The requested URL returned error: 403

先配置user.name与user.email

```shell
git config add user.name xxx
git config add user.email xxx
```

然后修改.git/config，在origin-url将用户名$USER添加进去

[remote "origin"]
	url = https://$USER@github.com/xxxx/yyy.git
	fetch = +refs/heads/*:refs/remotes/origin/*