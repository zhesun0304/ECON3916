# 🧠 GenAI Expansion — The P.R.I.M.E. Protocol  
**From Naive Assumptions to Real-World Risk Modeling**

---

## 📌 Project Overview

This lab explores how **model assumptions shape risk estimates** in startup runway simulations.  
We begin with a *naive* independence model and progressively introduce **economic realism**, showing how correlation between revenue and burn fundamentally alters the **Probability of Ruin**.

The goal is not to “force” outcomes, but to **reveal mechanisms**.

---

## 🎯 Learning Objectives

- Understand why **population size does NOT affect confidence intervals**
- Visualize **convergence** and the **Central Limit Theorem**
- Simulate **startup runway risk** using Monte Carlo methods
- Learn why **correlation acts as a natural hedge**
- Practice **model calibration near decision boundaries**

---

## 🧪 Phase 1: Convergence & the House Edge

We simulate a bettor with a true 50% win rate over thousands of bets and show:

- Win rates converge (Law of Large Numbers)
- A 50% picker **still loses money** under -110 odds
- The breakeven line (52.38%) is rarely crossed

📉 **Key Insight:**  
> Skill without edge is still negative EV.

---

## 📐 Phase 2: The Central Limit Theorem (CLT)

We simulate sample means for different sample sizes:

- `n = 1` → chaotic, non-Normal
- `n = 2` → smoothing begins
- `n = 30` → bell-shaped, approximately Normal

Underlying data is **Uniform(0, 10)** — deliberately non-Normal.

📊 **Key Insight:**  
> Even chaos becomes predictable when averaged.

---

## 🥣 Phase 3: The Soup Analogy (Confidence Intervals)

We compute the **Margin of Error** for two populations:

- Population A: 1,000 users  
- Population B: 1,000,000 users  

Both use the same sample size (`n = 100`).

📌 Result:
```text
Margin of Error is identical.
