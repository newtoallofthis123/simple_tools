import subprocess

Hi = "Hello World"
useless_cat_call = subprocess.run(["cat"], stdout=subprocess.PIPE, text=True, input=Hi,shell=True)
print(useless_cat_call.stdout)