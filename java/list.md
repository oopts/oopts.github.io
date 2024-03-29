# 一览

## 集合

### map

- HashMap
  - `hashcode` 与 `equals`
    - equals一致, hashcode 必定一致 ; hashcode 一致, equals 不一定一致
    - hashcode 默认值为内存地址, equals 默认比较内存地址
  - 结构 : 数组 + (链表/红黑树树)   `>=8 变为红黑树, <=6 退化为链表`
  - 扩容 : 扩容阈值 = 负载容量 * 负载因子
    - eg: 存储一万条数据 `new HashMap((10000 / 负载因子) + 1)`
    - 每次扩容, 负载容量 * 2

- LinkedHashMap
  - 继承自HashMap, 并维护一条双向链表 `即 Node 添加了属性 before 和 after`

- ConcurrentHashMap
  - 锁一个数组槽位, 而不是整个MAP
  - 锁的选择

### set

- HashSet
- LinkedHashSet
- TreeSet

### list

- ArrayList
- LinkedList

## 多线程

- Synchronized
- ReentrantLock
- AQS 与 JUC
- ThreadPool
- ThreadLocal
- CompleteFutureTask

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
- 垃圾回收器

## Vue3

## 秒杀场景

## 服务认证与授权
