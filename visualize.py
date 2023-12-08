import matplotlib.pyplot as plt
import csv
from meals import * 

def calculate_averages(cur, conn):
    cur.execute(
        """
        SELECT categories.category_name, AVG(meals.num_ingredients)
        FROM meals
        JOIN categories
        ON meals.category_id = categories.id
        GROUP BY categories.category_name
        """
    )
    avg_data = cur.fetchall()
    conn.close()
    return avg_data

def create_barchart(avg_data):
    categories, averages = zip(*avg_data)

    colors = ['lightpink', 'purple']
    color_array = []
    for i in range(len(categories)):
        color_index = i % len(colors)
        color_array.append(colors[color_index])

    plt.figure(figsize = (10,6))
    plt.bar(categories, averages, color = color_array)
    plt.xlabel('Category')
    plt.ylabel('Average Number of Ingredients')
    plt.title('Average Number of Ingredients Per Category')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    
    plt.show()

def write_averages_to_csv(avg_data, filename):
    with open(filename, 'a', newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)

    csvwriter.writerow(['Category', 'Average Number of Ingredients'])

    for row in avg_data:
        csvwriter.writerow(row)
    

cur, conn = set_up('meals_by_id.db')

avg_data = calculate_averages(cur, conn)
create_barchart(avg_data)
write_averages_to_csv(avg_data, 'output.csv')

conn.close()