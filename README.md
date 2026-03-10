# GPU Inventory Monitor and Discord Bot

## Overview

This project is a Python based inventory monitoring tool that checks product availability on online retailers and returns the results through a Discord bot command. The current implementation focuses on monitoring GPU inventory from Newegg, but the system was designed with expansion in mind so additional retailers such as Best Buy can be added without restructuring the entire project.

The main goal of the project is to automate the process of checking stock availability for high demand hardware while also demonstrating practical software engineering concepts such as modular architecture, separation of concerns, and reusable scraping components.

Users in a Discord server can request current GPU availability using a command. The bot then runs the monitoring logic, scrapes the retailer website, formats the results, and returns a readable table directly in Discord.

## Key Features

* Real time inventory checks for GPUs on Newegg
* Discord bot command that returns current availability
* Modular architecture designed for multi retailer support
* Selenium based browser automation for dynamic websites
* Structured output formatted into clean tables for readability
* Expandable monitoring system that allows additional retailer adapters to be added easily

## How It Works

The system is designed around a modular architecture where each component has a single responsibility.

The browser module handles the creation and configuration of the Selenium WebDriver. This includes settings such as headless execution and optional proxy support.

The monitor modules contain the scraping logic for each supported retailer. Each monitor inherits from a shared base monitor which ensures that all sites expose the same interface. This allows the system to add new retailers without changing the rest of the program.

The Newegg monitor contains the logic for parsing product listings, checking stock availability, extracting product titles, prices, and links, and returning that information as structured data.

The data is then formatted into a readable table and sent back to the Discord bot, which responds to the user who issued the command.

This structure keeps the scraping logic separate from the bot logic, making the project easier to maintain and extend.

## Example Discord Command

A user in the Discord server can request current GPU inventory with the following command.

!checkgpu

The bot will scrape the configured retailer page and return a formatted table showing available GPUs, price information, and product links.

## Project Structure

main.py
- Handles the orchestration of the program and connects all modules together

browser
driver_factory.py
- Creates and configures the Selenium browser driver

monitors
base_monitor.py
- Defines the shared interface for all retailer monitors

newegg_monitor.py
- Contains the scraping logic for Newegg product listings

bestbuy_monitor.py
- Placeholder monitor for future Best Buy integration

bot
bot.py
- Handles configuration and connection of Discord bot

commands
checkgpu.py
- Creates the command !checkgpu which the user can call to trigger the NewEgg GPU inventory scraper.

utils
proxy_manager.py
- Optional proxy management for rotating requests.

data_formatter.py
- Formats data into a readable table to be displayed.




## Technologies Used

Python
Selenium WebDriver
Discord API
Pandas
Tabulate

## Future Improvements

* Additional retailer support including Best Buy and Amazon
* Proxy rotation and anti bot detection improvements
* Scheduled monitoring with automated alerts for newly available products
* Caching and filtering to detect only newly available inventory
* Docker support for easier deployment
* Cloud hosting for continuous monitoring
* Optimization of scraping performance to reduce page load time and improve data extraction efficiency.

## Purpose of the Project

Originally, this project was designed as a personal "stock checker" for GPU availability while I was looking for available GPUs to buy in early 2025 when finding a GPU available was difficult. Commonly, GPUs would be released online at a set time where other “bots” would mass buy these GPUs and resell them for a higher price. While these “buying bots” increasingly received bans and websites began cracking down on bot purchases by enabling captcha fields along with other verification processes, I decided to make a bot that notifies me of available product, so I can be one of the first to purchase my GPU. While I eventually found an available GPU by luck when testing this script in its early development, I decided to continue the project to at least a somewhat finished state to learn software architecture, automation, and web scraping while also demonstrating clean code structure that can accept multiple data sources and integrations. This project is still under development, and I plan to continue improving the bot as outlined in the Future Improvements section.

