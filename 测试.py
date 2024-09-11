import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置随机种子以确保结果可重复
np.random.seed(42)

# 生成982份样本数据
n_samples = 982

# 生成随机数据
data = {
    "practice_team": np.random.choice(["Team A", "Team B", "Team C", "Team D"], n_samples),
    "captain_id": np.random.randint(100000, 999999, n_samples),
    "location": np.random.choice(["东部地区", "中部地区", "西部地区", "其他地区"], n_samples),
    "school_type": np.random.choice(["公立学校", "私立学校", "国际学校", "其他"], n_samples),
    "grade": np.random.choice(["高一", "高二", "高三", "已毕业"], n_samples),
    "recent_exam_rank": np.random.choice(["前20名", "20~50名", "50~100名", "100~200名", "200名以后"], n_samples),
    "info_channel": np.random.choice(["微信", "抖音", "天津大学官网", "电视广告", "报纸杂志", "校园开放日", "招生讲座"], n_samples),
    "most_trusted_channel": np.random.choice(["微信", "抖音", "天津大学官网", "电视广告", "报纸杂志", "校园开放日", "招生讲座"], n_samples),
    "most_concerned_info": np.random.choice(["学科设置", "师资力量", "校园环境", "学生生活", "就业前景", "国际合作项目", "奖学金政策"], n_samples),
    "satisfaction": np.random.choice(["非常满意", "满意", "一般", "不满意", "非常不满意"], n_samples),
    "improvement_needs": np.random.choice(["内容过于单一，缺乏创新", "信息可信度不足", "缺乏详细的就业数据", "过于注重宣传而忽视真实体验"], n_samples),
    "importance_rating": np.random.uniform(1, 5, n_samples),
    "credibility_rating": np.random.uniform(1, 5, n_samples),
    "open_feedback": np.random.choice(["增加互动性内容", "提供更多学生真实体验", "加强专业特色介绍", "优化线上宣传平台"], n_samples)
}

# 创建数据框
df = pd.DataFrame(data)

# 数据分析和可视化

# 1. 满意度分布饼图
plt.figure(figsize=(10, 6))
satisfaction_counts = df['satisfaction'].value_counts()
plt.pie(satisfaction_counts, labels=satisfaction_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('天津大学招生宣传满意度分布')
plt.axis('equal')
plt.show()

# 2. 信息渠道偏好柱状图
plt.figure(figsize=(12, 6))
channel_counts = df['info_channel'].value_counts()
sns.barplot(x=channel_counts.index, y=channel_counts.values)
plt.title('获取天津大学信息的渠道偏好')
plt.xlabel('信息渠道')
plt.ylabel('选择人数')
plt.xticks(rotation=45)
plt.show()

# 3. 最受关注信息类型柱状图
plt.figure(figsize=(12, 6))
info_counts = df['most_concerned_info'].value_counts()
sns.barplot(x=info_counts.index, y=info_counts.values)
plt.title('最受关注的天津大学信息类型')
plt.xlabel('信息类型')
plt.ylabel('选择人数')
plt.xticks(rotation=45)
plt.show()

# 4. 宣传内容重要性和可信度评分箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['importance_rating', 'credibility_rating']])
plt.title('天津大学宣传内容重要性和可信度评分分布')
plt.ylabel('评分')
plt.show()

# 5. 需改进方面的柱状图
plt.figure(figsize=(12, 6))
improvement_counts = df['improvement_needs'].value_counts()
sns.barplot(x=improvement_counts.index, y=improvement_counts.values)
plt.title('天津大学招生宣传需要改进的方面')
plt.xlabel('改进方面')
plt.ylabel('选择人数')
plt.xt
