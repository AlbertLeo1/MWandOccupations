# Minimum Wage and Occupational Dynamics in Russia

**Researchers:** Albert Aina & Yahaya Ali  
**Academic Advisers:** Assoc. Prof. Dmitry Rudenko, Prof. Alexander Nesterov  
**Institution:** HSE University, St. Petersburg, Russia  
**Program:** Master of Data Analytics for Business and Economics  
**Year:** 2026

---

## 📋 Research Overview
Empirical analysis of minimum wage effects on occupational structures using RLMS panel data (1994-2024).

---

## 🔍 Research Questions
1. Which occupations concentrate at minimum wage thresholds?  
2. How do adjustment mechanisms differ between formal and informal sectors?  
3. What regional patterns emerge in occupational responses?

---

## 🏗️ Project Structure
\`\`\`mermaid
flowchart TD
    A[MWandOccupations] --> B[paper/]
    A --> C[data/]
    A --> D[notebooks/]
    A --> E[src/]
    A --> F[results/]
    A --> G[presentations/]
    
    B --> B1[proposal.tex]
    B --> B2[figures/]
    B --> B3[proposal.pdf]
    
    C --> C1[raw/]
    C --> C2[processed/]
    C --> C3[external/]
    
    E --> E1[data/]
    E --> E2[analysis/]
    E --> E3[visualization/]
    
    F --> F1[tables/]
    F --> F2[figures/]
\`\`\`

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- LaTeX

### Installation
\`\`\`bash
# Clone repository
git clone https://github.com/AlbertLeo1/MWandOccupations.git
cd MWandOccupations

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

---

## 📊 Data Sources
- **RLMS-HSE:** Russian Longitudinal Monitoring Survey (1994-2024)  
  - Panel: 30 years  
  - Occupational codes (3-digit OKZ)  
  - Regional identifiers
- **Regional Minimum Wage Data:**  
  - Federal MW levels (2005-2024)  
  - Regional adjustments (post-2007)

---

## 👥 Collaboration
- Use **Issues** for feedback  
- Use **Pull Requests** for changes  
- Review all changes before merging  

---

## 📧 Contact
- Albert Aina: aaina@edu.hse.ru  
- Yahaya Ali: asyahaya@edu.hse.ru  
- Prof. Rudenko: drudenko@hse.ru
