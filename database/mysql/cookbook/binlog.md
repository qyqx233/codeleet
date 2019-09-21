## 引言

二进制日志包含数据库所有的更改记录，包括数据和结构两方面。开启二进制服务会带来轻微的性能影响。二进制日志可以保证数据库故障时数据是安全的。

主要作用：复制，时间点恢复

## 使用二进制

使用`show variables like '%log_bin%'`查看二进制日志相关配置

my.cnf `mysqld`配置段新增`server_id=123`，`log_bin=E:/AppRun/data` *ps:log_bin是全路径*
`log_bin`可以置空，此时默认保存位置是`datadir`

一旦binlog文件大小达到1G（默认)，新文件就会被创建，可以使用`set @@GLOBAL.max_binlog_size=536870912`动态设置

使用`set SQL_LOG_BIN=0`，当前会话内所有SQL语句都不会被记录到binlog，重新开启执行`set SQL_LOG_BIN=1`

`show binary logs` 查看binlog文件

`flush logs` 关闭当前二进制文件，并开启新文件

`binlog_expire_logs_seconds` `binlog_expire_logs_days` 设置日期的过期时间

`purge binary logs to server1.000004` 00004之前的日志都会被删除

`purge binary logs before '2017-01-12 12:32:00'`

`purge master logs to 'server1.000004'` 

`reset master` 删除所有日志


## 二进制格式

1. statement 记录实际执行的SQL语句
2. ROW 记录每行的修改
3. MIXED 当需要时mysql会从statement切换到ROW（有些语句在不同服务器上执行时会得到不同的结果，例如`uuid()`，这种情况下会切换到ROW模式）

在全局范围内设置格式 `set global binlog_format='statement'` or `set global binlog_format='row'`

## 忽略要使用二进制格式的数据库

## 迁移二进制