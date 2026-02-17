## 📊 Audit 02: Deconstructing Statistical Lies

This audit investigates how **seemingly “strong” metrics can systematically mislead decision-makers** when robustness, base rates, or missing data are ignored.  
The analysis is organized around three common statistical failure modes.

---

### 🧱 1. Latency Skew & Fragile Metrics
**Problem:** Average latency was inflated by a small number of extreme outliers.  
**Method:** Compared **Standard Deviation (SD)** vs **Median Absolute Deviation (MAD)** using manual implementations.  
**Finding:**  
- SD exploded in the presence of 20 extreme delays  
- MAD remained stable, correctly reflecting typical system performance  

**Insight:** Metrics based on squared deviations are fragile; robust statistics are essential for skewed systems.

---

### 🎯 2. False Positives & the Base Rate Fallacy
**Problem:** A plagiarism detector advertised “98% accuracy,” masking real-world risk.  
**Method:** Bayesian audit of posterior probability \( P(\text{Cheater} \mid \text{Flagged}) \) across different base rates.  
**Finding:**  
- In low-incidence settings (0.1% base rate), **most flagged cases were innocent**
- High sensitivity and specificity do **not** guarantee reliable decisions  

**Insight:** Accuracy claims without base rates are meaningless and can cause severe institutional harm.

---

### ⚰️ 3. Survivorship Bias & Missing Failures
**Problem:** Financial platforms report performance using only surviving assets.  
**Method:** Simulated 10,000 token launches using a heavy-tailed (Pareto) distribution.  
**Finding:**  
- Mean market cap of “survivors” was orders of magnitude higher than the full population  
- Ignoring failed tokens creates a false narrative of success  

**Insight:** Deleting failures is equivalent to falsifying the data-generating process.

---

### ✅ Key Takeaway
Statistical lies are rarely caused by bad math — they emerge from **bad assumptions**.  
Robust metrics, Bayesian reasoning, and full population visibility are necessary to preserve analytical integrity.
