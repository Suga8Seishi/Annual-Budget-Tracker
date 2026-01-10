"""Annual Budget Tracker - A fun project to learn Python."""

import csv
import json

import matplotlib.pyplot as plt

all_savings = []
all_months = []

total_saving = 0
M_OF_M = 12
for ms in range(1, M_OF_M + 1):
    print(f"\n mou num {ms} ")

    ma = int(input("in your ma مصروفك "))
    dahl = int(input("input your دخلك "))
    saving = dahl - ma

    all_savings.append(saving)
    all_months.append(ms)

    print(f"your ادخارك is {saving:,}")
    total_saving += saving


print(f"اجمالي دخلك {M_OF_M} هو {total_saving:,}")

if total_saving >= 400:
    print("جيد")
elif total_saving == 0:
    print("خسارة زيادة والديون ستطاردك ههههه")
else:
    print("ناااااااايس يا الديون")


with open("my_budget.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["الشهر", "الادخار"])
    writer.writerow(["ادخار سنة 2025", total_saving])


data = {"total_saving": total_saving, "months": M_OF_M}
with open("my_budget.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)


plt.plot(all_months, all_savings, marker="o", color="green")
plt.title("Financial Growth 2026")
plt.xlabel("Month")
plt.ylabel("Savings")
plt.grid(True)
plt.show()
