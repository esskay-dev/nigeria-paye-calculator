# Nigeria PAYE Tax Calculator

A simple Python command-line application that calculates **Personal Income Tax (PAYE)** in Nigeria based on the official progressive tax bands.

---

## Features

- Accepts annual income as user input
- Automatically applies Nigerian PAYE tax bands
- Calculates:
  - Gross Salary
  - Annual PAYE Tax
  - Net Income
- Handles formatted inputs (e.g. `3,600,000`)
- Outputs clean, readable currency values (₦)

---

## Nigerian PAYE Tax Bands Used

| Band | Income Range (₦) | Rate |
|:----:|------------------|:----:|
| 1 | First 800,000 | 0% |
| 2 | Next 2,200,000 | 15% |
| 3 | Next 900,000 | 18% |
| 4 | Next 13,000,000 | 21% |
| 5 | Next 25,500,000 | 23% |
| 6 | Above 50,000,000 | 25% |

---

## Tech Stack

- Python

---

## How to Run

1. Clone the repository:
   ```bash
   git clone http://localhost:8502/