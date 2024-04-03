# 一览

## 集合

### map

::: details HashMap

- `hashcode` 与 `equals`
  - equals一致, hashcode 必定一致 ; hashcode 一致, equals 不一定一致
  - hashcode 默认值为内存地址, equals 默认比较内存地址
- 结构 : 数组 + (链表/红黑树树)   `>=8 变为红黑树, <=6 退化为链表`
- 扩容 : 扩容阈值 = 负载容量 * 负载因子
  - eg: 存储一万条数据 `new HashMap((10000 / 负载因子) + 1)`
  - 每次扩容, 负载容量 * 2

:::

::: details LinkedHashMap

- 继承自HashMap, 并维护一条双向链表 `即 Node 添加了属性 before 和 after`
  
:::

::: details ConcurrentHashMap

- 锁一个数组槽位, 而不是整个MAP `锁分段`
  - 锁定当前链表/红黑树的首节点
- 加锁方式
  - 数组位首节点为null ,CAS添加首节点
  - synchronized(首节点)

:::

### set

::: details HashSet

- 内部持有一个 HashMap 对象

:::

::: details LinkedHashSet

- 内部持有一个 LinkedHashMap 对象

:::

::: details TreeSet

- 底层使用红黑树
- 可自定义排序方式
:::

### list

::: details ArrayList

- 底层使用数组, `查询快, 增删慢` `增删需要copy数组`

  :::
::: details LinkedList

- 底层使用双向链表  `增删快, 查询慢`

  :::

## 多线程

::: details 线程状态
`new` `Running` `waitting` `blocked` `terminated`

:::

::: details 线程安全三大特性

- 原子性 : 一个或多个操作, 要么全部执行成功, 要么不执行
  - synchronized
  - ~~final~~
- 有序性 : 按照代码顺序先后执行
  - synchronized
  - ~~volatile : `禁止指令重排序`, 保证`读`与`写`的执行顺序~~
- 可见性 : 一个线程修改的状态对另一个线程是可见的
  - synchronized : `内存屏障`
  - volatile : 基于`内存屏障` -> 写入后添加`store barrier`,读取前添加 `load barrier`

:::

::: details Synchronized

::: details 锁升级

- 无锁
- 偏向锁
  - 只有一个线程一次或多次访问
  - 首次访问时会将`线程ID`记录在`锁对象`的`对象头`中
  - 不加锁
- 轻量级锁
  - 当前线程的`线程ID`与记录的`偏向锁`的`线程ID`不一致, 升级为`轻量级锁`
  - 使用 CAS
- 重量级锁
  - CAS获取锁时,自旋次数达到一定的阈值, 或发现其他线程在竞争此锁, 升级为`重量级锁`
  - 使用操作系统提供的互斥量(mutex)来实现锁, 会进行`用户态`和`内核态`的切换, 会进行线程的`阻塞`和`唤醒`
- 锁粗化 : 根据逃逸分析将多个锁对象合并为一个锁
- 锁消除 : 根据逃逸分析, 去除不存在资源共享的场景的锁
- 重量级锁与轻量级锁
  - 重量级 :   不自旋, 不消耗CPU ; 线程会阻塞,响应时间慢;  追求吞吐量  /同步块执行时间长
  - 轻量级锁 : 自旋,   会消耗CPU ; 线程不阻塞,相应世家快;  追求响应时间/同步代码执行时间短
- 实例对象  
  - 对象头
    - Mark Word
      - `hashcode` `锁信息` `分代年龄` `GC标志` 等
    - Class Metadata Address : 指向该对象所属类的元数据
  - 实例变量 : 存放类的属性信息数据
  - 填充对象 : 为了字节对齐

:::

- Monitor : 使用重量级锁时, `mark word`重量级锁指针指向对应的Monitor
  - 由`ObjectMonitor`实现
  - 内部组成
    - _waitSet : 等待被唤醒的队列
    - _entryList : 阻塞队列
    - _owner : 持有者
    - _count : 计数器, 重入一次 +1, 释放一次 -1

:::

::: details ReentrantLock

:::
::: details AQS 与 JUC

:::

::: details ThreadPool

:::

::: details ThreadLocal

:::

::: details CompleteFutureTask

:::

## NIO && Reactor

## 源码

### Spring

- IOC
- AOP
- 事务
- Bean的生命周期

### SpringMVC

- 访问流程
- 八大组件

### MyBatis

- 分页
- 缓存
- 插件
- 获取插入的自增长ID  `usegeneratedkeys=true`  `keyproperty=id`

### SpringBoot

- 自动配置

## DB 与 中间件

### Mysql

- SQL优化
- InnoDB
- B+Tree
- 分库分表
- 主从复制
- MVCC

### Redis

### RabbitMQ / RocketMQ

## 微服务 SpringCloud

## 分布式事务

## JVM

- 类加载
- JMM
  - 内存屏障
  - 指令重排序
- 垃圾回收器

## Vue3

## 秒杀场景

## 服务认证与授权
