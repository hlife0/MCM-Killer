// Full Zero-Inflated Negative Binomial Hierarchical Model
// Purpose: Complete implementation of model_design_1.md Section 3
// DATA Gate Requirements:
//   1. Prior N(0,3) instead of N(0,10)
//   2. Non-centered parameterization for random effects
//   3. Increased warmup to 1500

data {
  int<lower=1> N;                          // 观测数
  int<lower=1> K;                          // 特征数
  int<lower=1> J;                          // 国家数
  int<lower=0> y[N];                       // 奖牌数
  matrix[N, K] X;                          // 特征矩阵
  int<lower=1, upper=J> country_idx[N];    // 国家索引
}

parameters {
  // 固定效应 (均值模型)
  vector[K] beta;

  // 随机效应 (非中心化参数化 - DATA Gate 要求)
  vector<lower=0>[2] sigma;                // 随机效应标准差
  vector[J] z_u;                           // 标准化随机效应 (截距)
  vector[J] z_v;                           // 标准化随机斜率

  // 零膨胀参数
  vector[K] gamma;                         // 零膨胀线性预测器系数
  real<lower=0> theta;                     // NB overdispersion
}

transformed parameters {
  // 非中心化参数化 (DATA Gate 要求: 提高采样效率)
  vector[J] u = sigma[1] * z_u;            // 国家随机截距
  vector[J] v = sigma[2] * z_v;            // 国家随机斜率

  // 均值线性预测器 (log 链接)
  vector[N] mu = X * beta;

  // 添加随机效应 (国家 + 国家×时间交互)
  for (n in 1:N) {
    mu[n] = mu[n] + u[country_idx[n]] + v[country_idx[n]] * X[n, 5];  // X[:,5] = year_normalized
  }

  // 零膨胀概率线性预测器 (logit 链接)
  vector[N] logit_pi = X * gamma;
}

model {
  // 先验 (DATA Gate 要求: N(0,3) 而非 N(0,10))
  beta ~ normal(0, 3);
  gamma ~ normal(0, 3);

  // 超先验 (分层)
  sigma ~ cauchy(0, 2);
  z_u ~ normal(0, 1);                       // 非中心化
  z_v ~ normal(0, 1);                       // 非中心化

  theta ~ gamma(2, 0.1);

  // 似然 (零膨胀负二项)
  for (n in 1:N) {
    if (y[n] == 0) {
      // P(y=0) = pi + (1-pi) * NB(0)
      target += log_mix(inv_logit(logit_pi[n]),
                       0,
                       neg_binomial_2_log_lpmf(y[n] | mu[n], theta));
    } else {
      // P(y>0) = (1-pi) * NB(y)
      target += log1m(inv_logit(logit_pi[n])) +
                neg_binomial_2_log_lpmf(y[n] | mu[n], theta);
    }
  }
}

generated quantities {
  int y_rep[N];                            // 后验预测
  real log_lik[N];                         // 用于 LOO-CV

  for (n in 1:N) {
    real pi = inv_logit(logit_pi[n]);

    // 后验预测
    if (bernoulli_rng(pi))
      y_rep[n] = 0;
    else
      y_rep[n] = neg_binomial_2_log_rng(mu[n], theta);

    // 对数似然 (用于模型比较)
    if (y[n] == 0) {
      log_lik[n] = log_sum_exp(
        log(pi),
        log1m(pi) + neg_binomial_2_log_lpmf(y[n] | mu[n], theta)
      );
    } else {
      log_lik[n] = log1m(pi) + neg_binomial_2_log_lpmf(y[n] | mu[n], theta);
    }
  }
}
