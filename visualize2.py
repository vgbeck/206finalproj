import requests
import json
import os
import sqlite3
import ssl
import pprint
import matplotlib.pyplot as plt
import csv


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


def christmas(cur, conn):
        
    cur.execute(
        """
            SELECT country.name
            FROM country
            JOIN holiday
            ON holiday.country_id = country.id
            WHERE holiday.name = 'Christmas Day'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def independance_day(cur, conn):
    cur.execute(
        """
            SELECT country.name
            FROM country
            JOIN holiday
            ON holiday.country_id = country.id
            WHERE holiday.name = 'Independence Day'
        """
    )
    res2 = cur.fetchall()
    conn.commit()
    return res2

def may_day(cur, conn):
    cur.execute(
        """
            SELECT country.name
            FROM country
            JOIN holiday
            ON holiday.country_id = country.id
            WHERE holiday.name = 'May Day'
        """
    )
    res3 = cur.fetchall()
    conn.commit()
    return res3

def stephen_day(cur, conn):
    cur.execute(
        """
            SELECT country.name
            FROM country
            JOIN holiday
            ON holiday.country_id = country.id
            WHERE holiday.name = 'Constitution Day'
        """
    )
    res3 = cur.fetchall()
    conn.commit()
    return res3

def patrick_day(cur, conn):
    cur.execute(
        """
            SELECT country.name
            FROM country
            JOIN holiday
            ON holiday.country_id = country.id
            WHERE holiday.name = 'Easter Sunday'
        """
    )
    res3 = cur.fetchall()
    conn.commit()
    return res3

def first_half_us(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date <'2024-07-02' AND country.name = 'United States'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def second_half_us(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date > '2024-07-02' AND country.name = 'United States'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res


def first_half_canada(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date <'2024-07-02' AND country.name = 'Canada'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def second_half_canada(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date > '2024-07-02' AND country.name = 'Canada'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def first_half_mexico(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date <'2024-07-02' AND country.name = 'Mexico'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def second_half_mexico(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date > '2024-07-02' AND country.name = 'Mexico'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def first_half_iceland(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date <'2024-07-02' AND country.name = 'Iceland'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def second_half_iceland(cur,conn):
    cur.execute(
        """
            SELECT holiday.name
            FROM holiday
            JOIN country
            ON holiday.country_id = country.id
            WHERE holiday.date > '2024-07-02' AND country.name = 'Iceland'
        """
    )
    res = cur.fetchall()
    conn.commit()
    return res

def visualize(cur, conn):

    data = dict()
    # colors = []
    # bar(color = colors)
    data["Christmas Day"] = len(christmas(cur, conn))
    data["Independance Day"] = len(independance_day(cur, conn))
    data["Saint Stephens Day"] = len(stephen_day(cur, conn))
    data["Saint Patricks Day"] = len(patrick_day(cur, conn))
    data["May Day"] = len(may_day(cur, conn))
    names = list(data.keys())
    vals = list(data.values())
    colors = ["crimson", "pink", "palevioletred", "plum" , "lightcoral"]
    plt.bar(names,vals, color = colors)
    plt.xlabel("Holiday")
    plt.ylabel("Number of occurances across all countries")
    plt.title("Holiday count")
   
    plt.show()
    file_path = 'output.csv'
    return data.items()


def visualis_two_pie(cur, conn):
    us1 = len(first_half_us(cur,conn))
    us2 = len(second_half_us(cur,conn))
    canada1 = len(first_half_canada(cur,conn))
    canada2 = len(second_half_canada(cur,conn))
    mexico1 = len(first_half_mexico(cur, conn))
    mexico2 = len(second_half_mexico(cur, conn))
    iceland1 = len(first_half_iceland(cur, conn))
    iceland2 = len(second_half_iceland(cur, conn))

    labels1 = ["First half", "Second half"]
    sizes1 = [us1, us2]

# Data for the second pie chart
    labels2 = ["First half", "Second half"]
    sizes2 = [canada1, canada2]

    labels3 = ["First half", "Second half"]
    sizes3 = [mexico1, mexico2]

    labels4 = ["First half", "Second half"]
    sizes4 = [iceland1, iceland2]

# Create subplots with 1 row and 2 columns 

    fig, axs = plt.subplots(2, 2)
    fig.suptitle("Number of Holidays in each Half of the Year")

# Plot the first pie chart
    axs[0][0].pie(sizes1, labels=labels1, autopct='%1.1f%%')
    axs[0][0].set_title('United States')

# Plot the second pie chart
    axs[0][1].pie(sizes2, labels=labels2, autopct='%1.1f%%')
    axs[0][1].set_title('Canada')

    axs[1][0].pie(sizes3, labels=labels3, autopct='%1.1f%%')
    axs[1][0].set_title('Mexico')

    axs[1][1].pie(sizes4, labels=labels4, autopct='%1.1f%%')
    axs[1][1].set_title('Iceland')
# Adjust the layout
    plt.tight_layout()
# Display the plot
    plt.show()
    return [sizes1, sizes2, sizes3, sizes4]




def main():
    cur, conn = setUpDatabase("meals_by_id.db")
    bar = visualize(cur, conn)
    pie = visualis_two_pie(cur, conn)

    with open("output.csv", 'w', newline='') as file:
        # Create a CSV writer object
        # writer = csv.writer(file)
        csvwriter = csv.writer(file, quoting = csv.QUOTE_MINIMAL)

        # Write the data to the CSV file
        csvwriter.writerow(['Holiday', ' Number of countries observing'])
        csvwriter.writerows(bar)
        csvwriter.writerow([])
        csvwriter.writerow(['Number of Holidays celebrated in first half of Year', 'Number of Holidays celebrated in second half of Year'])
        csvwriter.writerow(['(In order of US', ' Canada', ' Mexico', ' Iceland)'])
        csvwriter.writerows(pie)


if __name__ == "__main__":
    main()