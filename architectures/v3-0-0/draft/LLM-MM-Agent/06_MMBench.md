# LLM-MM-Agent: MMBench 数据集

> Path: `clean version/LLM-MM-Agent/MMBench/`

---

### `__init__.py`
包初始化文件。

---

### `README.md`
数据集说明文档，介绍MMBench的组织结构、数据格式、使用方法。

---

## Dataset 目录 (`dataset/`)

存储历年MCM/ICM竞赛题目的数据文件，按年份和题目编号组织。

### `2000_C/`
2000年C题数据，包含两个CSV文件（data1.csv, data2.csv）。

### `2002_C/`
2002年C题数据，包含直方图数据（histogram.csv）和三个表格数据（table1-3.csv）。

### `2003_C/`
2003年C题数据，包含一个表格文件（table1.csv）。

### `2006_C/`
2006年C题数据，关于WHO成员国的人口、健康、经济数据。包含多个XLS文件：
- `age_data.xls`：年龄数据
- `birth_rate_data.xls`：出生率数据
- `fertility_data.xls`：生育率数据
- `hiv_aids_data.xls`：HIV/AIDS数据
- `income_data.xls`：收入数据
- `life_expectancy_0_data.xls`：预期寿命数据
- `list_WHO_member_states.xls`：WHO成员国列表
- `population_data.xls`：人口数据
- `vaccination_rate_data.xls`：疫苗接种率数据

### `2012_C/`
2012年C题数据，关于网络论坛的数据。包含Messages.csv（消息）、Names.csv（用户名）、Topics.csv（话题）。

### `2015_C/`
2015年C题数据，包含一个表格文件（table1.csv）。

### `2016_C/`
2016年C题数据，关于大学评分卡数据。包含三个XLSX文件：数据字典、学校UID、最新队列数据。

### `2017_C/`
2017年MCM C题数据（2017_MCM_Problem_C_Data.csv）。

### `2017_D/`
2017年ICM D题数据（2017_ICM_Problem_D_Data.csv）。

### `2018_C/`
2018年C题数据（ProblemCData.xlsx）。

### `2019_C/`
2019年C题数据，关于毒品管制和人口统计数据。
- `MCM_NFLIS_Data.xlsx`：毒品报告数据
- `ACS_10_5YR_DP02/` ~ `ACS_16_5YR_DP02/`：美国社区调查数据（7年数据），每个目录包含数据文件、元数据、注释

### `2020_C/`
2020年C题数据，关于亚马逊产品评论。包含三个TSV文件：吹风机、微波炉、安抚奶嘴的评论数据。

### `2020_D/`
2020年D题数据，关于足球比赛数据。包含fullevents.csv（完整事件）、matches.csv（比赛）、passingevents.csv（传球事件）。

### `2021_C/`
2021年C题数据，关于胡蜂检测和图像识别。
- `2021MCMProblemC_DataSet.xlsx`：数据集
- `2021MCM_ProblemC_Images_by_GlobalID.xlsx`：图像清单
- `2021MCM_ProblemC_Files/`：200+张胡蜂图片（JPG/PNG格式）

### `2024_C/`, `2025_C/`
最新年份的数据文件。

---

## Problem 目录 (`problem/`)

存储历年题目的JSON格式陈述。

### 文件命名规则
`{YEAR}_{LETTER}.json`，如`2000_A.json`、`2024_C.json`。

### 题目类型
- **A/B**：MCM连续型题目
- **C**：MCM数据洞察题目
- **D/E/F**：ICM跨学科题目
- **Y/Z**：其他类型

### JSON结构
每个题目文件包含：
- `year`: 年份
- `type`: 题目类型（MCM/ICM）
- `letter`: 题目编号（A/B/C/D/E/F）
- `title`: 题目标题
- `description`: 问题描述
- `requirements`: 要求
- `data_files`: 相关数据文件

---

## Evaluation 目录 (`evaluation/`)

### `__init__.py`
包初始化文件。

### `model.py`
评估模型实现，定义评估指标和方法。

### `prompts.py`
评估提示词，用于生成评估报告和质量评分。

### `run_evaluation.py`
单次评估运行器，执行单个任务或题目的评估。

### `run_evaluation_batch.py`
批量评估运行器，批量执行多个任务或题目的评估。

### `utils.py`
评估工具函数，提供评估相关的辅助功能。

---

## Example Solution 目录 (`example_solution/`)

### `example1.json`, `example2.json`
示例解决方案文件，展示标准解决方案的格式和结构。

---

## Processed Data 目录 (`processed_data/`)

存储原始数据集的处理版本，包括清洗后的数据、特征工程后的数据、预处理的缓存。避免重复处理原始数据。

---

**文档版本**: v1.0
