+   1.简述瀑布模型、增量模型、螺旋模型（含原型方法），并分析优缺点
     + 瀑布模型

       + 优点：
         + 有利于大型软件开发过程中人员的组织、管理，
         + 有利于软件开发方法和工具的研究，从而提高了大型软件项目开发的质量和效率。
       + 缺点：
         + （1）开发过程一般不能逆转，否则代价太大；
         + （2）实际的项目开发很难严格按该模型进行；
         + （3）客户往往很难清楚地给出所有的需求，而该模型却要求如此。
         + （4）软件的实际情况必须到项目开发的后期客户才能看到，这要求客户有足够的耐心。
     + 增量模型
       + 优点：
         + （1）采用增量模型的优点是人员分配灵活，刚开始不用投入大量人力资源；
         + （2）如果核心产品很受欢迎，则可增加人力实现下一个增量；
         + （3）可先发布部分功能给客户，对客户起到镇静剂的作用。
       + 缺点：
         + （1）并行开发构件有可能遇到不能集成的风险，软件必须具备开放式的体系结构；
         + （2）增量模型的灵活性可以使其适应这种变化的能力大大优于瀑布模型和快速原型模型，但也很容易退化为边做边改模型，从而是软件过程的控制失去整体性。
   + 螺旋模型
       + 优点：
         + （1）设计上的灵活性,可以在项目的各个阶段进行变更；
         + （2）以小的分段来构建大型系统,使成本计算变得简单容易；
         + （3）客户始终参与每个阶段的开发,保证了项目不偏离正确方向以及项目的可控性；
         + （4） 随着项目推进,客户始终掌握项目的最新信息 , 从而他或她能够和管理层有效地交互。
       + 缺点：
         + （1）采用螺旋模型需要具有相当丰富的风险评估经验和专门知识，在风险较大的项目开发中，如果未能够及时标识风险，势必造成重大损失；
         + （2）过多的迭代次数会增加开发成本，延迟提交时间。
+ 2.简述统一过程三大特点，与面向对象的方法有什么关系？
   + 用例驱动
  + 以架构为中心的
  + 受控的迭代式增量开发
    统一过程是一个面向对象且基于网络的程序开发方法论，它给出了有关软件开发过程组织及实施的指导。
+ 3.简述统一过程四个阶段的划分准则是什么？每个阶段关键的里程碑是什么？
    + 1． 初始阶段
      +   划分准则：初始阶段的目标是为系统建立商业案例并确定项目的边界，其主要工作为：识别外部交互实体、定义交互特性和关注业务与需求方面的主要风险
      +   里程碑：生命周期目标里程碑，生命周期目标里程碑评价项目基本的生存能力
  +  2． 细化阶段
     +   划分准则：细化阶段的目标是分析问题领域，建立健全的体系结构基础，编制项目计划，淘汰项目中最高风险的元素。
     +   里程碑：生命周期结构里程碑。生命周期结构里程碑为系统的结构建立了管理基准并使项目小组能够在构建阶段中进行衡量。此刻，要检验详细的系统目标和范围、结构的选择以及主要风险的解决方案。
  + 3． 构造阶段
      +   划分准则：构建阶段是一个制造过程，其重点放在管理资源及控制运作以优化成本、进度和质量。
      +   里程碑：初始功能里程碑。初始功能里程碑决定了产品是否可以在测试环境中进行部署。此刻，要确定软件、环境、用户是否可以开始系统的运作。
  + 4． 交付阶段
    +   划分准则：交付阶段的重点是确保软件对最终用户是可用的，其主要工作是为发布做准备的产品测试并基于用户反馈的少量的调整
    +   里程碑：产品发布里程碑。此时，要确定目标是否实现，是否应该开始另一个开发周期。在一些情况下这个里程碑可能与下一个周期的初始阶段的结束重合。
+ 软件企业为什么能按固定节奏生产、固定周期发布软件产品？它给企业项目管理带来哪些好处？

        软件企业采用基于统一过程的软件项目规划，利用软件产品范围的弹性，  
        合理规划范围（20%业务决定80%满意度），使得软件生产按固定节奏运行，   
        固定迭代周期、固定开发周期、固定升级周期。统一过程中，  
        软件开发生命周期根据时间（固定周期发布）和RUP的核心工作流（固定节奏生产）  
        划分为二维空间。时间维从组织管理的角度描述整个软件开发生命周期，  
        是RUP的动态组成部分，核心工作流从技术角度描述RUP的静态组成部分  
