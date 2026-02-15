# 📊 Amazon Bestselling Books — Exploratory Data Analysis

## Overview

This project performs structured Exploratory Data Analysis (EDA) on Amazon’s bestselling books dataset using Python (Pandas).

The objective was to extract meaningful insights about author dominance, genre performance, rating distribution, and publishing trends through systematic aggregation and statistical analysis.

---

## Dataset Features

- Title  
- Author  
- Rating  
- Reviews  
- Price  
- Year  
- Genre  

---

## Business Questions Explored

1. Which authors dominate the bestseller landscape?
2. Does genre influence rating performance?
3. How tightly clustered are bestseller ratings?
4. What are the highest and lowest rated bestsellers?
5. How does publishing frequency vary across years?

---

## Data Preparation

✔ Removed duplicate entries  
✔ Standardized column names  
✔ Cleaned and validated dataset structure  

---

## Analytical Techniques Used

- Frequency analysis (`value_counts`)
- Grouped aggregation (`groupby`)
- Descriptive statistics
- Extremum identification (`idxmax`, `idxmin`)
- CSV export for summarized insights

---

## Key Insights

- Bestseller ratings are heavily concentrated between 4.5–4.9.
- A small number of authors repeatedly dominate the rankings.
- Genre differences exist but average ratings remain relatively close.
- High ratings are common among bestsellers, suggesting potential platform bias or curated listing effects.
- Commercial success is not determined by ratings alone.

---

## Output Files

- `top_authors.csv` — Top 10 most frequent authors  
- `avg_rating_by_genre.csv` — Average rating grouped by genre  

---

## Tech Stack

Python  
Pandas  

---

## Future Enhancements

- Add visualization layer (Matplotlib / Seaborn)
- Perform price vs rating correlation analysis
- Build an interactive dashboard (Streamlit / Tableau)
- Extend into predictive modeling

---

Computer Science Student | Aspiring Data Analyst  
Focused on structured data storytelling and insight extraction.
