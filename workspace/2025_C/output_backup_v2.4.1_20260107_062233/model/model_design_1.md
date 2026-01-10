# 模型设计 v1

## 问题建模

### 1.1 问题类型

这是一个**面板数据零膨胀计数预测问题**，具有以下数学特征：

- **响应变量**：非负整数（奖牌数）
- **数据结构**：T × N 面板（时间 × 国家）
- **零膨胀**：P(Y = 0) 显著高于标准分布
- **层次结构**：国家 → 项目 → 时间
- **不确定性要求**：需要提供预测区间

### 1.2 数学框架

采用**贝叶斯零膨胀分层负二项模型**（Bayesian Zero-Inflated Hierarchical Negative Binomial Model）

---

## 变量定义

### 2.1 索引（Indices）

| 符号 | 含义 | 范围 |
|------|------|------|
| i | 国家编号 | 1, 2, ..., N |
| t | 年份（奥运会） | 1896, 1900, ..., 2024, 2028 |
| s | 运动项目 | 1, 2, ..., S |
| k | 奖牌类型 | Gold, Total |

### 2.2 响应变量（Response Variables）

| 符号 | 含义 | 类型 | 范围 |
|------|------|------|------|
| Y<sub>Gold,i,t</sub> | 国家i在年份t的金牌数 | 离散 | {0, 1, 2, ...} |
| Y<sub>Total,i,t</sub> | 国家i在年份t的总奖牌数 | 离散 | {0, 1, 2, ...} |
| Z<sub>i,t</sub> | 是否获奖（零膨胀指示） | 二值 | {0, 1} |

### 2.3 解释变量（Predictors）

| 符号 | 含义 | 类型 | 说明 |
|------|------|------|------|
| Host<sub>t</sub> | 主办国标识 | 二值 | Host<sub>t</sub> = 1 当国家i是主办国 |
| Events<sub>t</sub> | 该届奥运会项目总数 | 连续 | 影响总奖牌池 |
| Year<sub>t</sub> | 标准化年份 | 连续 | 捕捉长期趋势 |
| Lag<sub>Y,i,t-1</sub> | 上一届奖牌数 | 离散 | 自回归项 |
| Coach<sub>i,t</sub> | 教练效应指标 | 连续 | （教练效应专用） |
| X<sub>s,t</sub> | 项目s在年份t的奖牌数 | 离散 | 用于项目-国家匹配 |

### 2.4 潜变量（Latent Variables）

| 符号 | 含义 | 类型 |
|------|------|------|
| μ<sub>i,t</sub> | 负二项均值参数 | 连续 |
| π<sub>i,t</sub> | 零膨胀概率 | 连续 ∈ [0,1] |
| θ | 过程离散度参数 | 连续 > 0 |
| u<sub>0,i</sub> | 国家随机截距 | 连续 |
| v<sub>1,i</sub> | 国家随机斜率（时间） | 连续 |
| ε<sub>i,t</sub> | 时间随机效应 | 连续 |

---

## 目标函数

### 3.1 主模型：零膨胀负二似然（Zero-Inflated Negative Binomial Likelihood）

对于金牌模型：

$$
Y_{Gold,i,t} \sim \text{Zero-Inflated Negative Binomial}(\mu_{Gold,i,t}, \theta_{Gold}, \pi_{Gold,i,t})
$$

概率质量函数：

$$
P(Y_{Gold,i,t} = y) = \begin{cases}
\pi_{Gold,i,t} + (1-\pi_{Gold,i,t}) \cdot \left(\frac{\theta_{Gold}}{\theta_{Gold} + \mu_{Gold,i,t}}\right)^{\theta_{Gold}} & \text{if } y = 0 \\
(1-\pi_{Gold,i,t}) \cdot {y + \theta_{Gold} - 1 \choose y} \left(\frac{\mu_{Gold,i,t}}{\theta_{Gold} + \mu_{Gold,i,t}}\right)^y \left(\frac{\theta_{Gold}}{\theta_{Gold} + \mu_{Gold,i,t}}\right)^{\theta_{Gold}} & \text{if } y > 0
\end{cases}
$$

类似地定义总奖牌模型。

### 3.2 链接函数（Link Functions）

**均值模型**（log链接）：

$$
\log(\mu_{Gold,i,t}) = \beta_{Gold,0} + \beta_{Gold,1} \cdot Host_{i,t} + \beta_{Gold,2} \cdot \log(Events_t) + \beta_{Gold,3} \cdot Year_t + \beta_{Gold,4} \cdot \log(Y_{Gold,i,t-1} + 1) + u_{Gold,0,i} + v_{Gold,1,i} \cdot Year_t + \varepsilon_{Gold,i,t}
$$

**零膨胀模型**（logit链接）：

$$
\text{logit}(\pi_{Gold,i,t}) = \gamma_{Gold,0} + \gamma_{Gold,1} \cdot \text{PastSuccess}_{i,t} + \gamma_{Gold,2} \cdot Host_{i,t} + w_{Gold,i}
$$

其中：

$$
\text{PastSuccess}_{i,t} = \frac{1}{4}\sum_{\tau=1}^{4} \mathbb{I}(Y_{Gold,i,t-\tau} > 0)
$$

### 3.3 分层先验（Hierarchical Priors）

**国家随机效应**：

$$
\begin{aligned}
u_{Gold,0,i} &\sim \mathcal{N}(0, \sigma_u^2) \\
v_{Gold,1,i} &\sim \mathcal{N}(0, \sigma_v^2) \\
w_{Gold,i} &\sim \mathcal{N}(0, \sigma_w^2)
\end{aligned}
$$

**超先验**（Hyperpriors）：

$$
\begin{aligned}
\sigma_u, \sigma_v, \sigma_w &\sim \text{Half-Cauchy}(0, 2) \\
\beta_{Gold,k} &\sim \mathcal{N}(0, 10) \quad \forall k \\
\gamma_{Gold,k} &\sim \mathcal{N}(0, 5) \quad \forall k \\
\theta_{Gold} &\sim \text{Gamma}(2, 0.1)
\end{aligned}
$$

---

## 约束条件

### 4.1 数据约束

1. **非负性**：Y<sub>i,t</sub> ≥ 0 ∀ i, t
2. **整数性**：Y<sub>i,t</sub> ∈ ℤ<sub>≥0</sub> ∀ i, t
3. **时间连续性**：相邻奥运会间隔4年（除特殊情况）
4. **奖牌总数**：Y<sub>Total,i,t</sub> ≥ Y<sub>Gold,i,t</sub> ∀ i, t

### 4.2 模型约束

1. **零膨胀概率**：0 ≤ π<sub>i,t</sub> ≤ 1
2. **离散度**：θ > 0
3. **方差**：σ<sub>u</sub>, σ<sub>v</sub>, σ<sub>w</sub> > 0

### 4.3 预测约束

1. **总和约束**：∑<sub>i</sub> Y<sub>k,i,t</sub> ≤ TotalMedals<sub>t</sub> （奖牌池上限）
2. **单调性**：Y<sub>Gold,i,t</sub> 的预测应与历史趋势一致（极端情况除外）

---

## 求解策略

### 5.1 贝叶斯推断框架

使用**哈密顿蒙特卡洛**（Hamiltonian Monte Carlo - HMC）进行后验推断。

**工具选择**：
- **Stan** (推荐) 或 **PyMC** 作为概率编程框架
- 4条链，每条2000次迭代（warmup: 1000, sampling: 1000）
- 收敛诊断：$\hat{R} < 1.01$, ESS > 400

### 5.2 具体步骤

#### Step 1: 数据预处理（交给 data_engineer）
1. 标准化所有连续变量
2. 处理缺失值（多重插补或删除）
3. 构建lag features
4. 标准化国家名称

#### Step 2: Baseline模型
1. 简单Poisson回归
2. 检查overdispersion（方差/均值比）
3. 评估零膨胀程度

#### Step 3: 完整模型
1. Zero-Inflated Negative Binomial
2. 加入随机效应
3. 加入自回归项

#### Step 4: 模型比较
1. WAIC / LOO-CV 比较
2. 后验预测检验
3. 残差分析

#### Step 5: 2028年预测
1. 生成后验预测分布
2. 提取预测区间（2.5%, 50%, 97.5% 分位数）
3. 识别进步/退步国家

#### Step 6: 敏感性分析
1. 不同先验的影响
2. 不同模型规格的影响

---

## 所需特征

### 6.1 核心特征（必需）

| 特征名 | 来源 | 类型 | 计算方法 |
|--------|------|------|----------|
| gold_lag1 | summerOly_medal_counts.csv | 离散 | Y<sub>Gold,i,t-4</sub> |
| gold_lag2 | summerOly_medal_counts.csv | 离散 | Y<sub>Gold,i,t-8</sub> |
| total_lag1 | summerOly_medal_counts.csv | 离散 | Y<sub>Total,i,t-4</sub> |
| host_flag | summerOly_hosts.csv | 二值 | 1 if 国家i = 主办国, else 0 |
| events_count | summerOly_programs.csv | 连续 | ∑<sub>s</sub> Events<sub>s,t</sub> |
| year_normalized | - | 连续 | (Year - 1896) / (2024 - 1896) |
| past_success | derived | 连续 | 过去4届获奖比例 |

### 6.2 项目层面特征（用于项目分析）

| 特征名 | 来源 | 类型 | 计算方法 |
|--------|------|------|----------|
| country_sport_match | derived | 离散 | 国家在该项目的历史奖牌数 |
| sport_importance | derived | 连续 | 该项目对该国的贡献率 |
| host_sport_advantage | derived | 连续 | 主办国在该项目的优势系数 |

### 6.3 教练效应特征（用于教练分析）

| 特征名 | 来源 | 类型 | 计算方法 |
|--------|------|------|----------|
| coach_change_indicator | derived | 二值 | 识别著名教练流动年份 |
| post_change_dummy | derived | 二值 | 教练流动后的窗口期 |
| treatment_intensity | derived | 连续 | 受影响运动员数量 |

**注意**：这些特征需要从 athlete 数据中推导。

---

## 预期输出

### 7.1 模型参数输出

| 输出 | 类型 | 说明 |
|------|------|------|
| β<sub>k</sub> | 后验分布 | 固定效应系数 |
| u<sub>0,i</sub> | 后验分布 | 国家随机效应（实力） |
| v<sub>1,i</sub> | 后验分布 | 国家时间趋势 |
| σ<sub>u</sub>, σ<sub>v</sub> | 后验分布 | 层次方差 |
| θ | 后验分布 | 离散度参数 |
| π<sub>i,t</sub> | 后验分布 | 零膨胀概率 |

### 7.2 预测输出

| 输出 | 类型 | 说明 |
|------|------|------|
| Ŷ<sub>Gold,i,2028</sub> | 预测分布 | 2028年各国金牌预测 |
| Ŷ<sub>Total,i,2028</sub> | 预测分布 | 2028年各国总奖牌预测 |
| CI<sub>95%</sub> | 区间 | 95% 预测区间 |
| P(Y > 0)<sub>i,2028</sub> | 概率 | 首次获奖概率 |
| ΔY<sub>i</sub> = Ŷ<sub>i,2028</sub> - Y<sub>i,2024</sub> | 分布 | 变化量（进步/退步） |

### 7.3 模型评估输出

| 指标 | 公式 | 目标 |
|------|------|------|
| RMSE | √(∑(Ŷ - Y)² / n) | 最小化 |
| MAE | ∑\|Ŷ - Y\| / n | 最小化 |
| CRPS | ∑∫(F(y) - 1(y≥Y))²dy | 最小化 |
| PIT均匀性 | - | 接近均匀 |
| Coverage | P(Y ∈ CI) | 接近名义水平 |

### 7.4 可视化输出（给 visualizer）

1. **预测地图**：世界地图上展示2028年预测奖牌数
2. **时间序列图**：历史数据 + 预测 + 不确定性带
3. **排名变化**：2024 vs 2028排名变化
4. **随机效应图**：各国实力排名（u<sub>0,i</sub>）
5. **项目重要性**：各国优势项目热力图
6. **零膨胀概率**：首次获奖国家地图

---

## 模型假设

### 8.1 核心假设

1. **马尔可夫性**：Y<sub>t</sub> 只依赖于 Y<sub>t-1</sub>, Y<sub>t-2</sub>, ...，不依赖更早历史
2. **平稳性**：随机效应的分布不随时间变化
3. **可交换性**：在观察到数据前，国家是可交换的（通过层次结构建模差异）
4. **条件独立性**：给定随机效应和协变量，各国家的观测相互独立

### 8.2 需要验证的假设

1. **线性趋势**：Year 对 log(μ) 的影响是线性的
2. **overdispersion稳定性**：θ 不随时间或国家变化
3. **零膨胀机制**：零 inflation 的 logistic 模型设定正确

---

## 教练效应子模型

### 9.1 识别策略

使用 **合成控制方法**（Synthetic Control Method）：

对于每个著名教练案例：

1. **定义处理单元**：聘请教练的国家-项目组合
2. **构建合成对照**：使用未聘请教练的相似国家加权平均
3. **估计效应**：Δ = Y<sub>treated</sub> - Y<sub>synthetic</sub>

### 9.2 相似性度量

$$
\text{Similarity}_{i,j} = \sum_{k} w_k \cdot |X_{i,k} - X_{j,k}|
$$

其中 X 包括：
- 历史奖牌数
- 参赛项目数
- GDP（如果有）
- 地理区域

### 9.3 效应估计

$$
\hat{\tau}_{coach} = \frac{1}{T_{post}} \sum_{t \in T_{post}} (Y_{i,t} - \hat{Y}_{i,t}^{synthetic})
$$

显著性检验： placebo test（随机分配处理时间）

---

## 实现建议

### 10.1 软件/包

| 任务 | 推荐工具 |
|------|---------|
| 贝叶斯建模 | **Stan** (cmdstanr 或 rstan) 或 **brms** (R) |
| 数据处理 | pandas, numpy (Python) 或 data.table (R) |
| 可视化 | matplotlib, seaborn (Python) 或 ggplot2 (R) |
| 预测区间 | 后验预测分布 |

### 10.2 计算资源

- **内存**：至少 8GB RAM（用于存储后验样本）
- **时间**：完整模型可能需要 2-6 小时运行
- **并行**：使用多链并行运行

### 10.3 代码结构

```
model/
├── data_preprocessing.py    # 数据预处理
├── baseline_model.stan       # Stan baseline模型代码
├── full_model.stan           # Stan完整模型代码
├── fit_model.R               # 模型拟合脚本
├── diagnostics.R             # 模型诊断
├── predict_2028.R            # 预测脚本
└── coach_analysis.py         # 教练效应分析
```

---

## 模型验证计划

### 11.1 交叉验证

**时间序列交叉验证**：
- 训练集：1896-2000
- 验证集：2004-2020
- 测试集：2024

### 11.2 后验预测检验

生成 replicated data Y<sup>rep</sup> 并比较：
- 分布形状
- 零的比例
- 极值比例
- 时间序列相关性

### 11.3 模型比较

使用 **Leave-One-Out Cross-Validation** (LOO-CV)：
- 计算LOOIC
- 模型权重比较

---

## 不确定性来源

### 12.1 参数不确定性
- 后验分布的宽度
- 通过 MCMC 样本自然量化

### 12.2 过程不确定性
- 负二项的 overdispersion
- 通过 θ 参数量化

### 12.3 模型不确定性
- 不同模型规格的差异
- 通过贝叶斯模型平均（BMA）或多模型比较

### 12.4 数据不确定性
- 测量误差
- 国家名称变化
- 通过数据敏感性分析

---

## 风险与缓解

| 风险 | 影响 | 缓解策略 |
|------|------|---------|
| 零膨胀模型不收敛 | 无法获得预测 | 简化为标准NB模型 |
| 计算时间过长 | 无法完成 | 使用variational Bayes近似 |
| 2028年超出历史范围 | 预测不可靠 | 使用保守预测区间 |
| 教练效应无法识别 | 无法完成需求5 | 转为相关性分析 |

---

**设计完成时间**: 2026-01-05T15:45:00Z
**Modeler**: v1
**下一步**: 交给 feasibility_checker 评估可行性
