# team-10

# Sogrape Webscraper

Between the afternoon of the 23rd and the morning of the 26th October 2023, Sogrape and 42 Porto hosted a Hackathon under the following theme: “Online Wine Price Harvesting Challenge”.
The challenge the participants were tasked with was implementing a web scraping system able to collect wine prices from national online stores on a daily basis, and to develop an interactive and intuitive interface to display the same data.


We are presenting an automated web scraping website that will allow Sogrape’s employees to easily compare pricing between several retailers for the same product, and to keep track of price fluctuations over time, in an automated manner.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- [XAMPP](https://www.apachefriends.org/index.html) installed.
- [Python](https://www.python.org/downloads/) installed.

## Installation

1. **Clone the repository:**

    ```bash
    (https://github.com/hackathon-sogrape/team-10.git)
    ```

2. **Install XAMPP:**

   - Download and install [XAMPP](https://www.apachefriends.org/index.html).

3. **Start Apache and MySQL in XAMPP:**

   - Launch XAMPP Control Panel.
   - Click "Start" next to Apache and MySQL.

4. **Configure your project:**

   - Copy your project files to the XAMPP web server directory (usually `C:\xampp\htdocs\hack_dashboard` on Windows).
   - Edit your project configuration files if necessary.

5. **Install Python and required packages:**

   - Download and install [Python](https://www.python.org/downloads/).
   - Open the Windows command prompt.
   - Navigate to your project directory.
   - Install the required packages using pip:

    ```bash
    python -m pip install -r requirements.txt
    ```
    or install them individually using:
   ```bash
    pip install <package>
    ```
## Usage

1. **Start XAMPP:**

   - Launch XAMPP Control Panel.
   - Click "Start" next to Apache.
  
2. **Run an SQL server instance and use our 'mydb_wine.sql' file:**

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

    ```

4. **Access your PHP website:**

   - Ensure XAMPP is running.
   - Click "Admin" button to acces the root/index of our website.

5. **Run the Python code:**

   - Open a terminal/command prompt.
   - Navigate to your project directory.
   - Execute your Python script using the following command:

    ```bash
    python main.py
    ```
6. **Refresh the dashboard using the button**
    All the data of the SQL will appear.
   
## License

This project is licensed under the [MIT License](LICENSE).
