# 🧪 Lab 6: The Architecture of Bias

## 📌 Project Overview
This lab investigates how **bias enters machine learning systems before any model is trained**, focusing on the **Data Generating Process (DGP)**, sampling mechanisms, and experimental integrity. The project demonstrates that many downstream model failures originate from **data collection and assignment errors**, not algorithm choice.

---

## 🎯 Objective
To analyze and diagnose multiple forms of data bias—including **sampling variance, covariate shift, and experimental assignment failure**—using principled statistical and econometric techniques.

---

## 🛠 Tech Stack
- **Python**
- **pandas / numpy** — data manipulation and simulation
- **scipy.stats** — Chi-Square hypothesis testing
- **scikit-learn** — stratified sampling utilities
- **seaborn** — dataset ingestion (Titanic)

---

## 🔬 Methodology

### 1️⃣ Simple Random Sampling & Variance Demonstration
- Manually implemented **Simple Random Sampling (SRS)** using NumPy index shuffling.
- Split the Titanic dataset into 80/20 Train/Test sets.
- Quantified **sampling variance** by comparing survival rates across splits.
- Demonstrated how naïve random sampling can introduce **non-trivial bias** even under correct assumptions.

---

### 2️⃣ Stratified Sampling to Eliminate Covariate Shift
- Identified passenger class (`pclass`) as a major driver of survival probability.
- Applied **Stratified Sampling** using `sklearn.train_test_split(..., stratify=...)`.
- Enforced identical class distributions across Train and Test sets.
- Verified elimination of covariate shift through distributional checks.

---

### 3️⃣ Sample Ratio Mismatch (SRM) Forensic Audit
- Simulated an A/B experiment with a planned 50/50 split.
- Detected imbalance between Control and Treatment groups.
- Applied a **Chi-Square Goodness-of-Fit Test** to distinguish:
  - Random fluctuation  
  - Engineering failures (e.g., load balancer bias, routing bugs)
- Interpreted SRM as a **pipeline integrity failure**, not experimental noise.

---

## 📐 Key Concepts Demonstrated
- Data Generating Process (DGP)
- Sampling variance vs. systematic bias
- Covariate shift
- Sample Ratio Mismatch (SRM)
- Statistical forensics in experimentation
- Pre-model bias diagnostics

---

## 🧠 Theoretical Extension: Survivorship Bias & Ghost Data

### ❓ Why does analyzing only successful Unicorn startups lead to Survivorship Bias?

When analyzing only **successful Unicorn startups** (e.g., those featured on TechCrunch), the dataset is **conditionally observed**:
- Startups appear **only if they survive and succeed**
- Failed, unfunded, or quietly exited startups are systematically missing

This leads to **Survivorship Bias**, where estimated relationships (e.g., between strategy, funding, or founder traits and success) are **upward biased**, because failure cases are excluded by construction.

---

### 👻 What specific Ghost Data is required to fix this using a Heckman Correction?

To correct this bias using a **Heckman Selection Model**, you need **selection-stage Ghost Data**, including:

- **Non-Unicorn startups** that:
  - Failed
  - Shut down
  - Never received media coverage
- Variables affecting *selection* but not *outcomes*, such as:
  - Geographic ecosystem strength
  - Industry funding climate
  - Investor network access
  - Media exposure probability

This Ghost Data allows modeling:
1. **Selection Equation**: Probability of being observed (featured / surviving)
2. **Outcome Equation**: Performance conditional on selection

Without observing the *unselected population*, causal inference is structurally impossible.

---

## ✅ Takeaway
Bias is often **architectural**, not algorithmic.  
Understanding *who enters the dataset—and why* is as important as model accuracy itself.

This lab emphasizes that **fairness, validity, and causality begin at data ingestion**, not model tuning.
