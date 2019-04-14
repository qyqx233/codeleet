```
export PGHOME=/usr/local/soft/postgresql-11.2
export PGDATA=/opt/data/postgres
export PATH=$PGHOME/bin:$PATH
export MANPATH=$PGHOME/share/man:$MANPATH
export LANG=en_US.utf8
export DATE=`date +"%Y-%m-%d %H:%M:%S"`
export LD_LIBRARY_PATH=$PGHOME/lib:$LD_LIBRARY_PATH
alias rm='rm  -i'
alias ll='ls -lh'
#alias pg_start='pg_ctl start -D $PGDATA'
#alias pg_stop='pg_ctl stop -D $PGDATA -m fast'

#psql -h 主机名 -p 端口号 -U 用户名 -W(强制口令提示) [-d]数据库名
#psql -h $GHOST -p $PGPORT -U $PGUSER -W -d $PGDATABASE
#PGHOST 设置数据库服务器名。 如果它以一个斜杠开头，那么它声明一个 Unix 域套接字而不是 TCP/IP 通讯； 其值就是该套接字文件存储的目录（在缺省安装中，这个目录会是 /tmp）
#export PGHOST=$PGDATA
export PGHOST=localhost
#PGPORT 设置 TCP 端口号或者设置与 PostgreSQL 通讯的 Unix 域套接字的文件扩展。
export PGPORT=5432
export PGUSER=postgres #用于与数据库连接的用户名，initdb -U posgtres指定

set -o vi
alias l='ls -lrt'
export PYTHONPATH=/usr/soft/python3/lib64/python3.6/lib-dynload
```

修改 `$PGDATA/postgres.conf`

```
unix_socket_directories = '/var/run/postgresql'
```

```sh
groupadd postgres
useradd -g postgres -d /home/postgres postgres
mkdir /home/postgres
chown postgres:postgres /home/postgres
mkdir /var/run/postgresql
chown postgres:postgres /var/run/postgresql
initdb -d $PGDATA
pg_ctl start -D $PGDATA
```
CREATE USER root WITH SUPERUSER

pg_hba.conf 新增一行
