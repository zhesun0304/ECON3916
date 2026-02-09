# 📊 Lab 4 — Descriptive Statistics: Robustness in a Skewed World
**Computational Statistics & Economic Forensics**

---

## 🧠 Lab Objective: The “Tech Economist” Mindset
In traditional statistics, the **mean** is often treated as the most informative summary statistic.  
This lab challenges that assumption.

In a modern **tech-driven economy**—where data is skewed, capped, and heavy-tailed—the average becomes a *vanity metric*.  
The goal of this lab is to **understand robustness**, detect **economic anomalies**, and learn how **outliers reshape economic narratives**.

---

## 📦 Dataset
* **Source:** California Housing Dataset (Scikit-Learn)
* **Context:** Proxy for marketplace data (e.g., Zillow, Airbnb)
* **Key Feature:**  
  *`MedHouseVal` is capped at 5.0 ($500k)* → a classic **ceiling effect** common in real-world tech datasets

---

## 🔍 Phase 1 — Data Inspection & Skewness
We begin by visually and statistically inspecting the distribution of housing values.

**Key takeaway:**  
The distribution is **right-skewed and artificially capped**, meaning:
- The mean is fragile
- Tail behavior dominates economic interpretation

---

## 📐 Phase 2 — Manual Statistical Forensics (No AI)
Before automation, we manually identify outliers using **Tukey’s 1.5 × IQR rule**.

### What We Do
- Compute **Q1, Q3, and IQR**
- Construct **Tukey fences**
- Flag income outliers (`MedInc`) manually

### Why This Matters
- The **median resists distortion**
- The **mean breaks down** under extreme values
- This phase builds intuition for *why robustness matters*

---

## 📦 Visualization: IQR Outliers
A boxplot reveals how:
- High-income districts pull the mean upward
- Most observations cluster tightly below the tail

This demonstrates the **“Elon Musk Effect”** — a few extreme values distort the story of the majority.

---

## 🤖 Phase 3 — Algorithmic Anomaly Detection (Isolation Forest)
Univariate rules miss **multivariate anomalies**.

We apply **Isolation Forest**, an unsupervised ML model that detects:
- Rare
- Isolated
- Structurally unusual observations

### Features Used
- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population

### Output
A new boolean flag:
```python
outlier_iso = True / False
