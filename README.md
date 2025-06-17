# 🔍 IP-Spy

**IP-Spy** is a lightweight and powerful command-line tool built with Python that helps you trace and gather information about any public IP address. Whether you're a cybersecurity enthusiast, ethical hacker, or just curious, IP-Spy gives you quick access to location-based IP info like city, ISP, and coordinates — all from your terminal.

> 📦 Developer: **Pabit**  
> 🛠️ Tool Type: CLI  
> 🎯 Purpose: Educational / Reconnaissance  
> 🐍 Language: Python

---

## 🚀 Features

- ✅ Trace your **own public IP**
- ✅ Trace **any external IP address**
- 🌐 Shows:
  - Country
  - Region
  - City
  - ZIP code
  - Latitude & Longitude
  - ISP & Organization
- 🎨 Clean colored CLI output using `colorama`
- 🔓 Open source (MIT Licensed)

---

## 📸 Demo

```bash
$ python ip_spy.py -i 8.8.8.8

[+] IP Info for: 8.8.8.8
Country: United States
Region: California
City: Mountain View
ZIP: 94035
Latitude: 37.386
Longitude: -122.0838
ISP: Google LLC
Org: Google Public DNS
