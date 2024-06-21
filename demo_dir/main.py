from banking import BnkAcc, SAcc, Cust

c = Cust("Jane", 67890)
chk_acc = BnkAcc(3, 800)
sav_acc = SAcc(4, 1500, 0.03)
c.add_acc(chk_acc)
c.add_acc(sav_acc)
chk_acc.dep(300)
chk_acc.wdraw(200)
sav_acc.ai()

print(f"Chk bal: ${chk_acc.b}")
print("Chk trans:")
for tr in chk_acc.t:
    print(f"{tr.d}: {tr.t} of ${tr.a}")

print(f"Sav bal: ${sav_acc.b}")
print("Sav trans:")
for tr in sav_acc.t:
    print(f"{tr.d}: {tr.t} of ${tr.a}")

print(f"Tot bal for {c.nm}: ${c.get_tot_bal()}")

