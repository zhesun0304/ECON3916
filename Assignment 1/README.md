# 📊 The Cost of Living Crisis: A Data-Driven Analysis

## 📌 Project Overview
Official inflation statistics suggest that price pressures in the United States have moderated in recent years.  
However, for students living in **high-cost urban areas**—such as **Boston**—everyday expenses tell a very different story.

The national **Consumer Price Index (CPI)** is a population-weighted average designed to reflect the spending patterns of a “typical” consumer. While appropriate for macroeconomic monitoring, this average masks substantial heterogeneity across subpopulations. Students face a **distinct consumption basket**, dominated by tuition, rent near universities, and food away from home, that is poorly represented in the official CPI.

This project investigates whether national inflation metrics **systematically understate the cost-of-living pressures experienced by students**, and quantifies the extent of this divergence using a custom price index.

---

## 🎯 Research Question
**Does the national CPI accurately capture inflation as experienced by students living in high-cost urban environments, or does it understate their true cost-of-living growth?**

---

## 🧠 Conceptual Motivation: Why the “Average” CPI Fails Students
The CPI is constructed using expenditure weights derived from the **average U.S. household**.  
Students, however, differ from the typical consumer in several key ways:

- A larger share of spending is allocated to **housing near universities**
- **Tuition and fees** play a central role in annual expenses
- Consumption skews toward **food away from home** rather than groceries
- Certain discretionary services (e.g., streaming platforms) have higher relative importance

Because these categories either receive **lower weights** or are **excluded entirely** from the official CPI basket, student-experienced inflation may diverge substantially from national averages. This project formalizes that intuition using index theory and data.

---

## 🛠️ Methodology
I constructed a custom **Student Spending Price Index (Student SPI)** using Python and publicly available data from the **Federal Reserve Economic Data (FRED) API**.

### Data Sources
The analysis integrates the following CPI series:
- **National CPI (CPIAUCSL)** as the benchmark measure of overall U.S. inflation  
- **Boston–Cambridge–Newton CPI (CUURA103SA0)** to capture regional price dynamics  

### Student-Relevant CPI Components
To proxy student consumption, I selected CPI sub-components that closely align with student spending patterns:
- Tuition and fees  
- Rent of primary residence  
- Food away from home (restaurant prices)  
- Streaming services  

### Index Construction
- All CPI series were **re-indexed to a common base year (2016 = 100)** to ensure comparability across differing CPI base years  
- Following **Laspeyres price index theory**, I applied **student-specific expenditure weights** to construct the Student SPI  
- Inflation trends were visualized and compared across:
  - National CPI  
  - Regional (Boston-area) CPI  
  - Student Spending Price Index  

This framework allows for a direct comparison between official inflation measures and student-experienced cost growth over time.

---

## 📈 Key Findings
The analysis reveals a persistent and widening divergence between official inflation metrics and student-experienced inflation:

- Student-relevant expenses have increased **substantially faster** than the national CPI since 2016  
- By **2024–2025**, the Student SPI exceeds the national CPI by approximately **10–15 percentage points**, indicating a sustained inflation gap  
- Inflation in the **Boston metropolitan area** consistently tracks above the national average, underscoring the importance of geographic context  
- The divergence between national CPI and Student SPI **widens over time**, suggesting that national averages systematically understate cost-of-living pressures faced by students in high-cost urban environments  

---

## 📘 Interpretation & Implications
These results demonstrate how **index construction**, **expenditure weighting**, and **geographic variation** fundamentally shape measured inflation.

While the national CPI remains a critical macroeconomic indicator, it is not well-suited to capture the lived experiences of subpopulations with distinct consumption baskets. For students, expenses such as **tuition** and **urban housing** exert disproportionate influence, leading to inflation rates that exceed national averages.

The findings highlight the importance of **distributional and subgroup-specific price indices** when evaluating economic well-being, affordability, and policy impacts.

---

## 🧰 Tools & Skills Demonstrated
- **Python** (*pandas, matplotlib*)  
- **API-based data collection** (*fredapi*)  
- **Index normalization** and **Laspeyres price index construction**  
- Economic reasoning and data storytelling  
- Visualization of **regional and distributional inflation disparities**  

---

## 📎 Notes
This
