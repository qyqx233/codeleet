RST的含义为“复位”，它是TCP在某些错误情况下所发出的一种TCP分节。有三个条件可以产生RST:

>SYN到达某端口但此端口上没有正在监听的服务器。
>TCP想取消一个已有连接
>TCP接收了一个根本不存在的连接上的分节。

1. Connect 函数返回错误ECONNREFUSED
如果对客户的SYN的响应是RST，则表明该服务器主机在我们指定的端口上没有进程在等待与之连接（例如服务器进程也许没有启动），这称为硬错（hard error），客户一接收到RST，马上就返回错误ECONNREFUSED.

TCP为监听套接口维护两个队列。两个队列之和不超过listen函数第二个参数backlog。

当一个客户SYN到达时，若两个队列都是满的，TCP就忽略此分节，且不发送RST.这个因为：这种情况是暂时的，客户TCP将重发SYN，期望不久就能在队列中找到空闲条目。要是TCP服务器发送了一个RST，客户connect函数将立即发送一个错误，强制应用进程处理这种情况，而不是让TCP正常的重传机制来处理。还有，客户区别不了这两种情况：作为SYN的响应，意为“此端口上没有服务器”的RST和意为“有服务器在此端口上但其队列满”的 RST.
Posix.1g允许以下两种处理方法：忽略新的SYN，或为此SYN响应一个RST.历史上，所有源自Berkeley的实现都是忽略新的SYN。

2. 如果杀掉服务器端处理客户端的子进程，进程退出后，关闭它打开的所有文件描述符，此时，当服务器TCP接收到来自此客户端的数据时，由于先前打开的那个套接字接口的进程已终止，所以以RST响应。

经常遇到的问题：
如果不判断read , write函数的返回值，就不知道服务器是否响应了RST, 此时客户端如果向接收了RST的套接口进行写操作时，内核给该进程发一个SIGPIPE信号。此信号的缺省行为就是终止进程，所以，进程必须捕获它以免不情愿地被终止。

进程不论是捕获了该信号并从其信号处理程序返回，还是不理会该信号，写操作都返回EPIPE错误。


3. 服务器主机崩溃后重启
如果服务器主机与客户端建立连接后崩溃，如果此时，客户端向服务器发送数据，而服务器已经崩溃不能响应客户端ACK，客户TCP将持续重传数据分节，试图从服务器上接收一个ACK，如果服务器一直崩溃客户端会发现服务器已经崩溃或目的地不可达，但可能需要比较长的时间； 如果服务器在客户端发现崩溃前重启，服务器的TCP丢失了崩溃前的所有连接信息，所以服务器TCP对接收的客户数据分节以RST响应。

服务端去世后，如果客户端继续send，不会立刻发现错误，调用read的时候，会抛出错误 errno=104　`connetction reset by peer`