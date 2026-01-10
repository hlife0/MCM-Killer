// Baseline Poisson Model
// Purpose: Verify overdispersion (if variance >> mean, need Negative Binomial)
// DATA Gate Requirement: Prior N(0,3) instead of N(0,10)

data {
  int<lower=1> N;              // 观测数
  int<lower=1> K;              // 特征数
  matrix[N, K] X;              // 特征矩阵 (已包含对数变换)
  int<lower=0> y[N];           // 奖牌数
}

parameters {
  vector[K] beta;              // 回归系数
}

model {
  // 先验 (DATA Gate 要求: N(0,3) 而非 N(0,10))
  beta ~ normal(0, 3);

  // 似然
  y ~ poisson_log(X * beta);
}

generated quantities {
  int y_rep[N];                // 后验预测
  real mean_y = mean(to_vector(y));
  real var_y = variance(to_vector(y));
  real dispersion = var_y / mean_y;  // > 1 表示 overdispersion

  for (n in 1:N)
    y_rep[n] = poisson_log_rng(X[n] * beta);
}
