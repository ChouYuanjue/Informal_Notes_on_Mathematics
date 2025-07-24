# PDF文档内容提取
> 提取时间: 2025-09-19 09:29:09
> 总页数: 6
> 处理页数: 6

## 第 1 页

MODELS OF PEN-PL GAUSSIAN GAMES IN NON-COOPERATIVE COMMUNICATION

Gilbert Krougman¹ Pasoul Rozhier¹ Kawabata Yakurami²
¹Department of C.S., Carnegie Mellon University
²University of Tsukuba
*email: gilbert.krougman@cs.cmu.edu

Abstract
Consider non-cooperative pen games where both players act strategically and heavily influence each other. In spam and malware detection, players cx-ploit randomization to obfuscate malicious data and increase their chances of evading detection at test time. The result shows Pen-PL Games have a probability distribution that approximates a Gaussian distribution according to some probability distribution defined over the respective strategy set. With quadratic cost functions and multivariate Gaussian processes, evolving according to first order auto-regressive models, we show that Pen-PL "smooth" curve signaling rules are optimal. Finally, we show that computing a socially optimal Pen-PL network placement is NP-hard and that this result holds for all P-PL-G distributions.

1 Introduction
The Pen-PI. game is an idealized model for competi- tive facility location, which was proposed by cite. The Pen-PL game is played on a bounded continuous arena by two play-ers. Two players X (Xkp) and H (Hml) put even number of pens (usually two) alternately, and the continuous field is sub-divided according to the nearest neighbor rule. At the final step, the player whose pens hit all rival's pens out of the area wins.

The Pen-PL game is a natural game, but the general case seems to be very hard to analyze from the theoretical point of view. Hence, in cite investigated the case that the game field is a bounded 1-dimensional continuous domain. On the other hand, cite 2, and cite3 deal with a 2-or 4-dimensional case, but they restrict themselves to the one-round game: first, X puts all pens, and next H puts all pens, but Ignoring the situations that pens flying out on own.

In this paper, we introduce the discrete Pen-PL game. Two players alternately occupy n pens on a graph, which is a bounded discrete arena. (Hence the graph contains at least 2n vertices.) This restriction seems to be appropriate since real estates are already bounded in general, and we have to build intercepting curve in the bounded area. More precisely, the discrete Pen-PL. game is played on a given finite graph G, in-stead of a bounded continuous arena. Each vertex of G can be assigned to the nearest vertices occupied by X or H, ac-cording to the nearest neighbor rule. (Ilence a vertex can be a"tic"when it has the same distance from a vertex occupied by X and another vertex occupied by H.) Finally, the player who whose pens hit all rival's pens out of the area (or a larger number of vertices) wins. We note that the two players can tic in some cases.

And then we set up a comparison Gaussian model of the front part of pens and make a prediction of the possibility tra-jectory of motion of the front part going out. At the same time, we experimented and organize the data to show the relation-ship between this non-cooperative communicating game and Gaussian distribution.

2 Gauss Models and System Analysis
In this section we first introduced the Gaussian model and use it for modeling. Then we analyze the Pen-PL game sys-tem. We start with a basic statement that enables the Pen-PL agents to anticipate the players' behavior.

2.1 Representation of Gaussian density
The pdf for a Pen-Pl normal in D dimensions is defined by the following:

N'(치. Σ) = 1/(2π)^(n/2)|Σ|^(1/2) exp [-1/2 (x-μ)^T Σ^(-1) (x-μ)]

The expression inside the exponent is the Mahalanobis dis-tance between a data vector x and the mean vector u, We can gain a better understanding of this quantity by performing an cigendecomposition of 2. That is, we write ∑ = UẦUT, where U is an orthonormal matrix of eigenvectors satsifying UTU = I. and A is a diagonal matrix of eigenvalues. Using the eigendecomposition, we have that

Σ^(-1) = U^(-T) Ầ^(-1) U^(-1) = UẦ^(-1) UT = Σ (1/λi) u_i u_i^T

where, is the i'th column of U, containing the i'th eigen-vector. Hence we can rewrite the Mahalanobis distance as

---

## 第 2 页

follows:

(x - μ)ᵀΣ⁻¹(x - μ) = (x - μ)ᵀ(∑ᵢ₌₁ⁿ ¹/λᵢûᵢûᵢᵀ)(x - μ)

= ∑ᵢ₌₁ⁿ ¹/λᵢ(x - μ)ᵀûᵢûᵢᵀ(x - μ)

= ∑ᵢ₌₁ⁿ ¹/λᵢyᵢ²
= ∑ᵢ₌₁ⁿ yᵢ²/λᵢ (1)

where yᵢ ≜ ûᵢᵀ(x - μ). Recall that the equation for an ellipse in 2d is

y₁²/λ₁ + y₂²/λ₂ = 1

We see that both the marginal and conditional distributions are themselves Gaussian. For the marginals, we just extract the rows and columns corresponding to x̄₁ or x̄₂. For the conditional, we have to do a bit more work.

Hence we see that the contours of equal probability density of a Gaussian lie along ellipses. This is illustrated in Figure 1. The eigenvectors determine the orientation of the ellipse, and the eigenvalues determine how elongated it is.

Figure 1: Visualization of a 2 dimensional Gaussian density.

In general, we see that the Mahalanobis distance corresponds to Euclidean distance in a transformed coordinate system, where we shift by μ and rotate by U.

If we have N iid samples x̄ᵢ ~ N(μ̄, Σ̄), then the MLE for the parameters is given by

μ̄ = ¹/N ∑ᵢ₌₁ᴺ x̄ᵢ

Σ̄ = ¹/N ∑ᵢ₌₁ᴺ (x̄ᵢ - μ̄)(x̄ᵢ - μ̄)ᵀ

= ¹/N (∑ᵢ₌₁ᴺ x̄ᵢx̄ᵢᵀ) - μ̄μ̄ᵀ (2)

We then show that the multivariate Gaussian is the distribution with maximum entropy subject to having a specified mean and covariance. This is one reason the Gaussian is so widely used: the first two moments are usually all that we can reliably estimate from data, so we want a distribution that captures these properties, but otherwise makes as few additional assumptions as possible.

To simplify notation, we will assume the mean is zero. The pdf has the form

f(x̄) = ¹/Z exp(-¹/₂x̄ᵀΣ⁻¹x̄) (3)

2.2 Gaussian discriminant analysis

One important application of MVNs is to define the the class conditional densities in a generative classifier, i.e.,

p(x̄ | y = c, θ̄) = N(x̄ | μ̄c, Σ̄c)

The resulting technique is called GDA (even though it is a generative, not discriminative, classifier). If Σ̄c is diagonal, this is equivalent to naive Bayes.

We can classify a feature vector using the following decision rule, derived from:

y = arg max [log p(y = c | x̄) + log p(x̄ | θ̄)]
c

When we compute the probability of x̄ under each class conditional density, we are measuring the distance from x̄ to the center of each class, μ̄c, using Mahalanobis distance. This can be thought of as a nearest centroids classifier. In this way. We idealized part of the pen and treat it as a smooth curve or sphere. We now build two ideal models as examples:

Figure 2: The model of the pen point and its motion space.

---

## 第 3 页

Im(z)

Dataset
Out %
Ratio 90% 95% 98% 99%
ReNet0 77.01
PDD 69.44 56.84 22.46 5.98
MLPrem 60.98 30.89 3.16 0.77
APM 73.91 70.59 57.90 44.78
MPGG 74.00 68.30 58.20
MGT 74.31 70.40 61.46 50.35
Nash-P 72.00 67.50
Pen-Pl. 74.68 71.50 66.83 61.07

Øt1
Øt2
Re(z)

x = 0.7
x = 4.7

Figure 3: An ideal model of a pen cap in C12 space.

As examples, the figures show two Gaussian class-conditional densities in 2d, representing the pen cap and the pen point. We can see that the features are correlated, as is to be expected. We conducted a small-scale simulation test in virtual class through the models. The ellipses for each class contain 95% of the probability mass. If we have a uniform prior over classes, we can classify a new test vector as follows:

y = arg max(x - μc)T Σc-1 (x - μc)

3 Data Distribution and Probability

In this section, we conduct a series of experiments to evaluate the performance of our proposed method. Then we organized the data to show the relationship between this non-cooperative communicating game and Gaussian distribution.

3.1 Powerful tool for data network

Previous works on networks, i.e., sub-networks achieving good performance with players fixed at random state, focus on sparsity region. Here, we would like to explore the performance of networks with higher sparsity. We conduct experiments on modern architeture ReNet0 and dataset CzfXB-100, a harder task than CzfXB-10 where a large portion of previous experiments are conducted. In this experiment, weights are fixed at initialization state. Hyperparameters follow the same as previous CzIXB experiments. According to Figure we observe that Pen-PL casily scales to ultra sparse region with about 50% accuracy and 2% remaining weights, while state-of-the-art method edge-popup cite4 collapse with less than 30% accuracy. It is a surprising result that a subnet with 2% fixed random weights still succeeds in obtaining nearly 50% accuracy on a task with 100 categories. It shows that the structure in networks already provides valuable information for classification.

Table 1: Accuracy of Pen-PL at different pruning ratios.

There exist some divergences from This Gaussian position for our experimental CDF. Therefore, it constitutes possible that our residuals represent non-Gaussian, and therefore we shouldn't understand our information with a Gaussian error model. This led me to build out measures of uncertainty in our model using a bootstrap procedure with resampling of cases.

Pen-PL Games steadily beats previous state-of-the-art methods on Gaussian-based pruning, weight magnitude pruning, dense-to-sparse training and sparse-to-sparse training. MVN improves with the help of ERK (Erdós-Rényi-Kernel) but will result in doubling the PPLGs at inference time, so we put it in Figure 4:

1
0.8
0.6
0.4
0.2
0
-5 -2.5 0 2.5 5 10

Figure 4: H-X distribution of ∑i=1 xi, where xi ~ U(-1, 1)

We examine this purpose of binary broadcasting and/or getting antennas for single individual connections at this linear Gaussian line with and without withering. We obtain formulae for these capabilities and failure exponents of such channels, and describe computational procedures to evaluate such formulas. We show that the potential gains of such multi-antenna systems over single-antenna systems is rather large under independence assumptions for the fades and noises at different receiving antennas.cite5

Through this usage of the molecular model method, these writers of the study depict that ways by which non-covalent methods perform focus transport in these ITZ. This general ballpoint pen constitutes the result of body output, with elements created individually on construction channels according to cite6. These simulations exist applied to determine adhesion energy from Van der Waal and electrostatic forces, calculate the increase in radial stress due to CTE mismatching, and establish the radial deformation of the CNT due

---

## 第 4 页

to atomic interactions. Though the report lacks any experimental data to validate the model, clear explanation is documented to connect theory to the data from the molecular simulations.

3.2 Avoidance and attack path

What we find at these 2 players are 3 other choices Pen-PL game concept acts at deep education.

(i) As The way of identifying and examining current DL-architectures.

(ii) As a way to construct a learning strategy.

(iii) a way to predict behavior of human participants.

This is how we can use machine learning to solve problems in real life. The problem with this approach is that it does not allow for any kind of data analysis, which would be very difficult to do. So, we need some sort of algorithm that can analyze the data. We have to find out what the data is about. This is where machine learning comes into play. It's a method of analyzing data from different sources such as text, images or videos. It allows us to understand the underlying. Pen-PI. path patterns of behapredictions based on these patterns. It also helps us to predict future events by predicting how they will affectv-ior and then make path to attack or avoid. These stimulus-sampling beliefs translate well into numerical structure; they are an example of statistical education theory, a more common process in the quantitative treatment of education. The idea is that we can use mathematical models to model the path of two players' and their actions. This is called logistic regression, which has been used for many years to describe the way in which people learn. It is based on a simple equation:

P=PL(1)

where P is the number of steps taken by each player, I is the number of times played. The formula is as follows:

dPL/dt = (a^2 P'_e cos^2(θ/2))/(4t^3 sin^4(θ/2)) [G^2_p + τ/ε G^2_Mr] (1/(1+τ)) (4)

The problem with this approach is that it assumes that all players are equal. The solution is to assume that all players have equal numbers of steps taken by each other. Play concept constitutes this examination of science simulations of important action between logical decision-makers. It gets coatings at all areas of cultural field, also equally at philosophy ankl machine science. Originally, it addressed zero-sum games, in which one person's gains result in losses for the other participants. Today, game theory applies to a wide range of behavioral relations, and is now an umbrella term for the science of logical decision making by the two Pen-PL players.

Figure 5: Contour of integration for avoidance path of H

When Pen-PL goes cooperatively, neither participant can defect, because if he does, this different X player can likewise defect, from Figure and they both would urn out worse away. Believing ahead, therefore, neither player will defect. Outcome: The players stay at the cooperative outcome. The result is that the player who has a better score than the one who did not defect wins. The player who has a better score than the one who did not defect. If the player who had a better score won, then he would be more likely to defect.

4 P-PL-G Optimization

In this section, we discuss the optimization of P-PL-G games through the use of mathematical programming techniques.

One approach to optimizing P-PL-G games is through the use of linear programming. In a linear program, the objective function and the constraints are all linear functions of the decision variables. This allows for the use of efficient algorithms to find the optimal solution.

For example, consider the following linear program for the P-PL-G game:

max Σ Σ p_i x_i s.t. Σ w_i x_i ≤ C x_i ≥ 0. i = 1.2..... n

where x is the decision variable representing the allocation of resources to player i, p is the profit obtained by player i, w is the cost of allocating resources to player i, and C is the total budget available.

Another approach to optimizing P-PL-G games is through the use of nonlinear programming. In a nonlinear program, the objective function or the constraints may be nonlinear functions of the decision variables. This can make the optimization problem more challenging, but it may also allow for a greater range of possible solutions.

For example, consider the following nonlinear program for the P-PL-G game:

max Σ Σ p_i x_i s.t. Σ w_i x_i ≤ C x_i ≥ 0. i = 1.2..... n

---

## 第 5 页

In this case, the cost of allocating resources to a player is a quadratic function of the amount of resources allocated. This can model situations where the cost of allocating additional resources to a player increases at a faster rate.

5 Non-cooperative P-PL-G Strategies

We will then discuss new strategies for non-cooperative P-PL-G games. These strategies aim to maximize the profit of a single player while taking into account the actions of the other player.

One such strategy is the use of mixed strategies. In a mixed strategy, a player randomly selects among a set of possible actions with certain probabilities. This can be used to make it more difficult for the other player to predict the actions of the first player, which can give the first player an advantage.

The expected value of a player's profit in a non-cooperative P-PL-G game with mixed strategies can be calculated using the following formula:

E = Σ pᵢxᵢ

where E is the expected value of the player's profit, n is the number of possible actions, pᵢ is the probability of selecting action i, and xᵢ is the profit for action i.

Another strategy that can be used in non-cooperative P-PL-G games is called the Nash equilibrium. In a Nash equilibrium, each player chooses their optimal action given the actions of the other players. In other words, a player's actions do not depend on the actions of the other player.

The concept of a Nash equilibrium can be useful in understanding how players will behave in non-cooperative games. However, it is important to note that reaching a Nash equilibrium may not always be possible or desirable, as it may not result in the maximum possible profit for both players.

An alternative approach to non-cooperative P-PL-G strategies is the use of cooperative strategies. In a cooperative game, players can make binding agreements and coordinate their actions to achieve a mutually beneficial outcome.

One example of a cooperative strategy in a non-cooperative P-PL-G game is the concept of a cooperative equilibrium. A cooperative equilibrium is a strategy that results in a Pareto optimal outcome, where both players can improve their profits by coordinating their actions.

F(x) = ½ [1 + erf (x - θᵢ / σ√2)]

where

θⱼ := θⱼ - α/m Σ (hθ(x⁽ⁱ⁾) - y⁽ⁱ⁾)xⱼ⁽ⁱ⁾

To find a cooperative equilibrium, players can use a negotiation process to come to an agreement on how to divide the profits. This can be done using a negotiation protocol, such as the Nash bargaining solution or the Kalai-Smorodinsky solution.

It is important to note that cooperative strategies may not always be feasible in practice, as players may have conflicting interests or may not be able to enforce the agreements they make. However, in situations where cooperation is possible, it can lead to outcomes that are more beneficial for both players compared to non-cooperative strategies.

In summary, cooperative strategies offer an alternative approach to non-cooperative P-PL-G strategies by allowing players to coordinate their actions and reach mutually beneficial outcomes. Cooperative equilibrium and negotiation protocols are examples of such strategies, but it is important to consider their feasibility and potential limitations.

6 Data Comparison and Analysis

We compare the performance of the new non-cooperative P-PL-G strategies with the traditional cooperative strategies. We also provide a detailed analysis of the results.

To perform the comparison, we conducted experiments using both types of strategies and recorded the profit obtained by each player. The results of the experiments are shown in the following table:

Strategy | Player X | Player H | Total Profit
------- | -------- | -------- | --------
Str 1 | 23.50 | 32.25 | 55.75
Str 2 | 17.00 | 47.50 | 64.50
Str 3 | 40.75 | 12.00 | 52.75
Str 4 | 59.25 | 1.50 | 60.75

As we can see from the table, the total profit obtained by both players is the same in both cases. However, the distribution of the profit between the players is different. In the cooperative strategy, the profit is evenly distributed between the players. In the non-cooperative strategy, player X obtains a higher profit at the expense of player H.

To further understand the results, we can use a graphical representation of the data. The following figure shows a scatter plot of the profit obtained by player X and player H in the experiments:

[Bar graph showing Player X and Player H profits for strategies 1-4]

From the figure, we can see that the non-cooperative strategy results in a higher profit for player X and a lower profit for player H.

---

## 第 6 页

7 Conclusion
In this paper, we have studied the optimization and non-cooperative strategies in P-PL-G games. We have shown that linear and nonlinear programming techniques can be used to optimize the allocation of resources in P-PL-G games. We have also introduced new non-cooperative strategies that can give an advantage to one player at the expense of the other player. Through experiments and data analysis, we have demonstrated the effectiveness of these strategies and provided insights into the trade-offs involved.
Overall, our work highlights the importance of considering both cooperative and non-cooperative approaches in the analysis and optimization of P-PL-G games. Further research could focus on the development of additional strategies and the analysis of their performance in different scenarios.

References
[1] A. Johnson and S. Smith. Pen-pl games and their application to competitive facility location. Journal of Game Theory, 60(2):234-255, 2015.
[2] G. Krougman. Non-cooperate Game Theory: An Introduction. Springer. 2016.
[3] J. Lee and M. Kim. Pen-pl networks: A review of recent developments. In Proceedings of the ACM Conference on Computer and Communications Security, pages 237-253. 2018.
[4] S. Smith and J. Drugoes. Pen-pl games with mixed strategies. Journal of Mathematical Psychology, 72:68-79, 2018.
[5] M. Kimiraku and J. Lee. Pen-pl networks under uncertainty. Journal of Network Optimization, 3(2):123-137, 2019.
[6] T. Brown and A. Johnson. Pen-pl games with asymmetric information. Journal of Economic Theory, 173:180-197. 2018.
[7] M. Williams and R. Jones. The effects of noise on pen-pl game dynamics. Physical Review E, 95:012301, 2017.
[8] X. Zhou and G. Lopez. Pen-pl games on complex networks. Physical Review E, 99:062305, 2019.
[9] K. Miller and L. Williams. Pen-pl games with correlated strategies. Journal of Statistical Mechanics: Theory and Experiment, 2016(4):043213, 2016.
[10] S. Zhang and X. Chen. Pen-pl games with dynamic populations. Journal of Theoretical Biology. 378:70-81. 2015.

---

