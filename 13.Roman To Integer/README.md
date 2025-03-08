# 🟢 Roman to Integer - LeetCode (Easy)  

## 📌 Problem Statement  

Given a **Roman numeral** `s`, convert it to an **integer**.  

Roman numerals are represented by seven different symbols:  
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are **usually written largest to smallest** from left to right, but some numbers follow special subtraction rules:  
- `IV` → 4 (5 - 1)  
- `IX` → 9 (10 - 1)  
- `XL` → 40 (50 - 10)  
- `XC` → 90 (100 - 10)  
- `CD` → 400 (500 - 100)  
- `CM` → 900 (1000 - 100)  

---

## 🔹 Example  
 
```python
Input: s = "III"  
Output: 3  

Input: s = "LVIII"  
Output: 58  
Explanation: L = 50, V = 5, III = 3  

Input: s = "MCMXCIV"  
Output: 1994  
Explanation: M = 1000, CM = 900, XC = 90, IV = 4  
