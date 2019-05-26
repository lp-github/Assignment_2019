###目标：
得到一个Boundery Comdition : B 使得			
$\lbrace{ Dom, B,∧_{j≠i} A_j }\rbrace|– ¬A_i$
###说明：

$A_j$有以下形式：
$A_j: A=>C$
$¬A_i有以下形式：$
$¬A_i: L_1 ∧ L_2∧...∧L_n$

###步骤：
+ 初始化$B=¬A_i$
+ 迭代         
  +   找到一对匹配的C与L，求一个置换$\mu:=mgu(L,C)$
  +   $ A^{'}= A.\mu$
    + 将B中对应的L用$A^{'}替换掉$

迭代，直到边界条件变得有意义或者足够精确到容易设计场景来消除分歧
###举例说明：
资源管理系统中：
+ 在用户的view下：
$$
\forall u: User,r:Resource\newline
Using(u,r)=>o[Needs(u,r)->Using(u,r)]
$$
+ 在管理员的view下：
$$
\forall u:User,r:Resource\newline
Using(u,r)=>\Diamond_{\leq d}¬Using(u,r)
$$
we take negation of staff's view as initialization of B
$$
    \Diamond \exist u:User,r:Resource\newline
    Using(u,r) ∧ \square_{\leq d}Using(u,r)
$$
take assertion in User's view into consideration:
take u,r in B as instantiation of User and Resource
$$
 Using(u,r)   : satisfied\newline
=>:\newline
o[Needs(u,r)->Using(u,r)]\space satisfied\space
$$
and obtain by modus ponens:
$$
o Needs(u,r)->o Using(u,r)
$$
so the new B and A show as below:
$$
o Needs(u,r)->o Using(u,r)\newline
\space\newline\space
\Diamond \space \exists u:User,r:Resource\newline
Using(u,r)∧\square_{\leq d}Using(u,r)
\newline \space
\newline 
$$
modified to same format to combine
$$
o\space Needs(u,r)-> o\space Using(u,r)\newline\space\newline
\Diamond \space \exists u:User,r:Resource\newline
Using(u,r)∧\square_{\lt d}\space o\space Using(u,r)
$$
replace oUsing(u,r) with o Needs(u,r) in B,obtain

$$
\Diamond\exists u:User,r:Resource
\newline
Using(u,r)∧\square_{\lt d}o \space Needs(u,r)\newline
$$

thereby obtain the boundary condition causing divergence:

$$
\Diamond\exists u:User,r:Resource\newline
Using(u,r)∧\square_{\leq d}o\space Needs(u,r)  
$$
**there is a question above,which is slightly different from instance from paper**-
##Divergence Pattern
###Achieve-Avoid Pattern
$$
P=>\Diamond Q\newline
R=>\square ¬ S\newline
Q=>S
\newline\space\newline
Boudary Condition:\newline
    \Diamond(P∧R)
$$
####example:
in resource management system
Goal Achieve[RequstSatisfied]:
$$    FormalDef:\space \forall u:User,r:Resource\newline
    Requesting(u,r)=>\Diamond Using(u,r)
$$
Goal Avoid[UnReliableResourseUsed]:
$$
FormalDef:\space \forall u:User,r:Resource\newline
¬Reliable(r)=>\square ¬Using(u,r)
$$
with instantiations
$$
P:Requesting(u,r)\newline
Q:Using(u,r)\newline
R:¬Reliable(r)\newline
S:Using(u,r)
$$
and the boundary obtained by$\Diamond (P∧R) $without any formal derivation
$$
\Diamond[Requesting(u,r)∧¬Reliable(r)]
$$
###Retraction Pattern
$$P=>\Diamond Q \newline
Q=>P
\newline\space\newline
Boundary\space Condition:\newline
    \Diamond[P∧(¬ Q\space \mu\space \square ¬ P)]
$$
####example
take a patient monitering system into consideration:
$$
A_1: Critical=>\Diamond Alarm\newline
A_2: Alarm=>Critical
$$
with instantiation:
$$
P: Critical\newline
Q: Alarm
$$
one can easily get boundary condition by instantiating it:
$$
\Diamond [P∧(¬Q\space\mu \space\square ¬P)]\newline
\Diamond [Critical∧(¬Alarm\space\mu \space\square ¬Critical)]
$$
**Notes**:this Boundary Condition means:

    Cirtical situation occurs and then disappers before the alarm arise
###Other Pattern
$$
P=>(Q \space W \space   S)\newline
Q=>R
\newline\space\newline
Boundary\space Condition\newline
\Diamond(P∧R∧¬S)\mu(P∧¬R∧¬S)
$$
####example
apply this pattern to a library system:
$$
A_1:Borrowing(u,bc)=>(HasPermission(u,bc) \space W \space   DueDate(u,bc))\newline
A_2:HasPermission(u,bc)=>Member(u,lib)
$$
 with instantiations:
$$
P:Borrowing(u,bc)\newline
Q:HasPermission(u,bc)\newline
R:Member(u,lib)\newline
S:DueDate(u,bc)\newline
and the Boundary Condition as:\newline
    \Diamond(Borrowing(u,bc)∧Member(u,lib)∧¬DueDate(u，bc))\mu(Borrowing(u,bc)∧¬Member(u,lib)∧¬DueDate(u,bc))
$$
**Notes**:
    this boundary condition means that a lib member borrow a book copy and lost its membership before the DueDate for returning the borrowed copies 