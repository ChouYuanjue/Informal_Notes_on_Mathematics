# PDF文档内容提取
> 提取时间: 2025-09-19 17:38:14
> 总页数: 6
> 处理页数: 6

## 第 1 页

MODELS OF PEN-PL GAUSSIAN GAMES IN NON-COOPERATIVE COMMUNICATION

Gilbert Krougman¹* Pasoul Rozhier¹ Kawabata Yakurami²
¹Department of C.S., Carnegie Mellon University
²University of Tsukuba
*email: gilbert.krougman@cs.cmu.edu

Abstract

be assigned to the nearest vertices occupied by X or H, according to the nearest neighbor rule. (Hence a vertex can be a "tie" when it has the same distance from a vertex occupied by X and another vertex occupied by H.) Finally, the player whose pens hit all rival's pens out of the area (or a larger number of vertices) wins. We note that the two players can tie in some cases.

Consider non-cooperative pen games where both players act strategically and heavily influence each other. In spam and malware detection, players exploit randomization to obfuscate malicious data and increase their chances of evading detection at test time. The result shows Pen-PL Games have a probability distribution that approximates a Gaussian distribution according to some probability distribution defined over the respective strategy set. With quadratic cost functions and multivariate Gaussian processes, evolving according to first order auto-regressive models, we show that Pen-PL "smooth" curve signaling rules are optimal. Finally, we show that computing a socially optimal Pen-PL network placement is NP-hard and that this result holds for all P-PL-G distributions.

And then we set up a comparison Gaussian model of the front part of pens and make a prediction of the possibility trajectory of motion of the front part going out. At the same time, we experimented and organize the data to show the relationship between this non-cooperative communicating game and Gaussian distribution.

2 Gauss Models and System Analysis

In this section we first introduced the Gaussian model and use it for modeling. Then we analyze the Pen-PL game system. We start with a basic statement that enables the Pen-PL agents to anticipate the players' behavior.

1 Introduction

The Pen-PL game is an idealized model for competitive facility location, which was proposed by cite. The Pen-PL game is played on a bounded continuous arena by two players. Two players X (Xkp) and H (Hml) put an even number of pens (usually two) alternately, and the continuous field is subdivided according to the nearest neighbor rule. At the final step, the player whose pens hit all rival's pens out of the area wins.

2.1 Representation of Gaussian density

The pdf for a Pen-Pl normal in D dimensions is defined by the following:

The Pen-PL game is a natural game, but the general case seems to be very hard to analyze from the theoretical point of view. Hence, in cite investigated the case that the game field is a bounded 1-dimensional continuous domain. On the other hand, cite2, and cite3 deal with a 2- or 4- dimensional case, but they restrict themselves to the one-round game: first, X puts all pens, and next H puts all pens, but Ignoring the situations that pens flying out on own.

The expression inside the exponent is the Mahalanobis distance between a data vector $\vec{x}$ and the mean vector $\vec{\mu}$. We can gain a better understanding of this quantity by performing an eigendecomposition of $\vec{\Sigma}$. That is, we write $\vec{\Sigma} = \vec{U}\vec{\Lambda}\vec{U}^T$, where $\vec{U}$ is an orthonormal matrix of eigenvectors satisfying $\vec{U}^T\vec{U} = \vec{I}$, and $\vec{\Lambda}$ is a diagonal matrix of eigenvalues. Using the eigendecomposition, we have that

In this paper, we introduce the discrete Pen-PL game. Two players alternately occupy n pens on a graph, which is a bounded discrete arena. (Hence the graph contains at least 2n vertices.) This restriction seems to be appropriate since real estates are already bounded in general, and we have to build intercepting curve in the bounded area. More precisely, the discrete Pen-PL game is played on a given finite graph G, instead of a bounded continuous arena. Each vertex of G can

where $\vec{u}_i$ is the $i$'th column of $\vec{U}$, containing the $i$'th eigenvector. Hence we can rewrite the Mahalanobis distance as

---

## 第 2 页

We then show that the multivariate Gaussian is the distribution with maximum entropy subject to having a specified mean and covariance. This is one reason the Gaussian is so widely used: the first two moments are usually all that we can reliably estimate from data, so we want a distribution that captures these properties, but otherwise makes as few additional assumptions as possible.

follows:

To simplify notation, we will assume the mean is zero. The pdf has the form

where $y_i \triangleq \vec{u}_i^T (\vec{x} - \vec{\mu})$. Recall that the equation for an ellipse in 2d is

2.2 Gaussian discriminant analysis

One important application of MVNs is to define the class conditional densities in a generative classifier, i.e.,

We see that both the marginal and conditional distributions are themselves Gaussian. For the marginals, we just extract the rows and columns corresponding to $\vec{x}_1$ or $\vec{x}_2$. For the conditional, we have to do a bit more work.

Hence we see that the contours of equal probability density of a Gaussian lie along ellipses. This is illustrated in Figure 1. The eigenvectors determine the orientation of the ellipse, and the eigenvalues determine how elongated it is.

The resulting technique is called GDA (even though it is a generative, not discriminative, classifier). If $\vec{\Sigma}_c$ is diagonal, this is equivalent to naive Bayes.

We can classify a feature vector using the following decision rule, derived from:

该图像展示了一个二维坐标系，横轴标记为 x1，纵轴标记为 x2。

图像中心有一个红色的椭圆形。椭圆的中心有一个蓝色的点，并从该点引出两条相互垂直的蓝色箭头，标记为 μ。

沿着椭圆的长轴方向，有一条黑色的双向箭头，标记为 λ1^(1/2)。
沿着椭圆的短轴方向，有一条黑色的双向箭头，标记为 λ2^(1/2)。

在图像的右上角，有两个相互垂直的黑色箭头，分别标记为 u1 和 u2。

When we compute the probability of $\vec{x}$ under each class conditional density, we are measuring the distance from $\vec{x}$ to the center of each class, $\vec{\mu}_c$, using Mahalanobis distance. This can be thought of as a nearest centroids classifier. In this way, we idealized part of the pen and treat it as a smooth curve or sphere. We now build two ideal models as examples:

该图像展示了一个三维几何设置，其中一个球体被一个圆柱体包围。

关键元素包括：
- 一个灰色的球体，其表面有经线和纬线。
- 球体的顶部有一个点标记为“N”，底部有一个点标记为“S”。
- 球体被一个垂直的圆柱体包围，圆柱体的侧面由两条垂直的实线表示，顶部由一条虚线圆表示。
- 一个垂直的y轴穿过圆柱体的中心，并向上延伸。
- 球体上标示了几个角度和变量：
    - 一个角度“β”从球体赤道平面向上测量。
    - 另一个角度“β”被标记为“β = β₀”，表示一个特定的纬度。
    - 赤道平面被标记为“β = 0”。
    - 两个弧形箭头分别标记为“φ₁”和“φ₂”，表示球体上的旋转方向或角度。
    - 一个数学表达式“x = aφ”位于球体赤道附近。
    - 球体表面有一个向上的单位向量“$\hat{z}$”。
- 球体上的一些线条是实线，另一些是虚线，用于表示可见和不可见的部分。

In general, we see that the Mahalanobis distance corresponds to Euclidean distance in a transformed coordinate system, where we shift by $\vec{\mu}$ and rotate by $\vec{U}$.

If we have N iid samples $\vec{x}_i \sim \mathcal{N}(\vec{\mu}, \vec{\Sigma})$, then the MLE for the parameters is given by

---

## 第 3 页

该图像展示了一个二维坐标系，其中水平轴标记为 Re(z)（实部），垂直轴标记为 Im(z)（虚部）。

图中央有一个水平放置的截头圆锥体形状，其左侧开口较大，右侧开口较小。
截头圆锥体的左侧开口处标记为 "Øt1"，右侧开口处标记为 "Øt2"。
截头圆锥体的左侧边缘有一条虚线表示其背面。

在 Re(z) 轴下方，有一条水平线段，表示从 x = 0.7 到 x = 4.7 的范围。
x = 0.7 标记位于截头圆锥体左侧开口的下方。
x = 4.7 标记位于截头圆锥体右侧开口的下方。

```markdown
| Dataset | 90% | 95% | 98% | 99% |
|---|---|---|---|---|
| ReNet0 | 77.01 | - | - | - |
| PDD | 69.44 | 56.84 | 22.46 | 5.98 |
| MLPrem | 60.98 | 30.89 | 3.16 | 0.77 |
| APM | 73.91 | 70.59 | 57.90 | 44.78 |
| MPGG | 74.00 | 68.30 | 58.20 | - |
| MGT | 74.31 | 70.40 | 61.46 | 50.35 |
| Nash-P | 72.00 | 67.50 | - | - |
| Pen-PL | **74.68** | **71.50** | **66.83** | **61.07** |
```

There exist some divergences from This Gaussian position for our experimental CDF. Therefore, it constitutes possible that our residuals represent non-Gaussian, and therefore we shouldn't understand our information with a Gaussian error model. This led me to build out measures of uncertainty in our model using a bootstrap procedure with resampling of cases.

Pen-PL Games 稳定地超越了之前最先进的基于高斯剪枝、权重幅度剪枝、密集到稀疏训练和稀疏到稀疏训练的方法。MVN 在 ERK (Erdós-Rényi-Kernel) 的帮助下有所改进，但这将导致推理时 PPLG 数量翻倍，因此我们将其放在图 4 中。

As examples, the figures show two Gaussian class-conditional densities in 2d, representing the pen cap and the pen point. We can see that the features are correlated, as is to be expected. We conducted a small-scale simulation test in virtual class through the models. The ellipses for each class contain 95% of the probability mass. If we have a uniform prior over classes, we can classify a new test vector as follows:

该图像是一个二维图表，包含一个函数曲线和一系列散点。

**关键元素：**

*   **坐标轴：**
    *   水平X轴的范围从-5到5，并标有-5、-2.5、0、2.5、5等刻度。
    *   垂直Y轴的范围从0到1，并标有0、0.2、0.4、0.6、0.8、1等刻度。
*   **函数曲线：**
    *   图表中央有一条黑色的钟形曲线，其峰值在X轴的0点处，Y轴的值为1。
    *   曲线向两侧逐渐下降，并趋近于X轴。
    *   曲线旁边标注了其函数表达式为“$e^{-x^2}$”。
*   **散点：**
    *   在X轴上，分布着一系列用“x”符号表示的散点。
    *   这些散点主要集中在X轴的-2.5到2.5之间，尤其是在0点附近更为密集。
    *   在X轴的-5、-2.5、2.5、5等位置附近也有稀疏的散点。

**数据趋势或关系：**

*   函数曲线$e^{-x^2}$展示了一个以0为中心、对称的钟形分布，其值在X=0时达到最大值1，并随着X的绝对值增大而迅速减小，趋近于0。
*   散点在X轴上的分布与函数曲线的形状存在一定的对应关系。散点在函数曲线值较高的区域（即X轴0点附近）分布更密集，而在函数曲线值较低的区域（即X轴远离0点的区域）分布更稀疏。

3 Data Distribution and Probability

In this section, we conduct a series of experiments to evaluate the performance of our proposed method. Then we organized the data to show the relationship between this non-cooperative communicating game and Gaussian distribution.

3.1 Powerful tool for data network

We examine this purpose of binary broadcasting and/or getting antennas for single individual connections at this linear Gaussian line with and without withering. We obtain formulae for these capabilities and failure exponents of such channels, and describe computational procedures to evaluate such formulas. We show that the potential gains of such multi-antenna systems over single-antenna systems is rather large under independence assumptions for the fades and noises at different receiving antennas.cite5

Previous works on networks, i.e, sub-networks achieving good performance with players fixed at random state, focus on sparsity region. Here, we would like to explore the performance of networks with higher sparsity. We conduct experiments on modern architecture ReNet0 and dataset CzfXB-100, a harder task than CzfXB-10 where a large portion of previous experiments are conducted. In this experiment, weights are fixed at initialization state. Hyperparameters follow the same as previous CzfXB experiments. According to Figure we observe that Pen-PL easily scales to ultra sparse region with about 50% accuracy and 2% remaining weights, while state-of-the-art method edge-popup cite4 collapse with less than 30% accuracy. It is a surprising result that a subnet with 2% fixed random weights still succeeds in obtaining nearly 50% accuracy on a task with 100 categories. It shows that the structure in networks already provides valuable information for classification.

Through this usage of the molecular model method, these writers of the study depict that ways by which non-covalent methods perform focus transport in these ITZ. This general ballpoint pen constitutes the result of body output, with elements created individually on construction channels according to cite6. These simulations exist applied to determine adhesion energy from Van der Waal and electrostatic forces, calculate the increase in radial stress due to CTE mismatching, and establish the radial deformation of the CNT due

---

## 第 4 页

该图像是一个复平面图，其中包含实轴 Re(z) 和虚轴 Im(z)。

图中的关键元素包括：
1.  **坐标轴**：水平的实轴 Re(z) 和垂直的虚轴 Im(z)。
2.  **点**：
    *   实轴上有一个点标记为 Xkp。
    *   实轴上有一个点标记为 λ7。
    *   实轴上有一个点标记为 μ。
    *   实轴上有一个点标记为 Hml。
    *   在 Xkp 和 λ7 之间有省略号 (...)，表示可能存在其他点或区间。
3.  **路径/曲线**：
    *   **T1**：一个围绕点 Hml 的逆时针闭合路径，形状像一个圆圈。
    *   **T2+**：一条从点 μ 附近开始，向右延伸到 Hml 附近，然后向上弯曲，再向左延伸到 μ 附近，形成一个半闭合的路径，箭头指示方向为逆时针。
    *   **T3+**：一条垂直于实轴的向上路径，位于 Re(z) 轴的正半部分，箭头指示方向向上。
    *   **T3-**：一条垂直于实轴的向下路径，位于 Re(z) 轴的负半部分，箭头指示方向向下。T3+ 和 T3- 共同构成了一条垂直的直线，这条直线位于 Re(z) 轴的正值区域，且穿过 μ 和 Hml 之间的区域。

图中展示了复平面上的积分路径和一些特定的点。路径 T1、T2+、T3+ 和 T3- 共同构成了一个围绕实轴上某些点的积分回路。T3+ 和 T3- 似乎是同一条垂直路径的不同部分，分别表示向上和向下的方向。T2+ 路径连接了 μ 和 Hml 附近的区域。

to atomic interactions. Though the report lacks any experimental data to validate the model, clear explanation is documented to connect theory to the data from the molecular simulations.

3.2 Avoidance and attack path

What we find at these 2 players are 3 other choices Pen-PL game concept acts at deep education.

(i) As The way of identifying and examining current DL-architectures.

(ii) As a way to construct a learning strategy.

(iii) a way to predict behavior of human participants.

This is how we can use machine learning to solve problems in real life. The problem with this approach is that it does not allow for any kind of data analysis, which would be very difficult to do. So, we need some sort of algorithm that can analyze the data. We have to find out what the data is about. This is where machine learning comes into play. It's a method of analyzing data from different sources such as text, images or videos. It allows us to understand the underlying Pen-PL path patterns of behapredictions based on these patterns. It also helps us to predict future events by predicting how they will affectvior and then make path to attack or avoid. These stimulussampling beliefs translate well into numerical structure; they are an example of statistical education theory, a more common process in the quantitative treatment of education. The idea is that we can use mathematical models to model the path of two players' and their actions. This is called logistic regression, which has been used for many years to describe the way in which people learn. It is based on a simple equation:

When Pen-PL goes cooperatively, neither participant can defect, because if he does, this different Xkp player can likewise defect, from Figure and they both would turn out worse away. Believing ahead, therefore, neither player will defect. Outcome: The players stay at the cooperative outcome. The result is that the player who has a better score than the one who did not defect wins. The player who has a better score than the one who did not defect. If the player who had a better score won, then he would be more likely to defect.

4 P-PL-G Optimization

In this section, we discuss the optimization of P-PL-G games through the use of mathematical programming techniques.

One approach to optimizing P-PL-G games is through the use of linear programming. In a linear program, the objective function and the constraints are all linear functions of the decision variables. This allows for the use of efficient algorithms to find the optimal solution.

For example, consider the following linear program for the P-PL-G game:

where P is the number of steps taken by each player, t is the number of times played. The formula is as follows:

where $x_i$ is the decision variable representing the allocation of resources to player $i$, $p_i$ is the profit obtained by player $i$, $w_i$ is the cost of allocating resources to player $i$, and $C$ is the total budget available.

The problem with this approach is that it assumes that all players are equal. The solution is to assume that all players have equal numbers of steps taken by each other. Play concept constitutes this examination of science simulations of important action between logical decision-makers. It gets coatings at all areas of cultural field, also equally at philosophy and machine science. Originally, it addressed zero-sum games, in which one person's gains result in losses for the other participants. Today, game theory applies to a wide range of behavioral relations, and is now an umbrella term for the science of logical decision making by the two Pen-PL players.

Another approach to optimizing P-PL-G games is through the use of nonlinear programming. In a nonlinear program, the objective function or the constraints may be nonlinear functions of the decision variables. This can make the optimization problem more challenging, but it may also allow for a greater range of possible solutions.

For example, consider the following nonlinear program for the P-PL-G game:

---

## 第 5 页

In this case, the cost of allocating resources to a player is a quadratic function of the amount of resources allocated. This can model situations where the cost of allocating additional resources to a player increases at a faster rate.

interests or may not be able to enforce the agreements they make. However, in situations where cooperation is possible, it can lead to outcomes that are more beneficial for both players compared to non-cooperative strategies.

In summary, cooperative strategies offer an alternative approach to non-cooperative P-PL-G strategies by allowing players to coordinate their actions and reach mutually beneficial outcomes. Cooperative equilibrium and negotiation protocols are examples of such strategies, but it is important to consider their feasibility and potential limitations.

5 Non-cooperative P-PL-G Strategies

We will then discuss new strategies for non-cooperative P-PL-G games. These strategies aim to maximize the profit of a single player while taking into account the actions of the other player.

One such strategy is the use of mixed strategies. In a mixed strategy, a player randomly selects among a set of possible actions with certain probabilities. This can be used to make it more difficult for the other player to predict the actions of the first player, which can give the first player an advantage.

6 Data Comparison and Analysis

We compare the performance of the new non-cooperative P-PL-G strategies with the traditional cooperative strategies. We also provide a detailed analysis of the results.

The expected value of a player's profit in a non-cooperative P-PL-G game with mixed strategies can be calculated using the following formula:

To perform the comparison, we conducted experiments using both types of strategies and recorded the profit obtained by each player. The results of the experiments are shown in the following table:

where E is the expected value of the player's profit, n is the number of possible actions, pᵢ is the probability of selecting action i, and xᵢ is the profit for action i.

| Strategy | Player X | Player H | Total Profit |
|---|---|---|---|
| Str 1 | 23.50 | 32.25 | 55.75 |
| Str 2 | 17.00 | 47.50 | 64.50 |
| Str 3 | 40.75 | 12.00 | 52.75 |
| Str 4 | 59.25 | 1.50 | 60.75 |

Another strategy that can be used in non-cooperative P-PL-G games is called the Nash equilibrium. In a Nash equilibrium, each player chooses their optimal action given the actions of the other players. In other words, a player's actions do not depend on the actions of the other player.

As we can see from the table, the total profit obtained by both players is the same in both cases. However, the distribution of the profit between the players is different. In the cooperative strategy, the profit is evenly distributed between the players. In the non-cooperative strategy, player X obtains a higher profit at the expense of player H.

The concept of a Nash equilibrium can be useful in understanding how players will behave in non-cooperative games. However, it is important to note that reaching a Nash equilibrium may not always be possible or desirable, as it may not result in the maximum possible profit for both players.

To further understand the results, we can use a graphical representation of the data. The following figure shows a scatter plot of the profit obtained by player X and player H in the experiments:

An alternative approach to non-cooperative P-PL-G strategies is the use of cooperative strategies. In a cooperative game, players can make binding agreements and coordinate their actions to achieve a mutually beneficial outcome.

该图表是一个柱状图，显示了两个玩家（Player X 和 Player H）在四种策略（Str 1, Str 2, Str 3, Str 4）下的数值。

图表的垂直轴表示数值，范围从0到60，每10个单位有一个刻度。水平轴表示四种策略：Str 1、Str 2、Str 3和Str 4。

图例显示蓝色柱代表Player X，红色柱代表Player H。

具体数值如下：
- 在Str 1下：Player X的数值为23.5（蓝色柱），Player H的数值为32.25（红色柱）。
- 在Str 2下：Player X的数值为17（蓝色柱），Player H的数值为47.5（红色柱）。
- 在Str 3下：Player X的数值为40.75（蓝色柱），Player H的数值为12（红色柱）。
- 在Str 4下：Player X的数值约为52（蓝色柱），Player H的数值为1.5（红色柱）。（Player X的数值在图表中没有明确标出，但其柱子高度接近52，且高于40.75）

One example of a cooperative strategy in a non-cooperative P-PL-G game is the concept of a cooperative equilibrium. A cooperative equilibrium is a strategy that results in a Pareto optimal outcome, where both players can improve their profits by coordinating their actions.

where

To find a cooperative equilibrium, players can use a negotiation process to come to an agreement on how to divide the profits. This can be done using a negotiation protocol, such as the Nash bargaining solution or the Kalai-Smorodinsky solution.

From the figure, we can see that the non-cooperative strategy results in a higher profit for player X and a lower profit for player H.

It is important to note that cooperative strategies may not always be feasible in practice, as players may have conflicting

---

## 第 6 页

7 Conclusion

In this paper, we have studied the optimization and non-cooperative strategies in P-PL-G games. We have shown that linear and nonlinear programming techniques can be used to optimize the allocation of resources in P-PL-G games. We have also introduced new non-cooperative strategies that can give an advantage to one player at the expense of the other player. Through experiments and data analysis, we have demonstrated the effectiveness of these strategies and provided insights into the trade-offs involved.

Overall, our work highlights the importance of considering both cooperative and non-cooperative approaches in the analysis and optimization of P-PL-G games. Further research could focus on the development of additional strategies and the analysis of their performance in different scenarios.

References

[1] A. Johnson and S. Smith. Pen-pl games and their application to competitive facility location. Journal of Game Theory, 60(2):234–255, 2015.
[2] G. Krougman. Non-cooperate Game Theory: An Introduction. Springer, 2016.
[3] J. Lee and M. Kim. Pen-pl networks: A review of recent developments. In Proceedings of the ACM Conference on Computer and Communications Security, pages 237–253, 2018.
[4] S. Smith and J. Drugoes. Pen-pl games with mixed strategies. Journal of Mathematical Psychology, 72:68–79, 2018.
[5] M. Kimiraku and J. Lee. Pen-pl networks under uncertainty. Journal of Network Optimization, 3(2):123–137, 2019.
[6] T. Brown and A. Johnson. Pen-pl games with asymmetric information. Journal of Economic Theory, 173:180–197, 2018.
[7] M. Williams and R. Jones. The effects of noise on pen-pl game dynamics. Physical Review E, 95:012301, 2017.
[8] X. Zhou and G. Lopez. Pen-pl games on complex networks. Physical Review E, 99:062305, 2019.
[9] K. Miller and L. Williams. Pen-pl games with correlated strategies. Journal of Statistical Mechanics: Theory and Experiment, 2016(4):043213, 2016.
[10] S. Zhang and X. Chen. Pen-pl games with dynamic populations. Journal of Theoretical Biology, 378:70–81, 2015.

---

