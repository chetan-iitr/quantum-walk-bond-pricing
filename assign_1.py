import math
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Question 1
def price_zero_coupon_bond(face_value,yield_rate,time_to_maturity):
    discount_factor = math.exp(-((yield_rate/100)*time_to_maturity))
    present_value = face_value*discount_factor
    return present_value

## part 1
print(f"The present value of 1-year T-bill is {price_zero_coupon_bond(1000,5,1)}")
## part 2
print(f"The present value of 5-year T-bill is {price_zero_coupon_bond(1000,5,5)}")


# Question 2
bond_values={}
for rate in range(1,21):
    bond_values[rate] = price_zero_coupon_bond(100,rate,10)
df = pd.DataFrame(
    {
        'Yield (%)': bond_values.keys(),
        'Bond Price ($)': bond_values.values()
    }
)
df['Bond Price ($)']=df['Bond Price ($)'].round(2)
print (df)


# Question 3 
# making a path for the saved plot
file_dir = Path(__file__).parent
plot_dir = file_dir/"plots"
plot_dir.mkdir(parents=True, exist_ok=True)
plot_path = plot_dir/ "bond_price_plot.png"

for maturity in [2, 10, 30]:
    bond_prices = []
    yields=[]
    for rate in range(1,21):
        yields.append(rate)
        price = price_zero_coupon_bond(100,rate,maturity)
        bond_prices.append(price)
    plt.plot(yields,bond_prices,label=f"{maturity}Y")
plt.title("Bond Price vs Yield")
plt.xlabel("Yield")
plt.ylabel("Bond price")
plt.legend()
plt.savefig(plot_path,dpi = 300)
plt.show()
        
