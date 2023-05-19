# This entrypoint file to be used in development. Start by reading README.mdfrom pytest import main
#
from arithmetic_arranger import arithmetic_arranger
from time_calculator import add_time

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(add_time("11:55 PM", "72:12", "wednesday"))

# Run unit tests automatically
# main(['-vv'])
