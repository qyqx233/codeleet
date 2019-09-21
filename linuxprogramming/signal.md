父进程避免僵尸进程

交给系统*init*去处理
```c
signal(SIGCHLD,SIG_IGN);
```

全局屏蔽某个信号
```c
struct sigaction sa;
sa.sa_handler = SIG_IGN;
sigaction( SIGPIPE, &sa, 0 );
```

*signal*函数设置的信号句柄只能起一次作用，信号被捕获后信号句柄被还原成默认值

*sigaction*设置的信号句柄可以一直生效，直到你修改它的值
