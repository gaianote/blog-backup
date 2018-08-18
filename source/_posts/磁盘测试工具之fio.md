---
title: 磁盘测试工具之fio
date: 2018-07-31 09:48:15
tags:
---

FIO是测试IOPS的非常好的工具，用来对硬件进行压力测试和验证，支持13种不同的I/O引擎

<!--more-->

## 安装

centos可以使用yum安装

```
yum install fio
```

## 命令行模式

安装完成后，使用命令行输入以下命令，便可以开始测试了。

```bash
fio -filename=/tmp/test_randread -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=2G -numjobs=10 -runtime=60 -group_reporting -name=mytest
```

以上命令的含义是随机读写：(可直接用，向磁盘写一个2G文件，10线程，随机读1分钟，给出结果)


## Job file模式

需要测试多种情况下的多个job时，可以将所有配置参数写在一个配置文件当中，然后使用`fio config_file`方式运行即可。

说明：

1. 配置文件划分为多个区域，每个区域的参数设置均作用于其下方的区域；
2. global区域进行全局的参数配置；
3. 非特定名字的区域（fist_job）则被视为一个运行任务。

配置文件 config_file 示例：

```
#-start job file-
[global]
ioengine=psync
iodepth=1
size=20g
bs=4k
direct=1
runtime = 180
filename=/dev/sdb1
[fist_job]
rw=write
[second_job]
rw=randwrite
#-end job file-
```

## 测试结果分析

```
fio-3.1
Starting 10 threads
Jobs: 10 (f=10): [r(10)][100.0%][r=2944KiB/s,w=0KiB/s][r=184,w=0 IOPS][eta 00m:00s]
mytest: (groupid=0, jobs=10): err= 0: pid=345: Tue Jul 31 02:51:46 2018
   read: IOPS=192, BW=3083KiB/s (3157kB/s)(181MiB/60061msec)
    clat (usec): min=981, max=578165, avg=51855.31, stdev=54091.70
     lat (usec): min=981, max=578166, avg=51857.14, stdev=54091.67
    clat percentiles (msec):
     |  1.00th=[    7],  5.00th=[    9], 10.00th=[   12], 20.00th=[   16],
     | 30.00th=[   21], 40.00th=[   27], 50.00th=[   34], 60.00th=[   44],
     | 70.00th=[   59], 80.00th=[   80], 90.00th=[  113], 95.00th=[  146],
     | 99.00th=[  253], 99.50th=[  321], 99.90th=[  558], 99.95th=[  567],
     | 99.99th=[  575]
   bw (  KiB/s): min=   32, max=  673, per=10.00%, avg=308.35, stdev=102.75, samples=1200
   iops        : min=    2, max=   42, avg=19.26, stdev= 6.42, samples=1200
  lat (usec)   : 1000=0.01%
  lat (msec)   : 2=0.35%, 4=0.03%, 10=6.73%, 20=22.14%, 50=35.07%
  lat (msec)   : 100=22.67%, 250=11.95%, 500=0.86%, 750=0.19%
  cpu          : usr=0.05%, sys=0.18%, ctx=11629, majf=0, minf=40
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwt: total=11573,0,0, short=0,0,0, dropped=0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=3083KiB/s (3157kB/s), 3083KiB/s-3083KiB/s (3157kB/s-3157kB/s), io=181MiB (190MB), run=60061-60061msec

Disk stats (read/write):
  sda: ios=11540/10, merge=0/6, ticks=596750/360, in_queue=597720, util=99.95%
```

* bw：磁盘的吞吐量，这个是顺序读写考察的重点 。
* iops：磁盘的每秒读写次数，这个是随机读写考察的重点。
* runt：线程运行时长。
* slat（usec）：提交延迟，单位是微秒，向内核提交一个IO请求所需的时间。
* clat（usec）：完成延迟，它是提交到内核和IO完成经过的时间，不包括提交延迟。
* min：最快时间；max：最慢时间；avg：平均时间；stdev：
* lat:一个设置数据块大小的读/写请求从提交到完成所需的时间。
* clat percentiles（usec）:完成时间的百分比分布，如大约99%的请求是在14毫秒之内完成。
* CPU：cpu使用率。
* issued:total=r=0/w=16777216   总共发出0个读请求，16777216个写请求。


## 参数说明

### IO类型

`rw=str`,向文件发起的IO类型

* `rw=read` 顺序读
* `rw=write` 顺序写
* `rw=randwrite` 随机写
* `rw=randread` 随机读
* `rw=rw` 顺序混合读写
* `rw=randrw` 随机混合读写

### 单次IO的数据大小

产生的IO单元的大小，可以是一个孤立的值，也可以是一个范围。

`bs=int`,单次IO的block size,默认为4k。如果是单个值的话，将会对读写都生效。如果是一个逗号，再跟一个int值的话，则是仅对于写有效。

* `bs = 8k` 读写都使用8k的块
* `bs = 4k,8k` 读使用4k的块，写使用8k的块
* `bs = ,8k`   使得写采用8k的块，读采用默认的值。

### IO数据总量

`size=int`,将会读/写多少数据

这个job IO总共要传输的数据的大小。FIO将会执行到所有的数据传输完成，除非设定了运行时间（runtime选项）。除非有特定的nrfiles选项和filesize选项被设置，fio将会在job定义的文件中平分这个大小。如果这个值不设置的话，fio将会使用这个文件或设备的总大小。如果这些文件不存在的话，size选项一定要给出。也可以给出一个1到100的百分比。e.g. size=20%，fio将会使用给定的文件或设备的20%的空间。

### IO引擎

`ioengine=str`,定义job向文件发起IO的方式。

* `sync` 基本的read,write.lseek用来作定位
* `psync` 基本的pread,pwrite
* `vsync` 基本的readv,writev
* `libaio` Linux专有的异步IO。Linux仅支持非buffered IO的队列行为。
* `posixaio` glibc posix异步IO
* `solarisaio` solaris独有的异步IO
* `windowsaio` windows独有的异步IO
* `mmap` 文件通过内存映射到用户空间，使用memcpy写入和读出数据
* `splice` 使用splice和vmsplice在用户空间和内核之间传输数据
* `syslet-rw` 使用syslet 系统调用来构造普通的read/write异步IO
* `sg` SCSI generic sg v3 io.可以是使用SG_IO ioctl来同步，或是目标是一个sg字符设备，我们使用read和write执行异步IO
* `null` 不传输任何数据，只是伪装成这样。主要用于训练使用fio，或是基本debug/test的目的。
* `net` 根据给定的host:port通过网络传输数据。根据具体的协议，hostname,port,listen,filename这些选项将被用来说明建立哪种连接，协议选项将决定哪种协议被使用。
* `netsplice` 像net，但是使用splic/vmsplice来映射数据和发送/接收数据。
* `cpuio` 不传输任何的数据，但是要根据cpuload=和cpucycle=选项占用CPU周期.e.g. cpuload=85将使用job不做任何的实际IO，但要占用85%的CPU周期。在SMP机器上，使用numjobs=来获取需要的CPU，因为cpuload仅会载入单个CPU，然后占用需要的比例。
* `guasi` GUASI IO引擎是一般的用于异步IO的用户空间异步系统调用接口
* `rdma` RDMA I/O引擎支持RDMA内存语义（RDMA_WRITE/RDMA_READ）和通道主义(Send/Recv）用于InfiniBand,RoCE和iWARP协议
* `external` 指明要调用一个外部的IO引擎（二进制文件）。e.g. ioengine=external:/tmp/foo.o将载入/tmp下的foo.o这个IO引擎

### IO depth

`iodepth=int`,如果IO引擎是异步的，这个指定我们需要保持的队列深度

默认对于每个文件来说是1，可以设置一个更大的值来提供并发度。iodepth大于1不会影响同步IO引擎（除非verify_async这个选项被设置）

### IO类型

`direct=bool`,true,则标明采用non-buffered io.同O_DIRECT效果一样。ZFS和Solaris不支持direct io，在windows同步IO引擎不支持direct io
`buffered=bool`,true,则标明采用buffered io。是direct的反义词，默认是true

### job文件数量

`nrfiles=int`,用于这个job的文件数目,默认为1,表示负载将分发到几个文件之中
`openfiles=int`,在同一时间可以同时打开的文件数目，默认同nrfiles相等，可以设置小一些，来限制同时打开的文件数目。

### 线程数

`numjobs=int`,创建大量的线程/进程来执行同一件事。我们将这样一系列的job，看作一个特定的group

###  其它

* `name=str`,job名，用于输出信息用的名字。如果不设置的话，fio输出信息时将采用job name，如果设置的话，将用设置的名字。在命令行中，这个参数有特殊的作用，标明一个新job的开始。
* `description=str`,job的说明信息,在job运行的时候不起作用，只是在输出文件描述信息的时候才起作用。
* `directory=str`,使用的文件的路径前缀，默认是./
* `filename=str`,一般情况下，fio会根据job名，线程号，文件名来产生一个文件名。如果，想在多个job之间共享同一个文件的话，可以设定一个名字来代替默认的名字.如果ioengine是‘net’的话，文件名则是以这种格式=host,port,protocol.如果ioengine是基于文件的话，可以通过‘:’分割来设定一系列的文件。e.g. filename=/dev/sda:/dev/sdb 希望job打开/dev/sda和/dev/sdb作为两个工作文件。
* `opendir=str`,让fio递归的添加目录下和子目录下的所有文件。
* `lockfile=str`,fio在文件上执行IO之前默认是不锁文件的，这样的话，当有多个线程在此文件上执行IO的话，会造成结果的不一致。这个选项可以用来共享文件的负载，支持的锁类型：
    * none 默认不使用锁
    * exclusive 排它锁
    * readwrite 读写锁

  在后面可以加一个数字后缀，如果设置的话，每一个线程将会执行这个数字指定的IO后才会放弃锁，因为锁的开销是比较大的，所以这种方式可以加速IO。
* `kb_base=int`,size换算单位，1000/1024,默认为1024
* `randrepeat=bool`,对于随机IO负载，配置生成器的种子，使得路径是可以预估的，使得每次重复执行生成的序列是一样的。
* `use_os_rand=bool`,fio可以使用操作系统的随机数产生器，也可以使用fio内部的随机数产生器（基于tausworthe），默认是采用fio内部的产生器,质量更好，速度更快。

* `fallocate=str`,如何准备测试文件
    * `none` 不执行预分配空间
    * `posix` 通过posix_fallocate()预分配空间
    * `keep` 通过fallocate()（设置FALLOC_FL_KEEP_SIZE）预分配空间

  0 none的别名,出于兼容性,1 posix的别名，出于兼容性，并不是在所有的平台上都有效，‘keep’仅在linux上有效，ZFS不支持。默认为‘posix’
* `fadvise_hint=bool`,默认fio将使用fadvise()来告知内核fio要产生的IO类型，如果不想告诉kernel来执行一些特定的IO类型的话，可行关闭这个选项。如果设置的话，fio将使用`POSIX_FADV_SEWUENTIAL`来作顺序IO，使用`POSIX_FADV_RANDOM`来做随机IO
* `filesize=int`,单个文件的大小，可以是一个范围，在这种情况下，fio将会在一个范围内选择一个大小来决定单个文件大小，如果没有设置的话，所有的文件将会是同样的大小。
* `fill_device=bool,fill_fs=bool`,填满空间直到达到终止条件ENOSPC，只对顺序写有意义。对于读负载，首行要填满挂载点，然后再启动IO，对于裸设备结点，这个设置则没有什么意义，因为，它的大小已被被文件系统知道了，此外写的超出文件将不会返回ENOSPC.
* `blockalign=int,ba=int`,配置随机io的对齐边界。默认是与blocksize的配置一致，对于direct_io，最小为512b,因为它与依赖的硬件块大小，对于使用文件的随机map来说，这个选项不起作用。
* `blocksize_range=irange,bsrange=irange`,不再采用单一的块大小，而是定义一个范围，fio将采用混合io块大小.IO单元大小一般是给定最小值的备数。同时应用于读写，当然也可以通过‘,’来隔开分别配置读写。
* `bssplit=str`,可以更为精确的控制产生的block size.这个选项可以用来定义各个块大小所占的权重.格式是

    ```
    bssplit=blocksize/percentage;blocksize/percentage
    bssplit=4k/10:64k/50;32k/40
    ```

    产生的这样的负载：50% 64k的块，10% 4k的块, 40% 32k的块
    可以分别为读和写来设置

    ```
    bssplit=2k/50:4k/50,4k/90:8k/10
    ```

    产生这样的负载：读（50% 64k的块，50% 4k的块），写（90% 4k的块, 10% 8k的块）

* `blocksize_unaligned,bs_unaligned`,如果这个选项被设置的，在bsrange范围内的大小都可以产生，这个选项对于direct io没有作用，因为对于direct io至少需要扇区对齐。
* `zero_buffers`,如果这个选项设置的话，IO buffer全部位将被初始为0,如果没有置位的话，将会是随机数.
* `refill_buffers`,如果这个选项设置的话，fio将在每次submit之后都会将重新填满IO buffer,默认都会在初始是填满，以后重复利用。这个选项只有在zero_buffers没有设置的话，这个选项才有作用。
* `scramble_buffer=bool`,如果refilee_buffers成本太高的话，但是负载要求不使用重复数据块，设置这个选项的话，可以轻微的改动IO buffer内容，这种方法骗不过聪明的块压缩算法，但是可以骗过一些简单的算法。
* `buffer_compress_percentage=int`,如果这个设置的话，fio将会尝试提供可以压缩到特定级别的Buffer内容。FIO是能完提供混合的0和随机数来实现的
* `file_service_type=str`,fio切换job时，如何选择文件，支持下面的选项
    * `random` 随机选择一个文件
    * `roundrobin` 循环使用打开的文件，默认
    * `sequential` 完成一个文件后，再移动到下一个文件
    这个选项可以加后缀数字，标明切换到下一个新的频繁程度。`random:4` 每4次IO后，将会切换到一下随机的文件
* `iodepth_batch_submit=int,iodepth_batch=int`,这个定义了一次性提交几个IO，默认是1，意味着一旦准备好就提交IO，这个选项可以用来一次性批量提交IO
* `iodepth_batch_complete=int`,这个选项定义了一次取回多少个IO，如果定义为1的话，意味着我们将向内核请求最小为1个IO.
* `iodepth_low=int`,这个水位标志标明什么时候开始重新填充这个队列，默认是同iodepth是一样的，意味着，每时每刻都在尝试填满这个队列。如果iodepth设置为16，而iodepth设置为4的话，那么fio将等到depth下降到4才开始重新填充
* `offset=int`,在文件特定的偏移开始读数据,在这个offset之前的数据将不会被使用，有效的文件大小=real_size-offset
* `offset_increment=int`,如果这个选项被设置的话，实际的offset=offset+offset_increment * thread_number,线程号是从0开始的一个计数器，对于每一个job来说是递增的。这个选项对于几个job同时并行在不交界的地方操作一个文件是有用的。
* `fsync=int`,如果写一个文件的话，每n次IO传输完block后，都会进行一次同步脏数据的操作。
* `fdatasync=int`,同fsync，但是采用fdatasync()来同步数据，但不同步元数据
* `sync_file_range=str:val`,对于每‘val’个写操作，将执行sync_file_range()。FIO将跟踪从上次sync_file_range()调用之扣的写范围，‘str’可以是以下的选择
    `wait_before SYNC_FILE_RANGE_WAIT_BEFORE`
    `write SYNC_FILE_RANGE_WRITE`
    `wait_after SYNC_FILE_RANGE_WAIT_AFTER`
    示例：`sync_file_range=wait_before,write:8`,fio将在每8次写后使用`SYNC_FILE_RANGE_WAIT_BEFORE|SYNC_FILE_RANGE_WRITE`
* `overwrite=bool`,如果是true的话，写一个文件的话，将会覆盖已经存在的数据。如果文件不存在的话，它将会在写阶段开始的时候创建这个文件。
* `end_fsync=bool`,如果是true的话，当job退出的话，fsync将会同步文件内容
* `fsync_on_close=bool`,如果是true的话，关闭时，fio将会同步脏文件，不同于end_fsync的时，它将会在每个文件关闭时都会发生，而不是只在job结束时。
* `rwmixread=int`,混合读写中，读占的百分比
* `rwmixwrite=int`,混合读写中，写占的百分比；如果rwmixread=int和rwmixwrite=int同时使用的话并且相加不等于100%的话，第二个值将会覆盖第一个值。这可能要干扰比例的设定,如果要求fio来限制读和写到一定的比率。在果在这种情况下，那么分布会的有点的不同。
* `norandommap`,一般情况下，fio在做随机IO时，将会覆盖文件的每一个block.如果这个选项设置的话，fio将只是获取一个新的随机offset,而不会查询过去的历史。这意味着一些块可能没有读或写，一些块可能要读/写很多次。在个选项与verify=互斥，并只有多个块大小（bsrange=）正在使用，因为fio只会记录完整的块的重写。
* `nice=int`,根据给定的nice值来运行这个job
* `prio=int`,设置job的优先级，linux将这个值限制在0-7之间，0是最高的。
* `prioclass=int`,设置优先级等级。
* `thinktime=int`,上一个IO完成之后，拖延x毫秒，然后跳到下一个。可以用来访真应用进行的处理。
* `thinktime_spin=int`,只有在thinktime设置时才有效，在为了sleep完thinktime规定的时间之前，假装花费CPU时间来做一些与数据接收有关的事情。
* `thinktime_blocks`,只有在thinktime设置时才有效，控制在等等‘thinktime’的时间内产生多少个block，如果没有设置的话，这个值将是1，每次block后，都会将等待‘thinktime’us。
    * `rate=int`,限制job的带宽。
    * `rate=500k`,限制读和写到500k/s
    * `rate=1m,500k`,限制读到1MB/s，限制写到500KB/s
    * `rate=,500k` , 限制写到500kb/s
    * `rate=500k`, 限制读到500KB/s
* `ratemin=int`,告诉fio尽最在能力来保证这个最小的带宽，如果不能满足这个需要，将会导致程序退出。
* `rate_iops=int`,将带宽限制到固定数目的IOPS，基本上同rate一样，只是独立于带宽，如果job是指定了一个block size范围，而不是一个固定的值的话，最小blocksize将会作为标准。
* `rate_iops_min=int`,如果fio达不到这个IOPS的话，将会导致job退出。
* `ratecycle=int`,几个毫秒内的平均带宽。用于‘rate’和‘ratemin’
* `cpumask=int`,设置job使用的CPU.给出的参数是一个掩码来设置job可以运行的CPU。所以，如果要允许CPU在1和5上的话，可以通过10进制数来设置（1<<1 | 1<<5），或是34
* `cpus_allowed=str`,功能同cpumask一样，但是允许通过一段文本来设置允许的CPU。e.g.上面的例子可是这样写`cpus_allowed=1,5`。这个选项允许设置一个CPU范围，如`cpus_allowed=1,5,8-15`
`startdelay=time`,fio启动几秒后再启动job。只有在job文件包含几个jobs时才有效，是为了将某个job延时几秒后执行。
* `runtime=time`,控制fio在执行设定的时间后退出执行。很难来控制单个job的运行时间，所以这个参数是用来控制总的运行时间。
* `time_based`,如果设置的话，即使file已被完全读写或写完，也要执行完runtime规定的时间。它是通过循环执行相同的负载来实现的。
* **`ramp_time=time`**,设定在记录任何性能信息之前要运行特定负载的时间。这个用来等性能稳定后，再记录日志结果，因此可以减少生成稳定的结果需要的运行时间。
* `sync=bool`,使用sync来进行buffered写。对于多数引擎，这意味着使用O_SYNC
* `iomem=str,mem=str`,fio可以使用各种各样的类型的内存用来io单元buffer.
    * `malloc` 使用malloc()
    * `shm` 使用共享内存.通过shmget()分配
    * `shmhuge` 同shm一样，可以使用huge pages
    * `mmap` 使用mmap。可以是匿名内存，或是支持的文件，如果一个文件名在选项后面设置的话，格式是mem=mmap:/path/to/file
    * `mmaphuge` 使用mmapped huge file.在mmaphuge扣面添加文件名，alamem=mmaphuge:/hugetlbfs/file
    分配的区域是由job允许的最大block size * io 队列的长度。对于shmhuge和mmaphuge，系统应该有空闲的页来分配。这个可以通过检测和设置`reading/writing /proc/sys/vm/nr_hugepages`来实现（linux）。FIO假设一个huge page是4MB。所以要计算对于一个JOB文件需要的Huge page数量，加上所有jobs的队列长度再乘以最大块大小，然后除以每个huge page的大小。可以通过查看/proc/meminfo来看huge pages的大小。如果通过设置nr_hugepages=0来使得不允许分配huge pages，使用mmaphug或是shmhuge将会失败。

    * `mmaphuge` 需要挂载hugelbfs而且要指定文件的位置，所以如果要挂载在/huge下的话，可以使用mem=mmaphuge:/huge/somefile
* `iomem_align=int`,标明IO内存缓冲的内存对齐方式。
* `hugepage-size=int`,设置huge page的大小。至少要与系统的设定相等。默认是4MB，必然是MB的倍数，所以用hugepage-size=Xm是用来避免出现不是2的整数次方的情况。
* `exitall`当一个job退出时，会终止运行其它的job，默认是等待所有的job都完成，FIO才退出，但有时候这并不是我们想要的。
* `bwavgtime=int`,在给定时间内的平均带宽。值是以毫秒为单位的
* `iopsavgtime=int`,在给定时间内的平均IOPS，值是以毫秒为单位的
* `create_serialize=bool`,job将会串行化创建job,这将会用来避免数据文件的交叉，这依赖于文件系统和系统的CPU数
* `create_fsync=bool`,创建后同步数据文件，这是默认的值
* `create_on_open=bool`,不会为IO预先创建文件，只是在要向文件发起IO的时候，才创建open()
* `create_only=bool`,如果设置为true的话，fio将只运行到job的配置阶段。如果文件需要部署或是更新的磁盘的话，只有上面的事才会做，实际的文件内容并没有执行。
* `pre_read=bool`,如果这个选项被设置的话，在执行IO操作之前，文件将会被预读到内存.这会删除‘invalidate’标志，因为预读数据，然后丢弃cache中的数据的话，是没有意义的。这只是对可以seek的IO引擎有效，因为这允许读相同的数据多次。因此对于network和splice不起作用。
* `unlink=bool`,完成后将删除job产生的文件。默认是not,如果设置为true的话，将会花很多时间重复创建这些文件。
* `loops=int`,重复运行某个job多次，默认是1
* `do_verify=bool`,写完成后，执行一个校验的阶段，只有当verify设置的时候才有效。默认是true
* `verify=str`,写一个文件时，每次执行完一个job扣，fio可以检验文件内容.允许的校验算法是：md5,crc64,crc32c,crc32c-intel,crc32,crc16,crc7,sha512,sha256,sha1,meta,null.这个选项可以用来执行重复的burn-in测试，来保证写数据已经正确的读回。如果是read或随机读，fio将假设它将会检验先前写的文件。如果是各种格式的写，verify将会是对新写入的数据进行校验。
* `stonewall,wait_for_previous`,等待先前的job执行完成后，再启动一个新的job。可以用来在job文件中加入串行化的点。stone wall也用来启动一个新reporting group
* `new_group`,启动一个新的reporting group。如果这个选项没有设置的话，在job文件中的job将属于相同的reporting group，除非通过stonewall隔开
* `group_reporting`,如果‘numjobs’设置的话，我们感兴趣的可能是打印group的统计值，而不是一个单独的job。这在‘numjobs’的值很大时，一般是设置为true的，可以减少输出的信息量。如果‘group_reporting’设置的话，fio将会显示最终的per-groupreport而不是每一个job都会显示
* `thread`,fio默认会使用fork()创建job，如果这个选项设置的话，fio将使用pthread_create来创建线程
* `zonesize=int`,将一个文件分为设定的大小的zone
* `zoneskip=int`,跳过这个zone的数据都被读完后，会跳过设定数目的zone.
* `write_iolog=str`,将IO模式写到一个指定的文件中。为每一个job指定一个单独的文件，否则iolog将会分散的的，文件将会冲突。
* `read_iolog=str`,将开一个指定的文件，回复里面的日志。这可以用来存储一个负载，并进行重放。给出的iolog也可以是一个二进制文件，允许fio来重放通过blktrace获取的负载。
* `replay_no_stall`,当使用read_iolog重放I/O时，默认是尝试遵守这个时间戳，在每个IOPS之前会有适当的延迟。通过设置这个属性，将不会遵守这个时间戳，会根据期望的顺序，尝试回复，越快越好。结果就是相同类型的IO，但是不同的时间
* `replay_redirect`,当使用`read_iolog`回放IO时，默认的行为是在每一个IOP来源的`major/minor`设备上回放IOPS。这在有些情况是不是期望的，比如在另一台机器上回放，或是更换了硬件，使是`major/minor`映射关系发生了改变。`Replay_redirect`将会导致所有的IOPS回放到单个设备上，不管这些IO来源于哪里.比如：`replay_redirect=/dev/sdc`将会使得所有的IO都会重定向到`/dev/sdc`.这就意味着多个设备的数据都会重放到一个设置，如果想来自己多个设备的数据重放到多个设置的话，需要处理我们的trace，生成独立的trace，再使用fio进行重放，不过这会破坏多个设备访问的严格次序。
* `write_bw_log=str`,在job file写这个job的带宽日志。可以在他们的生命周期内存储job的带宽数据。内部的`fio_generate_plots`脚本可以使用gnuplot将这些文本转化成图。
* `write_lat_log=str`,同`write_bw_log`类似，只是这个选项可以存储io提交，完成和总的响应时间。如果没有指定文件名，默认的文件名是`jobname_type.log`。即使给出了文件名，fio也会添加两种类型的log。如果我们指定`write_lat_log=foo`,实际的log名将是`foo_slat.log`,`foo_slat.log`和`foo_lat.log`.这会帮助`fio_generate_plot`来自动处理log
* `write_iops_log=str`,类似于`write_bw_log`,但是写的是IOPS.如果没有给定文件名的话，默认的文件名是jobname_type.log。
* `log_avg_msec=int`,默认，fio每完成一个IO将会记录一个日志（iops,latency,bw log）。当向磁盘写日志的时候，将会很快变的很大。设置这个选项的话，fio将会在一定的时期内平均这些值，指少日志的数量，默认是0
* `lockmem=int`,使用mlock可以指定特定的内存大小，用来访真少量内存
* `exec_preren=str`,运行job之前，通过过system执行指定的命令
* `exec_postrun=str`,job执行完成后，通过system执行指定的命令
* `ioscheduler=str`,在运行之前，尝试将文件所在的设备切换到指定的调度器。
* `cpuload=int`,如果job是非常占用CPU周期的，可以指定战胜CPU周期的百分比。
* `cpuchunks=int`,如果job是非常战胜CPU周期的，将load分拆为时间的cycles，以毫秒为单位
* `disk_util=bool`,产生磁盘利用率统计信息。默认是打开的
* `disable_lat=bool`,延迟的有效数字。
* `clat_percentiles=bool`,允许报告完成完成响应时间的百分比
* `continue_on_error=str`,一般情况下，一旦检测到错误，fio将会退出这个job.如果这个选项设置的话，fio将会一直执行到有‘non-fatal错误‘（EIO或EILSEQ）或是执行时间耗完，或是指定的I/Osize完成。如果这个选项设置的话，将会添加两个状态，总的错误计数和第一个error。允许的值是
    * `none` 全部IO或检验错误后，都会退出
    * `read` 读错误时会继续执行，其它的错误会退出
    * `write` 写错误时会继续执行，其它的错误会退出
    * `io` 任何IO error时会继续执行，其它的错误会退出
    * `verify` 校验错误时会继续执行，其它的错误会退出
    * `all` 遇到所有的错误都会继续执行
* `uid=int`,不是使用调用者的用户来执行，而是指定用户ID
* `gid=int`,设置group id
