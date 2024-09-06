from valuation import YieldCurve

# file name here
file = f"cad_ois.json"

# create a YieldCurve object
c = YieldCurve(file)

# save yield curve data as a csv file
c.csvCreate()

# YieldCurve.PV(cashflow, tenor) returns the present value of cashflow
c.present_value(1000,'1d')

# YieldCurve.showData(rowNum) shows the first rowNum rows of yield data
#c.showData(15)

# YieldCurve.showYieldCurve() plots yield curve
#c.showYieldCurve()

# YieldCurve.insight(cashflow) shows insight of the bond, such as profit, profit per day, present value
#c.insight(100)
