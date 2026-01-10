// Negative Binomial Model
// Purpose: Verify zero-inflation (if zero proportion > NB prediction, need ZINB)
// DATA Gate Requirement: Prior N(0,3) instead of N(0,10)

data {
  int<lower=1> N;              // 观测数
  int<lower=1> K;              // 特征数
  matrix[N, K] X;              // 特征矩阵 (已包含对数变换)
  int<lower=0> y[N];           // 奖牌数
}

parameters {
  vector[K] beta;              // 回归系数
  real<lower=0> theta;         // overdispersion 参数
}

model {
  // 先验 (DATA Gate 要求: N(0,3) 而非 N(0,10))
  beta ~ normal(0, 3);
  theta ~ gamma(2, 0.1);       // 弱信息先验

  // 似然
  y ~ neg_binomial_2_log(X * beta, theta);
}

generated quantities {
  int y_rep[N];                // 后验预测
  real zero_prop_obs = mean(to_vector(y) == 0);  // 观测零比例

  for (n in 1:N)
    y_rep[n] = neg_binomial_2_log_rng(X[n] * beta, theta);
}
