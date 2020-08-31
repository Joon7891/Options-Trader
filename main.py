from app import App
from options_data import *

from pricing import *

print(get_risk_free_rate(Maturity.M1))

app = App()
app.mainloop()