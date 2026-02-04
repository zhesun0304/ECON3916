## 🎯 Purpose of This Lab

**The goal of this lab is to evaluate how modeling assumptions affect risk measurement and capital planning.**  
Standard Monte Carlo simulations often assume that revenue drivers follow a Normal (bell-curve) distribution. While convenient, this assumption understates the likelihood of extreme outcomes observed in real markets.

This lab introduces a **fat-tail stress test** by replacing normally distributed new sales with a **Student’s *t*-distribution**, which allows for more frequent extreme positive and negative outcomes.

---

## 📉 Why Fat Tails Matter

Empirical evidence from financial markets, crypto exchanges, and SaaS businesses shows that rare but severe shocks occur more often than predicted by normal distributions. These “fat-tail” events can arise from:
- Market crashes or liquidity shocks  
- Failed enterprise deals  
- Sudden regulatory or platform disruptions  

Ignoring fat tails can lead to **systematic underestimation of downside risk**.

---

## 🔬 What This Lab Tests

This phase compares two Monte Carlo revenue models:

- **Baseline Model:**  
  New sales follow a Normal distribution

- **Stress-Test Model:**  
  New sales follow a scaled Student’s *t*-distribution (fat tails)

Both models are calibrated to the same average sales level and volatility to isolate the impact of tail risk.

---

## 📊 Key Risk Metrics Evaluated

- **Probability of Revenue Decline**  
- **Value at Risk (VaR)** — the 5th percentile of projected revenue outcomes  

These metrics focus on **downside exposure**, not average performance.

---

## 🧠 Key Insight

> Even when average revenue appears stable, fat-tail models reveal deeper and more frequent downside risks.

As a result, the fat-tail model implies **higher required capital reserves** to ensure solvency under extreme but plausible stress scenarios.

---

## ✅ Learning Outcome

This lab demonstrates that **risk is driven by tail behavior, not averages**.  
Stress testing with fat-tailed distributions provides a more realistic and conservative assessment of revenue risk than traditional normal-based models.
