#!/usr/bin/python3

import sys
import random

from .utils import err_exit

# Module for colors
try:
    from rich import print
except:
    err_exit("Error: >rich< module not found.")

# Colors
re = "[bold red]"
cy = "[bold cyan]"
wh = "[white]"
gr = "[bold green]"
ma = "[bold magenta]"
ye = "[bold yellow]"
bl = "[bold blue]"

banner1=f"""
      {ma}Malware can not hide from us! 💪🏻
                          {wh}- by 16, 17, 54
"""
banner2=f"""
      {re}We fight against malware! 🥷🏻🥷🏻
                          {wh}- by 16, 17, 54 

"""
banner3=f"""
      {gr}Malware reverse engineering tool 🔎
                          {wh}- by 16, 17, 54
"""
banner4=f"""
      {wh}We are ready to analyze malware! 🕵️‍♂️🕵️‍♂️
                          {gr}- by 16, 17, 54
"""
banner5=f"""
        {re}Reverse Engineering tool is ready to use! 😎
                          {wh}- by 16, 17, 54
"""
banner6=f"""
      {ma}Malware are dangerous! Be aware! 💀💀
                          {bl}- by 16, 17, 54
            
"""
banner7=f"""
      {wh}Welcome to malware analysis tool! 🙏🏻
                          {gr}- by 16, 17, 54
"""
banner8=f"""
      {cy}Revere Engineering tool is ready to use! 😀
                          {wh}- by 16, 17, 54
"""
banner9=f"""
      {re}Malware be aware! ☠️
                          {ma}- by 16, 17, 54
"""
banner10=f"""
      {gr}Malware analysis is fun 🥳🥳
                          {re}- by 16, 17, 54
"""

randomBanner = random.randint(1, 10)
if randomBanner == 1:
    print(banner1)
elif randomBanner == 2:
    print(banner2)
elif randomBanner == 3:
    print(banner3)
elif randomBanner == 4:
    print(banner4)
elif randomBanner == 5:
    print(banner5)
elif randomBanner == 6:
    print(banner6)
elif randomBanner == 7:
    print(banner7)
elif randomBanner == 8:
    print(banner8)
elif randomBanner == 9:
    print(banner9)
elif randomBanner == 10:
    print(banner10)
else:
    pass