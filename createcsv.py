import csv
"""
<option value="Heberden's node">Heberden's node</option>
  <o
  ption value="Murphy's sign">Murphy's sign</option>
"""
import csv

with open('creativepulkit.csv', mode='w') as creativepulkit:
    pulkitwriter = csv.writer(creativepulkit, delimiter=',')

    #employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    #employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

    with open('output1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            strin= '<option value="'+row[0]+'">'+row[0]+'</option>'
            print(strin)
            pulkitwriter.writerow([strin])
        




    